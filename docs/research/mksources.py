#!/usr/bin/env python3
"""Build SOURCES.md from every citation in the research corpus.

Classifies each URL found in the research files:
  CITED      - a markdown link [title](url), or a bare URL inside a source-key
               table row (line begins with '|'). These carry a claim.
  ENCOUNTERED- any other bare URL: search-result listings, pages that were
               blocked or unreachable, pages noted as checked-and-rejected.
Run after adding research so the bibliography never drifts from the reports.
"""
import re, os
from collections import defaultdict

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # docs/
FILES = {
    "research/agents/fc26_ai.md": "FC 26 AI & difficulty",
    "research/agents/fc26_controls.md": "FC 26 controls & settings",
    "research/agents/fc26_tactics.md": "FC 26 tactics & roles",
    "research/agents/fc26_advanced.md": "FC 26 advanced layer (2026-11-04)",
    "legendary-playbook.md": "Legendary Playbook",
}

PUB = [
    ("ea.com/games", "EA SPORTS — Pitch Notes (primary)"),
    ("ea.com/able", "EA SPORTS — Help & settings (primary)"),
    ("forums.ea.com/blog", "EA SPORTS — update notes on EA Forums (primary)"),
    ("forums.ea.com", "EA Forums — player reports (anecdotal)"),
    ("ea.com", "EA SPORTS — other"),
    ("fifplay.com", "FIFPlay — controls & reference"),
    ("fifauteam.com", "FIFAUTeam — tactics & systems"),
    ("mp1st.com", "MP1st — patch reporting"),
    ("soccergaming.com", "SoccerGaming — patch reporting"),
    ("fut.gg", "fut.gg — community tactics"),
    ("operationsports.com", "Operation Sports"),
    ("redbull.com", "Red Bull — meta guides"),
    ("realsport101.com", "RealSport101 — settings"),
    ("dexerto.com", "Dexerto — settings"),
    ("earlygame.com", "EarlyGame (DE) — settings & passing"),
    ("sportskeeda.com", "Sportskeeda — settings & tips"),
    ("pcgamer.com", "PC Gamer — FIFA 23 testing"),
    ("ggrecon.com", "GGRecon — pro player tips"),
    ("teamgullit.com", "Team Gullit — pro coaching"),
    ("pmc.ncbi.nlm.nih.gov", "Academic (PubMed Central)"),
    ("claude.ai", "This project's own artifacts"),
]

def publisher(url):
    for frag, name in PUB:
        if frag in url:
            return name
    host = re.sub(r"^https?://(www\.)?", "", url).split("/")[0]
    return host

def gkey(name):
    if name.startswith("EA SPORTS"):
        return (0, name)
    if "EA Forums" in name:
        return (1, name)
    if any(k in name for k in ("MP1st", "SoccerGaming")):
        return (2, name)
    if any(k in name for k in ("FIFPlay", "FIFAUTeam")):
        return (3, name)
    if "own artifacts" in name:
        return (9, name)
    return (5, name)

link_re = re.compile(r"\[([^\]\[]{1,180})\]\((https?://[^\s\)]+)\)")
url_re  = re.compile(r"https?://[^\s<>\"'\)\],;|]+")

cited, seen_any = {}, {}
for rel, label in FILES.items():
    p = os.path.join(BASE, rel)
    if not os.path.exists(p):
        continue
    for ln in open(p, encoding="utf-8"):
        md = {}
        for m in link_re.finditer(ln):
            url = m.group(2).rstrip(".,);")
            md[url] = m.group(1).strip()
        is_table = ln.lstrip().startswith("|")
        for m in url_re.finditer(ln):
            url = m.group(0).rstrip(".,);")
            rec = seen_any.setdefault(url, set())
            rec.add(label)
            if url in md or is_table:
                c = cited.setdefault(url, {"titles": set(), "where": set()})
                if url in md:
                    c["titles"].add(md[url])
                c["where"].add(label)

encountered = {u: w for u, w in seen_any.items() if u not in cited}

groups = defaultdict(list)
for url, r in cited.items():
    groups[publisher(url)].append((url, r))

L = []
A = L.append
A("# Sources")
A("")
A(f"**{len(cited)} cited sources** across the research corpus, grouped by publisher and")
A("ordered by evidential weight: EA's own pages first, then outlets reproducing EA's")
A("notes, then reference sites, then community and opinion.")
A("")
A(f"A further {len(encountered)} URLs were encountered but not cited — search-result")
A("listings, pages that were blocked or unreachable, and pages checked and rejected.")
A("They are kept at the end so a later pass does not re-walk the same dead ends.")
A("")
A("Generated from the citations in `agents/*.md` and `../legendary-playbook.md`.")
A("Regenerate with `python docs/research/mksources.py` after adding research, so this")
A("file never drifts from what the reports actually cite.")
A("")
A("## How to weigh these")
A("")
A("| Tier | Meaning | What it supports |")
A("|---|---|---|")
A("| **Primary (EA)** | EA Pitch Notes, update notes, settings guides | A claim may rest on this alone |")
A("| **Patch reporting** | MP1st, SoccerGaming reproducing EA text | Dates, and EA text no longer live |")
A("| **Reference sites** | FIFPlay, FIFAUTeam | Inputs and system values — spot-check; can carry stale rows |")
A("| **Outlet guides** | Red Bull, RealSport101, Dexerto, EarlyGame, Sportskeeda | Settings opinion, not fact |")
A("| **Community** | fut.gg, EA Forums posts | Direction of travel only; never sole support for a factual claim |")
A("")
A("Where a claim rests only on a non-EA source, the agent reports say so in their")
A("confidence column, and `qa/claim_verdicts.md` records it as a verdict.")
A("")
A("---")
A("")
for name in sorted(groups, key=gkey):
    A(f"## {name}")
    A("")
    for url, r in sorted(groups[name]):
        titles = [t for t in r["titles"] if t and not t.startswith("http")]
        title = max(titles, key=len) if titles else url
        A(f"- [{title}]({url})")
        A(f"  <br>*cited in: {', '.join(sorted(r['where']))}*")
    A("")

A("---")
A("")
A("## Encountered but not cited")
A("")
A("Dead ends, blocked pages and rejected sources. Listed so a later research pass")
A("does not spend budget re-checking them.")
A("")
for url in sorted(encountered):
    A(f"- {url} — *seen in: {', '.join(sorted(encountered[url]))}*")
A("")

open(os.path.join(BASE, "research/SOURCES.md"), "w", encoding="utf-8").write("\n".join(L))
print(f"cited: {len(cited)}   encountered-only: {len(encountered)}")
for name in sorted(groups, key=gkey):
    print(f"  {len(groups[name]):3d}  {name}")

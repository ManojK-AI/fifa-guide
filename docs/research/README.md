# Research archive

Everything the FIFA guide's content rests on. The point of this directory is that
**no future research pass has to redo work that was already done** — before
researching anything, check here first.

Research date: **2026-10-06**. Patch coverage: **EA FC 26 v1.0.2 → v1.6.6** (last
FC 26 update found, released 2026-08-06).

## Start here

| If you want to… | Read |
|---|---|
| Know whether a topic was already researched | This file's [coverage map](#coverage-map) |
| Find a source for a specific claim | [`SOURCES.md`](SOURCES.md) — 79 cited sources, graded by weight |
| Know how far to trust a finding | [`METHODOLOGY.md`](METHODOLOGY.md) — confidence scale and the evidence limits |
| Know which claims were checked and what failed | [`VERIFICATION_LOG.md`](VERIFICATION_LOG.md) — 102 claims, verdicts, unresolved issues |
| Add new research without duplicating | [`TEMPLATE.md`](TEMPLATE.md) — the format, and the rules for appending |
| Read the raw findings | [`agents/`](agents/) — the three full reports |
| See the QA evidence | [`qa/`](qa/) — claim verdicts, test code, logs, bug screenshots |

## Coverage map

What has already been researched, and to what depth. **Check this before starting
any new research** — most FC 26 gameplay questions are already answered in
`agents/`.

| Area | File | Depth | Confidence |
|---|---|---|---|
| Squad Battles mode, difficulty tiers, points multipliers | `agents/fc26_ai.md` §1 | Thorough | High (EA) + med (FIFAUTeam) |
| CPU AI behaviour changes by patch, v1.0.2 → v1.6.6 | `agents/fc26_ai.md` | Thorough | High — EA notes quoted verbatim |
| Competitive vs Authentic tuning, CPU fatigue | `agents/fc26_ai.md` | Thorough | High (EA Gameplay Deep Dive) |
| Legendary/Ultimate difficulty internals | `agents/fc26_ai.md` | **Gap** — EA never published FC 26 numbers | n/a |
| Xbox/PlayStation control inputs, Classic config | `agents/fc26_controls.md` §1 | Thorough | Med — no official EA controls page exists |
| Controls that changed from FIFA 23 | `agents/fc26_controls.md` | Thorough | High for 4 identified changes |
| Camera, zoom, radar, assist, defending settings | `agents/fc26_controls.md` | Thorough | Med (outlet recommendations) |
| D-pad quick tactics | `agents/fc26_controls.md` | Thorough | Med — sources disagree, see Problem 12 |
| Team tactics: Build-Up, Defensive Approach, Line Height | `agents/fc26_tactics.md` §1 | Thorough | High (FC 25 FC IQ) / med-high (FC 26) |
| Player Roles and Focuses | `agents/fc26_tactics.md` | Thorough | Med — one complete list only |
| PlayStyles, AcceleRATE | `agents/fc26_tactics.md` | Thorough | High (EA) + med (FIFAUTeam) |
| What FC 26 removed vs FIFA 23 | `agents/fc26_tactics.md` §3 | Thorough | High |
| Meta tactics against the CPU | `agents/fc26_tactics.md` | **Thin** — no priority-outlet guide exists | Low (community) |
| FIFA 23 tactics, instructions, controls | `../legendary-playbook.md` Sources | Moderate | Med (FIFPlay, PC Gamer, GGRecon) |
| Advanced layer: shot selection, full pass kit, manual defending, game-state tactics, points maths | `agents/fc26_advanced.md` §1, §3 | Thorough (built on the archive) | High/med for facts; Coach's calls labelled |
| FC 26 skill moves (new moves, inputs, stars) | `agents/fc26_advanced.md` §2 | **Thin** — search excerpts only | Low-med (Unconfirmed) |
| Set pieces: free kicks, penalties | `agents/fc26_advanced.md` §2, §4 | **Thin** — power conflicts, no penalty method | Low |
| Player Lock, Match Facts xG, Practice Arena | `agents/fc26_advanced.md` §2 | Thin — search excerpts only | Low-med (Unconfirmed) |

### Known gaps — research these if you need them

These were looked for and **not found**. They are not oversights; re-searching them
is likely to cost budget for nothing unless new sources have appeared since
2026-10-06.

- EA has never published FC 26's difficulty-slider numbers (the FIFA 23 figures of
  90% / 100% on attacking intelligence, defending intelligence, reaction speed and
  marking have no FC 26 equivalent).
- No official EA FC 26 controls page could be confirmed to exist.
- No EA Help article on FC 26 tactics was found.
- No priority-outlet guide exists on beating Legendary or Ultimate CPU in FC 26.
- `fifplay.com/fc-26-difficulty-levels/` could not be fetched — unknown whether it exists.
- Patches not checked: v1.1.2, any v1.3.x point release, v1.5.2, v1.6.5.
- A second complete FC 26 list of Roles and Focuses was never found (the search
  budget ran out), so the Roles list rests on one source plus fut.gg.
- **2026-11-04:** no guide page could be opened at all: the session's network policy
  blocked every guide host. Everything tagged Unconfirmed in the Pro tab came from search
  excerpts and is listed for checking in `agents/fc26_advanced.md` §5. Allow those hosts in
  the cloud environment's network settings before the next research pass.
- No FC 26 penalty method was found; free-kick power advice conflicts between guides.

## The three agent reports

Each was produced by a separate research agent on 2026-10-06, working one domain.
Each report opens with its own "how the evidence was gathered" header — read that
before trusting any individual line.

| Report | Size | Scope |
|---|---|---|
| [`agents/fc26_ai.md`](agents/fc26_ai.md) | 657 lines | CPU AI, difficulty, gameplay presets, every patch v1.0.2–v1.6.6 |
| [`agents/fc26_tactics.md`](agents/fc26_tactics.md) | 552 lines | Tactics, Roles, PlayStyles, AcceleRATE, the anti-AI meta |
| [`agents/fc26_controls.md`](agents/fc26_controls.md) | 402 lines | Xbox/PS inputs, settings, what changed from FIFA 23 |
| [`agents/fc26_advanced.md`](agents/fc26_advanced.md) | 2026-11-04 | The advanced layer: what the archive proved but the guide never used, search-only findings, coach's calls, and the pages still to open |

All three use the same line format:

```
claim — "verbatim quote" — [source, date](url) — confidence
```

Confidence is `high` / `med` / `low`; `**Inference**` marks the agent's own
reasoning where no source states it directly. See `METHODOLOGY.md`.

## QA and verification

[`qa/`](qa/) holds the fact-check and test evidence.

| File | What it is |
|---|---|
| `qa/claim_verdicts.md` | **The important one.** All 102 factual claims in the page, each with a verdict and the reason |
| `qa/playbook_fc26_additions.md` | The 14 FC 26 additions made to the Legendary Playbook, each with its source |
| `qa/claims_fc26.json` | Machine-readable claim set extracted from the page (38 KB) |
| `qa/claims_js.json` | Claim set extracted from `game.js` overrides (17 KB) |
| `qa/page_structure_and_harness.md` | Page DOM structure, debug hooks, test-harness API — read before writing tests |
| `qa/playbook_snapshot.xml` / `_annotated.txt` | The Playbook as it stood when fact-checked, with block ids the verdicts reference |
| `qa/functional/` | 13 test modules, their logs and JSON results |
| `qa/standards/` | Accessibility, contrast, language-consistency and storage checks |
| `qa/bug-screenshots/` | 6 screenshots of bugs that were found and fixed — states that no longer exist |

### Screenshots: what is here and what is not

The 6 screenshots in `qa/bug-screenshots/` show defects that were **fixed**, so they
cannot be regenerated. They are kept.

About 200 further screenshots (≈31 MB) of the page rendering correctly at 320/390/820/1280 px
in light and dark mode were **not** copied into the repo. Nothing is lost: the page
and the scripts that produce them are both here, so
`python docs/research/qa/standards/shots_visual.py` regenerates them on demand.

## Rules for adding research

1. **Read the coverage map above first.** If a topic is listed as thorough, read that
   report before searching the web.
2. **Check "Known gaps".** If it is listed there, it was already looked for and not
   found; only re-search if you have reason to think new sources exist.
3. **Check `SOURCES.md`, including the "Encountered but not cited" section at the
   bottom** — 95 URLs that were dead ends, blocked, or rejected. Do not re-walk them.
4. Append new findings using [`TEMPLATE.md`](TEMPLATE.md). Date every entry.
5. Re-run `python docs/research/mksources.py` so `SOURCES.md` picks up new citations.
6. Add a dated row to `VERIFICATION_LOG.md`.

## Provenance

The guide page, the Playbook and this archive were produced in a Claude session on
2026-10-06/07. The research was done by three parallel agents, fact-checked against
sources claim by claim, and verified with browser automation. Final state: **0 test
failures**; the unresolved content issues are itemised in `VERIFICATION_LOG.md`.

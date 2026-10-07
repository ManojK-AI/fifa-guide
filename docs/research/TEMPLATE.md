# Adding research without duplicating it

Two things live here: a **briefing prompt** to hand any future AI session so it reads
the archive before searching, and the **file format** for new findings.

---

## 1. The briefing prompt

This is the part that actually prevents duplicated work. Paste it at the start of any
new research session on this project, with your question appended.

```
This project has an existing research archive at docs/research/. Before you search
the web for anything, do this:

1. Read docs/research/README.md — its coverage map says what has already been
   researched and to what depth, and its "Known gaps" section lists what was
   already looked for and NOT found.
2. Read the relevant report in docs/research/agents/ in full. The three reports
   cover FC 26 AI and difficulty, tactics and roles, and controls and settings.
   Most FC 26 gameplay questions are already answered there.
3. Read docs/research/METHODOLOGY.md so you match the existing evidence format,
   confidence scale, and source weighting.
4. Check the "Encountered but not cited" section at the bottom of
   docs/research/SOURCES.md — 95 URLs that were dead ends, blocked or rejected.
   Do not re-walk them.
5. Read docs/research/VERIFICATION_LOG.md for issues that are still open.

Then tell me, before searching: what is already answered, what is a known gap, and
what genuinely needs new research. Do not re-research what is covered.

When you do add findings:
- Append to the relevant agents/*.md file, or create a new one if the domain is new.
- Use the existing line format: claim — "verbatim quote" — [source, date](url) — confidence
- Date every entry and mark it as a later pass.
- Re-run: python docs/research/mksources.py
- Add a dated entry to docs/research/VERIFICATION_LOG.md.
- If a new finding contradicts an existing one, do not silently overwrite it.
  Record both and say which source is stronger and why.

My question:
```

### Why this works

The archive's value is that it records **negative results** as well as positive ones.
Knowing that EA never published FC 26's difficulty numbers, that no official controls
page could be found, and that 95 specific URLs are dead ends is worth as much as the
findings themselves — it is the part a fresh session would otherwise spend its whole
search budget rediscovering.

---

## 2. Format for new findings

### Where it goes

| New research is about… | Append to |
|---|---|
| CPU AI, difficulty, patch behaviour | `agents/fc26_ai.md` |
| Tactics, Roles, PlayStyles, meta | `agents/fc26_tactics.md` |
| Controls, settings, inputs | `agents/fc26_controls.md` |
| A new game (FC 27, say) | New file: `agents/fc27_<domain>.md` |
| A domain none of these cover | New file: `agents/<game>_<domain>.md`, and add a row to the README coverage map |

### Line format

```
claim — "verbatim quote" — [source tag, date](url) — confidence
```

- `high` = EA's own page, or an outlet reproducing EA verbatim
- `med` = reputable outlet or established fan site, or several agreeing forum posts
- `low` = a single forum anecdote, or a low-tier site
- `**Inference**` = your own reasoning, no source states it
- Tag anything not about the report's main game: `[FC 25]`, `[FIFA 23]`, `[FC 27]`
- `"…"` marks words trimmed from a quote

### Section header for a later pass

Append, don't interleave. Open each new pass with its own header so the original
research stays distinguishable:

```markdown
---

# Pass 2 — YYYY-MM-DD

Scope: <what this pass covered>
Why: <what prompted it — new patch, gap, contradiction found>

**How the evidence was gathered**
- <tool limits, budget, anything that constrains these findings>
- <confidence scale if it differs from METHODOLOGY.md>

## <Section>

<findings in the line format above>
```

### If a new finding contradicts an old one

Record both. Add a note under the original line rather than editing it out:

```markdown
> **Superseded 2026-11-02 (pass 2):** v1.7.0 changed this. New value: <x> —
> "quote" — [EA TU 1.7.0, 2026-11-01](url) — high. The line above was correct
> for v1.6.6 and earlier.
```

The old line stays. Someone reading the page as it was in October needs to know what
it was based on then.

---

## 3. Checklist for finishing a research pass

- [ ] Findings appended to the right `agents/*.md`, in the line format, dated
- [ ] Contradictions recorded as superseded notes, not deleted
- [ ] `python docs/research/mksources.py` re-run so `SOURCES.md` is current
- [ ] New dead ends added to the research file so they reach the "Encountered" list
- [ ] Dated entry added to `VERIFICATION_LOG.md`, including anything left open
- [ ] `README.md` coverage map updated — new rows, and gaps closed or newly found
- [ ] If page content changed: `python build.py`, then `python smoke.py` and
      `python checks2.py`
- [ ] Committed with a message saying what was researched and what changed

---

## 4. If you change the page's factual claims

New research that alters what the page says needs the claim re-verified, not just
the research updated. The original pass did this by extracting every claim to
`qa/claims_fc26.json` and judging each against its source. At minimum, for each
claim you touch:

1. Name the source that supports it and quote the supporting text.
2. Check the page's own citation actually points at that source — two of the
   original 102 claims were true but cited the wrong page.
3. Keep EA's qualifiers. "Slightly reduced" is not "reduced"; dropping hedges
   accounted for the two most frequent problems in the first pass (Problems 5 and 6).
4. Add the claim and its verdict to `qa/claim_verdicts.md` with the date.

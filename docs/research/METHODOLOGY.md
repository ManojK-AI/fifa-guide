# Methodology

How the research was done, how far to trust it, and what constrained it. Read this
before adding to the archive or relying on a specific line.

## Shape of the work

Three research agents ran in parallel on 2026-10-06, one per domain, each writing a
standalone report. They did not share findings mid-flight, which is deliberate: the
three reports overlap on a few points (patch dates, the Gameplay Deep Dive), and
where two independently-produced reports agree, that agreement is worth something.
Where they disagree, the disagreement is itself recorded rather than smoothed over.

| Agent | Domain | Output |
|---|---|---|
| 1 | CPU AI, difficulty, gameplay presets, patch history | `agents/fc26_ai.md` |
| 2 | Tactics, Roles, PlayStyles, AcceleRATE, anti-AI meta | `agents/fc26_tactics.md` |
| 3 | Controls, settings, FIFA 23 → FC 26 input changes | `agents/fc26_controls.md` |

After the reports came in, a separate fact-check pass extracted every factual claim
the page made and tested each one against the reports and their sources. That pass
produced `qa/claim_verdicts.md`. A third pass ran browser automation against the
built page. The sequence matters: **research → build → fact-check against sources →
functional test**. The fact-check deliberately ran against the built page rather
than the research, so it caught claims that drifted during writing.

## Evidence format

Every line in the agent reports follows one shape:

```
claim — "verbatim quote" — [source tag, date](url) — confidence
```

- `"…"` inside a quote marks words left out.
- Text without quotation marks was paraphrased by the fetch tool and is weaker
  than quoted text.
- `**Inference**` marks the agent's own mapping where no source states the point
  directly. Inferences are not facts and are flagged as such.
- `[FC 25]`, `[FC 27]`, `[FIFA 23]` tag any line that is **not** about FC 26.
  Untagged lines are FC 26.

## Confidence scale

| Level | Means |
|---|---|
| **high** | EA's own page, or an outlet reproducing EA's notes verbatim |
| **med** | A reputable outlet or established fan site, or several forum posts that agree |
| **low** | A single forum anecdote, or a low-tier site |

A claim in the finished page should rest on `high`, or on `med` with the uncertainty
stated in the page text. One claim rested on neither and was caught — see
`VERIFICATION_LOG.md`, Problem 1.

## Constraints on the evidence

These shaped what could be gathered. They are **properties of the research
environment**, not of the sources, and they will apply again to any future pass run
the same way.

**Quote length was capped.** All EA text came through a web-fetch tool whose
extractor truncates each quote at roughly 125 characters. Long passages were
requested in pieces and reassembled. The quotes are verbatim fragments, but no
quote was verified character-by-character against the live page. **Spot-check any
quote before republishing it word for word.**

**`ea.com` could not be downloaded directly.** The sandbox network policy blocked
`curl` to ea.com, so every EA quote came through the fetch tool rather than from
raw HTML. This is why MP1st and SoccerGaming appear so often: they reproduce EA's
notes and were reachable.

**EA forum posts show only relative ages.** The forums render "9 months ago" rather
than a date. Forum citations are reported as they read on **2026-10-06** — a
forum date in these reports is an inference from that anchor, and the drift grows
as this archive ages. Problem 13 in the verification log is exactly this failure.

**The search budget ran out.** Agent 1 exhausted its 200-call budget near the end of
its run; agent 2's ran out before it found a second complete Roles list. Gaps caused
by this are marked "not found" in the reports and listed under "Known gaps" in
`README.md`. They are *unknowns*, not *negatives* — "not found" never means "does
not exist".

**One page could not be fetched at all.** `fifplay.com/fc-26-difficulty-levels/`
returned nothing because a permission prompt went unanswered, so whether that page
exists is unknown.

**German sources were translated.** The EarlyGame articles are in German;
translations are marked `[≈EN]`, and the PlayStation-button notation in them was
mapped to Xbox (X=A, △=Y, ▢=X, R1=RB, L1=LB).

## Source weighting

Set out in full in [`SOURCES.md`](SOURCES.md). In short: EA's own pages can carry a
claim alone. Patch-reporting outlets are good for dates and for EA text no longer
live. Reference sites (FIFPlay, FIFAUTeam) are good for inputs and system values but
**can carry stale rows from the previous game** — FIFPlay's FC 26 controls page was
found to contain at least one FC 25 row, which is why input claims were cross-checked
against two or three sources. Community posts show direction of travel and never
support a factual claim on their own.

## The fact-check pass

Every factual claim in the page was extracted into `qa/claims_fc26.json` and
`qa/claims_js.json`, then judged against the research. Each got one of five verdicts:

| Verdict | Meaning | Count |
|---|---|---|
| Supported | The cited source says this | 65 |
| Partly supported | True in substance, but the page overstates or misquotes it | 23 |
| OK (advice) | A recommendation or description with no factual claim to source | 11 |
| Supported, but not by its cited source | True, but the citation points at the wrong page | 2 |
| Not supported | No source says this | 1 |

The two citation mismatches and the one unsupported claim matter most: they are the
failures that a reader checking the page's own sources would have discovered.

## Functional verification

Browser automation via Playwright (Chromium at `/opt/pw-browsers`), driven through
`harness.py`, which wraps the page exactly as the publisher does, serves fonts
locally, and collects console errors. 13 functional modules under `qa/functional/`
and 8 standards scripts under `qa/standards/` cover both games, all four tabs, all
31 clips in both camera views, trainer rounds, keyboard paths, accessibility,
colour contrast, language consistency and storage failure modes, at 320/390/820/1280 px
in light and dark mode.

The page exposes debug hooks (`__lrrMode`, `__lrrGame`, `__lrrShow`, `__lrrTrain`,
`__lrrAnsPt`, `__lrrScene`) so tests can drive it to an exact state rather than
clicking through. `qa/page_structure_and_harness.md` documents them — **read it
before writing new tests.**

Final state: 0 failures across `smoke.py`, `checks2.py` and the module suites.

## What this methodology does not give you

It establishes what EA published and what reference sites state. It does **not**
establish how FC 26 actually behaves on your console. Every claim about CPU
behaviour derives from patch notes and community reports, not from instrumented
play. Where the page gives tactical advice, that advice is reasoning from the
documented changes — it is not measured. Treat the tactics sections as hypotheses
to test in your own match log, which is what the Playbook's match-log table is for.

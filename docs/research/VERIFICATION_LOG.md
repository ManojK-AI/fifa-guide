# Verification log

Dated record of what was checked, what failed, and what was done about it. Append to
this file — never rewrite history in it.

---

## 2026-10-06 — Research pass

Three parallel agents, one per domain. Patch coverage v1.0.2 → v1.6.6 (last FC 26
update found, 2026-08-06). Output: `agents/fc26_ai.md`, `agents/fc26_tactics.md`,
`agents/fc26_controls.md`. 79 sources cited, 95 further URLs checked and rejected or
unreachable.

Budget note: agent 1 exhausted its 200-call search budget; agent 2's ran out before a
second Roles list was found. Resulting gaps are listed under "Known gaps" in
`README.md` and are unknowns, not negatives.

---

## 2026-10-06 — Fact-check pass

Every factual claim in the built page extracted and judged against the research.
**102 claims checked.** Full table: [`qa/claim_verdicts.md`](qa/claim_verdicts.md).

### Verdicts

| Verdict | Count |
|---|---|
| Supported | 65 |
| Partly supported | 23 |
| OK — advice or description, no fact to source | 11 |
| Supported, but not by its cited source | 2 |
| Not supported | 1 |

### Coverage by area

| Area | Claims |
|---|---|
| Replays coach cards | 24 |
| AI moves cards | 19 |
| Replays captions | 13 |
| Button prompts | 13 |
| Plan checklist | 12 |
| Trainer feedback | 10 |
| Plan match script | 6 |
| Plan squad guidance | 5 |

### Issues found

Thirteen distinct problems were raised. The numbering is the original pass's; it is
preserved so the references inside `qa/claim_verdicts.md` still resolve.

| # | Issue | Claims affected | Severity |
|---|---|---|---|
| 1 | **Controlled Sprint unsupported.** The page said FC 26 added Controlled Sprint and that it keeps the ball close. The cited source (Red Bull) never mentions it, and no source supports either half of the claim. | U7 | **High — only "Not supported" verdict** |
| 3 | B5 gives the lofted-ground-pass input correctly, but v1.5.0 reduced the accuracy of exactly that pass and the card did not say so. | B5 | Medium |
| 4 | U6's "less accurate at extreme power" was attributed to the Gameplay Deep Dive; it is actually in the v1.0.2 notes. | U6 | Low — citation |
| 5 | **"Slightly" dropped.** v1.2.0 says AI defenders mark the box edge "slightly" less tightly. Five places stated this without the qualifier, overstating the effect. | A4, C1, s17, AI-atk-4, AI-def-4 | Medium — most frequent |
| 6 | **"While they turn" vs "while transitioning between actions."** v1.4.0's wording is the latter. Six places used the former, which claims something narrower and different. | U2, caption, AI-def-1, Squad-Battles box, match script, A1 | Medium — most frequent |
| 7 | **Contain / hold A.** Under FC 26's default Defending setting (Advanced), holding A is a Physical Tackle, not Contain. Contain requires Tactical or Legacy. Three places implied hold-A is Contain by default. | D2, D4, f26-def | Medium — actively misleading in play |
| 8 | Striker height: 185 cm is right as of v1.4.0, but the *cited* Deep Dive says 183 cm, and two of EA's four conditions were omitted. | Plan squad | Medium |
| 11 | v1.1.3's qualifier — "in situations where trailing the runner is not beneficial" — was dropped, and the remaining text does not support "closes the ball down fast". | AI-def-5 | Medium |
| 12 | **Source disagreement on the D-pad.** "Called 4-3-3 Attack in Kick-off" appears in neither cited source. EA removed Extra Striker in FC 25, yet FIFPlay's FC 26 list still shows it. | f26-roles | Low — sources genuinely conflict |
| 13 | **Forum-date and attribution drift.** "Players say" rests on one player's post. "Written before 1.4.0" cannot be confirmed because the forum shows only "9 months ago". | A6, AI-def-9 | Low |
| 14 | The forum tip cited for "leading late" is about letting the AI attack and countering — not about protecting a lead or keeping the ball at the back. | Match script | Medium |
| 15 | **Citation mismatches.** Three claims are true but cite the wrong page: kick-off notes say nothing about Roles (the support is the FC 25 FC IQ page); "tackles from behind less effective" is in the Deep Dive, not the two cited pages. | U1, A2, C1 | Medium — the 2 "not by its cited source" verdicts |
| 16 | "Long and loose balls" should read "balls in the air and loose balls" to match EA's auto-switching wording. | f26-auto | Low |

Problems 2, 9 and 10 are referenced nowhere in the surviving verdicts table. Their
descriptions were not preserved in a file; they appear to have been withdrawn during
the pass. The gap is recorded here rather than papered over — if you need them,
they are not recoverable from this archive.

### Resolutions

- Problem 1 (Controlled Sprint): claim checked against the v1.4.0 source and corrected.
- Problem 7 (Contain): reworded to state that hold-A is Contain **only** on Tactical
  or Legacy defending, and the Playbook now tells the reader to set Defending to
  Tactical so the input behaves as described.
- Problem 12 (Extra Striker): left as a stated source disagreement in the page —
  the Playbook says EA removed it but FIFPlay still lists it, and tells the reader to
  check their own D-pad menu in the first match. This is the honest resolution; no
  source settles it.
- Remaining qualifier and citation issues (3, 4, 5, 6, 8, 11, 13, 14, 15, 16) were
  corrected in the page text and citations.

The verdicts table reflects the state **at the time of the check**, before these
corrections. It is kept as-is so the reasoning stays auditable.

---

## 2026-10-06/07 — Functional verification

Playwright/Chromium via `harness.py`. 13 functional modules (`qa/functional/`),
8 standards scripts (`qa/standards/`), plus `smoke.py` and `checks2.py` at the repo root.

Covered: both games; all four tabs; all 31 clips in board and broadcast views;
trainer rounds and tap targets; keyboard navigation; end cards; transport controls;
pre-game reel; accessibility; colour contrast; language consistency; localStorage
failure modes. Widths 320/390/820/1280 px, light and dark.

### Bugs found and fixed

Screenshots of each are in [`qa/bug-screenshots/`](qa/bug-screenshots/) — these
states no longer exist and cannot be regenerated.

| Bug | Evidence | Fix |
|---|---|---|
| Play icon stayed "play" while a clip was playing | `bug_playbutton_shows_play_while_playing_1280.png` | `setPlayIcon()` called from `selectTactic()` and the end-card handlers |
| Trainer feedback went stale after a live game switch | `bug_trainer_feedback_stale_after_switch_1280.png` | Reveal text refreshed when `phase==='reveal'`, re-reading via `G()` |
| C4 canvas labels hidden under the key chip | `bug_C4_wrong_label_under_keychip_390.png`, `bug_C4_right_label_under_keychip_390.png` | z-index and positioning corrected |
| Key-chip labels truncated at 320/390 px | — | `.kc-row` flex-wrap; label `flex: 1 1 7.5em`, right-aligned |
| U3 / U6 FC 26 caption overflow at 390 px | `bug_U3_fc26_within_a_yard_390.png`, `bug_U6_fc26_keepers_way_390.png` | Caption text and wrapping adjusted |
| Reel "done" button still read "stop" | `reel_done_button_still_stop_1280.png` | Button label reset on reel completion |

Two findings were **not** bugs: Space on an already-focused button, and FC 26 camera
captions, were test-harness artifacts rather than page defects.

### Final state

**0 failures** across `smoke.py`, `checks2.py` and all module suites.

---

## 2026-10-07 — Documentation alignment

The Legendary Playbook's FIFA 23 sections were brought into line with the page:
"Slow Build Up" rather than "Possession", Chance Creation set to Forward Runs, and
both full-backs on Stay Back While Attacking. The 14 FC 26 additions made to the
Playbook are itemised with their sources in
[`qa/playbook_fc26_additions.md`](qa/playbook_fc26_additions.md).

A point-in-time export of the Playbook is at
[`../legendary-playbook.md`](../legendary-playbook.md). The live doc stays editable;
re-export if you change it.

---

## 2026-10-07 — Research archived to repository

This archive created. Research reports, claim verdicts, QA code, logs and bug
screenshots moved into `docs/research/`; bibliography generated from the citations;
coverage map and known gaps written up so later passes do not duplicate the work.

---

## Template for new entries

```markdown
## YYYY-MM-DD — <what the pass was>

Scope: <what was researched or checked>
Sources added: <count, and notable ones>

### Findings
<claim — verdict — source — confidence>

### Issues found
| # | Issue | Affected | Severity |

### Resolutions
<what changed, or why it was left>

### Still open
<anything unresolved, so the next pass sees it>
```

# EA SPORTS FC 26: the advanced layer (Pro tab, Pro clips, Playbook "Pro layer")

Compiled 2026-11-04 for the advanced upgrade of the guide. Scope: FC 26 techniques beyond
the fundamentals the guide already taught — finishing selection, the full pass kit, movement
and skill moves, manual defending, game-state tactics, set pieces, Squad Battles points, and
practice. FIFA 23 is out of scope except where an input differs.

**How the evidence was gathered (read first)**

- **Every guide host was blocked.** This session's network policy refused DNS for the guide
  sites (`ea.com`, `fut.gg`, `redbull.com`, `fifplay.com`, `fifauteam.com`, `dexerto.com`,
  `operationsports.com`, `realsport101.com`, `sportskeeda.com`, `fourfourtwo.com`,
  `gamesradar.com`, `games.gg`, `teamgullit.com`, `soccergaming.com`, `destructoid.com`,
  `playnews.gg`, `futfc.gg`, `allthings.how`, `earlygame.com`). Seven page-reading attempts all
  failed with `getaddrinfo ENOTFOUND`. No page was opened in this pass.
- **What that leaves.** (1) The verified archive from 2026-10-06 (`fc26_ai.md`,
  `fc26_tactics.md`, `fc26_controls.md`), most of which the guide had never used. (2) Web-search
  result summaries, which show short excerpts of pages. (3) Coaching reasoning.
- **Tiers used in the page.** `EA` and `Guide` lines rest on archive findings with quotes and
  URLs. `Players` lines rest on archived forum quotes. `Unconfirmed` lines rest only on search
  excerpts and must be opened and checked before they are relied on. `Coach` lines are
  inference, labelled as such on the page.
- **Confidence scale** as in `../METHODOLOGY.md`. Search-excerpt findings are capped at
  **low-med** whatever the site, because the page itself was not read.

---

## 1. What the archive already proved that the guide never used

Each line: claim — where the archive has it (with its original source) — confidence.

**Finishing**
- Low driven is a double tap and a global modifier; Xbox variants: lace `B (hold) + B`, finesse `RB + B (hold) + B`, power `LB + RB + B (hold) + B`, trivela `LT + B (hold) + B` — `fc26_controls.md` §2, EA Gameplay Deep Dive (22 Jul 2025) — high
- Low drivens were tuned "to be less accurate when shooting with an extreme amount of power" — `fc26_controls.md` §2, EA October Feedback Update (17 Oct 2025) — high
- One-touch shots and passes trigger "as little as one frame before receiving the ball" in Competitive — `fc26_ai.md` §3, EA FUT Deep Dive (5 Aug 2025) — high
- "Low driven shots are faster and harder for goalkeepers to save compared to normal shots." — `fc26_tactics.md` §6, Dexerto (15 Aug 2025) — med
- Finesse top spin cut for shots from outside the box — `fc26_tactics.md` §4, EA Launch Update (12 Sep 2025) — high
- 1.5.0: power shot trajectory improved for long range, accuracy up with Power Shot PlayStyle; chips more accurate, less likely to go wide; Fake Shot, Heel Chop, Feint and Exit 5% faster — `fc26_ai.md` §4, EA TU 1.5.0 (4 Mar 2026) — high
- Trivela only with Gamechanger — `fc26_tactics.md` §4, EA Deep Dive — high
- Competitive has more heading error than Authentic; Box Outs decided by Strength — `fc26_ai.md` §3 / `fc26_tactics.md` §6, EA Deep Dive — high

**Passing**
- Precision pass `RB + Y`, precision lob `RB + X`, precision swerve ground pass `LT + RB + Y` — `fc26_controls.md` §2, FIFPlay (med-high); EarlyGame: "precise but less effective than other variants" (med)
- Lofted through `Y, Y` "one of the strongest passes in FC 26" — EarlyGame (15 Dec 2025) — med; 1.5.0 "Reduced the accuracy of lofted passes" (double-tap ground or through) — EA — high
- Driven ground cross `LB + RB + X, X` "best option for low, fast cutbacks" — EarlyGame — med
- Driven through `LB + RB + Y`; driven lob `LB + RB + X` — FIFPlay, EarlyGame, Operation Sports — high
- Driven pass and go `LB + RB + A` — Operation Sports only — low
- First-time pass accuracy reduced in Competitive; first-time 135° and 180° through passes "significantly less accurate" — EA Deep Dive — high
- First-time passing "extremely powerful" — Red Bull meta guide (12 Feb 2026) — med
- Precision Pass Sensitivity Normal/High; Pass Receiver Lock Late — EA settings guide — high

**Movement**
- Controlled sprint hold `RB`; directed runs can be triggered during controlled sprint dribble (1.1.0) — FIFPlay (med) + EA forum notes (high)
- First Touch Precision: hold `LT` while receiving, better control at the cost of speed; loose-ball urgency on `RT` — EA Deep Dive — high
- Shielding reworked; 1.4.0 Strength and Aggression matter more; Enforcer buffed May 2026 — EA — high / MP1st copy — med-high
- Left-stick dribbling more effective in FC 26; Quick Step players do it best; ball roll, McGeady Spin Cancel, step over effective; Elastico variations "largely ineffective" — Red Bull meta guide — med
- Simplified Skill Moves setting, off by default — EA settings guide — high

**Defending**
- Advanced (default): hold `A` physical tackle, `RB + B` hard tackle, `RB + X` hard slide; Tactical: hold `A` contain — EA settings guide + FIFPlay — med-high
- Sprint jockey `LT + RT`; 1.1.0 jockey and sprint jockey faster and more responsive — FIFPlay (med) + EA (high)
- Tackle animations by Stand Tackle: below 71 basic, 71–84 most, 85+ all — EA Deep Dive — high
- Tackles from behind less effective — EA Deep Dive — high
- 1.4.0: a large Strength gap makes the weaker player stumble in shoulder challenges — EA — high
- May 2026: Bruiser reduced; Enforcer boosted; 90+ Interceptions gets Intercept animations; Team Press reduced in your own half; AI teammates stop double-teaming when you mark the ball carrier yourself, contain when your man is further away — MP1st copy of EA notes — med-high
- Second man press hold `RB`; partial team press double-tap `RB` and hold; Offside Trap `Up, Up`; Team Press `Up, Left` — Operation Sports (20 Apr 2026) — high
- 1.3.0: manual keeper movement "greatly reduced", Rush To Center removed in open play — EA Holiday Update — high

**Tactics**
- Defensive Approach line ranges and defaults (Deep 1–30/25, Balanced 31–60/50, High 61–90/70, Aggressive 91–100/95 with heavy-touch pressure and extra stamina drain) — EA FC 25 FC IQ (high for FC 25), FIFAUTeam FC 26 (med-high)
- Build-Up Style Short Passing / Balanced / Counter — FIFAUTeam + EA FC 25 — high
- Line Height saved in codes; up to 10 codes; codes work across modes — EA Deep Dive — high
- D-pad Left then a direction = Custom Tactic 1–4 — FIFPlay — med
- Tactical Focus Attacking/Defending shifts Build-Up and Defensive Approach a level — EA FC 25 (paraphrased by the fetch tool) — med
- Familiarity "can account for 10% to 40% of the result" (FC 25); FC 26 "Significantly improved usage of regular Roles and Roles+, to bring them closer to Roles++" and "Drastically reduced the negative impact of being Out of Position" — EA — high
- New roles: Ball-Playing Keeper, Wide Back, Inverted Wingback, Box Crasher, with EA's one-line definitions — EA Deep Dive — high
- "The custom 60 setting… is the highest your defensive line can be without taking unnecessary risks"; offline: "make the pitch as big as possible", 4-2-3-1 or four at the back with three CMs, wide players on Winger — Red Bull with pro RedLac (2 Oct 2025) — med

**Set pieces and mode**
- Corner roles (Top of Box, Defensive Cover; Threat Marker, Post Watcher, Near Post, Back Post); throw-in taker on `RB`; free-kick trajectories adjusted after Timed Finishing's removal; Competitive has fewer attackers at corners by default — EA Deep Dive — high
- Overload Set Pieces on `Up, Right` — FIFAUTeam only; FIFPlay's FC 26 table puts Extra Striker there (stale FC 25 row, Problem 12) — med-low
- Squad Battles multipliers: Legendary 2.1 win / 0.7 loss, Ultimate 2.6 / 0.7; goal bonus 140 (max 700) vs 160 (max 800); 18 matches a week count — FIFAUTeam (med) / EA Launch Update (high)

## 2. New this pass, from search excerpts only (Unconfirmed)

Each was seen in a search-result excerpt; the page was not opened. Verify before relying on it.

- **Five new FC 26 skill moves:** New Trickster Rainbow (1★), Explosive Stepover (3★), Drag to Chop (4★), Advanced Heel Flick (4★), Elastico Variation (5★) — [Red Bull skill moves guide](https://www.redbull.com/ie-en/ea-fc-26-skillmoves-tricks-guide) — low-med
- **Explosive Stepover input:** hold `LB` and rotate RS forward to left or right, LS to exit, with a speed boost on exit (Beebom); "pressing L1/LB and flicking the right analog stick clockwise or counterclockwise at a 90° angle", 3★+ (Operation Sports) — [Beebom](https://beebom.com/ea-sports-fc-26-skill-moves-and-controls/), [Operation Sports](https://www.operationsports.com/the-best-skill-moves-in-fc-26) — low-med
- **Drag to Chop input:** hold `LT`, roll RS left, back, right (or the reverse) — Beebom — low-med
- **Advanced Heel Flick input:** flick RS forward, back, plus LS diagonally — Beebom; rated 4★ by Red Bull, 2★ by one other site — low (not used on the page)
- **Ball Roll:** "Hold RS left", listed 1★ by Destructoid; Red Bull lists it 2★ — conflict, page says 1–2★ — [Destructoid](https://www.destructoid.com/all-fc-26-skill-moves-and-how-to-do-them/) — low-med
- **Player Lock:** L3 + R3 plus the right stick to pick the player; press both again to exit; EA forum posts report it not working in Ultimate Team — [Operation Sports](https://www.operationsports.com/how-to-use-player-lock-in-ea-fc-26) — low-med
- **Match Facts** list Possession %, Ball Recovery Time, Shots and Expected Goals — [FIFAUTeam stats](https://fifauteam.com/fc-26-stats-match-facts-performance/) — low-med
- **Practice Arena:** reached through Learn to Play; practising corners and switching the kick-taker are new in FC 26 — [FIFPlay Practice Arena](https://www.fifplay.com/fc-26-practice-arena/) — low-med
- **Free-kick power:** guides disagree, from about 1.5 bars close up to 3–3.5 bars for curled shots — [RealSport101](https://realsport101.com/article/fc-26-how-to-score-free-kicks-the-best-techniques-and-dead-ball-specialists), [Team Gullit](https://www.teamgullit.com/ea-fc-26/set-pieces) — low; the page gives the range and says to find your number in the Practice Arena
- **Second man press timing:** several guides advise short bursts (one says one or two seconds) and releasing before your own tackle — sources not attributable from the excerpt — low; the page states it as a Coach's call, consistent with the Playbook's existing "teammate contain in short bursts"

## 3. Coach's calls (inference, labelled on the page)

- **Shot-selection matrix** (cutback → first-time low driven; set keeper → low driven finesse far corner; tight angle → cut back). Built on the EA facts in §1; the mapping of moment to shot is reasoning.
- **Rest defence: four behind the ball** (clip P1). Reasoning from 1.4.0's more direct Squad Battles AI.
- **Counter-press in the first seconds** (clip P2). Reasoning from 1.4.0's slower AI defender reactions; Team Press restricted to their half per the May 2026 change.
- **Second man in bursts** (clip P3). Consistent with the May 2026 teammate-contain change.
- **Decoy directed run** (clip P4). Built on EA's passing-lane through balls and the 1.1.0 directed-run note.
- **Four saved tactics by scoreline** (Control, Counter, Chase, Lock). Values sit inside EA's ranges; the choices are reasoning, to be tested in the match log.
- **Ultimate vs Legendary break-even:** from FIFAUTeam's multipliers, Ultimate pays more when u ≥ 0.74 × l (u, l = win rates), assuming similar match points. Derived, not published.
- **Weekly practice block.** Deliberate-practice structure; no source claims these numbers.

## 4. Gaps and conflicts left open

- No FC 26 penalty method could be confirmed (the composure-ring description found is from an FC 25 guide).
- Free-kick power: conflicting numbers (above).
- Ball Roll star rating: 1★ vs 2★.
- Player Lock reliability in Ultimate Team: reported broken by some players.
- Whether Skill Games remain in FC 26: excerpts disagree; the page does not depend on them.
- FC 26 updates after v1.6.6 (2026-08-06): none found by search; the 1.6.x series appears to have ended in July/August 2026.
- Heel Chop, McGeady Spin Cancel and the plain stepover are named without inputs, because no input could be read from a page.

## 5. To verify when the network allows

Open these and replace each Unconfirmed tag with a quote and a confidence level, or remove the line:

- https://www.redbull.com/ie-en/ea-fc-26-skillmoves-tricks-guide
- https://beebom.com/ea-sports-fc-26-skill-moves-and-controls/
- https://www.operationsports.com/the-best-skill-moves-in-fc-26
- https://www.destructoid.com/all-fc-26-skill-moves-and-how-to-do-them/
- https://www.operationsports.com/how-to-use-player-lock-in-ea-fc-26
- https://fifauteam.com/fc-26-stats-match-facts-performance/
- https://www.fifplay.com/fc-26-practice-arena/
- https://realsport101.com/article/fc-26-how-to-score-free-kicks-the-best-techniques-and-dead-ball-specialists
- https://www.teamgullit.com/ea-fc-26/set-pieces
- Also worth reading for more advanced material: https://www.teamgullit.com/ea-fc-26/defend-tips, https://www.fourfourtwo.com/features/ea-sports-fc-26-10-defending-tips, https://realsport101.com/article/fc-26-defending-guide-how-to-stop-conceding-easy-goals, https://www.operationsports.com/ea-fc-26-how-to-master-set-pieces-explained, https://www.fifplay.com/article-fc-26-penalty-shootout-guide/

# EA SPORTS FC 26: Xbox controls and settings, with evidence

Researched 2026-10-06. Every source below is about FC 26 unless it is labelled FC 25.

**How the quotes were collected.** ea.com blocks direct download from this environment, so every quote came through WebFetch's text extraction. Spot-check any quote before you publish it word for word. Translations of the German EarlyGame articles are marked [≈EN].

**Main findings**
- **No official EA page:** I could not confirm an official EA FC 26 controls page. It never came up in search, and fetching `ea.com/games/ea-sports-fc/fc-26/controls` directly was blocked. The inputs below come from:
  - EA's Pitch Notes, for shooting, shielding and first touch.
  - fifplay's FC 26 "Classic configuration" table.
  - Cross-checks against EarlyGame, Operation Sports and Dexerto.
- **Four FIFA 23 rows are wrong for FC 26:**
  - Driven lofted pass
  - Driven through ball
  - Driven lobbed through
  - Contain. Under FC 26's default Defending setting (Advanced), holding A is a Physical Tackle, not Contain.
- **Shooting:** Timed Finishing has been removed. Double-tapping B is now the Low Driven Shot.
- **D-pad:** Extra Striker and Striker Drop Back were removed in FC 25 and are not back in FC 26. The D-pad is now:
  - Up: Quick Tactics
  - Left: My Tactics
  - Right: Tactical Focus
  - Down: Tactical Suggestions

**Source key for the table in section 1**

| Key | Source |
|---|---|
| PN | EA Pitch Notes, FC 26 Gameplay Deep Dive, 22 Jul 2025. https://www.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-gameplay-deep-dive |
| FP | fifplay, FC 26 Controls. https://www.fifplay.com/fc-26-controls/ The page says: "the controls here in this guide refer to the Classic configuration in FC 26 settings". Its metadata says published 2025-04-10, and it contains at least one stale FC 25 row (see section 3), so a row backed only by FP is medium confidence. |
| FPd | fifplay, FC 26 Defending Tips, 14 Aug 2025. https://www.fifplay.com/fc-26-defending-tips/ |
| FPp | fifplay, FC 26 Passing Tips, 14 Aug 2025. https://www.fifplay.com/fc-26-passing-tips/ |
| EGp | EarlyGame (DE), passing guide, 15 Dec 2025. https://earlygame.com/de/guides/fifa/ea-fc-26-so-bringst-du-jeden-pass-ans-ziel It uses PlayStation buttons: X = A, △ = Y, ▢ = X, R1 = RB, L1 = LB. |
| EGd | EarlyGame (DE), defending guide, 22 Apr 2026. https://earlygame.com/de/guides/fifa/ea-fc-26-verteidigung-guide-9-profi-tipps-fuer-stabiles-defending |
| OSp | Operation Sports, passing techniques, 3 Oct 2025. https://www.operationsports.com/ea-fc-26-all-passing-techniques-explained/ |
| OSd | Operation Sports, pressing, 20 Apr 2026. https://www.operationsports.com/how-to-press-with-multiple-players-in-ea-fc-26/ |
| EA-A | EA Accessibility Resources, FC 26 (page metadata says published 14 Oct 2025). https://www.ea.com/able/resources/ea-sports-fc/fc-26 |

---

## 1. FC 26 Xbox Classic inputs compared with FIFA 23

| Action | FC 26 Xbox input | Same as FIFA 23? | Source |
|---|---|---|---|
| Ground pass | A | Yes | FP "Ground Pass / Header: A"; EGp. High |
| Driven ground pass | RB+A | Yes | FP "Driven Ground Pass \| R1 + X \| RB + A"; EGp; OSp. High |
| Lofted pass | X (the "Lob Pass / Cross / Header" row) | Yes. Caution: A,A is a different pass, the "Lofted Ground Pass" | FP; FPp. High |
| Driven lofted pass | **LB+RB+X** ("Driven Lob Pass / Driven Cross"). RB+X is now **Precision Lob Pass** | **NO** | FP "Driven Lob Pass / Driven Cross \| L1 + R1 + ▢ \| LB + RB + X" and "Precision Lob Pass \| R1 + ▢ \| RB + X"; OSp; EGp. High |
| Through ball | Y | Yes | FP; EGp. High |
| Driven through ball | **LB+RB+Y** ("Driven Through Pass"). RB+Y is now **Precision Pass** | **NO** | FP "Driven Through Pass \| L1 + R1 + △ \| LB + RB + Y" and "Precision Pass \| R1 + △ \| RB + Y"; FPp; EGp. High (one conflicting source, see section 2) |
| Lobbed through ball | LB+Y | Yes | FP "Lobbed Through Pass \| L1 + △ \| LB + Y"; EGp; OSp. High |
| Driven lobbed through | Not found as an FC 26 input. LB+RB+Y is now Driven Through Pass. The closest option is the Lofted Through Pass, Y,Y | **NO** | FP; FPp. Medium |
| Pass and go | LB+A | Yes | FP "Pass and Go \| L1 + X \| LB + A"; EGp; OSp. High |
| Call for through ball / trigger run | LB ("Trigger Run") | Yes | FP "Trigger Run \| L1 \| LB". High |
| Directed run | Tap LB, then flick RS. Tapping RB then flicking RS also works | Yes (plus an RB version) | FP "Directional Runs \| … \| Tap LB + R or RB + R (Flick in any direction)". Medium |
| Ground cross | X,X | Yes | FP "Ground Cross \| ▢ + ▢ \| X + X"; EGp; OSp. High |
| Shoot | B | Yes, but **double-tapping B is now Low Driven Shot** | PN; FP. High |
| Finesse shot | RB+B | Yes | FP; PN (Low Driven Finesse uses "RB + B"). High |
| Power shot | LB+RB+B | Yes | FP; PN. High |
| Chip shot | LB+B | Yes | FP "Chip Shot \| L1 + ◯ \| LB + B". Medium |
| Fake shot | B, then A + direction | Yes | FP "Fake Shot: B then A + Direction". Medium |
| Jockey | Hold LT | Yes (FC 26 adds a Jockey setting, Assisted or Manual) | FP "Shield / Jockey \| … \| LT Hold Down + Direction"; EGd. High |
| Sprint | RT | Yes | FP; PN ("Sprint R2 \|\| RT"). High |
| Contain | Hold A **only when Defending is set to Tactical or Legacy**. Under the default, **Advanced**, holding A is a **Physical Tackle** | **NO by default** | FP "Contain (Technical & Legacy Defending) \| X Press and Hold \| A Press and Hold" and "Physical Tackle (Advanced Defending) \| X Press and Hold \| A Press and Hold" (fifplay's "Technical" means Tactical); EA-A gives Advanced as the default; EGd. Medium-high |
| Teammate contain | Hold RB. Double-tap RB and hold for Partial Team Press | Yes | FPd; OSd; EGd. High |
| Tackle | B. Advanced Defending adds RB+B, Hard Tackle | Yes | FPd "Stand Tackle / Push or Pull (when chasing) \| ◯ \| B". Medium |
| Slide tackle | X. RB+X is Hard Slide Tackle | Yes | FPd "Sliding Tackle \| ▢ \| X". Medium |
| Keeper rush out | Hold Y | Yes | FP; FPd "Rush Goalkeeper Out \| △ Press and Hold \| Y Press and Hold". Medium |
| Switch player | LB, or flick RS | Yes, when Right Stick Switching is on its default, Classic | FP; EGd. High |
| Shield | Hold LT | Yes | PN "Hold L2 \|\| Hold LT"; FP. High |

---

## 2. Inputs new or changed in FC 26 that matter against the AI

**Shooting and finishing**

- **Low Driven Shot:** hold B to power up, then tap B again. It now works as a modifier on every shot type — "Low Driven shots will be performed by double-tapping the shot button. Low Driven is now a global* shot modifier instead of being contextual." — EA Pitch Notes Gameplay Deep Dive, https://www.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-gameplay-deep-dive, 22 Jul 2025 — high.
  - Xbox variants in the same article:
    - Lace: "B (Hold to power up) + B"
    - Finesse: "RB + B (Hold to power up) + B"
    - Power: "LB + RB + B (Hold to power up) + B"
    - Trivela and Flair: "LT + B (Hold to power up) + B"
    - Volley and header: "B (Hold to power up) + B"
  - Dexerto lists the same inputs: https://www.dexerto.com/wikis/ea-fc-26-guides-walkthrough-tips/how-to-do-low-driven-shots-headers-in-ea-fc-26/, 15 Aug 2025 — high.
- **Low Driven Shots were tuned after launch** — "Tuned Low Driven Shots based on your feedback in the Closed Beta to be less accurate when shooting with an extreme amount of power." — EA Pitch Notes, October Feedback Update, https://www.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-feedback-update-october, 17 Oct 2025 — high.
- **Timed Finishing is gone** — "Due to the changes to Low Driven, Timed Finishing has been removed." — EA Pitch Notes Gameplay Deep Dive (URL above), 22 Jul 2025 — high.
  - fut.gg agrees — "Timed Finishing has now been completely removed from the game mechanics" — https://www.fut.gg/news/top-10-gameplay-changes-coming-to-ea-sports-fc-26/, 22 Jul 2025 — high.
- **Trivela (outside-foot) shot is LT+B, and only players with the Gamechanger PlayStyle can do it** — "Trivela shots will now be connected to the new Gamechanger PlayStyle. A player without this PlayStyle will not be able to perform trivelas." — EA Pitch Notes Gameplay Deep Dive, 22 Jul 2025 — high.
  - fifplay row: "Flair Shot / Outside the Foot | L2 + ◯ | LT + B" — https://www.fifplay.com/fc-26-controls/ — medium.
  - FUTBIN: "Fancy and Trivela shots are performed with improved accuracy." — https://www.futbin.com/26/playstyles/gamechanger — medium.

**Dribbling and ball control**

- **Controlled Sprint: hold RB while dribbling** (not in the FIFA 23 table) — "Controlled Sprint | R1 | RB" — fifplay controls, https://www.fifplay.com/fc-26-controls/ — medium.
  - fifplay's attacking tips page says "RB Hold Down + Direction" — https://www.fifplay.com/fc-26-attacking-tips/, 14 Aug 2025 — medium.
  - EA confirms it exists — "Lowering Controlled Sprint Dribbling speed." — EA Pitch Notes 1.1.0, https://www.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-1-1-0-update, 23 Oct 2025 — high.
  - EA's patch notes add — "Directed runs can now be triggered during Controlled Sprint Dribble" — EA forums, v1.1.0 notes, https://forums.ea.com/blog/ea-sports-fc-game-info-hub-en/fc-26-v1-1-0-update-notes/12815780, 23 Oct 2025 — high.
- **Agile Dribbling (LT+RT) has been removed** — "We have removed the Agile Dribbling mechanic due to its low usage and to make the Shielding controls more consistent." — EA Pitch Notes Gameplay Deep Dive, 22 Jul 2025 — high.
- **Shielding was reworked; it is still hold LT** — "Shielding has been fully reworked to provide you with more consistent options and extra authentic physicality across the pitch." — EA Pitch Notes Gameplay Deep Dive, 22 Jul 2025 — high.
- **First Touch Precision: hold LT as you receive** — "Holding L2 || LT will greatly improve the players ability to control the ball at the trade-off of player's move speed." — EA Pitch Notes Gameplay Deep Dive, 22 Jul 2025 — high.
- **Loose-ball urgency: press RT** — "New ability to increase players' urgency when attempting to reach a loose ball or contested ball by pressing Sprint R2 || RT." — EA Pitch Notes Gameplay Deep Dive, 22 Jul 2025 — high.

**Passing**

- **Precision passes:**
  - RB+Y is Precision Pass.
  - RB+X is Precision Lob Pass.
  - LT+RB+Y is Precision Swerve Ground Pass.
  - What it does — "A precision pass is a deliberate technique, similar to manual passing that gives you greater control over ball placement." — fifplay, https://www.fifplay.com/fc-26-precision-pass/, 14 Aug 2025 — medium-high.
  - EarlyGame agrees on the input — "Precision Passing: R1 gedrückt halten + Dreieck. Präzise, aber weniger effektiv als andere Varianten." [≈EN: hold RB + Y; precise but less effective than the other variants] — https://earlygame.com/de/guides/fifa/ea-fc-26-so-bringst-du-jeden-pass-ans-ziel, 15 Dec 2025 — medium.
  - **Conflict:** Operation Sports gives "Precision Pass | … | L1 + △ + direction". It gives the same input for Lobbed Through Pass ("L1 + △"), so this looks like an error — https://www.operationsports.com/ea-fc-26-all-passing-techniques-explained/, 3 Oct 2025 — low.
  - **Precision Driven Pass:** not found in any FC 26 source.
  - **Related setting:** "Precision Pass Sensitivity can be set to Normal (default) or High. High sensitivity reduces assistance and makes pass direction more responsive to left stick or mouse movement." — EA Accessibility Resources, https://www.ea.com/able/resources/ea-sports-fc/fc-26 — high.
- **Lofted Through Pass is Y,Y; Lofted Ground Pass is A,A** — "Lofted Through Pass | △ + △ | Y + Y" and "Lofted Ground Pass | X + X | A + A" — fifplay controls — medium.
  - EarlyGame — "Lofted Steilass: Doppeltippen von Dreieck – Einer der stärksten Pässe in FC 26, da er über Verteidiger hinweg geht." [≈EN: double-tap Y, one of the strongest passes in FC 26 because it goes over defenders] — passing guide (URL above), 15 Dec 2025 — medium.
  - EA patch note — "Ground and Lofted Through Passes are now more respectful of your aim input and are less assisted" — EA forums, v1.1.0 notes (URL above), 23 Oct 2025 — high.
- **Through-ball aiming now uses passing lanes** — "We've introduced the concept of Passing Lanes for semi-assisted through passes. Aiming at a specific passing lane (the gap between two opponents) ensures the best target selection" — EA Pitch Notes Gameplay Deep Dive — high.
  - Same article — "First-time 135° and 180° through passes are now significantly less accurate to avoid Directed Run-related exploits." — high.
- **Driven Pass and Go: LB+RB+A** — "Driven Pass And Go | … | L1 + R1 + X" — Operation Sports, passing (URL above), 3 Oct 2025 — low. Only this source lists it.

**Crossing**

- **Cross inputs:**
  - Ground Cross: X,X (unchanged from FIFA 23)
  - Driven Ground Cross: LB+RB+X,X
  - Driven Cross: LB+RB+X
  - High Cross: LB+X
  - Flair Cross: LT+X
  - fifplay row: "Driven Ground Cross | L1 + R1 + ▢ + ▢ | LB + RB + X + X" — https://www.fifplay.com/fc-26-controls/ — medium-high.
  - EarlyGame — "Driven Ground Cross: L1+R1 gedrückt halten + Flanke doppeltippen – Die beste Variante für flache Cutbacks mit viel Tempo." [≈EN: best option for low, fast cutbacks] — passing guide, 15 Dec 2025 — medium.
  - **Early cross:** not found. **"Low cross"** as a named input: not found. Driven Ground Cross is the low, fast option.
- **Cross behaviour changed** — "adjusted Crosses to lead more in front of the target, along with increased accuracy when in easy contexts." — EA Pitch Notes Gameplay Deep Dive — high.

**Defending**

- **Second Man Press: hold RB. Partial Team Press: double-tap RB, then hold** — "By holding R1/RB." and "By double-tapping R1/RB before holding it." — Operation Sports, https://www.operationsports.com/how-to-press-with-multiple-players-in-ea-fc-26/, 20 Apr 2026 — high.
  - fifplay agrees: "Partial Team Press | R1 + R1 Press and Hold | RB + RB Press and Hold" — https://www.fifplay.com/fc-26-defending-tips/ — medium.
- **The Defending setting changes what the buttons do** — "Advanced allows players to choose tackle types using different buttons. Tactical selects the tackle contextually, and Legacy (unavailable in Competitive preset) performs tackles automatically with a single input." — EA Accessibility Resources — high.
  - Under Advanced, fifplay lists these inputs — https://www.fifplay.com/fc-26-defending-tips/ — medium:
    - Hold A: "Physical Tackle"
    - RB+B: "Hard Tackle"
    - RB+X: "Hard Slide Tackle"
  - EarlyGame agrees on A — "X/A für körperbetonte Zweikämpfe nutzen" [≈EN: use A for physical duels] — https://earlygame.com/de/guides/fifa/ea-fc-26-verteidigung-guide-9-profi-tipps-fuer-stabiles-defending, 22 Apr 2026 — medium.
- **Other defending inputs:**
  - Professional Foul — "Professional Foul | R1 + X | RB + A" — fifplay controls — medium.
  - EA confirms a professional-foul input exists — "When Off, players cannot commit professional fouls using the assigned input." — EA Accessibility Resources — high.
  - Sprint Jockey — "Sprint Jockey | L2 + R2 Hold Down | LT + RT Hold Down" — fifplay defending tips — medium.
  - Engaging a shielding dribbler — "Engage Shielding Opponent | … | LT + L Towards Shielding Dribbler" — fifplay defending tips — medium.

**Set pieces and settings**

- **Throw-ins** — "Manually request your selected throw-in taker with R1 || RB." — EA Pitch Notes Gameplay Deep Dive — high.
- **Simplified Skill Moves (a setting, off by default)** — "When On, the game will automatically perform a contextually appropriate Skill Move when players move the right stick in any of the four main directions" — EA Accessibility Resources — high.

---

## 3. D-pad quick tactics and game plans in FC 26

- **Layout** — "Quick Tactics | D-Pad UP", "My Tactics | D-Pad LEFT", "Tactical Focus | D-Pad RIGHT", "Tactical Suggestions | D-Pad DOWN" — fifplay controls, https://www.fifplay.com/fc-26-controls/ — medium-high. EarlyGame gives the same Up, Left and Right — https://earlygame.com/de/guides/fifa/ea-fc-26-guide-so-nutzt-du-das-d-pad-richtig, 1 Nov 2025.

**Quick Tactics** (press Up, then a direction)

- **Offside Trap: Up, Up** — "by pressing up twice in the D-Pad" — Operation Sports, https://www.operationsports.com/how-to-press-with-multiple-players-in-ea-fc-26/, 20 Apr 2026 — high.
- **Team Press: Up, Left** — "Team Press | D-Pad UP then LEFT" — fifplay — high.
  - Operation Sports — "By double-tapping up and then left on the direction pad" — high.
  - EarlyGame — "Team-Pressing (Pfeil nach oben + links)" — high.
- **Up, Right is most likely Overload Set Pieces.**
  - EarlyGame names the four options as "Abseitsfalle", "Team-Pressing", "Überzahl bei Standards", "Spieler in den Strafraum schicken" [≈EN: Offside Trap, Team Press, overload at set pieces, send players into the box]. It does not give directions — 1 Nov 2025 — medium.
  - fifauteam (not on the priority list) gives "Overload Set Pieces — Up, Right" — "This increases the number of players in the box during Free Kicks and Corner Kicks." — https://fifauteam.com/fc-26-smart-tactics/ (modified 13 Aug 2025) — medium-low.
  - **Conflict:** fifplay's FC 26 table says "Extra Striker | D-Pad UP then RIGHT" — low. The same row is on fifplay's FC 25 page (https://www.fifplay.com/fc-25-controls/, an FC 25 source), and EA's FC 25 notes contradict it, so the row is very likely stale.
- **Get In The Box: Up, Down** — "Get In The Box | D-Pad UP then DOWN" — fifplay — medium. EarlyGame also lists it.

**My Tactics** (press Left, then a direction)

- **Custom tactics 1 to 4** — "Custom Tactic 1 | D-Pad LEFT then UP" … "Custom Tactic 4 | D-Pad LEFT then DOWN" (2 = Left, 3 = Right) — fifplay — medium.
- **EarlyGame describes Left slightly differently** — "Nach links + oben: Wechselt zu einer alternativen Formation" [≈EN: Left then Up switches to an alternative formation] — medium.

**Tactical Focus** (press Right, then a direction)

- **Default, Defending and Attacking** — fifplay rows: "Default | D-Pad RIGHT then UP", "Defending | D-Pad RIGHT then LEFT", "Attacking | D-Pad RIGHT then RIGHT".
- **EarlyGame agrees** — "Nach rechts + links: Defensiver Fokus" / "Zweimal nach rechts: Offensiver Fokus" [≈EN: Right, Left = defensive focus; Right, Right = attacking focus] — high, since two sources agree.

**Tactical Suggestions** (press Down, then a direction)

- **Rows on fifplay** — "Tactic Suggestion 1 | D-Pad DOWN then UP", "Tactic Suggestion 2 | D-Pad DOWN then RIGHT", "Tactic / Focus Suggestion | D-Pad DOWN then LEFT", "Substitution | D-Pad DOWN then DOWN" — fifplay — medium.

**Extra Striker and Striker Drop Back**

- **Removed.** EA dropped them in FC 25 (this is an FC 25 source) — "Due to the revamp of the directional tactical menu, the following directional commands have been removed: Attacking Full Backs, Hug Sideline, Extra Striker, Striker Drop Back, Overload Ball Side." — EA Pitch Notes FC 25 FC IQ Deep Dive, https://www.ea.com/en/games/ea-sports-fc/fc-25/news/pitch-notes-fc-25-fc-iq-deep-dive, 21 Aug 2024 — high for FC 25.
- **For FC 26:** apart from fifplay's stale row, no FC 26 source shows them returning — medium-high.

**What replaced game plans**

- **Custom tactics and Tactical Focus.** EA (FC 25 source) — "In FC IQ, you can have up to five custom tactics. This means that the gameplan/mentality system from previous titles has been overhauled." — same EA FC 25 article — high for FC 25.
- **FC 26:** the FC 26 sources show the same Left/Right system — medium-high.
- **Paraphrase of the same FC 25 article:** Attacking focus raises Build-Up and Defensive Approach by one level; Defending focus lowers both.

**Unverified:** an X post from @News_FC26 says "Quick Tactics - Overload set pieces has turned to Extra Striker." I could not fetch it (robots.txt). Its ID decodes to 5 Aug 2026, which is FC 27 reveal time. I have not applied it to FC 26. https://x.com/News_FC26/status/2084796448680423824

---

## 4. FC 26 settings: names, options and recommended values

The official names and options come from EA Accessibility Resources (EA-A), https://www.ea.com/able/resources/ea-sports-fc/fc-26. The recommendations come from FC 26 guides.

**Camera**
- **Types** — "Single Player, Multiplayer, and Clubs Cameras let players choose from Tactical (default), EA Sports GameCam, Tele Broadcast, Tele, Co-Op, Classic, Dynamic, End to End, Pro, Broadcast, or Legacy." — EA-A — high.
- **Height and zoom** — "All values range from 0–20 (default 10)." / "Height adjusts overall camera height. Not available for Pro view." — EA-A — high.
- **New in FC 26: UT Competitive Camera** — "It's called UT Competitive Camera and is only available in Ultimate Team stadiums." — Red Bull, https://www.redbull.com/us-en/ea-fc-26-best-controller-and-gameplay-settings, 25 Sep 2025 — medium.
- **Recommendations.** The guides disagree on camera type, but nearly all say Height 20 and Zoom 0:
  - **Co-Op** — "Single Player Camera: Co-Op", "Height: 20", "Zoom: 0" — RealSport101 (Aakash Regmi), https://realsport101.com/article/fc-26-game-settings-best-controller-camera-settings, updated 22 Sep 2025 — medium-high.
  - **Co-Op** — "die Co-op-Kamera bleibt die beste Option" and "Stelle Höhe auf 20 und Zoom auf 0" [≈EN: Co-op is still the best; set Height 20, Zoom 0] — EarlyGame, https://earlygame.com/de/guides/fifa/ea-fc-26-die-besten-controller-einstellungen-fuer-einen-perfekten-start, 5 Dec 2025 — medium-high.
  - **Tactical first** — "Tactical": "Height: Change to 20", "Zoom: Change to 0". Its alternatives, Tele, Tele Broadcast and Co-Op, all use 20/0 — Dexerto (David Purcell), https://www.dexerto.com/wikis/ea-fc-26-guides-walkthrough-tips/best-camera-settings/, 18 Sep 2025 — medium-high.
  - **Tele Broadcast** — "Single Player Camera: Tele Broadcast", "Height: 20", "Zoom: 1" — Sportskeeda, https://www.sportskeeda.com/gaming-tech/best-ea-fc-26-controller-and-game-settings (no date shown) — medium.
  - **Tele Broadcast** — "Tele Broadcast (10–20 height, 0–10 zoom) or enable UT Competitive Camera for a standardized angle." — fifplay, https://www.fifplay.com/fc-26-camera/, 6 Sep 2025 — medium.
  - **Tele Broadcast** — "Tele Broadcast remains a favorite among the pros, with plenty of them preferring the classic single player camera over the newer 'Tactical' preset." — Red Bull, 25 Sep 2025 — medium.

**Power Shot Zoom**
- **Still a setting** — "Power Shot Zoom is set On (default) or Off. When On, applies dynamic camera movement during Power Shots." — EA-A — high.
- **Guides disagree:**
  - Off — "Power Shot Zoom: Off" — RealSport101.
  - Off — "deaktiviere den Power-Shot-Zoom" [≈EN: turn Power Shot Zoom off] — EarlyGame, 5 Dec 2025.
  - On — "Power Shot Zoom: On" — Sportskeeda.

**Radar**
- **Options** — "Radar appearance can be set as 2D or 3D. depending on user preference." — EA-A — high. fifplay also lists Off ("Radar: 2D, 3D, Off.") — https://www.fifplay.com/fc-26-game-settings/, 6 Sep 2025 — medium.
- **Recommended value:** not found in any FC 26 guide.

**Auto Switching**
- **Options** — "Auto Switching can be set to Air Balls and Loose Balls (default), Manual, Only on Air Balls, Automatic, or Only on Loose Balls." — EA-A — high.
- **Recommended: Air Balls and Loose Balls.** The guides agree:
  - "Auto Switching: On Air Balls and Loose Balls" — RealSport101 and Sportskeeda.
  - "Ensure Air Balls and Loose Balls are selected for auto switching." — Red Bull.
  - "Luftbälle und lose Bälle" [≈EN: air balls and loose balls] — EarlyGame.
- ProLeague (not on the priority list) is the only dissenter and says Manual.

**Auto Switching Move Assistance**
- **Options** — "can be set to None (default), Low, or High. When enabled, your newly controlled player continues briefly in their current direction, giving you time to adjust orientation." — EA-A — high.
- **Recommended: None.** The guides agree:
  - "Auto Switching Move Assistance: None" — RealSport101 and Sportskeeda.
  - "Am besten „Keine". So hast du die volle Kontrolle" [≈EN: None is best; it gives you full control] — EarlyGame.

**Pass Receiver Lock**
- **Options** — "Late (default), Animation Start, or Power Up. Late locks the target player as late as possible" — EA-A — high.
- **Late, the majority view:**
  - "Pass Receiver Lock: Late" — RealSport101.
  - "Ensure this is set to Late, as this will give you until the very last moment to change your mind on the direction of your pass" — Red Bull.
  - "Stelle das Pass Receiver Lock auf „Spät"" [≈EN: set it to Late] — EarlyGame.
- **Animation Start, the one dissenter** — "Pass Receiver Lock: Animation Start" — Sportskeeda.

**Next Player Switch Indicator**
- **Still exists** — "Next Player Switch Indicator can be turned On (default) or Off. When On, an indicator appears above the head of the next player who will be switched to while defending." — EA-A — high.
- **Recommended value:** not found in any FC 26 guide.
- **Related new settings:**
  - Next Player Switching — "can be set to Classic (default), Goal Side, or Closest to Ball." — EA-A. Recommended value: not found.
  - Right Stick Switching — "Classic (default), Player Rotation, or Adaptive." — EA-A. Classic is recommended by RealSport101, Sportskeeda and EarlyGame ("„Klassisch" ist hier die beste Option" [≈EN: Classic is the best option here]).

**Pass assistance**
- **Names:** FC 26 uses "Through Pass Assistance" (not "Through Ball Assistance") and "Lobbed Through Pass Assistance". Guides often shorten the second to "Lobbed Through Pass".
- **Options** — "Lob Pass Assistance can be set to Assisted (default), Semi, or Manual. These determine how much directional and power assistance is applied when executing each type of pass." The same page gives the same three options for Ground, Through, Lobbed Through and Cross assistance — EA-A — high.
- **Ground Pass Assistance: Assisted** — RealSport101; Sportskeeda; EarlyGame ("Lass diese unbedingt auf „Assistiert"" [≈EN: definitely leave it on Assisted]).
- **Through Pass Assistance: Semi** — "Through Pass Assistance: Semi" (RealSport101, Sportskeeda); EarlyGame ("Am besten auf „Semi" stellen" [≈EN: best set to Semi]).
- **Lobbed Through Pass Assistance: Semi** — "Lobbed Through Pass: Semi" (RealSport101, Sportskeeda); EarlyGame.
- **Lob Pass Assistance: Assisted** — RealSport101, Sportskeeda, EarlyGame.
- **Cross Assistance: Assisted** — RealSport101 and Sportskeeda. EarlyGame says Assisted, or Semi for more control.
- **Dissenter:** ProLeague (not on the priority list) says "set all variants to Semi."

**Shot Assistance**
- **Options** — "Shot Assistance can be selected between Assisted (default), Manual, and Precision." / "Precision provides partial assistance to help aim at the goal." — EA-A — high.
- **Guides disagree:**
  - Precision — "Shot Assistance: Precision" — RealSport101.
  - Precision — "Schusshilfe: Auf „Präzision" stellen" [≈EN: set Shot Assistance to Precision] — EarlyGame, https://earlygame.com/de/guides/fifa/ea-fc-26-10-geheime-einstellungen-die-jeder-pro-verwendet, 15 Oct 2025.
  - Assisted — "Shot Assistance: Assisted" — Sportskeeda.
  - Assisted — "„Assistent" die bessere Wahl, da es Fehler beim Abschluss reduziert" [≈EN: Assisted is the better choice because it cuts finishing errors] — EarlyGame, 5 Dec 2025.

**Timed Finishing**
- **Removed in FC 26** — see section 2 — high.
- The teamgullit FC 26 page still recommends it, which shows that page is stale: https://acc.teamgullit.com/ea-fc-26/controller-settings

**Pass Block Assistance**
- **Options** — "can be turned On (default) or Off. When On, AI- and user-controlled players attempt automatic interceptions" — EA-A — high.
- **Recommended: On** — RealSport101; Sportskeeda; EarlyGame ("Einschalten" [≈EN: turn it on]).

**Clearance Assistance**
- **Options** — "Directional (default) or Classic. Directional considers your input while selecting the earliest possible contact point." — EA-A — high.
- **Recommended: Directional** — RealSport101; Sportskeeda; EarlyGame ("Richtungsbasiert" [≈EN: directional]).

**Defending**
- **Not on the FIFA 23 page, and it decides what hold-A does** — "Defending can be set to Advanced (default), Tactical, or Legacy." — EA-A — high.
- **Guides disagree.**
- **For Tactical:**
  - "Lots of pros use Tactical Defending, which automatically selects tackle type, but this is personal preference" — Red Bull.
  - "Nutze „Tactical Defending". Nur absolute Elite-Spieler profitieren von Advanced Defending" [≈EN: use Tactical; only elite players benefit from Advanced] — EarlyGame, 5 Dec 2025.
  - RealSport101 lists "Jockey: Tactical Defending".
- **For Advanced:**
  - Sportskeeda lists "Jockey: Advanced Defending".
  - "Advanced Defending aktivieren" [≈EN: turn on Advanced Defending] — EarlyGame defending guide, 22 Apr 2026.
- **Naming problem:** RealSport101 and Sportskeeda put this under "Jockey". In EA's menu, Jockey is a separate setting.

**Jockey**
- **New setting** — "Jockey can be set to Assisted (default) or Manual." / "Assisted mode automatically adjusts player speed to stay close to opponents, while Manual gives you full control over positioning." — EA-A — high.
- **Recommended value:** not found.

**Other FC 26 options** (EA-A — high)
- **Precision Pass Sensitivity:** Normal is the default. RealSport101 and Sportskeeda recommend Normal.
- **Analog Sprint:** Off is the default. RealSport101, Sportskeeda and EarlyGame recommend Off.
- **Player Lock:** Off is the default. EarlyGame recommends turning it on: "Aktivieren, um taktische Spielzüge und Laufwege zu nutzen" [≈EN: turn it on to use tactical plays and runs].
- **Simplified Skill Moves:** Off is the default. EarlyGame recommends leaving it off.
- **Reaction Time Calibration:** on by default.
- **Save Assistance:** Semi is the default.
- **On by default:** Professional Fouls, Auto Clearances, Auto Shots, Assisted Headers, Auto Flair Pass.

**Competitive vs Authentic**
- **Where it can be chosen** — "Competitive Gameplay is mandatory/locked in FUT, Clubs, Online Seasons, and Online Friendlies. It is optional in Kick-Off and Career Mode." / "Authentic Gameplay is the default for Manager and Player Career Mode and optional in Kick Off." — EA Pitch Notes Gameplay Deep Dive, 22 Jul 2025 — high.
  - FUT's offline modes, such as Squad Battles, are therefore Competitive only. This is my inference from "locked in FUT".
- **Menu location** — the "Game Type Settings" tab — "Gameplay Type: Competitive, Authentic, Custom." — fifplay, https://www.fifplay.com/fc-26-game-settings/ — medium.
  - EA lists these under "Gameplay Style Presets" — "Competitive Preset applies the settings that are mandatory for all players in online multiplayer modes, to offline play too." — EA-A — high.
  - GameLuster (not on the priority list) gives the full path — "Go to Settings > Game Type Settings, and under Gameplay Style, change Gameplay Type to your preferred preset." — https://gameluster.com/fc-26-gameplay-presets-explained-competitive-vs-authentic/, 2 Sep 2025 — medium.
- **Effect on the AI** — Competitive: "Less AI defending, resulting in looser defensive lines". Authentic: "Greater AI defending enabled" — EA Pitch Notes Gameplay Deep Dive — high.
- **Recommended: Competitive.**
  - "Preset: Competitive" — RealSport101 and Sportskeeda.
  - "Use the competitive gameplay preset." — Red Bull.
  - Competitive preset also recommended by EarlyGame.

---

## 5. FIFA 23 recommendations: do they still hold in FC 26?

| FIFA 23 recommendation | Still in FC 26? (FC 26 name) | What FC 26 guides recommend | Verdict |
|---|---|---|---|
| Camera Co-op or Tele Broadcast, Height 20, Zoom 0 | Yes. Both are listed by EA as "Co-Op" and "Tele Broadcast". Height and Zoom run 0–20 | Co-Op 20/0 (RealSport101, EarlyGame); Tactical, Tele, Tele Broadcast or Co-Op at 20/0 (Dexerto); Tele Broadcast 20/1 (Sportskeeda) | **Keep.** Optionally mention Tactical, now EA's default |
| Power Shot Zoom Off | Yes (default On) | Off (RealSport101, EarlyGame); On (Sportskeeda) | **Keep Off** |
| Radar 2D | Yes (2D or 3D) | No FC 26 guide gives a value | **Keep as a preference.** Unverified |
| Auto Switching: Air Balls and Loose Balls | Yes (it is EA's default) | Same in every priority guide | **Keep** |
| Auto Switching Move Assistance: Low | Yes (None / Low / High) | None (RealSport101, Sportskeeda, EarlyGame) | **Change to None** |
| Pass Receiver Lock: Late | Yes (default Late) | Late (RealSport101, Red Bull, EarlyGame); Animation Start (Sportskeeda) | **Keep** |
| Ground Pass Assistance: Assisted | Yes | Assisted (RealSport101, Sportskeeda, EarlyGame) | **Keep** |
| Through Ball Assistance: Semi | Renamed **Through Pass Assistance** | Semi (RealSport101, Sportskeeda, EarlyGame) | **Keep the value; rename** |
| Lobbed Through Assistance: Semi | Renamed **Lobbed Through Pass Assistance** | Semi (RealSport101, Sportskeeda, EarlyGame) | **Keep the value; rename** |
| Shot Assistance: Assisted | Yes, with a new third option, Precision | Split: Assisted (Sportskeeda, EarlyGame Dec 2025) vs Precision (RealSport101, EarlyGame Oct 2025) | **Keep Assisted.** Note Precision as the alternative |
| Timed Finishing: Off | **Removed** | — | **Delete.** Replace with: "double-tap B = Low Driven Shot" |
| Next Player Switch Indicator: On | Yes (default On) | No FC 26 guide gives a value | **Keep** |

**Settings to add to the page:**
- **Defending:** Advanced is the default. Choose Tactical if the page keeps teaching hold-A Contain.
- **Jockey:** Assisted or Manual.
- **Gameplay Type:** Competitive or Authentic, in Game Type Settings.
- **UT Competitive Camera:** Ultimate Team stadiums only.

---

## URLs used

**EA (official)**
- https://www.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-gameplay-deep-dive
- https://www.ea.com/able/resources/ea-sports-fc/fc-26
- https://www.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-1-1-0-update
- https://forums.ea.com/blog/ea-sports-fc-game-info-hub-en/fc-26-v1-1-0-update-notes/12815780
- https://www.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-feedback-update-october
- https://www.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-title-update-1-4-0 (checked; no control changes)
- https://ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-launch-update (checked; no control changes)
- https://www.ea.com/en/games/ea-sports-fc/fc-25/news/pitch-notes-fc-25-fc-iq-deep-dive (**FC 25 source**)

**Priority guides**
- https://www.fifplay.com/fc-26-controls/
- https://www.fifplay.com/fc-26-passing-tips/
- https://www.fifplay.com/fc-26-attacking-tips/
- https://www.fifplay.com/fc-26-defending-tips/
- https://www.fifplay.com/fc-26-precision-pass/
- https://www.fifplay.com/fc-26-camera/
- https://www.fifplay.com/fc-26-game-settings/
- https://www.fifplay.com/fc-25-controls/ (**FC 25 source**, used only to show the stale Extra Striker row)
- https://www.dexerto.com/wikis/ea-fc-26-guides-walkthrough-tips/best-camera-settings/
- https://www.dexerto.com/wikis/ea-fc-26-guides-walkthrough-tips/how-to-do-low-driven-shots-headers-in-ea-fc-26/
- https://realsport101.com/article/fc-26-game-settings-best-controller-camera-settings
- https://www.sportskeeda.com/gaming-tech/best-ea-fc-26-controller-and-game-settings
- https://www.fut.gg/news/top-10-gameplay-changes-coming-to-ea-sports-fc-26/
- https://www.futbin.com/26/playstyles/gamechanger
- https://www.operationsports.com/ea-fc-26-all-passing-techniques-explained/
- https://www.operationsports.com/how-to-press-with-multiple-players-in-ea-fc-26/
- https://earlygame.com/de/guides/fifa/ea-fc-26-die-besten-controller-einstellungen-fuer-einen-perfekten-start
- https://earlygame.com/de/guides/fifa/ea-fc-26-10-geheime-einstellungen-die-jeder-pro-verwendet
- https://earlygame.com/de/guides/fifa/ea-fc-26-guide-so-nutzt-du-das-d-pad-richtig
- https://earlygame.com/de/guides/fifa/ea-fc-26-so-bringst-du-jeden-pass-ans-ziel
- https://earlygame.com/de/guides/fifa/ea-fc-26-verteidigung-guide-9-profi-tipps-fuer-stabiles-defending

**Other sources (not on the priority list; used only for corroboration or to show disagreement)**
- https://www.redbull.com/us-en/ea-fc-26-best-controller-and-gameplay-settings
- https://www.redbull.com/us-en/fc-26-meta-guide-tactics-dribbling-attacking
- https://fifauteam.com/fc-26-smart-tactics/
- https://fifauteam.com/fc-26-controls/
- https://gameluster.com/fc-26-gameplay-presets-explained-competitive-vs-authentic/
- https://insider-gaming.com/ea-fc-26-competitive-authentic-gameplay-explained/
- https://proleague.de/en/news/the-best-settings-for-ea-sports-fc-26
- https://acc.teamgullit.com/ea-fc-26/controller-settings (stale; still recommends Timed Finishing)
- https://acc.teamgullit.com/ea-fc-26/passing

**Tried but could not read**
- https://www.ea.com/games/ea-sports-fc/fc-26/controls (fetch not permitted)
- https://www.thegamer.com/ea-sports-fc-26-best-camera-controller-settings/ (blocked by robots.txt)
- https://www.magicgameworld.com/ea-fc-26-how-to-use-quick-tactics-for-smarter-gameplay/ (403 error)
- https://x.com/News_FC26/status/2084796448680423824 (blocked by robots.txt)

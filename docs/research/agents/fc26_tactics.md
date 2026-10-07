# EA SPORTS FC 26: tactics, roles, PlayStyles, AcceleRATE and the meta against the AI

Research date: 2026-10-06. Scope: FC 26 only. Anything from FC 25 is marked **[FC 25]**. FC 27, FC 24 and FIFA 23 sources were left out (see the end).

**How to read this.** Each finding is written as: claim — "verbatim quote" — [source tag, date] — confidence. Each tag is listed with its name, date and URL in the Source key at the end. "…" marks a quote I trimmed. **Inference** marks my own mapping where no source states it.

**Limits on the evidence:**
- curl to ea.com was blocked by the network policy, so all EA text was pulled through a fetch tool that caps each quote at about 125 characters. The quotes are verbatim fragments, but I could not check them character by character against the live page.
- No EA Help article on FC 26 tactics was found.
- No guide from a priority outlet was found on beating the Legendary or Ultimate CPU in FC 26. The evidence about the CPU comes mostly from EA's patch notes and from community posts (low confidence).
- The search budget ran out before I found a second complete FC 26 list of roles and focuses.

---

## 1. Team Tactics in FC 26

The team-level fields are Formation, Build-Up Style, Defensive Approach and Line Height. On top of those sit a Role and Focus for each player and the set-piece assignments. Width, Players in Box and Chance Creation do not exist (see §3).

- FC 26 keeps the FC IQ system from FC 25, and FC 25 tactic codes still work — "FC 25 tactics codes are compatible with FC 26 and will be converted to the FC26 format when applied" — [S1, 22 Jul 2025] — high
- What EA says the FC 26 changes aim at — "covering gaps in positions/Roles, and adding a couple of new elements that better match real football" — [S1] — high

**Build-Up Style** (3 options; no default found)
- **Short Passing** — "Players will come short to support the ball carrier rather than make forward runs." — [S28; same wording in S15 FC 25, which tags it "come short" / "Transition time: patient"] — high
- **Balanced** — "Players will vary between forward runs and coming short. The team's transition to their in-possession shape will be steady." — [S28] — high
  - Changed in FC 26 — "Balanced Build Up - teams will have a more balanced approach, giving you run options as well as close-support options" — [S1] — high
- **Counter** — "Encourages players to get in behind the opposition's defense as the team transitions quickly." — [S28; S15 FC 25 tags it "forward runs" / "quick"] — high

**Defensive Approach** (4 options; each one sets a Line Height range)
- The ranges and defaults below come from EA **[FC 25]** [S15]. FIFAUTeam's FC 26 page [S28] repeats the same values. Confidence: high for FC 25, medium-high for FC 26.
- **Deep** — Line Height 1–30, default 25 — "A safety-first approach, with the defensive line dropping deeper to mark the opposition." — [S28] — EA FC 25 tags: "Run Tracking: line will drop with runs", "Pressure: none"
- **Balanced** — Line Height 31–60, default 50 — "Provides flexibility on how deep they drop and which runs to track." — [S28] — EA FC 25: "Pressure: none"
- **High** — Line Height 61–90, default 70 — "A riskier approach applying situational pressure, adopting a high line that tends not to track runs." — [S28] — EA FC 25: "Pressure: minimal"
- **Aggressive** — Line Height 91–100, default 95 — "Most front-footed approach, adopting a high line focusing on immediate press and offside traps." — [S28] — EA FC 25 tags: "Pressure on heavy touch", "Extra stamina drain"
- The default Defensive Approach itself: not found.

**Line Height**
- Line Height can be adjusted inside the chosen approach. A pro guide sets "Custom 60 - (press triangle/Y to adjust)" — [S42, 2 Oct 2025] — med

**What changed from FC 25** (all from [S1, 22 Jul 2025], high unless noted)
- Line Height is now saved — "Line Height gets saved to the Tactics Code"
- You can store more codes — "Can have up to 10 different Codes saved…"
- Codes work across modes — "Works in/between Ultimate Team, Career Mode, Kick-Off, Seasons, Friendlies."
- Tactical Suggestions keep your formation — "Tactical Suggestions will work with your existing formation…" and "Your formation will never change when accepting a Tactical Suggestion."
- New squad-screen views — "Out-of-Position Indicator and With/Without Ball View in Squad"
- A new chart — "Spider-chart Tactical Breakdown to help understand your tactic's strong/weak points at a glance"
- New set-piece assignments:
  - Attacking corners: Top of Box, Defensive Cover
  - Defending corners: Threat Marker, Post Watcher, Near Post, Back Post
  - Throw-ins: Left Throw-in Taker, Right Throw-in Taker
- The AI defensive line pushes up less — "Defensive Line Height - the defensive line will not automatically push up as far when trying to keep players offside"
- Attacking runs — "Increased the number of attacking runs"
- In-match Team Press was retuned on 28 May 2026 — "Reduced pressure on the ball carrier when Team Press is activated in the defensive half." — [S17, 28 May 2026] — med-high

---

## 2. Player Roles in FC 26

**New roles**
- The four new roles are named by EA — "The new Player Roles in FC 26 - Ball-Playing Keeper, Wide Back, Inverted Wingback, and Box Crasher" — [S1] — high
- **Ball-Playing Keeper** (GK) — "…supports build-up play as a passing option and stays on their line when their team is in defense." — [S1] — high
- **Wide Back** (CB) — "A central defender who opens wide to cover for the fullbacks." — [S1] — high
- **Inverted Wingback** (FB) — "…gets forward and adopts a central position high up the pitch when their team has the ball" — [S1] — high
- **Box Crasher** (CDM) — "A defensive midfielder who can get forward to join the attack, making trailing runs into the box…" — [S1] — high

**New Versatile focus**
- What it is — "New Focus - Versatile. Replaces 'Complete'." … "Can essentially perform whichever focus is more appropriate at the moment." — [S1] — high
- Which roles get it — "Added to Fullback, Classic 10, Winger, Poacher, Advanced Forward" — [S1] — high

**Roles are less strict in FC 26**
- "Players are less constrained by their Roles. If the opportunity presents itself, they can go beyond it…" — [S1] — high
- "All players will be more likely to make the best attacking run options instead of strictly following what their player Role dictates" — [S1] — high

**What Role, Role+ and Role++ mean**
- Definitions **[FC 25]**:
  - Base Role: "A base role means the player can play that Role. They are competent in that Role."
  - Role+: "…accomplished in the Role."
  - Role++: "'++' sign indicates the player is a world-class player in this role."
  - — [S15, 21 Aug 2024] — high
- How they affect positioning **[FC 25]** — "Players have more options and improved behaviors the higher the level of familiarity they possess in the Role." — [S15] — high
  - EA says familiarity "can account for 10% to 40% of the result".
  - In attack it affects the type and timing of runs and where players take up position.
  - In defence it affects "Marking reaction time, Marking distance, Cover distance… press tightness, Run tracking".
  - It also affects how fast players switch between attack and defence: "The lower the Familiarity the longer it takes for players to transition."
- How FC 26 retuned this — [S1] — high:
  - "Significantly improved usage of regular Roles and Roles+, to bring them closer to Roles++."
  - "Drastically reduced the negative impact of being Out of Position."
  - "Players can go beyond the 4th position in FC 26."
  - "There will be more players with Role++ throughout FC 26's cycle."
- How an FC 26 guide puts it — "Every player will have at least one Role+…" and "Having a Role+ or Role++ will heighten the effects of every player…" — [S29] — med

**Roles and their Focus options by position**
- The only complete FC 26 list I found is FIFAUTeam's [S29, updated 10 Aug 2025]. I checked it against EA's own list, which is for FC 25 [S15], and against the role/focus combinations used in FC 26 guides [S26, S27, S42, S44, S38].
- CONFLICT marks a disagreement between sources. Role names: high confidence. Focus lists: medium confidence; check the CONFLICT rows in the game.

| Pos | Role | FC 26 Focus (FIFAUTeam) | Check |
|---|---|---|---|
| GK | Goalkeeper | Defend, Balanced | Same as FC 25 |
| GK | Sweeper Keeper | Balanced, Build-Up | Same as FC 25 (Beebom FC 26 uses Balanced) |
| GK | **Ball-Playing Keeper (new)** | Build-Up | Dexerto gives no focus |
| CB | Defender | Defend, Balanced | Same as FC 25 |
| CB | Stopper | Balanced, Defend | CONFLICT: FC 25 had Balanced, Aggressive |
| CB | Ball-Playing Defender | Defend, Build-Up | CONFLICT: FC 25 also had Aggressive |
| CB | **Wide Back (new)** | Defend, Aggressive, Support | Dexerto agrees |
| FB | Fullback | Defend, Balanced, Versatile | Matches EA (Versatile added); fut.gg FC 26 uses Versatile and Defend |
| FB | Falseback | Defend, Balanced | Same as FC 25 |
| FB | Wingback | Balanced, Versatile | CONFLICT: FC 25 had Balanced, Support, and EA's FC 26 list of Versatile roles leaves out Wingback |
| FB | Attacking Wingback | Support, Attack | CONFLICT: FC 25 had Balanced, Attack |
| FB | **Inverted Wingback (new)** | Build-Up, Attack | Dexerto agrees |
| CDM | Holding | Defend, Roaming | CONFLICT: FC 25 also had Ball-Winning |
| CDM | Centre-Half | Defend | Same as FC 25 |
| CDM | Deep-Lying Playmaker | Defend, Roaming | CONFLICT: FC 25 had Defend, Build-Up, and FC 26 guides use DLP/Build-Up (fut.gg, Red Bull, Beebom), so FIFAUTeam is likely wrong here |
| CDM | Wide Half | Build-Up, Defend | Same as FC 25 |
| CDM | **Box Crasher (new)** | Balanced | Beebom FC 26 uses Box Crasher/Balanced |
| CM | Box-to-Box | Balanced, Ball Winning | CONFLICT: FC 25 had Balanced only |
| CM | Holding | Defend | CONFLICT: FC 25 had Defend, Ball-Winning |
| CM | Deep-Lying Playmaker | Defend | CONFLICT: FC 25 had Defend, Build-Up, and fut.gg FC 26 uses LCM DLP/Build-Up |
| CM | Playmaker | Attack, Roaming | Same as FC 25 |
| CM | Half-Winger | Support, Balanced, Attack | CONFLICT: FC 25 had Balanced, Attack |
| CAM | Playmaker | Balanced, Roaming | CONFLICT: FC 25 also had Build-Up |
| CAM | Shadow Striker | Attack | Same as FC 25 |
| CAM | Half-Winger | Roaming, Balanced, Attack | CONFLICT: FC 25 had Balanced, Attack |
| CAM | Classic 10 | Versatile, Wide, Attack | Matches EA (Versatile added) |
| LM/RM | Winger / Wide Midfielder / Wide Playmaker / Inside Forward | B/A/Versatile · Defend/Support/Build-Up · Attack · Balanced/Attack | CONFLICT: FC 25 Wide Midfielder had Balanced, Defend |
| LW/RW | Winger | Balanced, Attack, Versatile | Matches EA (Versatile added) |
| LW/RW | Inside Forward | Balanced, Attack, Roaming | Same as FC 25 |
| LW/RW | Wide Playmaker | Attack | CONFLICT: FC 25 had Attack, Build-Up |
| ST | Advanced Forward | Attack, Versatile | CONFLICT: FC 25 had Attack, Complete, Support (Complete is now Versatile; Support unclear) |
| ST | Poacher | Attack, Versatile | CONFLICT: FC 25 had Attack, Support |
| ST | Target Forward | Balanced, Attack, Wide | Same as FC 25 |
| ST | False 9 | Build-Up, Attack | CONFLICT: FC 25 had Build-Up only |

**Positions removed in FC 25** — "…no longer present in FC 25: The CF and LWB/RWB positions, Work Rate, Player Instructions" — [S15, FC 25] — high

---

## 3. Translating our FIFA 23 settings into FC 26

### Formation "4-3-3 (Attack)": two CMs plus a CAM

- **In Ultimate Team it is "4-3-3 (4)"** — high confidence on the shape, medium on the label.
  - fut.gg's FC 26 4-3-3(4) uses a Shadow Striker at CAM, a DLP at LCM and a Box-to-Box at RCM. Its CAM is described as "Links midfield, runs beyond ST." — [S26, 16 Feb 2026]
  - Beebom's FC 26 "4-3-3 (4)" section uses two Box-to-Box CMs and a Playmaker at CAM — [S44, 19 Sep 2025]
  - fifplay tags its "4-3-3 (4)" page "Ultimate Team" — [S34]
- **In Kick-off it is "4-3-3 Attack"** — med.
  - fifplay's formations page has "Kick Off" and "FUT" filters.
  - Its "4-3-3 Attack" page is tagged "Kickoff" and uses the diagram file `4-3-3-(4).jpg` — [S34]
  - Career Mode naming is not confirmed separately — med-low.
  - EA source for the name: not found.
- **The 4-3-3 variants in FC 26** — fifplay lists 45 formations. Each Kick Off page reuses the matching numbered diagram:

  | Kick Off name | Diagram file used | UT name | Shape |
  |---|---|---|---|
  | 4-3-3 Flat | `4-3-3.jpg` | 4-3-3 | three CMs |
  | 4-3-3 Holding | `4-3-3-(2).jpg` | 4-3-3 (2) | one CDM and two CMs (matches fut.gg's FC 26 4-3-3 (2): CDM DLP plus two Box-to-Box) |
  | 4-3-3 Defend | `4-3-3-(3).jpg` | 4-3-3 (3) | not confirmed for FC 26 |
  | 4-3-3 Attack | `4-3-3-(4).jpg` | 4-3-3 (4) | two CMs and a CAM |

  - FIFA 23's 4-3-3 (5) / False 9 is not in the FC 26 list. That fits EA removing the CF position in FC 25 (quote in §2).
  - Confidence: med for the name pairings, high for the CF removal.
- **Caution on fifplay:** its written descriptions are wrong in places. It calls 4-3-3 (4) "a flat three-man midfield" and says 4-3-3 (3) is "built around a central attacking midfielder (CAM)". Use the diagrams, fut.gg and Beebom instead.
- **Caution on naming:** some FC 26 Ultimate Team guides use descriptive names instead, e.g. Dexerto's "4-2-3-1 (Wide)" and Red Bull's "4-2-3-1 Wide". So the exact label the game shows in Ultimate Team is unconfirmed.

### Custom Tactics

- **Defensive Style became Defensive Approach** — "Transformed: Defensive Style" — [S15, FC 25] — high
  - Our **Balanced** maps to **Balanced**: Line Height 31–60, default 50 — high
  - **Pressure on Heavy Touch** is no longer an option on its own. EA lists "Pressure on heavy touch" as a trait of **Aggressive**, along with Line Height 91–100 and "Extra stamina drain" — [S15, FC 25] — med-high
  - **Inference:** you can no longer combine heavy-touch pressure with a medium-depth line.
- **The Width slider is gone** — "Removed: Defensive Width" / "Removed: Attacking Width" — [S15, FC 25] — high
  - Width now comes from the shape — "Things like your formation, the Roles assigned, and how much wide attacking support or wide defensive coverage you have are all important." — [S15] — high
  - No FC 26 source lists a Width setting — med-high
- **Depth became Line Height** — "Transformed: Defensive Depth" — [S15, FC 25] — high
  - **Inference:** "Depth about 10 below default" is roughly Line Height 40. That keeps the Balanced approach, whose default is 50.
  - EA gives no conversion between FIFA 23 Depth and FC 26 Line Height, so this is low-med.
- **Build Up Play became Build-Up Style** — "Transformed: Build-Up Play" — [S15, FC 25] — high
  - **Inference** from EA's descriptions (med):
    - Slow Build Up → Short Passing ("come short", "patient")
    - Balanced → Balanced
    - Fast Build Up → Counter ("forward runs", "quick")
  - **Long Ball** has no FC 26 equivalent. Counter is the closest (low confidence).
- **Chance Creation was removed** — "Removed: Chance Creation" — [S15, FC 25] — high
  - **Inference:** Build-Up Style and the roles now decide how players run and create chances.
- **Players in Box (we used 4) was removed** — "Removed: Players in Box" — [S15, FC 25] — high
  - The roles now decide how many players arrive in the box — "Flood the box. Your ST, Wingers, CAM, and RCM will all push forward." — [S26] — med

### Player Instructions

- **Player Instructions were removed and replaced by Roles and Focus** — "…no longer present in FC 25: … Player Instructions" — [S15, FC 25] — high
  - FC 26 makes roles looser still: "less constrained by their Roles" — [S1] — high
- **Full-backs on "Stay Back While Attacking" → Fullback, Defend focus** — med-high
  - EA's FC 25 description — "…prioritize protecting their own goal by staying back, holding the defensive line…" — [S15]
  - "Your backline remains astute, with fullbacks holding their positions instead of bombing forward" — [S44], Fullback/Defend
  - "RB Fullback / Focus: Defend / Forms back-three during attack." — [S26]
  - Falseback is **[FC 25]**-tagged "stays back, inverted run, no forward runs", but it tucks into midfield, so it is a poor fit (low).
- **Holding midfielder on "Stay Back While Attacking"** — med
  - The 4-3-3 (4) has no CDM slot.
  - In a CM slot, the options are:
    - **Holding (Defend)**, tagged **[FC 25]** "stay central, cover center, aggressive interceptions" and described as "…guarding their backline during attacks" — [S15]
    - **Deep-Lying Playmaker (Defend)**, tagged "stay central, cover center, stay in line" — [S15]
  - fut.gg's FC 26 4-3-3(4) uses LCM DLP/Build-Up as its deeper CM — [S26]
  - Red Bull on the DLP role at CDM: "Positionally disciplined to stop attacks, they will push forward slightly to continue attacks." — [S42] — so it is not a pure sitter.
  - For a true holding player, switch to 4-3-3 (2) / Holding. Its CDM can be Holding (**[FC 25]** "stays back") or Centre-Half ("stays back, drop between defenders") — [S15]
- **CM on "Stay On Edge Of Box For Cross"** — no equivalent found (low)
  - None of EA's FC 25 role descriptions mention the edge of the box ("absent" in [S15]).
  - The nearest thing is FC 26's "Top of Box" assignment, which applies to attacking corners only — [S1]
- **Striker and wingers on "Get In Behind"** — med-high
  - **Striker:** Poacher (**[FC 25]** tags "get in behind, stay forward, slow to come back"; FC 26 gives it the Versatile focus), or Advanced Forward ("…makes runs in behind for scoring chances") — [S15, S1]
  - **Wingers:** Inside Forward — "They tend to run in behind the defense." By contrast, Winger "will always stay wide, hugging the touchline" — [S15, FC 25]
  - **Whole team:** the Counter build-up style — "Encourages players to get in behind the opposition's defense…" — [S28]

---

## 4. PlayStyles in FC 26

**The full list.** fifplay [S35, 16 Aug 2025] and FIFAUTeam [S31, updated 1 Sep 2025] list the same names. They group a few differently.

| Category | PlayStyles |
|---|---|
| Finishing | Finesse Shot, Chip Shot, Power Shot, Dead Ball, Low Driven Shot, **Precision Header (new)**, **Gamechanger (new)**, Acrobatic |
| Passing | Incisive Pass, Pinged Pass, Long Ball Pass, Tiki Taka, Whipped Pass, **Inventive (new)** |
| Ball control | Technical, Rapid, First Touch, Trickster, Press Proven |
| Defending | Jockey, Block, Intercept, Anticipate, Slide Tackle, Bruiser, **Aerial Fortress (new)** |
| Physical | Quick Step, Relentless, Long Throw, **Enforcer (new)** |
| Goalkeeper | Far Throw, Footwork, Cross Claimer, Far Reach, Deflector, plus either "Rush Out" (FIFAUTeam) or "1v1 Close Down" (fifplay) — conflict, unresolved |

- Total count: Insider Gaming [S37] says 35, but both lists above give 36. EA's total: not found. Low confidence.

**The ones that matter against the AI** — fifplay's descriptions [S35] — med (they may be paraphrased):
- **Incisive Pass:** "Through Passes are more accurate, swerve passes have more curve."
- **Long Ball Pass:** "Lob and Lofted Through Passes are more accurate, travel faster."
- **Whipped Pass:** "All crosses are highly accurate, travel faster, and include more curve."
- **Finesse Shot:** "Performs finesse shots faster with additional curve and improved accuracy."
- **Low Driven Shot:** "Enhances ability to execute low driven shots with increased accuracy."
- **Quick Step:** "Accelerates quicker during Explosive Sprint…"
- **Jockey:** "Increased max speed of Sprint Jockey and faster transition speed."

**New, removed and renamed** — [S1] — high
- Removed: Power Header, Aerial, Trivela, Flair.
- **Precision Header** — "Refined from the former Power Header PlayStyle."
- **Aerial Fortress** — "A defensive player who dominates aerial battles only in defensive scenarios."
- **Gamechanger** — "…extraordinary and unconventional finishes, combining and refining from the former Flair and Trivela PlayStyles."
- **Inventive** — "A player specializing in creative passing, combining and refining the former Flair and Trivela PlayStyles."
- **Enforcer** — "A physical attacker who takes control through shielding and when initiating contact while dribbling."
- Trivela shots now need Gamechanger — "Trivela Shots can only be performed by players with this PlayStyle or PlayStyle+" — [S1] — high
- **Relentless** now also speeds up "short-term stamina regeneration" — [S1/S37] — high
- Why EA rebalanced: "the gap between top-tier attributes and PlayStyle effects was too wide". Its fix was to make high-attribute players "execute standard gameplay mechanics more reliably, even without the relevant PlayStyle." — [S1] — high

**What PlayStyle+ means**
- "PlayStyles+ take these traits to an elite level…" — [S31] — med
- EA's "+" versions are stronger effects of the same trait:
  - Inventive+: "Fancy and Trivela passes are performed with greatly improved accuracy."
  - Precision Header+: "Performs headers with greatly increased accuracy and power."
  - — [S1] — high
- Any limit on how many PlayStyle+ a player can have: not found.

**Buffs and nerfs from patches**
- **Launch (12 Sep 2025):** finesse shots from outside the box were toned down — "…we've reduced the top spin on these shots to ensure they can't be overused to score a goal." — [S2] — high
- **TU 1.0.4 (Oct 2025)** — [S5] — high:
  - "Addressed cases of players not being able to perform Physical Tackles, especially… (eg. Bruiser)."
  - "Addressed instances of Finesse Shots curling opposite of their intended direction."
- **TU 1.5.0 (4 Mar 2026)** — [S14] — high:
  - **Incisive Pass:** players without it but "with high attributes in Short Pass, Long Pass, and Curve" can now "contextually curve through balls"
  - **Power Shot:** "Increased Power Shot accuracy when taken with the Power Shot PlayStyle and PlayStyle+"
  - **Chip Shot:** "…perform Chip Shots with additional accuracy."
  - **Tiki Taka (nerf):** "The accuracy of ground and first-time passes with the Tiki Taka PlayStyle has been reduced."
  - **Inventive (buff):** accuracy "has been slightly increased"
- **World's Game update (28 May 2026)** — [S17/S18, mp1st copy of EA's notes] — med-high. fut.gg announced the Bruiser change in advance on 11 May 2026 [S24].
  - **Bruiser (nerf):** "Slightly reduced the boost to shoulder challenges from Bruiser and Bruiser+ PlayStyles."
  - **Enforcer (buff):** "Added a slight boost to the receiver of the shoulder challenge if they have Enforcer or Enforcer+."
  - **Intercept:** players without it but "with a 90+ Interceptions attribute rating" now get the same animations.

---

## 5. AcceleRATE in FC 26

**What changed from FC 25**
- FC 26 goes back to three types — "For FC 26, we're going back to 3 Acceleration Types to allow for a more predictable pace of play." — [S1] — high
- EA's reason — "We felt that three types were easier to understand and created a better acceleration balance." — [S1] — high

**How each type is decided** (EA, July 2025)

| Type | Requirements | Source |
|---|---|---|
| **Explosive** | "Agility minimum 65", "(Agility - Strength) >= 10", "Acceleration minimum 80", "Male height maximum 182cm (~6'0")", "Female height maximum 162cm (~5'4")" | [S1, 22 Jul 2025] — high |
| **Lengthy** | "Strength minimum 65", "(Strength - Agility) >= 4", "Acceleration minimum 40", "Male height minimum 183 cm (~6'1")", "Female height minimum 164cm (~5'5")" | [S1] — high as of July 2025 |
| **Controlled** | "any player that does not meet the other two requirements above." | [S1] — high |

- All three types now respond faster at the start — "Adjusted the early stages of all three types to be more responsive." — [S1] — high

**Patch change: TU 1.4.0 (5 Jan 2026)** — [S12/S13] — high
- EA fixed a bug — "Addressed an issue that was impacting Lengthy Acceleration Types, causing some players to not be considered lengthy."
- New Lengthy height minimum — "…the minimum Lengthy height requirement for men's players will be 185 cm, and 165 for women's players."
- Effect — "You can expect more players to have the Lengthy run type with this change."
- The other Lengthy requirements did not change: Strength ≥65, Strength−Agility ≥4, Acceleration ≥40.
- The 185 cm figure conflicts with the 183 cm in EA's July 2025 Deep Dive, and EA gives no previous value. EA also says the patch "refines the minimum and maximum height thresholds", but the new Explosive maximum height was not found.

**How each type behaves** — [S30, modified 16 Oct 2025] — med
- Explosive: "Quicker to start, but the acceleration rate slows down."
- Lengthy: "It starts slower but will thrive over longer distances."
- Controlled: "Accelerate uniformly in a controlled manner."

**Which type is meta**
- "Lengthy is the most popular of the three Accelerate types." / "…often considered overpowered." — [S30] — low-med
- That is the only source, and it gives no reasoning. No priority outlet gave an FC 26 meta verdict.

---

## 6. FC 26 meta against the AI

### How the CPU and the modes behave (EA, high confidence)

- **Which gameplay type each mode uses** — [S1] — high
  - "Competitive Gameplay is mandatory/locked in FUT, Clubs, Online Seasons, and Online Friendlies."
  - Squad Battles is part of FUT, so it uses Competitive (inference, high).
  - "Authentic Gameplay is the default for Manager and Player Career Mode and optional in Kick Off."
  - Kick-off and Career can toggle between the two.
- **Fatigue under Competitive** — [S1] — high
  - "User-controlled players are NOT AFFECTED by fatigue while being controlled."
  - "For AI players, they will have a reduction in Sprint Speed and Acceleration when fatigued…"
- **CPU teams play different styles** — [S1] — high
  - "some teams prefer to cross into the box more often, while others utilize slow buildup or fast tiki-taka attacking plays"
  - "specific teams will try to overwhelm you by pressing with multiple players at once, while others will just sit back and then press you aggressively"
  - "the CPU now powers up shots and passes the same way human players do"
- **v1.1.3 (4 Nov 2025): smarter CPU** — [S16, S10] — high. It applies to both Competitive and Authentic. The CPU will:
  - "Look for passes more often and make quicker decisions about them."
  - "Dribble more effectively with sharper turns…"
  - "Switch players on defense more often…"
- **Squad Battles CPU retuned** — high
  - November 2025: it "can hold the ball for too long and plays an overly possession based game" — [S10]
  - December 2025: it had become "too difficult and frustrating to play against, especially on higher difficulties" — [S11]
  - TU 1.4.0 (5 Jan 2026) changed it — "The CPU will now take a more proactive and attacking approach…" / "…will not focus on maintaining possession as much as before." — [S12]

### Formations, tactics and roles

- **Offline advice from a pro** — [S42, 2 Oct 2025] — med
  - "What we have learned in offline modes is to try and make the pitch as big as possible."
  - "We like to stick to a 4-2-3-1 or variation of four at the back with three central midfielders."
  - "…wide players set to the winger player role."
- **4-3-3(4) against "AI defending"** — [S26, 16 Feb 2026] — med by analogy; not tested against the CPU
  - Settings: Balanced build-up, Balanced approach, Line Height 60.
  - Roles: ST Advanced Forward/Attack · LW/RW Inside Forward/Balanced · CAM Shadow Striker/Attack · LCM DLP/Build-Up · RCM Box-to-Box/Balanced · LB Fullback/Versatile · RB Fullback/Defend · CBs Defender/Defend · GK Goalkeeper/Defend.
  - It targets human opponents, not the CPU: "…opponents who rely on AI defending while controlling only their CDMs…"
  - Why it works: "This overwhelms players who rely on AI auto-blocks."
  - Weakness: "It struggles against narrow, midfield-dominant formations like 4-1-2-1-2 Narrow or 4-3-2-1…"
- **4-3-3 (2) Ultimate Team meta** — Short Passing, Balanced, Line Height 50; ST Advanced Forward/Attack, wingers Inside Forward/Roaming, CMs Box-to-Box/Balanced, CDM DLP/Build-Up, FBs Fullback/Balanced — [S27, 25 Mar 2026] — med (aimed at human opponents)
- **Dexerto's Ultimate Team pick** — 4-2-1-3 is "easily the most balanced setup" (Counter, line 40) — [S39, dated 26 Aug 2026] — low-med for the CPU
- **Community, Squad Battles** — [S46, about Jan 2026] — low
  - "I play 4-2-3-1 wide, finesse+ on striker and cam, 88 pace on striker...spam runs from deep and easy finesse finish"
  - "let them through your defence a bit rather than let them pass around"
  - TU 1.4.0 made the CPU less possession-heavy, so this second tip may be out of date.
- **Difficulty levels** — FIFAUTeam gives a table, e.g. Ultimate "Attacking Intelligence 100%… Reaction Speed 100%" — [S33] — low. The page is dated Feb 2025 and is not EA data.

### Best way to attack

- **Tempo and first-time passing** — [S43, 12 Feb 2026] — med (aimed at human opponents)
  - "…fast counter-attacks built around quick triangular passing as one of the strongest attacking approaches in FC 26."
  - "First-time passes, in particular, are extremely powerful."
  - "Playing too slowly is counterproductive in FC 26."
  - EA backed this up in TU 1.5.0 — "Improved accuracy and speed of ground passing…" — [S14] — high
- **Through balls** — high
  - "Ground and Lofted Through Passes are now more respectful of your aim input and are less assisted." — [S7, 23 Oct 2025]
  - "Improved Through Pass Targets" (semi-assisted passes aim at gaps between opponents) — [S1]
  - "Improved through passing and crossing to better respect your aim input." — [S8]
- **Lobbed through balls** — high
  - "Reduced the accuracy of lofted passes." — [S14]
  - "Lowered headed lobbed through pass and cross accuracy." — [S7]
  - "Lob passes will have more driven trajectories when the path is unobstructed." — [S1]
- **Low driven shots** — high
  - "In FC 26, Low Driven shots will be performed by double-tapping the shot button." — [S1]
  - "Due to the changes to Low Driven, Timed Finishing has been removed." — [S1]
  - "Tuned Low Driven Shots… to be less accurate when shooting with an extreme amount of power." — [S3]
  - "Low driven shots are faster and harder for goalkeepers to save compared to normal shots." — [S40] — med
- **Finesse shots**
  - The outside-the-box nerf at launch — [S2] — high
  - "Cut inside for Finesse Shot angles or driven passes across box." — [S26] — med
  - Community reports of finesse+ working in Squad Battles — [S46] — low
- **Power and chip shots** — [S14] — high
  - "Improved the trajectory of Power Shots to increase the potential of scoring from longer ranges."
  - Chip shots: "Tuned Chip Shots to be less likely to go wide."
- **Crosses** — high
  - "adjusted Crosses to lead more in front of the target, along with increased accuracy" — [S1]
  - "Lowered crossing ball trajectory height to reduce the amount of crosses that were keeping the ball in the air…" — [S9]
  - Headers depend on strength — "The effectiveness of the Box Out is based on the Strength difference between the two players." — [S1]
- **Cutbacks:** no FC 26 source rates them — not found.
- **Runs into the box** — "Slightly increased frequency of AI teammate attacking runs into the box." — [S8] — high
  - The Red Bull guide says to use L1/LB runs and the R1/RB call-short — [S43] — med
- **Skill moves and dribbling** — Red Bull [S43] — med:
  - Effective: ball roll, McGeady Spin Cancel, step over
  - "Both Elastico variations are largely ineffective."
  - "Left-stick dribbling has also become more effective again in FC 26…"
  - "Players with these traits – particularly Quick Step – perform these actions more effectively."
- **Skill move changes from EA** — high
  - "Increased the speed of Fake Shot, Heel Chop, and Feint and Exit by 5%" — [S14]
  - Lane Change was made "faster" — [S1]

### Best way to defend

- **Jockey** — high
  - "improved Jockey movement to be more agile and responsive" — [S1]
  - "Slightly increased Sprint Jockey speed…" and "Moderately increased Jockey and Sprint Jockey responsiveness…" — [S6/S7, 23 Oct 2025]
- **AI teammates defend less for you** — high
  - "Slightly reduced how tightly AI defenders will mark pass receivers on the edge of their box." — [S8/S10]
  - EA's reason: users "could sometimes sit back on defense and let AI teammates do the hard work" — [S10]
  - TU 1.4.0: "reduce the reaction times of AI defenders when marking the ball carrier…" — [S12]
  - **Inference:** defending manually matters more than it did in FIFA 23.
- **Tackling** — [S1] — high
  - "Tackles From Behind - reduced the effectiveness of tackling from behind the dribbler"
  - The delay after a missed tackle is now "more consistent".
  - Strength now decides shoulder challenges — "Shoulder challenges between players with a large Strength Attribute difference will more often result in stumbling." — [S12]
- **Teammate contain and Team Press** — [S17] — med-high
  - When you are marking the ball carrier yourself, AI defenders "will no longer double-team the ball carrier"
  - When your defender is further away, they "will attempt to contain the ball carrier"
  - FIFAUTeam's "second man press" tip gets the button names wrong — [S32] — low
- **Line height**
  - "The custom 60 setting for defensive approach is the highest your defensive line can be without taking unnecessary risks." — [S42] — med
  - The AI line now pushes up less for offsides — [S1] — high
- **Pressing:** Aggressive costs "Extra stamina drain" — [S15, FC 25] — med. FC 26 detail: not found.

---

## 7. Checking our FIFA 23 squad advice against FC 26

- **"Lengthy striker"** — **partly supported, but the definition has changed.**
  - Lengthy now needs Strength ≥65, Strength−Agility ≥4, Acceleration ≥40 and, since TU 1.4.0, a height of at least 185 cm for men or 165 cm for women — [S12] — high
  - Strength pays off in FC 26 — high:
    - Box Outs depend on strength — [S1]
    - "players with higher Strength and Aggression Attributes can generally be better at shielding the ball." — [S12]
  - "Lengthy is the most popular…" — [S30] — low-med
  - The counterpoint is quick strikers in fast combination play — [S43, S46] — med/low
  - Wording suggestion: say "a tall (185 cm+), strong striker".
- **"Explosive or Controlled wingers and full-backs"** — **not addressed by any FC 26 source.**
  - The reasoning still holds: Explosive is "Quicker to start…" — [S30] — med
  - EA made the early phase of all three types more responsive, which may narrow the gap (inference) — [S1]
  - Controlled is now simply everyone who isn't Explosive or Lengthy — [S1] — high
- **"Quick defenders"** — **not directly addressed.**
  - EA: "Attacker Vs Defender Speed - improved the speed differentiation between Attackers versus Defenders to achieve an improved balance." — [S1] — high as a fact, but EA doesn't say which way it changed things.
  - Slower AI defender reactions since TU 1.4.0, plus pace loss for tired AI-controlled players under Competitive, both make the pace of the defender you control more valuable (inference) — [S12, S1]
- **"Quick full-backs and tall centre-backs"**
  - Tall centre-backs: **supported indirectly.**
    - "Player Height - adjusted animation consistency and speed for players based on height to balance the performance between tall and short players." — [S1]
    - The new Aerial Fortress PlayStyle — [S1]
    - Strength decides Box Outs — [S1]
    - Confidence: high for these facts, medium for the verdict.
  - Quick full-backs: **not addressed.**
- **"Pace up front"** — **supported** (med).
  - "fast counter-attacks… one of the strongest attacking approaches in FC 26" — [S43]
  - "88 pace on striker... spam runs from deep" — [S46] — low
  - "Acceleration and Sprint Speed remain the primary factors determining a player's overall speed." — [S30] — med
  - In Squad Battles (Competitive), fatigue does not slow the player you control — [S1] — high

### Sources not to use for the page

- **fifplay, "Best Attacking Formations in FC 26"** [S36, 10 Sep 2025] still recommends settings that don't exist in FC 26: "Mix 'Fast Build Up'…", "Forward Runs"/"Possession", and width 60–70.
- **The Online Gooner** [S45, 18 Jun 2026] describes "4-3-3 Attack" as "1 CDM (anchor) and 2 CMs" and recommends "Cover Centre" instructions. Both contradict EA and the FC 26 guides above.
- **fifplay's per-formation write-ups:** see the caution in §3.
- **soccergaming** [S21] dates the Bruiser/Enforcer change to TU 1.5.5 (7 May 2026). mp1st's notes for 1.5.5 [S19] contain no gameplay lines, and its 28 May notes [S17/S18] do contain the change. Go with 28 May.

---

## Source key and every URL used

**EA, FC 26**
- S1 EA, FC 26 Pitch Notes: Gameplay Deep Dive (22 Jul 2025) — https://www.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-gameplay-deep-dive
- S2 EA, FC 26 Launch Update Pitch Notes (12 Sep 2025) — https://www.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-launch-update
- S3 EA Forums, v1.0.2 notes (25 Sep 2025) — https://forums.ea.com/blog/ea-sports-fc-game-info-hub-en/fc-26-version-1-0-2-update-notes/12651602
- S4 EA Forums, v1.0.3 notes (about 2 Oct 2025) — https://forums.ea.com/blog/ea-sports-fc-game-info-hub-en/fc-26-version-1-0-3-update-notes/12696716
- S5 EA Forums, v1.0.4 notes (about 10 Oct 2025) — https://forums.ea.com/blog/ea-sports-fc-game-info-hub-en/fc-26-version-1-0-4-update-notes/12726867
- S6 EA, v1.1.0 Pitch Notes (23 Oct 2025) — https://www.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-1-1-0-update
- S7 EA Forums, v1.1.0 notes (23 Oct 2025) — https://forums.ea.com/blog/ea-sports-fc-game-info-hub-en/fc-26-v1-1-0-update-notes/12815780
- S8 EA Forums, v1.2.0 notes (Nov 2025; exact date not shown) — https://forums.ea.com/blog/ea-sports-fc-game-info-hub-en/ea-sports-fc-26-version-1-2-0-update-notes/12906902
- S9 EA Forums, v1.3.0 notes (Dec 2025; exact date not shown) — https://forums.ea.com/blog/ea-sports-fc-game-info-hub-en/ea-sports-fc-26-version-1-3-0-update-notes/12977359
- S10 EA, November Feedback Update (25 Nov 2025) — https://www.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-feedback-update-november
- S11 EA Forums, December Feedback Update by EA_Vendcera (date not shown) — https://forums.ea.com/discussions/fc-26-feedback-en/fc-26-december-feedback-update/13057507
- S12 EA, Title Update v1.4.0 Pitch Notes (5 Jan 2026; careers.ea.com mirror) — https://careers.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-title-update-1-4-0
- S13 EA Forums, v1.4.0 notes (5 Jan 2026) — https://forums.ea.com/blog/ea-sports-fc-game-info-hub-en/ea-sports-fc-26-version-1-4-0-update-notes/13073501
- S14 EA, Title Update v1.5.0 Pitch Notes (4 Mar 2026) — https://www.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-title-update-1-5-0

**EA, FC 25 (labelled)**
- S15 **[FC 25]** EA, FC 25 FC IQ Deep Dive (21 Aug 2024) — https://www.ea.com/games/ea-sports-fc/fc-25/news/pitch-notes-fc-25-fc-iq-deep-dive

**Patch-note copies**
- S16 mp1st, v1.1.3 CPU AI changes (4 Nov 2025) — https://mp1st.com/?p=298241
- S17 mp1st, World's Game update notes (28 May 2026) — https://mp1st.com/title-updates-and-patches/ea-sports-fc-26-update-may-28-patch-1-000-025-the-worlds-game-content
- S18 mp1st, World's Game patch 1.25 (28 May 2026) — https://mp1st.com/title-updates-and-patches/ea-sports-fc-26-the-worlds-game-update-released-patch-1-25
- S19 mp1st, v1.5.5 (8 May 2026) — https://mp1st.com/title-updates-and-patches/ea-sports-fc-26-update-may-8-applies-version-1-5-5-patch-1-24-1-000-023
- S20 mp1st, v1.6.2 (16 Jun 2026; no gameplay changes) — https://mp1st.com/title-updates-and-patches/ea-sports-fc-26-version-1-6-2-released-on-june-16-update-1-27-1-000-027
- S21 soccergaming, TU 1.5.5 (7 May 2026) — https://soccergaming.com/fc-26-title-update-1-5-5-full-patch-notes/
- S22 soccergaming, TU 1.5.3 (7 Apr 2026; goalkeeper back-pass fix only) — https://soccergaming.com/fc-26-title-update-1-5-3-full-patch-notes-and-key-changes/
- S23 soccergaming, TU 1.6.4 (no gameplay changes) — https://soccergaming.com/fc-26-title-update-1-6-4-patch-notes-released/

**Guides**
- S24 fut.gg, Bruiser nerf preview (11 May 2026) — https://www.fut.gg/news/bruiser-shoulder-barges-finally-nerfed-in-upcoming-fc-26-feedback-update/
- S25 fut.gg, Top 10 FC 26 gameplay changes (22 Jul 2025) — https://www.fut.gg/news/top-10-gameplay-changes-coming-to-ea-sports-fc-26/
- S26 fut.gg, 4-3-3(4) "Break AI Defending" (16 Feb 2026) — https://www.fut.gg/news/4-3-34-custom-tactics-the-hyper-aggressive-setup-to-break-ai-defending-in-fc-26/
- S27 fut.gg, Meta 4-3-3 (2) (25 Mar 2026) — https://fut.gg/news/meta-4-3-3-2-custom-tactics-the-best-balanced-possession-setup-in-fc-26
- S28 FIFAUTeam, FC 26 Tactics (modified 10 Aug 2025) — https://fifauteam.com/fc-26-tactics/
- S29 FIFAUTeam, FC 26 Roles (updated 10 Aug 2025) — https://fifauteam.com/fc-26-roles/
- S30 FIFAUTeam, FC 26 AcceleRATE (modified 16 Oct 2025) — https://fifauteam.com/fc-26-accelerate/
- S31 FIFAUTeam, FC 26 PlayStyles (modified 1 Sep 2025) — https://fifauteam.com/fc-26-playstyles-guide/
- S32 FIFAUTeam, FC 26 Defending (no date) — https://fifauteam.com/defend-fc-26/
- S33 FIFAUTeam, FC 26 Difficulty Levels (dated 12 Feb 2025) — https://fifauteam.com/fc-26-difficulty-levels-explained/
- S34 fifplay, FC 26 Formations (no date), plus the variant pages:
  - https://www.fifplay.com/fc-26/formations/
  - https://www.fifplay.com/fc-26/formations/4-3-3-attack/
  - https://www.fifplay.com/fc-26/formations/4-3-3-4/
  - https://www.fifplay.com/fc-26/formations/4-3-3-holding/
  - https://www.fifplay.com/fc-26/formations/4-3-3-defend/
  - https://www.fifplay.com/fc-26/formations/4-3-3-flat/
  - https://www.fifplay.com/fc-26/formations/4-3-3-3/
  - https://www.fifplay.com/fc-26/formations/4-2-3-1-wide/
- S35 fifplay, FC 26 PlayStyles (16 Aug 2025) — https://www.fifplay.com/fc-26-playstyles/
- S36 fifplay, Best Attacking Formations in FC 26 (10 Sep 2025; flagged above) — https://www.fifplay.com/fc-26-best-attacking-formations/
- S37 Insider Gaming, FC 26 PlayStyle changes (22 Jul 2025) — https://insider-gaming.com/every-ea-fc-26-playstyle-change-explained/
- S38 Dexerto, new FC 26 roles (22 Sep 2025) — https://www.dexerto.com/wikis/ea-fc-26-guides-walkthrough-tips/all-new-player-roles-explained/
- S39 Dexerto, best formations and custom tactics (dated 26 Aug 2026) — https://www.dexerto.com/wikis/ea-fc-26-guides-walkthrough-tips/best-formations-and-custom-tactics/
- S40 Dexerto, low driven shots and headers (15 Aug 2025) — https://www.dexerto.com/wikis/ea-fc-26-guides-walkthrough-tips/how-to-do-low-driven-shots-headers-in-ea-fc-26/
- S41 Dexerto, Career gameplay setting (18 Aug 2025; Competitive vs Authentic only) — https://www.dexerto.com/wikis/ea-fc-26-guides-walkthrough-tips/best-gameplay-setting-career/
- S42 Red Bull, FC 26 best tactics and formations, with pro player RedLac (2 Oct 2025) — https://www.redbull.com/us-en/ea-fc-26-best-tactics-formations
- S43 Red Bull, FC 26 meta guide (12 Feb 2026) — https://www.redbull.com/us-en/fc-26-meta-guide-tactics-dribbling-attacking
- S44 Beebom, EA FC 26 best formations (19 Sep 2025) — https://beebom.com/ea-fc-26-best-formations/amp/
- S45 The Online Gooner (18 Jun 2026; flagged above) — https://www.onlinegooner.com/articles/view/best-fc-26-formations-and-tactics-for-ultimate-team-after-the-world-cup-update

**Community (low confidence)**
- S46 EA Forums user thread, "Cheesing squad battles" (about Jan 2026) — https://forums.ea.com/discussions/fc-26-ultimate-team-en/cheesing-squad-battles/13016774
- S47 Steam thread, "FC 26 Ultimate Difficulty Way Too Easy" (19 Oct 2025; complaints only, no tactics) — https://steamcommunity.com/app/3405690/discussions/0/506217282369749123/

**Checked but not used** (generic, no EA reply, or no useful detail)
- https://www.fifplay.com/fc-26-attacking-tips/
- https://www.fifplay.com/fc-26-shooting-and-finishing-tips/
- https://forums.ea.com/discussions/fc-26-feedback-en/feedback--offline-gameplay-vs-cpu/12871837
- https://www.fut.gg/ea-sports-fc-25/fc-iq-tactics-revamp (FC 25)
- https://soccergaming.com/first-fc-26-title-update-announced-full-patch-notes/
- https://www.itemd2r.com/blog/fc-26/ea-sports-fc-26-title-update-140-full-gameplay-fut-breakdown
- https://fifauteam.com/fc-26-positions-guide
- https://www.dexerto.com/wikis/ea-fc-26-guides-walkthrough-tips/
- https://resident.com/resource-guide/2025/11/12/all-fc-26-positions-explained
- https://srand.publisher-collective.com/news/fc-26-manager-mode-player-roles

**Excluded because they cover the wrong game**
- https://www.fut.gg/tactics/4-3-3/ (FC 27)
- https://www.fut.gg/tactics/4-3-3-defend/ (FC 27)
- https://www.fut.gg/roles/cdm/ (FC 27)
- https://fut.gg/ea-sports-fc/accelerate/ (FC 24)

**Could not load**
- https://www.fifplay.com/fc-26-player-roles/ (permission request expired)
- https://www.teamgullit.com/ea-fc-26/formations (redirects to liquidfc.gg; permission request expired)
- These Red Bull pages rendered empty:
  - https://www.redbull.com/au-en/fc-26-meta-guide-tactics-dribbling-attacking
  - https://www.redbull.com/mk-mk/fc-26-meta-guide-tactics-dribbling-attacking
  - https://www.redbull.com/us-en/fc-26-ultimate-team-best-playstyles
  - https://www.redbull.com/ca-en/fc-26-ultimate-team-best-playstyles

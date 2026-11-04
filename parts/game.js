/* ======================= Game: FC 26 or FIFA 23 =======================
   The clips are the same football in both games. What changes in FC 26: some buttons, captions that
   quoted FIFA 23 patch facts, settings words (FC IQ roles instead of instructions), notes and sources. */
let GAME='fc26';
const REEL23=['U1','A1','U2','U3','A2','A3','U6'];
const REEL26=['U2','A1','U3','A2','A4','C1','U6'];
const U26={
  dd:'https://www.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-gameplay-deep-dive',
  fut:'https://www.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-fut-deep-dive',
  v102:'https://forums.ea.com/blog/ea-sports-fc-game-info-hub-en/fc-26-version-1-0-2-update-notes/12651602',
  v103:'https://forums.ea.com/blog/ea-sports-fc-game-info-hub-en/fc-26-version-1-0-3-update-notes/12696716',
  v110:'https://www.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-1-1-0-update',
  v110n:'https://forums.ea.com/blog/ea-sports-fc-game-info-hub-en/fc-26-v1-1-0-update-notes/12815780',
  v113:'https://forums.ea.com/blog/ea-sports-fc-game-info-hub-en/ea-sports-fc-26-version-1-1-3-update-notes/12876617',
  v120:'https://forums.ea.com/blog/ea-sports-fc-game-info-hub-en/ea-sports-fc-26-version-1-2-0-update-notes/12906902',
  v130:'https://forums.ea.com/blog/ea-sports-fc-game-info-hub-en/ea-sports-fc-26-version-1-3-0-update-notes/12977359',
  v140:'https://www.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-title-update-1-4-0',
  v140n:'https://forums.ea.com/blog/ea-sports-fc-game-info-hub-en/ea-sports-fc-26-version-1-4-0-update-notes/13073501',
  v150:'https://www.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-title-update-1-5-0',
  acc:'https://www.ea.com/able/resources/ea-sports-fc/fc-26',
  fc25iq:'https://www.ea.com/games/ea-sports-fc/fc-25/news/pitch-notes-fc-25-fc-iq-deep-dive',
  rbmeta:'https://www.redbull.com/us-en/fc-26-meta-guide-tactics-dribbling-attacking',
  egpass:'https://earlygame.com/de/guides/fifa/ea-fc-26-so-bringst-du-jeden-pass-ans-ziel',
  fpctl:'https://www.fifplay.com/fc-26-controls/',
  fp23ctl:'https://www.fifplay.com/fifa-23-controls/',
  cheese:'https://forums.ea.com/discussions/fc-26-ultimate-team-en/cheesing-squad-battles/13016774',
  sk23:'https://sportskeeda.com/esports/5-best-tips-defending-fifa-23-march-2023',
  may26:'https://mp1st.com/title-updates-and-patches/ea-sports-fc-26-the-worlds-game-update-released-patch-1-25'
};
const CONTAIN26='Hold A contains only on Tactical defending (or Legacy, which Ultimate Team doesn’t allow). On the default, Advanced, hold A is a physical tackle.';
const CONTAIN26_SRC=[{t:'FIFPlay: FC 26 controls (Contain vs Physical Tackle)',u:U26.fpctl},{t:'EA: FC 26 settings guide (Defending options)',u:U26.acc}];
/* Per-clip FC 26 overrides: cue, watch, setting, keys (coach card), n (the "In FC 26" note), src (one or a list) */
const F26={
  U1:{cue:'At kick-off, pass back to the edge of the circle. If their back line is still high, play a lobbed through ball over it.',
      setting:'Striker on Advanced Forward (Attack), so he makes runs in behind.',
      keys:[[['LB','+','Y'],'Lobbed through ball'],[['RB','+','B'],'Finesse, far post']],
      n:'Harder in FC 26: after kick-off the defence sits compact for a short time (update 1.0.3) and marks tighter (update 1.1.0). Go over the top only if their line is still high.',
      src:[{t:'EA update 1.0.3 notes: compact after kick-off',u:U26.v103},{t:'EA update 1.1.0 notes: tighter marking at kick-off',u:U26.v110n},{t:'EA FC IQ (FC 25, kept in FC 26): Advanced Forward runs in behind',u:U26.fc25iq}]},
  U2:{n:'Since update 1.4.0, AI defenders react slower when marking the man on the ball, so space opens while they reset.',
      src:{t:'EA update 1.4.0 notes: AI defenders react slower',u:U26.v140n}},
  U3:{n:'EA gives no block-reach number for FC 26, but update 1.5.0 made the Fake Shot 5% faster.',
      src:{t:'EA update 1.5.0: Fake Shot made faster',u:U26.v150}},
  U4:{keys:[[['LB','+','Y'],'Lobbed through ball']],
      n:'FIFA 23’s LB + RB + Y lob is gone: in FC 26 that combo plays a driven ground through ball. Use LB + Y to go over the top.',
      src:{t:'FIFPlay: FC 26 controls',u:U26.fpctl}},
  U5:{n:'Update 1.5.0 made chips more accurate. FC 26 keepers also choose better in one-on-ones, so chip only once he commits.',
      src:[{t:'EA update 1.5.0: chip shots more accurate',u:U26.v150},{t:'EA Gameplay Deep Dive: keepers in one-on-ones',u:U26.dd}]},
  U6:{cue:'A defender a few yards off, standing between you and the keeper? Shoot now, low. He is too far off to block it.',
      keys:[[['B','B'],'Low driven: double-tap B']],
      n:'Squad Battles has fewer automatic blocks. Low driven shot: double-tap B. Update 1.0.2 made very high power less accurate, so don’t max it.',
      src:[{t:'EA Gameplay Deep Dive: fewer auto blocks; double-tap for low driven',u:U26.dd},{t:'EA update 1.0.2 notes: low driven shots at extreme power',u:U26.v102}]},
  U7:{n:'Hold RB is Controlled Sprint in FC 26 (Agile Dribble in FIFA 23). Two men closing in? Still pass first.',
      src:[{t:'FIFPlay: FC 26 controls (Controlled Sprint)',u:U26.fpctl},{t:'FIFPlay: FIFA 23 controls (Agile Dribble)',u:U26.fp23ctl},{t:'Red Bull: quick, first-time passing is one of FC 26’s strongest attacks',u:U26.rbmeta}]},
  A1:{n:'Since update 1.4.0 the Squad Battles AI attacks more and keeps the ball less.',
      src:{t:'EA update 1.4.0: the Squad Battles AI attacks more',u:U26.v140}},
  A2:{n:'Update 1.1.3 made the AI dribble with sharper turns. Jockey got quicker (1.1.0) and tackles from behind got weaker, so stay in front of him.',
      src:[{t:'EA update 1.1.3 notes: sharper AI dribbling',u:U26.v113},{t:'EA update 1.1.0: quicker jockey',u:U26.v110},{t:'EA Gameplay Deep Dive: weaker tackles from behind',u:U26.dd}]},
  A3:{n:'Update 1.3.0 lowered crosses, so they arrive flatter. Cover the near post early.',
      src:{t:'EA update 1.3.0 notes: lower crosses',u:U26.v130}},
  A4:{n:'Since update 1.2.0, AI defenders, yours included, mark the edge of the box a little less tightly. Don’t count on a teammate to close that runner.',
      src:{t:'EA update 1.2.0 notes: slightly looser marking at the edge of the box',u:U26.v120}},
  A5:{n:'Chips got more accurate in update 1.5.0, so a keeper who charges all the way gets punished. The halfway tip itself is from FIFA 23 guides.',
      src:[{t:'EA update 1.5.0: chip shots more accurate',u:U26.v150},{t:'Sportskeeda (FIFA 23): bring the keeper halfway',u:U26.sk23}]},
  A6:{keys:[[['LB','+','Y'],'Over the top']],
      n:'Player tip (EA forums, around January 2026): the AI “seems to really struggle with counter attacks”. Update 1.4.0 then made it attack more, which should leave more space behind it.',
      src:[{t:'EA forums, player tip: the AI struggles with counter attacks',u:U26.cheese},{t:'EA update 1.4.0: the AI attacks more',u:U26.v140}]},
  B1:{setting:'One central midfielder as Deep-Lying Playmaker (Build-Up), so there is always a pass in front of your CBs.',
      n:'No Player Instructions in FC 26. Each player’s Role and Focus decide where he goes.',
      src:{t:'EA FC IQ (FC 25, kept in FC 26): instructions replaced by Roles',u:U26.fc25iq}},
  B5:{n:'Update 1.5.0 (March 2026) made lofted passes (double-tap A or Y) less accurate. Play one only when the man you’re aiming at has space.',
      src:{t:'EA update 1.5.0: lofted passes less accurate',u:U26.v150}},
  C1:{setting:'FC 26 has no edge-of-box instruction. Roles decide who arrives, so look back for the late man.',
      n:'Since update 1.2.0, AI defenders mark the edge of their box a little less tightly, so your cutback man has more room. Faster ball: hold LB + RB, double-tap X.',
      src:[{t:'EA update 1.2.0 notes: slightly looser marking at the edge of the box',u:U26.v120},{t:'EA FC IQ (FC 25, kept in FC 26): no Player Instructions',u:U26.fc25iq},{t:'EarlyGame (German): driven ground cross for cutbacks',u:U26.egpass}]},
  C4:{n:'Aim at the gap between two defenders: FC 26’s semi-assisted through balls pick the runner in that lane.',
      src:{t:'EA Gameplay Deep Dive: passing lanes for through balls',u:U26.dd}},
  C5:{n:'EA made one-touch shots more responsive in Competitive gameplay, which Squad Battles uses.',
      src:{t:'EA Ultimate Team Deep Dive: more responsive one-touch shooting',u:U26.fut}},
  D2:{n:CONTAIN26,src:CONTAIN26_SRC},
  D4:{n:CONTAIN26,src:CONTAIN26_SRC},
  /* Pro patterns (2026-11-04): same inputs in both games; FC 26 roles and patch context here */
  P1:{setting:'Pivot: Deep-Lying Playmaker (Build-Up). Far full-back: Fullback (Defend).',
      n:'Since update 1.4.0 the Squad Battles AI attacks more and keeps the ball less, so it counters the moment it wins the ball. Four behind it is your insurance.',
      src:{t:'EA update 1.4.0: Squad Battles AI more direct',u:U26.v140}},
  P2:{setting:'Long spell in their half? Quick tactic Team Press: D-pad Up, then Left.',
      n:'Since update 1.4.0 AI defenders react slower when marking the ball carrier, so space opens while they reset. Since May 2026 Team Press presses less in your own half, so use it in theirs.',
      src:[{t:'EA update 1.4.0 notes: AI defenders react slower',u:U26.v140n},{t:'MP1st: May 2026 update notes (Team Press)',u:U26.may26}]},
  P3:{n:'Since May 2026, AI teammates stop doubling up on the ball carrier while you mark him yourself, and contain him when your man is further away. Get tight yourself first, then use the second man.',
      src:{t:'MP1st: May 2026 update notes (teammate contain)',u:U26.may26}},
  P4:{setting:'Wingers on Inside Forward: they run in behind, inside their full-back.',
      n:'FC 26 semi-assisted through balls pick the runner in the lane you aim at, the gap between two defenders. Directed runs also work while you dribble with controlled sprint (hold RB), since update 1.1.0.',
      src:[{t:'EA Gameplay Deep Dive: passing lanes for through balls',u:U26.dd},{t:'EA update 1.1.0 notes: directed runs in controlled sprint',u:U26.v110n}]}
};
/* Button prompts that change in FC 26, keyed by the label the clips use */
const L26={
  'Driven lobbed through ball':[['LB','+','Y'],'Lobbed through ball'],
  'Driven lob through':[['LB','+','Y'],'Lobbed through ball'],
  'Driven lob over the top':[['LB','+','Y'],'Over the top'],
  'Driven lob: flatter and faster':[['LB','+','Y'],'Lobbed through ball'],
  'Driven lob':[['LB','+','RB','+','X'],'Driven lob'],
  'Driven lob for a longer switch':[['LB','+','RB','+','X'],'Driven lob for a longer switch'],
  'Driven lob switch':[['LB','+','RB','+','X'],'Driven lob switch'],
  'Driven through ball':[['LB','+','RB','+','Y'],'Driven through'],
  'Driven through ball, tight gaps':[['LB','+','RB','+','Y'],'Driven through ball, tight gaps'],
  'Shoot low, far post':[['B','B'],'Low driven, far post'],
  'Shoot now':[['B','B'],'Low driven'],
  'Low shot':[['B','B'],'Low driven shot'],
  'Contain':[['hold','A'],'Contain (Tactical)'],
  'Contain with your midfielder':[['hold','A'],'Contain with your midfielder (Tactical)'],
  'Contain with your pivot':[['hold','A'],'Contain with your pivot (Tactical)']
};
/* Captions that quoted FIFA 23 facts or buttons */
const SAY26={
  'Driven lob over their back line.':'Lobbed through ball over their back line.',
  'Blocked. CPU defenders block anything within about a yard.':'Blocked. He was close enough to get a foot to it.',
  'He is within a yard, so he would block it. Fake it first.':'He is right on you, so he would block it. Fake it first.',
  'He’s too far off to block it, and he’s in the keeper’s way.':'He’s too far off to block it.',
  'Shoot now. Low, far post.':'Shoot now. Low driven, far post.',
  'The keeper sees it late. Goal.':'Goal.',
  'Go now. They are slow to get back.':'Go now, before their defenders react.',
  'Gap behind you. The CPU loves this pass.':'Gap behind you. That’s the pass it looks for.',
  'On Ultimate, some CPU players get +10 to every stat on the ball.':'Since update 1.1.3 the AI dribbles with sharper turns.',
  'The CPU loves to cross. Now your box is short a defender.':'The cross is coming. Now your box is short a defender.',
  'CPU strikers with Chip Shot punish this.':'A chip punishes this. Chips got more accurate in update 1.5.0.',
  'Go now. Driven lob over their last two.':'Go now. Lobbed through over their last two.',
  'Pivot on Stay Back While Attacking. Always a pass in front of the CBs.':'Pivot as a Deep-Lying Playmaker. Always a pass in front of the CBs.'
};
/* Trainer feedback that quoted FIFA 23 facts or buttons */
const FB26={
  s5:'Everyone shifted to the ball, so the far side is empty. Switch it: X, or LB + RB + X for a driven one.',
  s11:'Their pressers are behind you and still turning. Drive forward with RT and attack the space.',
  s13:'He is close enough to block it. Fake shot first (B then A), then shoot with space.',
  s16:'Your CB stepped out and left a gap. Since update 1.4.0 the Squad Battles AI attacks more. Hold your line and press LB to switch to the CB nearest the runner.',
  s17:'Their midfielder arrives late at the edge of your box. Since update 1.2.0 your AI teammates mark the edge a little less tightly, so close him yourself while the pass travels.',
  s18:'Everyone shifted to the ball, so their far winger is free. A long switch is on. Keep your far full-back close enough to step out.',
  s19:'Their winger has the touchline. Get your full-back goal-side, jockey him outside, and keep your CBs in the box.',
  s21:'Chip shots got more accurate in FC 26 update 1.5.0, so a keeper who charges all the way gets chipped. Bring him halfway and make the striker decide.',
  s22:'No space ahead and two of them closing. Sprinting into them loses it. Pass, then move into space.',
  s23:'He’s too far off to block it. Shoot now: low driven (double-tap B) to the far post.'
};
SCENES.forEach(s=>{if(FB26[s.id])s.f26={fb:FB26[s.id]};});
let REEL=REEL26;
const is26=()=>GAME==='fc26';
function G(o,k){return is26()&&o.f26&&o.f26[k]!=null?o.f26[k]:o[k];}
function gsay(t){return is26()&&SAY26[t]||t;}
function gkey(tok,lab){return is26()&&L26[lab]?L26[lab]:[tok,lab];}
function f26(id){return is26()&&F26[id]||{};}
let updChecks=()=>{};

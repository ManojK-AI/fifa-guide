#!/usr/bin/env python3
"""Builds the Pro tab (advanced kit, FC 26 first): parts/pro.html.

Every line carries an evidence tag:
  EA          EA's own pages (Pitch Notes, update notes, settings guide)
  Guide       an established guide site (FIFPlay, Red Bull, EarlyGame, Operation Sports, Dexerto, fut.gg, FIFAUTeam)
  Players     players on EA's forums
  Coach       reasoning from the sourced facts; advice, not a measured fact
  Unconfirmed found through web search; the page itself could not be opened when this was written
See docs/research/agents/fc26_advanced.md for the evidence behind each line.
"""
import html, pathlib

U = {
  # EA
  'dd':     ('EA', 'EA: FC 26 Gameplay Deep Dive (Jul 2025)', 'https://www.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-gameplay-deep-dive'),
  'fut':    ('EA', 'EA: FC 26 Ultimate Team Deep Dive (Aug 2025)', 'https://www.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-fut-deep-dive'),
  'launch': ('EA', 'EA: FC 26 Launch Update (Sep 2025)', 'https://www.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-launch-update'),
  'oct':    ('EA', 'EA: FC 26 October Feedback Update (Oct 2025)', 'https://www.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-feedback-update-october'),
  'v110':   ('EA', 'EA: FC 26 update 1.1.0 Pitch Notes (Oct 2025)', 'https://www.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-1-1-0-update'),
  'v110n':  ('EA', 'EA: FC 26 update 1.1.0 notes (Oct 2025)', 'https://forums.ea.com/blog/ea-sports-fc-game-info-hub-en/fc-26-v1-1-0-update-notes/12815780'),
  'v130':   ('EA', 'EA: FC 26 Holiday Update, 1.3.0 (Dec 2025)', 'https://www.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-holiday-update'),
  'v140':   ('EA', 'EA: FC 26 Title Update 1.4.0 (Jan 2026)', 'https://www.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-title-update-1-4-0'),
  'v150':   ('EA', 'EA: FC 26 Title Update 1.5.0 (Mar 2026)', 'https://www.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-title-update-1-5-0'),
  'acc':    ('EA', 'EA: FC 26 settings and accessibility guide', 'https://www.ea.com/able/resources/ea-sports-fc/fc-26'),
  'fc25iq': ('EA', 'EA: FC IQ Deep Dive (FC 25; FC 26 keeps the system)', 'https://www.ea.com/games/ea-sports-fc/fc-25/news/pitch-notes-fc-25-fc-iq-deep-dive'),
  'may26':  ('EA', 'MP1st: copy of EA’s May 2026 update notes', 'https://mp1st.com/title-updates-and-patches/ea-sports-fc-26-the-worlds-game-update-released-patch-1-25'),
  # Guides
  'fpctl':  ('Guide', 'FIFPlay: FC 26 controls', 'https://www.fifplay.com/fc-26-controls/'),
  'fpdef':  ('Guide', 'FIFPlay: FC 26 defending tips', 'https://www.fifplay.com/fc-26-defending-tips/'),
  'fpprec': ('Guide', 'FIFPlay: FC 26 precision pass', 'https://www.fifplay.com/fc-26-precision-pass/'),
  'egpass': ('Guide', 'EarlyGame (German): FC 26 passing guide', 'https://earlygame.com/de/guides/fifa/ea-fc-26-so-bringst-du-jeden-pass-ans-ziel'),
  'osd':    ('Guide', 'Operation Sports: pressing with several players in FC 26', 'https://www.operationsports.com/how-to-press-with-multiple-players-in-ea-fc-26/'),
  'osp':    ('Guide', 'Operation Sports: every FC 26 passing technique', 'https://www.operationsports.com/ea-fc-26-all-passing-techniques-explained/'),
  'rbmeta': ('Guide', 'Red Bull: FC 26 meta guide (Feb 2026)', 'https://www.redbull.com/us-en/fc-26-meta-guide-tactics-dribbling-attacking'),
  'rbtac':  ('Guide', 'Red Bull: FC 26 tactics, with pro player RedLac (Oct 2025)', 'https://www.redbull.com/us-en/ea-fc-26-best-tactics-formations'),
  'dxld':   ('Guide', 'Dexerto: FC 26 low driven shots', 'https://www.dexerto.com/wikis/ea-fc-26-guides-walkthrough-tips/how-to-do-low-driven-shots-headers-in-ea-fc-26/'),
  'fautsm': ('Guide', 'FIFAUTeam: FC 26 quick tactics', 'https://fifauteam.com/fc-26-smart-tactics/'),
  'fautpts':('Guide', 'FIFAUTeam: FC 26 Squad Battles points', 'https://fifauteam.com/fc-26-squad-battle-points/'),
  # Players
  'cheese': ('Players', 'EA forums: “Cheesing squad battles”', 'https://forums.ea.com/discussions/fc-26-ultimate-team-en/cheesing-squad-battles/13016774'),
  # Found by search only (page not opened)
  'rbskill':('Unconfirmed', 'Red Bull: FC 26 skill moves guide', 'https://www.redbull.com/ie-en/ea-fc-26-skillmoves-tricks-guide'),
  'beebom': ('Unconfirmed', 'Beebom: all new FC 26 skill moves', 'https://beebom.com/ea-sports-fc-26-skill-moves-and-controls/'),
  'osskill':('Unconfirmed', 'Operation Sports: best FC 26 skill moves', 'https://www.operationsports.com/the-best-skill-moves-in-fc-26'),
  'dstr':   ('Unconfirmed', 'Destructoid: every FC 26 skill move', 'https://www.destructoid.com/all-fc-26-skill-moves-and-how-to-do-them/'),
  'oslock': ('Unconfirmed', 'Operation Sports: player lock in FC 26', 'https://www.operationsports.com/how-to-use-player-lock-in-ea-fc-26'),
  'fautst': ('Unconfirmed', 'FIFAUTeam: FC 26 match facts and stats', 'https://fifauteam.com/fc-26-stats-match-facts-performance/'),
  'fparena':('Unconfirmed', 'FIFPlay: FC 26 Practice Arena', 'https://www.fifplay.com/fc-26-practice-arena/'),
  'rs101fk':('Unconfirmed', 'RealSport101: FC 26 free kicks', 'https://realsport101.com/article/fc-26-how-to-score-free-kicks-the-best-techniques-and-dead-ball-specialists'),
  'tgsp':   ('Unconfirmed', 'Team Gullit: FC 26 set pieces', 'https://www.teamgullit.com/ea-fc-26/set-pieces'),
}
TAG_TITLE = {
  'EA': 'From EA’s own pages',
  'Guide': 'From an established guide site',
  'Players': 'What players report on EA’s forums',
  'Coach': 'Coach’s call: reasoning from the sourced facts, not a measured fact',
  'Unconfirmed': 'Found in search results; the page itself could not be opened when this was written',
}
TAG_TEXT = {'EA': 'EA', 'Guide': 'Guide', 'Players': 'Players', 'Coach': 'Coach’s call', 'Unconfirmed': 'Unconfirmed'}

SHORT = {'dd': 'EA Deep Dive', 'fut': 'EA UT Deep Dive', 'launch': 'EA launch update', 'oct': 'EA Oct 2025 update', 'v110': 'EA 1.1.0', 'v110n': 'EA 1.1.0 notes', 'v130': 'EA 1.3.0', 'v140': 'EA 1.4.0', 'v150': 'EA 1.5.0', 'acc': 'EA settings guide', 'fc25iq': 'EA FC IQ (FC 25)', 'may26': 'EA May 2026 notes (MP1st)', 'fpctl': 'FIFPlay controls', 'fpdef': 'FIFPlay defending', 'fpprec': 'FIFPlay precision pass', 'egpass': 'EarlyGame passing', 'osd': 'Operation Sports pressing', 'osp': 'Operation Sports passing', 'rbmeta': 'Red Bull meta guide', 'rbtac': 'Red Bull tactics', 'dxld': 'Dexerto', 'fautsm': 'FIFAUTeam quick tactics', 'fautpts': 'FIFAUTeam points', 'cheese': 'EA forums', 'rbskill': 'Red Bull skill moves', 'beebom': 'Beebom', 'osskill': 'Operation Sports skill moves', 'dstr': 'Destructoid', 'oslock': 'Operation Sports player lock', 'fautst': 'FIFAUTeam stats', 'fparena': 'FIFPlay Practice Arena', 'rs101fk': 'RealSport101', 'tgsp': 'Team Gullit'}
assert set(SHORT) == set(U)

def e(x): return html.escape(x, quote=True)

def tag(t):
    return f'<span class="ev ev-{t.lower()}" title="{e(TAG_TITLE[t])}">{e(TAG_TEXT[t])}</span>'

def ev(keys, coach=False):
    """Evidence line: one tag per evidence tier present, then the source links."""
    tiers = []
    for k in keys:
        t = U[k][0]
        if t not in tiers: tiers.append(t)
    if coach: tiers.append('Coach')
    links = ' · '.join(f'<a class="src" href="{e(U[k][2])}" target="_blank" rel="noopener" title="{e(U[k][1])}">{e(SHORT[k])}</a>' for k in keys)
    return '<span class="evl">' + ''.join(tag(t) for t in tiers) + (' ' + links if links else '') + '</span>'

def label(tokens):
    nm = lambda k: {'LS': 'left stick', 'RS': 'right stick'}.get(k, k)
    out, i = [], 0
    while i < len(tokens):
        k = tokens[i]
        if k in ('+', 'then'): out.append('plus' if k == '+' else 'then'); i += 1; continue
        if k == 'hold': out.append('hold ' + nm(tokens[i + 1])); i += 2; continue
        if i + 1 < len(tokens) and tokens[i + 1] == k: out.append('double-tap ' + nm(k)); i += 2; continue
        out.append(nm(k)); i += 1
    return ' '.join(out)

def keys(tokens):
    def one(t):
        if t == '+': return '<span class="kplus" aria-hidden="true">+</span>'
        if t in ('A', 'B', 'X', 'Y'): return f'<span class="k k-{t}" aria-hidden="true">{t}</span>'
        if t in ('LB', 'RB'): return f'<span class="k k-bump" aria-hidden="true">{t}</span>'
        if t in ('LT', 'RT'): return f'<span class="k k-trig" aria-hidden="true">{t}</span>'
        if t in ('LS', 'RS'): return f'<span class="k k-stick" aria-hidden="true">{t}</span>'
        return f'<span class="kword" aria-hidden="true">{e(t)}</span>'
    return f'<span class="kb" role="img" aria-label="{e(label(tokens))}">' + ''.join(one(t) for t in tokens) + '</span>'

def clip(k): return f'<button type="button" class="clip-ref" data-clip="{k}" aria-label="Watch clip {k}">▶ {k}</button>'

def table(cls, heads, rows):
    """Responsive table: on phones each row becomes a block, cells labelled by their column head."""
    th = ''.join(f'<th scope="col">{e(h)}</th>' for h in heads)
    body = ''
    for r in rows:
        cells = ''.join(f'<td data-l="{e(heads[i])}">{c}</td>' for i, c in enumerate(r))
        body += f'            <tr>{cells}</tr>\n'
    return f'          <table class="ptab {cls}">\n            <thead><tr>{th}</tr></thead>\n            <tbody>\n{body}            </tbody>\n          </table>\n'

def card(kicker, title, body, wide=False, extra=''):
    return (f'      <article class="pcard{" pwide" if wide else ""}{extra}">\n        <p class="coach-k">{e(kicker)}</p>\n'
            f'        <h2>{e(title)}</h2>\n{body}      </article>\n')

def li(text_html, evidence): return f'          <li><span>{text_html}</span> {evidence}</li>\n'

# ---------------------------------------------------------------- content
HEAD = f'''      <article class="pcard pwide pro-head">
        <p class="coach-k">Pro kit · FC 26</p>
        <h2>The next level</h2>
        <p>The other tabs stop the leaks: build-up, chances, balls in behind. This one is what separates winning on Legendary from running the game on Ultimate: the right shot for the moment, the full pass kit, manual defending, a tactic for every scoreline, and practice that actually transfers.</p>
        <p class="pintro">Inputs are FC 26 Classic controls on an Xbox pad. Every line says how sure it is:</p>
        <p class="evkey"><span class="evk">{tag('EA')} EA’s own notes</span><span class="evk">{tag('Guide')} an established guide</span><span class="evk">{tag('Players')} players on EA’s forums</span><span class="evk">{tag('Coach')} reasoning, not a measured fact</span><span class="evk">{tag('Unconfirmed')} found in search results only</span></p>
        <p class="n26 g23"><span class="n26-t"><b>Playing FIFA 23?</b> This tab is written for FC 26. Most inputs are the same, but these are FC 26 only: the double-tap low driven shot (FIFA 23 has Timed Finishing instead), precision passes, controlled sprint, the new skill moves, Roles and the tactics lab (FIFA 23 uses player instructions and game plans), and every patch note. The four Pro clips work in both games.</span></p>
      </article>
'''

FINISH = [
  ('Cutback to the edge or the penalty spot, you arrive first time', 'First-time low driven shot', keys(['B', 'B']) + '<span class="pnote">hold B briefly, tap again, before the ball reaches you</span>',
   'Low driven is a double tap in FC 26, and one-touch shots trigger as little as one frame before you receive. A guide rates low drivens faster and harder for keepers to save. ' + clip('C1') + ' ' + ev(['dd', 'fut', 'dxld'])),
  ('One-on-one, keeper rushing out', 'Chip', keys(['LB', '+', 'B']),
   'Update 1.5.0 made chips more accurate and less likely to go wide, more so with the Chip Shot PlayStyle. ' + clip('U5') + ' ' + ev(['v150'])),
  ('One-on-one, keeper set on his line', 'Low driven finesse to the far corner', keys(['RB', '+', 'B', 'B']) + '<span class="pnote">short hold</span>',
   'Low driven works with finesse too. Keep the press short: EA made low drivens less accurate at extreme power. ' + ev(['dd', 'oct'])),
  ('Edge of the box, after cutting in onto your strong foot', 'Finesse, far post', keys(['RB', '+', 'B']),
   'From the edge, not from range: at launch EA cut the top spin on finesse shots from outside the box. ' + ev(['launch'])),
  ('20 to 25 yards out with space, shooter has Power Shot', 'Power shot', keys(['LB', '+', 'RB', '+', 'B']),
   'Update 1.5.0 gave power shots a better trajectory from long range, and more accuracy with the Power Shot PlayStyle. ' + ev(['v150'])),
  ('A defender within a yard of you', 'Fake shot, then shoot', keys(['B', 'then', 'A']) + '<span class="pnote">plus a direction</span>',
   'Update 1.5.0 made the Fake Shot 5% faster. ' + clip('U3') + ' ' + ev(['v150'])),
  ('Tight angle near the byline', 'Don’t shoot: cut it back low', keys(['LB', '+', 'RB', '+', 'X', 'X']) + '<span class="pnote">driven ground cross</span>',
   'A guide rates the driven ground cross the best option for fast, low cutbacks. ' + ev(['egpass'], coach=True)),
  ('A high ball in their box', 'Head it only with a strong header', keys(['B']),
   'Squad Battles plays Competitive gameplay, which EA says has more heading error than Authentic. Strength decides who wins the ball in the air. ' + ev(['dd'])),
  ('You want the outside of the foot', 'Trivela', keys(['LT', '+', 'B']),
   'Only players with the Gamechanger PlayStyle can hit one in FC 26. ' + ev(['dd'])),
]
finish = card('Finishing', 'Pick the shot for the moment',
  '        <p>Shot choice beats shot power. Read the keeper and the nearest defender, then pick from this table.</p>\n' +
  table('t-finish', ['The moment', 'The shot', 'Input', 'Why'], [[e(a), f'<b>{e(b)}</b>', c, d] for a, b, c, d in FINISH]), wide=True)

PASS = [
  ('Driven ground pass', keys(['RB', '+', 'A']), 'Any pass that breaks a line. A soft one gets cut out.',
   'Update 1.5.0 made ground passes quicker and more accurate, most for good passers. ' + ev(['v150'])),
  ('Precision pass', keys(['RB', '+', 'Y']), 'Into space ahead of a runner, exactly where you aim. For space, not feet.',
   'A deliberate pass, close to manual. One guide calls it precise but less effective than the other options, so use it for the one pass that needs it. ' + ev(['fpprec', 'egpass'])),
  ('Precision lob', keys(['RB', '+', 'X']), 'Drop the ball onto a spot over a defender.', ev(['fpctl'])),
  ('Precision swerve pass', keys(['LT', '+', 'RB', '+', 'Y']), 'Bend a ground pass round the man standing in the lane.', ev(['fpprec'])),
  ('Lofted through ball', keys(['Y', 'Y']), 'Defenders tight on your runner: go over them.',
   'A guide calls it one of FC 26’s strongest passes, but update 1.5.0 cut lofted pass accuracy, so play it from a passer with time. ' + ev(['egpass', 'v150'])),
  ('Lobbed through ball', keys(['LB', '+', 'Y']), 'Their line is high and your runner is level with it.', clip('U4') + ' ' + ev(['fpctl'])),
  ('Driven through ball', keys(['LB', '+', 'RB', '+', 'Y']), 'A tight gap on the ground: faster than a plain through ball.', ev(['fpctl'])),
  ('Driven lob', keys(['LB', '+', 'RB', '+', 'X']), 'Fast switch to the far winger once they are all ball-side.', clip('C2') + ' ' + ev(['fpctl'])),
  ('Driven ground cross', keys(['LB', '+', 'RB', '+', 'X', 'X']), 'Low, fast cutback from the byline.', ev(['egpass'])),
  ('First-time pass', keys(['A']) + '<span class="pnote">tap before the ball arrives</span>', 'Quick triangles to beat a press. Forward or square, not back across your body.',
   'A guide rates first-time passing “extremely powerful”. EA: Competitive gameplay cuts first-time pass accuracy, and first-time through balls at 135° or 180° are much less accurate. ' + ev(['rbmeta', 'fut', 'dd'])),
  ('Pass and go', keys(['LB', '+', 'A']), 'The one-two at the edge of the box. One guide lists a driven version on LB + RB + A.', clip('C3') + ' ' + ev(['fpctl', 'osp'])),
]
passing = card('Passing', 'The full pass kit',
  '        <p>The Playbook’s button table covers the everyday passes. FC 26 has more than ten, and each one has its moment. Learn them one at a time.</p>\n' +
  table('t-pass', ['Pass', 'Input', 'Use it when', 'Evidence'], [[f'<b>{e(a)}</b>', b, e(c), d] for a, b, c, d in PASS]) +
  f'        <p class="pfoot">Two settings that go with this: Pass Receiver Lock on Late lets you change the target at the last moment, and Precision Pass Sensitivity on High cuts the assistance on precision passes. {ev(["acc"])}</p>\n', wide=True)

DEF = [
  ('<b>Choose your defending mode on purpose.</b> Tactical: hold A contains and the game picks the tackle. Advanced, the default: hold A is a physical tackle, RB + B a hard tackle, RB + X a hard slide. Stay on Tactical until your tackles are timed, then try Advanced for the extra tools.', ev(['acc', 'fpctl', 'fpdef'], coach=True)),
  (f'<b>Sprint jockey</b> {keys(["LT", "+", "RT"])} keeps you goal-side of a runner. Update 1.1.0 made jockey and sprint jockey faster and more responsive.', ev(['fpdef', 'v110'])),
  ('<b>Tackle when the ball leaves his foot</b> or when he turns his back to you. Never from behind: EA made tackles from behind less effective.', ev(['dd'], coach=True)),
  ('<b>Pick defenders by Stand Tackle.</b> 85 or more gets every tackle animation, 71 to 84 most of them, under 71 only the basic ones.', ev(['dd'])),
  ('<b>Shoulder only a weaker man.</b> Since update 1.4.0 a big Strength gap makes the weaker player stumble. Bruiser was toned down in May 2026.', ev(['v140', 'may26'])),
  ('<b>Put your interceptors in the lanes.</b> Since May 2026 players with 90+ Interceptions get the Intercept PlayStyle’s animations.', ev(['may26'])),
  (f'<b>Second man in bursts.</b> Hold RB for about a second, then let go before you tackle so he drops back into his lane. {clip("P3")} Since May 2026 AI teammates stop doubling up while you mark the man yourself, so get tight first.', ev(['may26'], coach=True)),
  (f'<b>Pressing calls.</b> Partial team press: double-tap RB and hold. Team Press: D-pad Up, then Left, in their half only since May 2026. Offside trap: Up, then Up, only when your line is set and their passer is under pressure. {clip("P2")}', ev(['osd', 'may26'], coach=True)),
  ('<b>Leave your keeper alone.</b> Update 1.3.0 greatly cut manual keeper movement and removed Rush to Center in open play. Hold Y only to come halfway.', ev(['v130'])),
  (f'<b>Switch to the man in the lane,</b> not the nearest one: flick the right stick. Keep the Next Player Switch Indicator on. {clip("D2")}', ev(['acc'], coach=True)),
]
defend = card('Defending', 'Defend by hand', '        <ul class="plist pro-list">\n' + ''.join(li(a, b) for a, b in DEF) + '        </ul>\n')

MOVE = [
  (f'<b>Controlled sprint:</b> hold {keys(["RB"])} while dribbling to carry it fast and close. Since update 1.1.0 you can trigger directed runs during it.', ev(['fpctl', 'v110', 'v110n'])),
  (f'<b>Directed run:</b> tap LB, then flick the right stick where you want him to go. Send one as a decoy and pass into the gap it leaves. {clip("P4")}', ev(['fpctl'], coach=True)),
  (f'<b>Player lock:</b> press both sticks in, {keys(["LS", "+", "RS"])}, to take a player off the ball and make his run yourself; press both again to let go. Some players say it doesn’t work in Ultimate Team, so try it in Kick-off first.', ev(['oslock'])),
  (f'<b>First touch:</b> hold {keys(["LT"])} as the pass arrives for a cleaner touch, at the cost of speed.', ev(['dd'])),
  (f'<b>Loose balls:</b> press {keys(["RT"])} to make your man attack the ball.', ev(['dd'])),
  ('<b>Shield:</b> hold LT. Since update 1.4.0 Strength and Aggression decide more of it, and Enforcer got a boost in May 2026.', ev(['v140', 'may26'])),
  ('<b>Left-stick dribbling</b> works better again in FC 26, best with Quick Step players.', ev(['rbmeta'])),
]
SKILL = [
  ('Fake shot', '1★', keys(['B', 'then', 'A']), 'The one move to master. 5% faster since update 1.5.0. ' + clip('U3') + ' ' + ev(['v150'])),
  ('Ball roll', '1–2★', keys(['hold', 'RS']) + '<span class="pnote">left or right</span>', 'Steps you across a defender’s line. Rated effective in FC 26; sources differ on its stars. ' + ev(['rbmeta', 'dstr'])),
  ('Explosive Stepover', '3★, new', keys(['hold', 'LB']) + '<span class="pnote">and roll RS from forward to the side, then LS to exit</span>', 'New in FC 26, with a burst of speed on the way out. ' + ev(['rbskill', 'beebom', 'osskill'])),
  ('Drag to Chop', '4★, new', keys(['hold', 'LT']) + '<span class="pnote">and roll RS left, back, right (or the reverse)</span>', 'New in FC 26. ' + ev(['rbskill', 'beebom'])),
]
move = card('Movement and dribbling', 'Move like a forward',
  '        <ul class="plist pro-list">\n' + ''.join(li(a, b) for a, b in MOVE) + '        </ul>\n' +
  '        <p class="ptab-h">Skill moves worth learning</p>\n' +
  table('t-skill', ['Move', 'Stars', 'Input', 'Why'], [[f'<b>{e(a)}</b>', e(b), c, d] for a, b, c, d in SKILL]) +
  f'        <p class="pfoot">Skip the Elastico variations: a guide calls them “largely ineffective” in FC 26. Heel Chop and Feint and Exit also got 5% faster in update 1.5.0. Simplified Skill Moves, off by default, turns a right-stick flick into a contextual move. {ev(["rbmeta", "v150", "acc"])}</p>\n')

TAC = [
  ('1. Control', 'Left, then Up', 'The default', '4-3-3 (4) · Build-Up Balanced · Defensive Approach Balanced · Line Height 45', 'Your base roles from the Plan tab.'),
  ('2. Counter', 'Left, then Left', 'They hog the ball, or you lead and they push up', '4-3-3 (4) · Build-Up Counter · Balanced · Line Height 40', 'Wingers Inside Forward (Attack). Striker Advanced Forward (Attack).'),
  ('3. Chase', 'Left, then Right', 'Losing after 70 minutes', '4-3-3 (4) · Build-Up Balanced · High · Line Height 65', 'One full-back Attacking Wingback (Attack). In the last ten minutes add Get In The Box: Up, then Down.'),
  ('4. Lock', 'Left, then Down', 'Winning after 75 minutes', '4-3-3 (2), one CDM · Build-Up Short Passing · Deep · Line Height 28', 'CDM Holding (Defend). Both full-backs Fullback (Defend). Wingers Winger (Balanced), so they stay wide.'),
]
TAC_NOTES = [
  ('<b>Four tactics, one D-pad.</b> D-pad Left, then a direction, picks Custom Tactic 1 to 4. FC 26 saves Line Height in the tactic code and keeps up to ten codes.', ev(['fpctl', 'dd'])),
  ('<b>The line ranges.</b> Deep 1–30 (default 25), Balanced 31–60 (50), High 61–90 (70), Aggressive 91–100 (95, presses heavy touches, drains stamina). A pro puts the ceiling at 60: “the highest your defensive line can be without taking unnecessary risks”.', ev(['fc25iq', 'rbtac'])),
  ('<b>Tactical Focus</b> on D-pad Right shifts both Build-Up and Defensive Approach a step: Right, then Right for attacking; Right, then Left for defending. EA described it this way for FC 25.', ev(['fc25iq', 'fpctl'])),
  (f'<b>Four behind the ball</b> in every plan except Chase: both CBs, the pivot and the far full-back. {clip("P1")}', ev(['v140'], coach=True)),
  ('<b>Role, Role+ and Role++.</b> EA says familiarity can make 10% to 40% of the difference (FC 25), and FC 26 brought Role and Role+ “closer to Role++” and cut the out-of-position penalty. Chase ++ in the pivot and striker roles, but don’t drop a better player for it.', ev(['fc25iq', 'dd'], coach=True)),
  ('<b>New FC 26 roles.</b> Box Crasher: a CDM who makes trailing runs into the box, made for Chase. Inverted Wingback: a full-back who moves central and high when you have the ball, risky against an AI that counters. Wide Back: a CB who opens wide to cover his full-back. Ball-Playing Keeper: an option in build-up who stays on his line in defence.', ev(['dd'], coach=True)),
  ('<b>A pro’s offline view:</b> “make the pitch as big as possible”, with four at the back and three central midfielders or a 4-2-3-1, and wide players on the Winger role. 4-2-3-1 Wide is the alternative Control plan to test.', ev(['rbtac'])),
]
tactics = card('Tactics lab', 'A tactic for every scoreline',
  '        <p>One tactic for 90 minutes leaves points on the pitch. Save four and switch with the score. The numbers are a starting point within EA’s ranges: change one thing every two or three matches and check your log. ' + tag('Coach') + '</p>\n' +
  table('t-tac', ['Plan', 'D-pad', 'When', 'Shape and team settings', 'Roles that change'], [[f'<b>{e(a)}</b>', e(b), e(c), e(d), e(f)] for a, b, c, d, f in TAC]) +
  '        <ul class="plist pro-list">\n' + ''.join(li(a, b) for a, b in TAC_NOTES) + '        </ul>\n', wide=True)

SET = [
  ('<b>Corner jobs.</b> FC 26 added attacking roles Top of Box and Defensive Cover, and defending ones Threat Marker, Post Watcher, Near Post and Back Post. Put a good finisher on Top of Box for the ball that comes back out.', ev(['dd'], coach=True)),
  ('<b>Go short more often.</b> In Competitive gameplay, which Squad Battles uses, fewer attackers go up for corners by default and headers miss more. A short corner and a cutback beats a 50/50 header. Crossing anyway? Overload Set Pieces (Up, then Right) adds bodies, per one guide.', ev(['dd', 'fautsm'], coach=True)),
  ('<b>Throw-ins.</b> Press RB to call your chosen throw-in taker. Long throws need the Long Throw PlayStyle.', ev(['dd'])),
  ('<b>Free kicks.</b> EA re-tuned free-kick flight when it removed Timed Finishing. Guides disagree on power, from about 1.5 to 3.5 bars, so find your taker’s number in the Practice Arena, which lets you change the kick-taker in FC 26. Use a Dead Ball PlayStyle player.', ev(['dd', 'rs101fk', 'tgsp', 'fparena'])),
  ('<b>Penalties.</b> No FC 26 method could be confirmed. Practise them in the Practice Arena before you trust one.', ''),
]
setp = card('Set pieces', 'Dead balls, live chances', '        <ul class="plist pro-list">\n' + ''.join(li(a, b) for a, b in SET) + '        </ul>\n')

pts_rows = [['Legendary', '2.1', '0.7', '140 (max 700)'], ['Ultimate', '2.6', '0.7', '160 (max 800)']]
points = card('Squad Battles', 'Play the points',
  table('t-pts', ['Difficulty', 'Win multiplier', 'Loss multiplier', 'Points per goal'], pts_rows) +
  f'        <p class="pfoot">{ev(["fautpts"])}</p>\n'
  f'        <p><b>When Ultimate pays more.</b> With the same match points either way, Ultimate is worth it once your Ultimate win rate is about three-quarters of your Legendary one (2.6u + 0.7(1−u) ≥ 2.1l + 0.7(1−l), so u ≥ 0.74 l). Win 80% on Legendary and Ultimate pays from about 59%. {tag("Coach")}</p>\n'
  f'        <p>Up to 18 matches a week count. Check each squad before kick-off: one player drops to World Class against teams rated 80 or more. {ev(["launch", "cheese"])}</p>\n')

PRACTICE = [
  'Practice Arena, 15 minutes, twice a week. Ten first-time low drivens from cutbacks, ten finesse shots from the edge, ten chips past a keeper coming out. Move up a station at 8 out of 10.',
  'One skill move a week: 50 reps in the arena, then use it in matches only in its moment from the table above.',
  'Scan trainer at Ultimate speed (1.4 seconds) until you score 8 out of 10 twice in a row.',
  'After every match, open Match Facts. One guide says it shows Expected Goals and Ball Recovery Time. Log your xG for and against, and how each goal against started.',
  'Change one thing at a time: a tactic setting or a habit, every two or three matches, then check the log.',
]
practice = card('Practice', 'Train like it matters',
  '        <p>Pros don’t just play more matches. They drill one thing, measure it, then test it in a match. Here is a week that works that way. ' + tag('Coach') + '</p>\n'
  '        <ol class="script">\n' + ''.join(f'          <li><span>{e(t)}</span></li>\n' for t in PRACTICE) + '        </ol>\n'
  f'        <p class="pfoot">Match Facts: {ev(["fautst"])} · Practice Arena: {ev(["fparena"])}</p>\n', wide=True)

ORDER = ['dd', 'fut', 'launch', 'oct', 'v110', 'v110n', 'v130', 'v140', 'v150', 'acc', 'fc25iq', 'may26',
         'fpctl', 'fpdef', 'fpprec', 'egpass', 'osd', 'osp', 'rbmeta', 'rbtac', 'dxld', 'fautsm', 'fautpts', 'cheese',
         'rbskill', 'beebom', 'osskill', 'dstr', 'oslock', 'fautst', 'fparena', 'rs101fk', 'tgsp']
assert sorted(ORDER) == sorted(U), set(U) ^ set(ORDER)
sources = ('      <article class="pcard pwide">\n        <p class="coach-k">Where this comes from</p>\n        <h2>Sources</h2>\n'
           '        <p class="pintro">Pages marked Unconfirmed were found through search but could not be opened when this tab was written (2026-11-04), so treat those lines as leads to test.</p>\n'
           '        <ol class="srcs">\n' +
           ''.join(f'          <li>{tag(U[k][0])} <a href="{e(U[k][2])}" target="_blank" rel="noopener">{e(U[k][1])}</a></li>\n' for k in ORDER) +
           '        </ol>\n      </article>\n')

panel = ('  <section class="panel" id="p-pro" role="tabpanel" aria-labelledby="mt-pro" hidden>\n    <div class="plan pro">\n' +
         HEAD + finish + passing + defend + move + tactics + setp + points + practice + sources +
         '    </div>\n  </section>\n')
p = pathlib.Path(__file__).with_name('parts') / 'pro.html'
p.write_text(panel)
print('wrote', p, len(panel))

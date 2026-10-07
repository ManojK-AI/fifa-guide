#!/usr/bin/env python3
"""Builds the FC 26 Plan tab pieces: settings checklist, match script, squad, straight talk, sources."""
import html, pathlib

U = {
  'dd':     ('EA Sports: FC 26 Pitch Notes, Gameplay Deep Dive', 'https://www.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-gameplay-deep-dive'),
  'fut':    ('EA Sports: FC 26 Pitch Notes, Ultimate Team Deep Dive', 'https://www.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-fut-deep-dive'),
  'cb':     ('EA Sports: FC 26 Closed Beta feedback update', 'https://www.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-closed-beta-feedback-update'),
  'launch': ('EA Sports: FC 26 Launch update', 'https://www.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-launch-update'),
  'v102':   ('EA: FC 26 update 1.0.2 notes (low driven shots)', 'https://forums.ea.com/blog/ea-sports-fc-game-info-hub-en/fc-26-version-1-0-2-update-notes/12651602'),
  'v103':   ('EA: FC 26 update 1.0.3 notes (kick-off defending)', 'https://forums.ea.com/blog/ea-sports-fc-game-info-hub-en/fc-26-version-1-0-3-update-notes/12696716'),
  'v110':   ('EA Sports: FC 26 update 1.1.0 Pitch Notes', 'https://www.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-1-1-0-update'),
  'v110n':  ('EA: FC 26 update 1.1.0 notes', 'https://forums.ea.com/blog/ea-sports-fc-game-info-hub-en/fc-26-v1-1-0-update-notes/12815780'),
  'v113':   ('EA: FC 26 update 1.1.3 notes (CPU AI)', 'https://forums.ea.com/blog/ea-sports-fc-game-info-hub-en/ea-sports-fc-26-version-1-1-3-update-notes/12876617'),
  'v120':   ('EA: FC 26 update 1.2.0 notes', 'https://forums.ea.com/blog/ea-sports-fc-game-info-hub-en/ea-sports-fc-26-version-1-2-0-update-notes/12906902'),
  'v130':   ('EA: FC 26 update 1.3.0 notes', 'https://forums.ea.com/blog/ea-sports-fc-game-info-hub-en/ea-sports-fc-26-version-1-3-0-update-notes/12977359'),
  'v140':   ('EA Sports: FC 26 Title Update 1.4.0 Pitch Notes', 'https://www.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-title-update-1-4-0'),
  'v140n':  ('EA: FC 26 update 1.4.0 notes', 'https://forums.ea.com/blog/ea-sports-fc-game-info-hub-en/ea-sports-fc-26-version-1-4-0-update-notes/13073501'),
  'v150':   ('EA Sports: FC 26 Title Update 1.5.0 Pitch Notes', 'https://www.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-title-update-1-5-0'),
  'acc':    ('EA: FC 26 accessibility and settings guide', 'https://www.ea.com/able/resources/ea-sports-fc/fc-26'),
  'fc25iq': ('EA Sports: FC 25 FC IQ deep dive (the tactics system FC 26 still uses)', 'https://www.ea.com/games/ea-sports-fc/fc-25/news/pitch-notes-fc-25-fc-iq-deep-dive'),
  'rs101':  ('RealSport101: best FC 26 controller and camera settings', 'https://realsport101.com/article/fc-26-game-settings-best-controller-camera-settings'),
  'sks':    ('Sportskeeda: best FC 26 controller and game settings', 'https://www.sportskeeda.com/gaming-tech/best-ea-fc-26-controller-and-game-settings'),
  'egset':  ('EarlyGame (German): best FC 26 controller settings', 'https://earlygame.com/de/guides/fifa/ea-fc-26-die-besten-controller-einstellungen-fuer-einen-perfekten-start'),
  'dxcam':  ('Dexerto: best FC 26 camera settings', 'https://www.dexerto.com/wikis/ea-fc-26-guides-walkthrough-tips/best-camera-settings/'),
  'rbset':  ('Red Bull: best FC 26 controller and gameplay settings', 'https://www.redbull.com/us-en/ea-fc-26-best-controller-and-gameplay-settings'),
  'rbmeta': ('Red Bull: FC 26 meta guide', 'https://www.redbull.com/us-en/fc-26-meta-guide-tactics-dribbling-attacking'),
  'futgg':  ('fut.gg: 4-3-3(4) custom tactics in FC 26', 'https://www.fut.gg/news/4-3-34-custom-tactics-the-hyper-aggressive-setup-to-break-ai-defending-in-fc-26/'),
  'fpform': ('FIFPlay: FC 26 4-3-3 Attack', 'https://www.fifplay.com/fc-26/formations/4-3-3-attack/'),
  'fpctl':  ('FIFPlay: FC 26 controls', 'https://www.fifplay.com/fc-26-controls/'),
  'fp23ctl':('FIFPlay: FIFA 23 controls (Agile Dribble)', 'https://www.fifplay.com/fifa-23-controls/'),
  'fpps':   ('FIFPlay: FC 26 PlayStyles', 'https://www.fifplay.com/fc-26-playstyles/'),
  'fautacc':('FIFAUTeam: FC 26 AcceleRATE', 'https://fifauteam.com/fc-26-accelerate/'),
  'fautpts':('FIFAUTeam: FC 26 Squad Battles points', 'https://fifauteam.com/fc-26-squad-battle-points/'),
  'egpass': ('EarlyGame (German): FC 26 passing guide', 'https://earlygame.com/de/guides/fifa/ea-fc-26-so-bringst-du-jeden-pass-ans-ziel'),
  'cheese': ('EA forums: “Cheesing squad battles” (player tips)', 'https://forums.ea.com/discussions/fc-26-ultimate-team-en/cheesing-squad-battles/13016774'),
  'disap':  ('EA forums: FC 26 Squad Battles player report', 'https://forums.ea.com/discussions/fc-26-ultimate-team-en/fc26-squad-battles-is-the-biggest-disappointment-of-the-game-itself/13093643'),
  'sk23':   ('Sportskeeda (FIFA 23): bring the keeper halfway', 'https://sportskeeda.com/esports/5-best-tips-defending-fifa-23-march-2023'),
  'jordet': ('Jordet and others (2020): scanning in Premier League players', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC7573254'),
}
SHORT = {'dd':'EA Deep Dive','fut':'EA Ultimate Team Deep Dive','v102':'EA update 1.0.2 notes','v103':'EA update 1.0.3 notes','v110':'EA update 1.1.0','v110n':'EA update 1.1.0 notes','v113':'EA update 1.1.3 notes',
         'v120':'EA update 1.2.0 notes','v130':'EA update 1.3.0 notes','v140':'EA update 1.4.0','v140n':'EA update 1.4.0 notes','v150':'EA update 1.5.0','acc':'EA settings guide','fc25iq':'EA FC IQ (FC 25)',
         'rs101':'RealSport101','sks':'Sportskeeda','egset':'EarlyGame settings (German)','dxcam':'Dexerto','rbset':'Red Bull settings','rbmeta':'Red Bull meta guide',
         'futgg':'fut.gg 4-3-3 (4)','fpctl':'FIFPlay controls','fpps':'FIFPlay PlayStyles','fautacc':'FIFAUTeam AcceleRATE','cheese':'EA forums (player tip)',
         'egpass':'EarlyGame passing (German)'}

def e(x): return html.escape(x, quote=True)
def a(k): return f'<a class="src" href="{e(U[k][1])}" target="_blank" rel="noopener">{e(SHORT[k])}</a>'
def srcs(keys): return ' · '.join(a(k) for k in keys)
def clip(k): return f'<button type="button" class="clip-ref" data-clip="{k}" aria-label="Watch clip {k}">▶ {k}</button>'

CHECKS = [
  ('cam',   'Camera: Co-Op, Height 20, Zoom 0.', 'You see almost the whole pitch, so free men and runners jump out. Too far away? Tele Broadcast at the same height and zoom.', ['rs101','dxcam']),
  ('pzoom', 'Power Shot Zoom: Off.', 'The camera stops moving in on power shots, so the box stays in view.', ['rs101','egset']),
  ('radar', 'Radar: 2D.', 'One glance shows the far side. My pick: FC 26 guides don’t name one.', []),
  ('ind',   'Next Player Switch Indicator: On.', 'Shows who you get when you press LB, so you switch to the right man first time.', ['acc']),
  ('auto',  'Auto Switching: Air Balls and Loose Balls. Auto Switching Move Assistance: None.', 'The game only switches for you on balls in the air and loose balls, and doesn’t keep your new player running in his old direction.', ['rs101','egset']),
  ('lock',  'Pass Receiver Lock: Late.', 'You can change who the pass goes to at the last moment if a lane closes.', ['rbset','rs101']),
  ('assist','Ground Pass: Assisted. Through Pass: Semi. Lobbed Through Pass: Semi. Shot Assistance: Assisted.', 'Full help on the passes you play most, more control over through balls. Some guides pick Precision for shots.', ['rs101','sks']),
  ('def',   'Defending: Tactical.', 'Keeps hold A as Contain, the way the clips here use it. On the default, Advanced, hold A is a physical tackle.', ['fpctl','acc','rbset']),
  ('shot',  'Learn the new low shot: double-tap B.', 'Timed Finishing is gone in FC 26. A double-tap of B is now a low driven shot.', ['dd']),
  ('tac',   'Tactics: Build-Up Style Balanced, Defensive Approach Balanced, Line Height 45.', 'Balanced build-up gives you runners and short options. A line just under the default 50 means fewer balls in behind you.', ['dd','fc25iq']),
  ('roles', 'Roles in 4-3-3 (4), also listed as 4-3-3 Attack.',
            'Striker: Advanced Forward (Attack)\nWingers: Inside Forward (Balanced)\nCAM: Shadow Striker (Attack)\nOne CM: Deep-Lying Playmaker (Build-Up)\nOther CM: Box-to-Box (Balanced)\nFull-backs: Fullback (Defend)\nCBs: Defender (Defend)\nBased on fut.gg’s FC 26 4-3-3 (4), with both full-backs on Defend.', ['futgg']),
  ('warm',  'One round of the Scan trainer at Legendary speed.', 'Wakes your eyes up before the first whistle.', []),
]

def check(k, b, t, s):
    tail = (' ' + srcs(s)) if s else ''
    body = e(t).replace('\n', '<br>')
    if '\n' in t:
        body = '<br>' + body
    return f'          <li><label><input type="checkbox" data-chk="f26-{k}"><span><b>{e(b)}</b> {body}{tail}</span></label></li>\n'

checks = ('        <p class="pintro g26">Most of these are in the Camera and Controller Settings menus. Tick each one once it is set.</p>\n'
          '        <ul class="checks g26">\n' + ''.join(check(*c) for c in CHECKS) + '        </ul>\n')

SCRIPT = [
  ('Kick-off.', 'FC 26 defenders sit compact right after kick-off. Pass back, keep it, and go over the top (LB + Y) only if their line is still high.', ['U1'], ['v103']),
  ('On the ball.', 'Look first. Quick, first-time passes. Aim through balls at the gap between two defenders.', ['C4'], ['rbmeta','dd']),
  ('In the box.', 'Cut it back to the edge. Defender within a yard? Fake shot. Keeper rushing out? Chip it (LB + B). Otherwise a low driven shot: double-tap B.', ['C1','U3','U5'], ['v120','v150']),
  ('Defending.', 'Hold your line and press with midfielders, not CBs. Jockey (LT), and never tackle from behind.', ['A1','A2'], ['dd','v110']),
  ('You win it.', 'Go forward fast. Since update 1.4.0 AI defenders react slower when marking the man on the ball.', ['U2'], ['v140n']),
  ('Leading late.', 'Keep the ball. If they push up, win it and counter: a player on EA’s forums says the AI “seems to really struggle with counter attacks”.', ['A6'], ['cheese']),
]
script = ('      <article class="pcard g26">\n        <p class="coach-k">Your match script</p>\n        <h2>Six steps, every game</h2>\n        <ol class="script">\n' +
          ''.join(f'          <li><span><b>{e(b)}</b> {e(t)} ' + ' '.join(clip(c) for c in cl) + ' ' + srcs(s) + '</span></li>\n' for b, t, cl, s in SCRIPT) +
          '        </ol>\n      </article>\n')

SQUAD = [
  ('Striker: tall and strong.', 'Since update 1.4.0 more tall players get Lengthy acceleration: a man needs 185 cm or more, Strength 65+, Strength at least 4 above Agility, and Acceleration 40+. Strength also wins shoulder challenges and battles for high balls.', ['v140','dd']),
  ('Wingers and full-backs: Explosive.', 'Quick off the mark over short bursts, for beating a man and for getting back.', ['dd','fautacc']),
  ('CBs: strong and good in the air.', 'Strength wins the battle for high balls at corners, and the new Aerial Fortress PlayStyle wins defensive headers.', ['dd']),
  ('PlayStyles worth having.', 'Finesse Shot and Low Driven Shot up front, Incisive Pass in midfield, Jockey and Intercept at the back.', ['fpps']),
  ('Pace up front.', 'Fast counters are one of FC 26’s strongest attacks, and players beating Squad Battles lean on fast players.', ['rbmeta','cheese']),
]
squad = ('      <article class="pcard g26">\n        <p class="coach-k">Your squad</p>\n        <h2>Players that fit this plan</h2>\n        <ul class="plist">\n' +
         ''.join(f'          <li><b>{e(b)}</b> {e(t)} {srcs(s)}</li>\n' for b, t, s in SQUAD) +
         '        </ul>\n      </article>\n')

honest = '''      <article class="pcard pwide honest g26">
        <p class="coach-k">Straight talk</p>
        <h2>What this can and can’t do</h2>
        <p>No guide promises you’ll beat Ultimate every game. EA retuned the Squad Battles AI in November 2025 (update 1.1.3) and January 2026 (update 1.4.0), and hasn’t published Legendary vs Ultimate numbers for FC 26.</p>
        <p>What every source agrees on: play into space, go fast once you win it, defend with patience. Set Defending to Tactical so your buttons match these clips. Then reps: win most Squad Battles on Legendary before you step up to Ultimate.</p>
      </article>
'''

ORDER = ['dd','fut','cb','launch','v102','v103','v110','v110n','v113','v120','v130','v140','v140n','v150','acc','fc25iq','rs101','sks','egset','dxcam','rbset','rbmeta',
         'futgg','fpctl','fp23ctl','fpps','fautacc','fautpts','egpass','cheese','disap','sk23','jordet']
sources = ('      <article class="pcard pwide g26">\n        <p class="coach-k">Where this comes from</p>\n        <h2>Sources</h2>\n        <ol class="srcs">\n' +
           ''.join(f'          <li><a href="{e(U[k][1])}" target="_blank" rel="noopener">{e(U[k][0])}</a></li>\n' for k in ORDER) +
           '        </ol>\n      </article>\n')

d = pathlib.Path(__file__).with_name('parts')
(d / 'plan26_checks.html').write_text(checks)
(d / 'plan26_cards.html').write_text(script + squad + honest + sources)
print('ok', len(checks), len(script + squad + honest + sources))

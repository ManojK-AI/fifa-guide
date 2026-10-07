#!/usr/bin/env python3
"""Builds the FC 26 scouting report (AI moves tab) as HTML, using the same markup as the FIFA 23 cards."""
import html, json, pathlib

S = {
  'dd':   ('EA, FC 26 Gameplay Deep Dive', 'https://www.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-gameplay-deep-dive'),
  'cb':   ('EA, Closed Beta feedback update', 'https://www.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-closed-beta-feedback-update'),
  'launch': ('EA, Launch update', 'https://www.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-launch-update'),
  'v110': ('EA, update 1.1.0', 'https://www.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-1-1-0-update'),
  'v113': ('EA, update 1.1.3 notes', 'https://forums.ea.com/blog/ea-sports-fc-game-info-hub-en/ea-sports-fc-26-version-1-1-3-update-notes/12876617'),
  'v120': ('EA, update 1.2.0 notes', 'https://forums.ea.com/blog/ea-sports-fc-game-info-hub-en/ea-sports-fc-26-version-1-2-0-update-notes/12906902'),
  'v130': ('EA, update 1.3.0 notes', 'https://forums.ea.com/blog/ea-sports-fc-game-info-hub-en/ea-sports-fc-26-version-1-3-0-update-notes/12977359'),
  'v140': ('EA, update 1.4.0', 'https://www.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-title-update-1-4-0'),
  'v140n': ('EA, update 1.4.0 notes', 'https://forums.ea.com/blog/ea-sports-fc-game-info-hub-en/ea-sports-fc-26-version-1-4-0-update-notes/13073501'),
  'v150': ('EA, update 1.5.0', 'https://www.ea.com/games/ea-sports-fc/fc-26/news/pitch-notes-fc26-title-update-1-5-0'),
  'rbmeta': ('Red Bull, FC 26 meta guide', 'https://www.redbull.com/us-en/fc-26-meta-guide-tactics-dribbling-attacking'),
  'cheese': ('EA forums, player tip', 'https://forums.ea.com/discussions/fc-26-ultimate-team-en/cheesing-squad-battles/13016774'),
  'disap': ('EA forums, player report', 'https://forums.ea.com/discussions/fc-26-ultimate-team-en/fc26-squad-battles-is-the-biggest-disappointment-of-the-game-itself/13093643'),
  'sk23': ('Sportskeeda (FIFA 23 tip)', 'https://sportskeeda.com/esports/5-best-tips-defending-fifa-23-march-2023'),
  'fautpts': ('FIFAUTeam, Squad Battles points', 'https://fifauteam.com/fc-26-squad-battle-points/'),
}

ATK = [
  dict(t='Goes forward fast',
       see='Their midfielder looking forward the moment he gets it, instead of passing it sideways.',
       do='Get your shape first. Press with a midfielder, keep your CBs home, and press LB to switch to the CB nearest their runner.',
       why='Since update 1.4.0 (January 2026) EA says the Squad Battles AI takes “a more proactive and attacking approach” and won’t keep the ball as much as before.',
       clips=['A1'], src=['v140']),
  dict(t='Through ball between your CBs',
       see='Their striker level with your last defender and a gap opening between your two CBs.',
       do='Don’t step out with a CB. Jockey (LT) goal-side of the runner and let a midfielder press the passer.',
       why='Since update 1.1.3 the AI looks for passes more often and decides quicker. A player reports pinpoint through balls between two defenders.',
       clips=['A1','D1'], src=['v113','disap']),
  dict(t='Sharp dribbler',
       see='A dribbler cutting back and changing direction instead of running in a straight line.',
       do='Jockey (LT) a yard off, on his inside. Never tackle from behind. Tackle (B) when he slows or turns his back.',
       why='Update 1.1.3 made the AI dribble with sharper turns and less time on the ball. EA also made tackles from behind less effective, and jockey quicker (update 1.1.0).',
       clips=['A2'], src=['v113','dd','v110']),
  dict(t='Late shot from the edge of your box',
       see='The ball goes wide near your box and their midfielder arrives late at the edge.',
       do='Keep one midfielder on the edge. Control him and close the runner while the pass travels.',
       why='EA says AI players are less timid about shooting and power up shots like a person. Since update 1.2.0 AI defenders, yours included, mark the edge of the box a little less tightly.',
       clips=['A4'], src=['cb','dd','v120']),
  dict(t='Crosses into your box',
       see='A winger with grass ahead of him on the touchline, or already at your byline.',
       do='Full-back goal-side and jockey him outside. CBs stay in the box. Switch to the near-post CB before the cross.',
       why='Pull a CB out to the winger and your box is short. Update 1.3.0 lowered crosses, so they come in flatter.',
       clips=['A3'], src=['v130']),
  dict(t='Quick passing through your lines',
       see='Short, fast passes into feet between your midfield and defence.',
       do='Stand in the passing lane and let the man come to you. Don’t chase the ball.',
       why='Update 1.5.0 made ground passes quicker and more accurate, most of all for good passers, the AI’s included.',
       clips=['D2'], src=['v150']),
  dict(t='Strong man shielding the ball',
       see='A big forward with his back to you, holding you off.',
       do='Don’t barge him from behind. Stay goal-side, bring a second man with hold RB, and win it when he turns.',
       why='Update 1.4.0 gave Strength and Aggression more say in shielding, and EA cut the success of tackles from behind.',
       clips=[], src=['v140','dd']),
  dict(t='Striker through on your keeper',
       see='Their striker clean through, your keeper on his line.',
       do='Hold Y briefly to bring the keeper halfway, then let him set. Don’t charge all the way.',
       why='Update 1.5.0 made chip shots more accurate, more so for strikers with the Chip Shot PlayStyle. The halfway idea itself is a FIFA 23 tip.',
       clips=['A5'], src=['v150','sk23']),
  dict(t='Corners',
       see='Their strongest players lining up in your box.',
       do='Put your strongest headers on the defending-corner jobs FC 26 added: Near Post, Back Post and Threat Marker.',
       why='FC 26 added those corner roles, and EA says stronger players now win the battle for a high ball.',
       clips=[], src=['dd']),
]

DEF = [
  dict(t='Slow to react in transition',
       see='You beat their first press and their defenders are slow to react.',
       do='Go now. Drive forward or play the runner before they reset.',
       why='Update 1.4.0: AI defenders react slower when marking the man on the ball, which leaves space while they reset.',
       clips=['U2'], src=['v140n']),
  dict(t='Looser line, fewer automatic blocks',
       see='Gaps in their back line and a defender a few yards off your striker.',
       do='Shoot early with a low driven shot (double-tap B), or slide the runner into the gap.',
       why='Squad Battles uses Competitive gameplay. EA lists “less AI defending, resulting in looser defensive lines” and “fewer auto tackles and auto blocks”.',
       clips=['U6','C4'], src=['dd']),
  dict(t='Gaps between two defenders',
       see='A runner and a lane between two of their defenders.',
       do='Aim the through ball (Y) at the gap, not at the player. Through Pass Assistance on Semi.',
       why='FC 26 semi-assisted through balls use passing lanes: aim at the gap between two opponents and the game picks the runner in it.',
       clips=['C4'], src=['dd','v110']),
  dict(t='Edge of its box left open',
       see='Their defenders dropping toward goal while your midfielder arrives late.',
       do='Get to the byline, then cut it back to the edge of the box.',
       why='Since update 1.2.0 AI defenders mark the edge of their box a little less tightly.',
       clips=['C1'], src=['v120']),
  dict(t='Two men close you down',
       see='Two of them stepping up to your man on the ball.',
       do='Pass and move. First-time passes, then run into the space they left.',
       why='Red Bull’s FC 26 meta guide rates quick, first-time passing as one of the strongest attacks, and calls first-time passes “extremely powerful”.',
       clips=['U7','C3'], src=['rbmeta']),
  dict(t='Blocks up close',
       see='A defender within a yard when your striker wants to shoot.',
       do='Fake shot first (B then A, with a direction), then shoot with space.',
       why='Close up he can get a foot to it. Update 1.5.0 made the Fake Shot 5% faster.',
       clips=['U3'], src=['v150']),
  dict(t='Keeper in a one-on-one',
       see='Your striker through, their keeper deciding whether to come.',
       do='If he rushes out, chip it (LB + B). If he stays home, low driven (double-tap B) to a corner.',
       why='EA says FC 26 keepers make “more reasonable” one-on-one decisions, and update 1.5.0 made chips more accurate.',
       clips=['U5'], src=['dd','v150']),
  dict(t='Finesse from the edge, not from range',
       see='Space at the edge of the box after a cut inside.',
       do='Cut inside, then finesse to the far post (RB + B). From long range, use a power shot (LB + RB + B).',
       why='At launch EA cut the top spin on finesse shots from outside the box. Update 1.5.0 made power shots better from range. Players still rate the stronger Finesse Shot+ PlayStyle in Squad Battles.',
       clips=['C3','U3'], src=['launch','v150','cheese']),
  dict(t='Leaves space when it attacks',
       see='Their full-backs and midfielders forward when you win the ball.',
       do='Win it, then go straight into the space behind them.',
       why='Update 1.4.0 made the Squad Battles AI more attacking. A player on EA’s forums says it “seems to really struggle with counter attacks”.',
       clips=['A6'], src=['v140','cheese']),
]

def e(x): return html.escape(x, quote=True)

def card(i, c):
    clips = ''.join(f'<button type="button" class="clip-ref" data-clip="{k}" aria-label="Watch clip {k}">▶ {k}</button>' for k in c['clips'])
    srcs = ' · '.join(f'<a class="src" href="{e(S[k][1])}" target="_blank" rel="noopener">{e(S[k][0])}</a>' for k in c['src'])
    return f'''        <article class="mcard">
          <h4><span class="mnum">{i}</span>{e(c['t'])}</h4>
          <p class="mrow"><b>You’ll see</b>{e(c['see'])}</p>
          <p class="mrow mdo"><b>Do this</b>{e(c['do'])}</p>
          <p class="mrow mwhy"><b>Why</b>{e(c['why'])}</p>
          <p class="mfoot">{clips}<span class="msrc">{srcs}</span></p>
        </article>
'''

def a(k, label=None):
    t, u = S[k]
    return f'<a class="src" href="{e(u)}" target="_blank" rel="noopener">{e(label or t)}</a>'

head = f'''    <div class="g26">
    <div class="ai-head">
      <div class="ai-intro">
        <p class="coach-k">Scouting report · FC 26 AI</p>
        <h2 class="ai-title">Know every move it makes</h2>
        <p class="ai-lede">What the FC 26 AI does, how to spot it early, and how to punish it. Each move comes from EA’s FC 26 patch notes, or from players and guides, and says which. Tap ▶ to watch it animated, or drill the reads in the trainer.</p>
      </div>
      <div class="ai-nums">
        <p class="coach-k">Squad Battles AI in FC 26</p>
        <table class="nums kv">
          <tbody>
            <tr><th scope="row">Gameplay</th><td>Competitive, always. EA locks it in Ultimate Team.</td></tr>
            <tr><th scope="row">Tiredness</th><td>EA says CPU-controlled players in Squad Battles aren’t affected by fatigue.</td></tr>
            <tr><th scope="row">Since update 1.4.0</th><td>The Squad Battles AI attacks more. AI defenders on both sides react slower.</td></tr>
            <tr><th scope="row">Ultimate vs Legendary</th><td>EA hasn’t published the numbers for FC 26.</td></tr>
          </tbody>
        </table>
        <p class="nums-note">Squad Battles runs from Beginner up to Ultimate. {a('dd','EA Deep Dive')} · {a('v140','EA update 1.4.0')} · {a('v140n','EA update 1.4.0 notes')} · {a('fautpts','FIFAUTeam')}</p>
      </div>
    </div>
    <section class="ai-sec" aria-labelledby="ai26-atk-h">
      <div class="ai-sec-h"><div><h3 id="ai26-atk-h">When it attacks you</h3><p>Nine moves to read and stop.</p></div><button type="button" class="drill" data-drill="def">Drill these reads ▶</button></div>
      <div class="mgrid">
'''
mid = '''      </div>
    </section>
    <section class="ai-sec" aria-labelledby="ai26-def-h">
      <div class="ai-sec-h"><div><h3 id="ai26-def-h">When it defends</h3><p>Nine habits to break.</p></div><button type="button" class="drill" data-drill="att">Drill these reads ▶</button></div>
      <div class="mgrid">
'''
tail = '''      </div>
    </section>
    </div>
'''
assert len(ATK) == 9 and len(DEF) == 9
out = head + ''.join(card(i+1, c) for i, c in enumerate(ATK)) + mid + ''.join(card(i+1, c) for i, c in enumerate(DEF)) + tail
p = pathlib.Path(__file__).with_name('parts') / 'ai26.html'
p.write_text(out)
print('wrote', p, len(out))

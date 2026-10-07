# Legendary Replay Room — QA notes

Files (read-only for QA; write your own scripts and output under your own folder inside qa/):
- work/replay-room.html — the page as it will be published. It is an HTML *fragment* (starts with <title>, no <html>/<head>); the publisher wraps it in its own skeleton. Use work/harness.py, which wraps it exactly like the publisher, serves fonts locally and collects console errors.
- work/harness.py — `open_page(browser, width, height, dark=False, game=None, storage=None)` returns (context, page, errors). `game` is 'fc26' or 'fc23' (pre-sets localStorage 'lrr:game'). Fonts come from work/fontpkg (the sandbox cannot reach Google Fonts).
- work/smoke.py — an example test using the harness.
- work/audit/fc26.json, work/audit/fc23.json — every visible string per tab, per clip (coach card, captions, key prompts) and trainer feedback, in each game mode.
- Playwright for Python is installed; Chromium is at /opt/pw-browsers (never run `playwright install`).

Page structure:
- Game switch in the masthead: buttons [data-gm="fc26"] / [data-gm="fc23"]; sets <html data-game="..."> and localStorage lrr:game. Default FC 26. Elements with class .g26 show only in FC 26, .g23 only in FIFA 23.
- Four tabs (#mt-trainer, #mt-ai, #mt-replays, #mt-plan) control panels #p-trainer, #p-ai, #p-replays, #p-plan. Arrow keys move between tabs.
- Trainer: canvas #tcv; Start button #tstart; levels [data-lv], focus [data-tf], camera [data-tv]; choices .tchoice; Next #tnext; feedback text #tsay; "Watch" button #tclip; summary #tsum.
- AI moves: cards .mcard; "Drill these reads" buttons [data-drill]; clip links .clip-ref[data-clip].
- Replays: picker .titem[data-i]; canvas #cv; caption #say; key chip #keychip/#kcRow; coach card #coach (#cWatch, #cCue, #cSet, #cKeys, #cNote, #cN26 = 'In FC 26' note, #cSrc); transport #playBtn, #prevBtn, #nextBtn, #restartBtn, scrubber #scrub, #jumpW/#jumpR (wrong/right), camera #viewBoard/#viewCam, speed #spdHalf/#spdOne/#spdFast; pre-game reel #reelBtn (FC 26 reel: U2 A1 U3 A2 A4 C1 U6; FIFA 23 reel: U1 A1 U2 U3 A2 A3 U6).
- Plan: checkboxes [data-chk] (FC 26 ones start with f26-), count #chkCount, reset #chkReset.
- Keyboard: trainer Space start/next, 1-3 pick; Replays Space play/pause, arrows change clip; V switches camera.

Debug hooks (window): __lrrMode(m), __lrrGame(g), __lrrShow(tacticIndex, 'wrong'|'right', clipSeconds, 'board'|'cam', mid), __lrrTrain(sceneIndex, flip, 'play'|'ask'|'reveal', pick, view), __lrrAnsPt(playerId?) -> screen point of the right answer during the 'ask' phase, __lrrScene(i, flip).

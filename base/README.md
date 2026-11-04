# base/

`replay-room-fifa23.html` is the page `build.py` starts from: the published FIFA 23
Replay Room (v3), wrapped in the artifact publisher's own `<head>` skeleton.
`build.py` keeps everything from `<title>` to the last `</script>`, then applies its
exact-match edits and inserts the FC 26 parts from `parts/`. `harness.py` reuses
the skeleton above `<title>` to wrap the built page the way the publisher does.

## Why it is here

Until 2026-11-04 both scripts read this page from `../live/index.html`, outside the
repo. It was never committed, so a fresh clone could not rebuild the page or run a
single test.

## How it was recovered

The original file was not available, so it was rebuilt from the committed
`replay-room.html` by undoing every edit `build.py` makes, in reverse order:
51 operations, with each inserted part masked so a reversed edit could only touch
the base page's own text. The publisher skeleton came from the live Replay Room
artifact.

**Check:** `python build.py` run on this file reproduces the committed
`replay-room.html` byte for byte (verified 2026-11-04, 282,538 bytes).

Two pieces could not be recovered exactly, because `build.py` throws them away. Neither
affects the built page:

| Piece | What happened to it | What is in this file instead |
|---|---|---|
| `initChecks()` | `build.py` replaces the whole function | A FIFA 23-only version, written to match the FC 26 one minus the game switch |
| `const REEL = [...]` | `build.py` deletes the line | The same line, placed at the top of the Playback section |

## Editing

Do not hand-edit the FIFA 23 content here unless you mean to change FIFA 23 for both
the base and the built page. Changes for FC 26, and anything new, go in `parts/` and
`build.py`. After any change run `python build.py`, then `python smoke.py` and
`python checks2.py`.

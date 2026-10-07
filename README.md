# FIFA Gaming Guide — EA FC 26 & FIFA 23

A comprehensive single-page HTML application with tactical guides, AI scouting reports, pre-game planning, and video replay analysis for both **EA FC 26** and **FIFA 23**.

## Overview

- **283 KB** single-file deployment (replay-room.html)
- **Dual-game support** with localStorage-based game switching
- **31 tactical clips** with canvas-based rendering and dual camera views (board + broadcast)
- **AI scouting reports** for both games with Gameplay/Tiredness analysis
- **Pre-game planner** with FC 26–specific checks and squad setup guidance
- **Trainer feedback** synchronized with game state
- **Responsive design** tested across 320–1280px widths and light/dark themes

## Project Structure

```
.
├── replay-room.html         # Final built artifact (open in browser)
├── build.py                 # Build script that composes all parts
├── parts/
│   ├── game.js             # FC 26 overrides, state management, utilities
│   ├── game.css            # Game-specific styles and layouts
│   ├── ai26.html           # FC 26 AI scouting report
│   ├── plan26_checks.html  # FC 26 pre-game checks
│   └── plan26_cards.html   # Squad setup and straight talk
├── make_ai26.py            # Generator for AI 26 content
├── make_plan26.py          # Generator for Plan 26 content
├── smoke.py                # Comprehensive functional test suite
├── checks2.py              # Targeted QA verification
├── harness.py              # Playwright test harness
├── docs/
│   ├── legendary-playbook.md   # The written coaching playbook
│   └── research/               # Source research, bibliography, verification log
│       ├── README.md           #   coverage map — READ BEFORE RESEARCHING
│       ├── SOURCES.md          #   79 cited sources + 95 logged dead ends
│       ├── METHODOLOGY.md      #   how it was gathered, confidence scale, limits
│       ├── VERIFICATION_LOG.md #   102 claims checked, issues, resolutions
│       ├── TEMPLATE.md         #   how to add research without duplicating
│       ├── agents/             #   the three full research reports
│       └── qa/                 #   claim verdicts, test code, logs, bug shots
└── fontpkg/                # Self-hosted fonts (Instrument Sans, Kalam, Big Shoulders)
```

## Documentation and research

The content in this page is not improvised — it rests on a researched, fact-checked
evidence base kept in [`docs/research/`](docs/research/).

**Before researching anything about FC 26 or FIFA 23, read
[`docs/research/README.md`](docs/research/README.md).** Its coverage map says what is
already answered and to what depth; its "Known gaps" section says what was already
searched for and not found. Re-researching covered ground wastes a search budget on
questions that already have answers in `docs/research/agents/`.

[`docs/research/TEMPLATE.md`](docs/research/TEMPLATE.md) contains a briefing prompt to
paste at the start of any future AI research session, so it reads the archive before
it starts searching.

| Want to… | Go to |
|---|---|
| Look up the source for a claim | `docs/research/SOURCES.md` |
| Judge how far to trust a finding | `docs/research/METHODOLOGY.md` |
| See what was checked and what failed | `docs/research/VERIFICATION_LOG.md` |
| Read the raw research | `docs/research/agents/` |
| Read the coaching playbook | `docs/legendary-playbook.md` |

## Quick Start

### Open the Guide
Simply open `replay-room.html` in any modern browser. No build step required for basic usage.

### Switching Between FC 26 and FIFA 23
Click the eyebrow toggle at the top-left to switch between the two games. Your choice is saved locally via localStorage.

## Development & Building

### Prerequisites
- Python 3.7+
- Node.js/npm (for Playwright tests)
- A modern browser (Chrome, Firefox, Safari, Edge)

### Local Setup

1. **Install test dependencies** (optional, for running tests):
   ```bash
   pip install playwright
   playwright install chromium
   ```

2. **Run the build** (if you modify parts):
   ```bash
   python build.py
   ```
   This regenerates `replay-room.html` from the modular parts.

3. **Run tests** (verify everything works):
   ```bash
   python smoke.py    # Comprehensive browser automation tests
   python checks2.py  # Targeted QA checks
   ```

## Key Features

### Game Switching (FC 26 ↔ FIFA 23)
- **AI reports**: Separate card analysis for each game
- **Button labels**: Xbox prompt labels tailored to each game's controls
- **Trainer feedback**: Updated captions and tips per game
- **Plan checks**: FC 26 has 12 specific setup checks; FIFA 23 uses generic guidance
- **Persistence**: Selected game saved to localStorage

### Tactical Clips (31 total)
Each clip includes:
- **Board view**: Overhead camera with player positions and movement
- **Broadcast view**: In-game camera perspective
- **Narrator voiceover**: Coach commentary with key tactical insights
- **Timer & playback**: Play/pause, loop support
- **Keyboard shortcuts**: Named buttons for quick access

### Canvas Rendering
- Real-time tactical animation with dual camera modes
- Responsive scaling to viewport size
- Dark-mode color contrast preservation

### AI Scouting Reports
**FC 26 cards** (9 ATK + 9 DEF):
- Gameplay analysis (chemistry, positioning, aggression)
- Tiredness factor and match impact
- Legendary vs Ultimate difficulty notes
- Source attribution

**FIFA 23 cards** (same structure, different tactics):
- Compatible analysis for legacy game

### Pre-Game Planning
**FC 26 Checks** (12 items):
- Camera, zoom, radar, auto-switching setup
- Assist and defending mode configuration
- Player roles and tactical setup
- Warm-up checklist

**FIFA 23**:
- General Squad Straight Talk
- Formation and role guidance

## Editing & Extending

### Modify Game.js (FC 26 Overrides)
Edit `parts/game.js` to:
- Change `F26` object entries (per-clip cue, setting, sources)
- Update `SAY26` captions
- Adjust `FB26` trainer feedback
- Modify `L26` Xbox button labels

**Common changes**:
```javascript
// Update AI captions
SAY26: {
  'old text': 'new text',
  // ...
}

// Override trainer feedback
FB26: {
  'old feedback': 'new feedback',
  // ...
}

// Fix clip references
F26: {
  'clip_name': { cue: 100, watch: [0, 2, 3], n: 'Note here' },
  // ...
}
```

### Regenerate Components
If you rebuild `parts/ai26.html` or `parts/plan26_checks.html`:
```bash
python make_ai26.py   # Regenerates parts/ai26.html
python make_plan26.py # Regenerates parts/plan26_checks.html
python build.py       # Recomposes into replay-room.html
```

### Test Your Changes
After editing:
```bash
python smoke.py      # Full browser test suite
python checks2.py    # Quick QA checks
```

## File Sizes

| File | Size | Purpose |
|------|------|---------|
| `replay-room.html` | 277 KB | Final artifact, self-contained, ready to deploy |
| `game.js` | 13 KB | FC 26 overrides and state management |
| `game.css` | 1.5 KB | Game-specific styles |
| `ai26.html` | 21 KB | FC 26 AI scouting report |
| `plan26_checks.html` | 6 KB | FC 26 pre-game checks |
| `plan26_cards.html` | 13 KB | Squad setup guidance |
| `fontpkg/` | 3.2 MB | Self-hosted fonts (Instrument Sans, Kalam, Big Shoulders) |

## Git Workflow

### Initial Commit
```bash
git add .
git commit -m "Initial commit: FIFA guide with FC 26 and FIFA 23 support"
```

### Making Changes
1. Edit a file (`parts/game.js`, `parts/game.css`, etc.)
2. Rebuild if needed: `python build.py`
3. Test: `python smoke.py`
4. Commit:
   ```bash
   git add <changed-files>
   git commit -m "Update: [describe change]"
   ```

### Pushing to GitHub (Optional)
```bash
git remote add origin https://github.com/yourusername/fifa-guide.git
git branch -M main
git push -u origin main
```

## Testing

### Smoke Tests (`smoke.py`)
Comprehensive browser automation covering:
- Both games (FC 26, FIFA 23)
- All tabs and sections
- Responsive widths (320, 390, 820, 1280px)
- Light and dark themes
- Clip playback in both camera views
- Trainer feedback synchronization
- No horizontal scroll on narrow viewports
- Play icon state management
- Keyboard accessibility

**Result**: 0 failures

### Targeted Checks (`checks2.py`)
Focused QA on specific scenarios:
- Play icon updates after clip selection
- Keyboard focus management
- Key-chip label rendering at small widths
- Clip reference resolution
- Button label correctness

**Result**: 0 failures

## Browser Support

- Chrome/Chromium 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Accessibility

- Focus management on all interactive elements
- ARIA labels for screen readers
- Keyboard navigation (arrows, Enter, Space)
- Color contrast compliance (light & dark modes)
- Responsive text sizing

## License

Developed for personal game coaching and learning. Uses fonts from Fontsource (open-source).

## Contact & Support

For issues, feature requests, or contributions:
- Open a GitHub issue (if pushing to GitHub)
- Review test output (`smoke.py` / `checks2.py`) for validation
- Check `build.py` for build process details

---

**Last Updated**: 2026-10-07  
**Version**: 1.4.0+FC26 (includes full EA FC 26 integration, passes all QA)

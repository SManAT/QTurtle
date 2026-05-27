# QTurtle PySide6 Application Skill

Complete skill for running, testing, and verifying the QTurtle Python IDE with turtle graphics support.

## Files in this Skill

- **SKILL.md** — Complete documentation for running and testing the application
- **QUICK_TEST.md** — Quick reference checklist for manual testing (2-3 minutes)
- **test_qturtle.py** — Automated Python test suite for programmatic verification
- **README.md** — This file

## Quick Start

### Run the Application
```bash
cd src
python qturtle.py
```

### Run Automated Tests
```bash
python .claude/skills/qturtle-run/test_qturtle.py
```

### Manual Test Checklist
See QUICK_TEST.md for a 2-3 minute manual verification.

## Features Covered by This Skill

### Core Application
- ✅ **PySide6/Qt6 GUI** — Window, menus, toolbars, statusbar
- ✅ **Light Theme** — Atom One Light colors throughout
- ✅ **Code Editor** — Python syntax highlighting, line numbers, dark text on light background
- ✅ **Console Output** — Read-only output pane with error highlighting

### Editor Features
- ✅ **Zoom Controls**
  - Ctrl+Plus (Ctrl+Shift+=) to zoom in
  - Ctrl+Minus to zoom out
  - Ctrl+Mouse Wheel for smooth zooming
  - Bounds: 8pt min, 32pt max
- ✅ **Syntax Highlighting** — Keywords, strings, comments, numbers, builtins
- ✅ **Auto-Indentation** — Smart indentation on Enter, maintains indentation
- ✅ **Tab Handling** — Tab inserts 4 spaces, Shift+Tab removes 4 spaces
- ✅ **Line Numbers** — Dynamic width based on file length

### File Operations
- ✅ **New** — Create new document with unsaved changes prompt
- ✅ **Open** — Load .py files with full content
- ✅ **Save** — Save to current file or select new location
- ✅ **Save As** — Save with new filename
- ✅ **Window Title** — Shows filename and modification indicator (*)

### Script Execution
- ✅ **Run** — Execute Python code in subprocess (F5 or button)
- ✅ **Stop** — Terminate running script
- ✅ **Console Output** — Real-time output and error display
- ✅ **Exit Codes** — Display script exit status
- ✅ **Turtle Graphics** — Automatic turtle.done() for interactive graphics

### Theme/Colors (Atom One Light)
- ✅ Light background (#FAFAFA)
- ✅ Dark text (#383A42)
- ✅ Purple keywords (#A626A4)
- ✅ Green strings (#50A14F)
- ✅ Orange numbers (#986801)
- ✅ Gray comments (#A0A1A7)
- ✅ Blue accents (#4078F2)

## Test Coverage

### Automated Tests (test_qturtle.py)
- Theme colors (background, text, editor palette)
- Zoom functionality (bounds, min/max enforcement)
- Editor properties (syntax highlighter, line numbers, modification tracking)
- File operations (new, save, open, paths)
- Console styling (colors, read-only state)

### Manual Tests (QUICK_TEST.md)
- Visual theme verification
- Zoom controls (keyboard and mouse wheel)
- Script execution and output
- File save/open dialogs
- Editor indentation and tab handling
- Error display in console

### Full Documentation (SKILL.md)
- Detailed feature descriptions
- Complete test sequence
- Troubleshooting guide
- Known behaviors
- Color reference

## Platform Support

| Platform | Status | Notes |
|----------|--------|-------|
| Windows | ✅ Fully supported | Primary development platform |
| Linux | ✅ Works (needs display) | Tested with X11 |
| macOS | ✅ Works (needs display) | Requires macOS 10.13+ |

## Requirements

- Python 3.8+
- PySide6 ≥ 6.4.0
- turtle module (stdlib)

## Installation

```bash
# Install application
pip install -e .

# Install dev dependencies (includes Qt tools)
pip install -e ".[dev]"
```

## Usage Examples

### Example 1: Quick Visual Test
```bash
# Start the app
cd src && python qturtle.py

# In the app:
# 1. Press Ctrl+Plus 3 times (font gets bigger)
# 2. Press Ctrl+Minus 3 times (font gets smaller)
# 3. Press F5 (run the turtle code)
# 4. Verify output in console
```

### Example 2: Automated Verification
```bash
# Run test suite
python .claude/skills/qturtle-run/test_qturtle.py

# Output:
# ✓ Theme Colors verified
# ✓ Zoom bounds enforced
# ✓ Editor properties working
# ✓ File operations functional
# ✓ Console output styled correctly
```

### Example 3: Manual Checklist
```bash
# Follow QUICK_TEST.md for 2-3 minute verification
# - Check window appearance
# - Test zoom (keyboard and mouse)
# - Run sample code
# - Verify colors match Atom One Light
```

## Future Enhancements

Possible additions to this skill:
- Performance benchmarking (startup time, zoom responsiveness)
- Stress testing (large file editing, many zoom operations)
- Error scenario testing (invalid Python code, missing files)
- UI interaction recording/playback
- Screenshot comparison for theme verification

## References

- **Main app** — src/qturtle.py
- **Editor** — src/editor.py
- **Script runner** — src/runner.py
- **UI definition** — src/ui/Ui_MainWindow.py
- **Styling** — src/css/styles.css
- **Configuration** — pyrightconfig.json, setup.cfg

## Support

For issues or improvements:
1. Check SKILL.md troubleshooting section
2. Run test_qturtle.py to identify failing features
3. Review QUICK_TEST.md for expected behavior
4. Check git history for recent changes

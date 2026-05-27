# QTurtle Quick Test Guide

Quick checklist for testing QTurtle application features.

## Launch App
```bash
cd src
python qturtle.py
```

## Visual Verification (1-2 minutes)

### Window & Theme
- [ ] Window opens with title "QTurtle - Untitled"
- [ ] Light theme with white background (#FAFAFA)
- [ ] Dark text (#383A42) on light background
- [ ] Menu bar: File, Edit, Run visible
- [ ] Toolbar with buttons visible
- [ ] Status bar shows cursor position (Line 1, Col 1)

### Editor
- [ ] Code editor shows default turtle graphics code
- [ ] Syntax highlighting: purple keywords, green strings, gray comments
- [ ] Line numbers visible on left side
- [ ] Console pane below editor

### Console
- [ ] Console is empty (ready for output)
- [ ] Light background, dark text (matches editor)

## Feature Testing (2-3 minutes)

### Zoom In
```
Press: Ctrl + Plus (multiple times)
⚠️  On Windows: Ctrl + Shift + = (Plus key)
Expected: Text gets larger, line numbers adjust
Max: 32pt font size
```

### Zoom Out
```
Press: Ctrl + Minus (multiple times)
Expected: Text gets smaller
Min: 8pt font size
```

### Mouse Wheel Zoom
```
Hold: Ctrl + Scroll wheel up
Expected: Text zooms in
Hold: Ctrl + Scroll wheel down
Expected: Text zooms out
Bounds: 8-32pt (should not go beyond)
```

### Run Code
```
Press: F5 or click "Run" button
Expected:
  - Console shows "--- Running ---"
  - Text executes
  - Console shows "--- Finished (exit code 0) ---"
```

### Stop Code
```
While script running: Click "Stop"
Expected: Script terminates
```

### Save File
```
Menu: File > Save As
Expected: Save dialog opens, file saves with .py extension
Title bar shows filename instead of "Untitled"
```

### New File
```
Menu: File > New
Expected: Editor clears, title shows "Untitled"
If unsaved: Prompt to save appears
```

## Automated Tests

Run Python test suite:
```bash
python .claude/skills/qturtle-run/test_qturtle.py
```

Tests verify:
- ✓ Theme colors (#FAFAFA background, #383A42 text)
- ✓ Zoom bounds (min 8pt, max 32pt)
- ✓ Editor properties (syntax highlighter, line numbers)
- ✓ File operations (new, save, open)
- ✓ Console output styling

## Color Reference (Atom One Light)

| Element | Color | Usage |
|---------|-------|-------|
| Background | #FAFAFA | Editor, console background |
| Text | #383A42 | Editor, console, menu text |
| Keywords | #A626A4 | `if`, `for`, `def`, etc. (bold) |
| Strings | #50A14F | "text" and 'text' |
| Numbers | #986801 | 123, 3.14, etc. |
| Comments | #A0A1A7 | # comment (italic) |
| Built-ins | #0184BC | `print`, `len`, `range`, etc. |
| Accent | #4078F2 | Buttons, status bar, hover states |
| Line numbers | #9FA1A7 | Line number text |
| Line num bg | #F5F5F5 | Line number area background |

## Common Issues & Fixes

| Issue | Fix |
|-------|-----|
| Zoom keys don't work | Make sure Ctrl modifier is pressed. Try Ctrl+Shift+= for Plus |
| Colors look wrong | Restart app, check PySide6 installation |
| Turtle window doesn't appear | Check turtle module installed: `python -c "import turtle"` |
| Can't open file | Make sure .py file is selected in dialog |
| Script won't run | Check syntax in editor (errors shown in red in console) |

## Performance Notes

- Zoom is instant (no lag)
- Syntax highlighting is real-time
- Script execution is non-blocking (UI stays responsive)
- File operations are fast (even large files)

## Cleanup

Close the app normally (Ctrl+Q or close window).
Verify no temporary files left behind:
```bash
ls /tmp/qturtle_* 2>/dev/null && echo "Temp files not cleaned" || echo "Cleanup OK"
```

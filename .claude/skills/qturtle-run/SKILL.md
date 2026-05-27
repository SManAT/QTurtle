# Run QTurtle Qt Application

description: Launch and test the QTurtle PySide6 application with editor, console, and zoom features

## Overview

QTurtle is a Python IDE for turtle graphics built with PySide6 (Qt6). This skill launches the application, verifies core functionality, and tests interactive features.

## Prerequisites

Ensure dependencies are installed:
```bash
pip install -e .
pip install -e ".[dev]"
```

## Launch Application

### Start QTurtle GUI
```bash
cd src
python qturtle.py
```

The application window opens with:
- **Light theme** (Atom One Light) — clean white background with dark text
- **Code editor** — top pane with Python syntax highlighting, line numbers, dark text on light background
- **Console output** — bottom pane for script output (1:3 ratio)
- **Menus and toolbar** — File, Edit, Run operations

### Window Appearance Checklist
- [ ] Title bar shows "QTurtle - Untitled"
- [ ] Light background (#FAFAFA) throughout
- [ ] Menu bar has File, Edit, Run menus
- [ ] Toolbar with action buttons visible
- [ ] Code editor shows default turtle graphics example code
- [ ] Console pane below editor is empty (ready for output)
- [ ] Status bar at bottom shows "Line 1, Col 1" (cursor position)

## Test Core Features

### 1. Code Editor
**Syntax Highlighting:**
- Keywords appear in purple (#A626A4) and bold
- Strings appear in green (#50A14F)
- Comments appear in gray (#A0A1A7) and italic
- Numbers appear in orange (#986801)
- Built-in functions appear in teal (#0184BC)

**Action:** Type some Python code in the editor to verify colors.

### 2. Zoom Functionality

#### Ctrl+Plus Zoom In
```
Press: Ctrl + Plus (or Ctrl + Shift + =)
Expected: Font size increases by 1pt, line numbers adjust
Repeat: Multiple times until text is noticeably larger
Max: 32pt (should not increase further)
```

#### Ctrl+Minus Zoom Out
```
Press: Ctrl + Minus (or Ctrl + -)
Expected: Font size decreases by 1pt, line numbers adjust
Repeat: Multiple times until text is noticeably smaller
Min: 8pt (should not decrease further)
```

#### Ctrl+Mouse Wheel Zoom
```
Press Ctrl and scroll mouse wheel up: Font increases
Press Ctrl and scroll mouse wheel down: Font decreases
Expected: Smooth zoom with proper bounds (8-32pt)
```

**Verification:**
- [ ] Ctrl+Plus increases font size (max 32pt)
- [ ] Ctrl+Minus decreases font size (min 8pt)
- [ ] Ctrl+Scroll wheel zooms correctly
- [ ] Line number area width updates with font size
- [ ] Zoom bounds are respected (doesn't go below 8pt or above 32pt)

### 3. Script Execution

**Action:** Run the default turtle graphics code
```
1. Click "Run" button or press F5
2. Observe console output shows "--- Running ---"
3. Turtle graphics window should appear (if turtle module available)
4. When complete, console shows "--- Finished (exit code 0) ---"
```

**Expected behavior:**
- [ ] Console clears before execution
- [ ] Output appears in console pane (red text for errors)
- [ ] Script can be stopped with "Stop" button
- [ ] Buttons toggle: Run enabled/disabled appropriately

### 4. File Operations

#### New File
```
Menu: File > New or Ctrl+N
Expected: Code editor clears, title shows "Untitled"
```

#### Open File
```
Menu: File > Open
Select any .py file
Expected: File content loads in editor, title shows filename
```

#### Save File
```
Menu: File > Save or Ctrl+S
If unsaved: Select location, file saves
Expected: Title bar loses asterisk (*) indicating saved state
```

### 5. Editor Actions

#### Auto-Indentation
```
1. Type: "if True:"
2. Press Enter
Expected: Next line automatically indented 4 spaces
3. Type more code at indented level
Expected: Correct indentation maintained
```

#### Tab Handling
```
1. Press Tab
Expected: Inserts 4 spaces (not a tab character)
2. Press Shift+Tab at start of indented line
Expected: Removes 4 spaces from line start
```

#### Auto-Complete (if implemented)
- Verify language keywords trigger highlighting
- Verify built-in functions are colored correctly

### 6. Theme Verification (Atom One Light)

**Colors:**
- Background: #FAFAFA (light off-white)
- Text: #383A42 (dark gray)
- Keywords: #A626A4 (purple)
- Strings: #50A14F (green)
- Numbers: #986801 (orange)
- Comments: #A0A1A7 (gray)
- Accents: #4078F2 (blue) — buttons, status bar
- Selection: #E5E5E6 (light gray)

**Action:** Verify these colors match expectations in editor and UI

## Test Sequence

Run this complete test sequence to verify all features:

1. **Launch** → verify window and light theme
2. **Zoom** → test Ctrl+Plus, Ctrl+Minus, Ctrl+Wheel (min/max bounds)
3. **Edit** → type code, verify syntax highlighting, test Tab/Shift+Tab
4. **Run** → execute default turtle code, verify output in console
5. **Save** → File > Save As, save a test file
6. **Reopen** → File > Open, load the saved file
7. **Close** → Verify unsaved changes prompt appears if edited
8. **Exit** → Close application cleanly

## Known Behaviors

- **Zoom not persistent:** Font size resets on app restart (by design)
- **Turtle window separate:** Turtle graphics appear in native window, not Qt editor
- **Temp files:** Script execution creates temporary .py files (auto-cleaned)
- **UTF-8 encoding:** Windows scripts automatically configured with UTF-8
- **Turtle epilog:** `turtle.done()` appended to keep graphics window open

## Troubleshooting

### App won't start
- Verify PySide6 installed: `pip show pyside6`
- Check Python version: Must be 3.8+
- Try from repo root: `cd src && python qturtle.py`

### Zoom keys not working
- Verify Ctrl modifier is pressed (not just Plus/Minus)
- Try both regular keyboard and numpad versions
- Check OS keyboard layout (some layouts map +/= differently)

### Turtle graphics not appearing
- Verify turtle module installed: `python -c "import turtle; print('OK')"`
- Some systems require display setup — see runner.py epilog

### Syntax highlighting not visible
- Verify light theme loaded correctly
- Check that PySide6 has proper color support
- Restart app if colors appear incorrect

## Skill Info

**Type:** Desktop GUI (PySide6/Qt6)  
**Platform:** Windows, Linux, macOS (with display)  
**Language:** Python 3.8+  
**Framework:** PySide6 ≥6.4.0  
**Interactions:** GUI window, keyboard input, mouse wheel, file dialogs

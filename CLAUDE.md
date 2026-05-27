# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**QTurtle** is a Python IDE for running turtle graphics scripts, built with PySide6 (Qt6). The application provides a code editor with Python syntax highlighting, line numbers, and a console for script output.

## Quick Start Commands

### Installation
```bash
pip install -e .
pip install -e ".[dev]"
```

### Running the Application
```bash
python src/qturtle.py
```

### Building an Executable
```bash
python auto_build.py
```
The build script detects your Python environment, verifies virtual environment usage, and bundles the app with PyInstaller. It outputs to `dist/`.

### Type Checking
Pyright is configured in `pyrightconfig.json`. Check types:
```bash
pyright src
```

### Code Quality
Linting rules are in `setup.cfg` (flake8, pylint, pycodestyle). The project excludes generated UI files and uses relaxed linting rules for UI maintenance.

## Architecture

### Core Components

**qturtle.py** - Main application window
- `MainWindow` class inherits from QMainWindow and orchestrates the entire application
- Manages file operations (New, Open, Save, Save As)
- Handles script execution via ScriptRunner
- Loads stylesheets from `src/css/`
- Displays modification status and cursor position in title bar and status bar
- Emits `modified` signal to update UI when code changes

**editor.py** - Custom code editor with enhancements
- `CodeEditor` extends QPlainTextEdit with Python syntax highlighting, line numbers, and auto-indentation
- `PythonHighlighter` provides syntax highlighting for keywords, builtins, strings, numbers, and comments using QSyntaxHighlighter
- `LineNumberArea` custom widget displays line numbers on the left margin
- Tab key inserts 4 spaces; Shift+Tab removes 4 spaces; F5 runs the script
- Auto-indentation adds extra indent after colons (for Python blocks)
- Dark theme palette with Consolas font at 12pt

**runner.py** - Subprocess script execution
- `ScriptRunner` executes Python code in a separate QProcess to keep the UI responsive
- Injects UTF-8 encoding setup at the start of scripts for Windows compatibility
- Appends turtle epilog (`turtle.done()`) to keep graphics windows open after script completion
- Emits signals: `output_received`, `error_received`, `finished_with_code`
- Cleans up temporary Python files after execution

**Ui_MainWindow.py** - Generated UI (DO NOT EDIT)
- Auto-generated from `Ui_MainWindow.ui` via Qt Designer
- Defines menu actions (File, Edit, Run), toolbar, and main widget layout
- Main widget uses a vertical splitter: CodeEditor (3:1 ratio) over console output (1:1 ratio)

### UI Layout

The main window uses a vertical splitter:
- **Top pane**: CodeEditor (Python code input)
- **Bottom pane**: Console output (read-only QPlainTextEdit with dark theme)
- Splitter ratio: 3:1 (code editor gets 3x more space than console)

## File Structure

```
src/
├── qturtle.py              # Main application window
├── editor.py               # Code editor with syntax highlighting
├── runner.py               # Subprocess runner for script execution
├── ui/
│   ├── Ui_MainWindow.py    # Generated UI (from Designer, do not edit)
│   └── Ui_MainWindow.ui    # Qt Designer UI file
├── css/
│   └── styles.css          # Application stylesheet
└── pyside6_template.egg-info/  # Package metadata

Root files:
├── auto_build.py           # PyInstaller build script
├── setup.cfg               # Linting and style configuration
├── pyrightconfig.json      # Pyright type checker config
└── pyproject.toml          # Package definition
```

## Modifying the UI

To modify the UI (window layout, menus, buttons):

1. Open `src/ui/Ui_MainWindow.ui` in Qt Designer
2. Make your changes and save
3. Regenerate the Python code: use the included `uicAll.bat` script or:
   ```bash
   pyside6-uic src/ui/Ui_MainWindow.ui -o src/ui/Ui_MainWindow.py
   ```
4. **DO NOT manually edit** `Ui_MainWindow.py` — it gets regenerated

## Dependencies

- **pyside6** ≥6.4.0 — Qt6 bindings for Python
- **pyqt6-tools** (dev) — Includes pyside6-uic for UI compilation
- **build, wheel** (dev) — Package building tools
- **pyinstaller** (build) — Creates executables

## Design Notes

- **Syntax highlighting** is implemented manually using QRegularExpression patterns, not using the standard Qt syntax highlighter templates, to maintain consistency with VS Code colors
- **Script execution** runs in a separate process to prevent blocking the UI during long operations
- **UTF-8 encoding** is explicitly configured at runtime for Windows compatibility (Python defaults to system encoding)
- **Turtle epilog** (`turtle.done()`) is appended to turtle scripts to keep graphics windows open, allowing users to interact with drawn graphics
- **Temporary files** are created via `tempfile.mkstemp()` for each script run and cleaned up after execution

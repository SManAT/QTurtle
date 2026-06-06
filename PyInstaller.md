# Deploying Python Programs

## Quick Comparison

| Tool | Binary Size | Build Time | Installer | Config |
|------|-------------|------------|-----------|--------|
| **PyInstaller** (+ UPX) | 120 MB (80 MB) | Fast | No | `pyproject.toml` |
| **Briefcase** | 220 MB | Medium | MSI/DMG/DEB | `pyproject.toml` |
| **Nuitka** | ~100-150MB | Slow (first) | No | `build_nuitka.bat` |
| **cx_Freeze** | 92 MB | Fast | No | `setup_cxfreeze.py` |

The binary sizes are tested with a Pyside6 minimal App. 

**When to use which:**

- **Quick testing / dev builds** → PyInstaller
- **Professional distribution** → Briefcase (MSI installer, app icon)
- **Smallest binary / native performance** → Nuitka
- **Alternative to PyInstaller** → cx_Freeze

---

## PyInstaller

Well-established, easy to set up. Configuration lives in `pyproject.toml`.

### Installation
```bash
pip install pyinstaller
pip install tomli  # Python 3.10 and earlier only
```

### Build
```bash
build_pyinstaller.bat
# or
python auto_build.py
```

Output: `dist\QTurtle\qturtle.exe`

### Configuration (`pyproject.toml`)
```toml
[tool.qturtle.build]
app_name = "QTurtle"
app_module = "src/qturtle.py"
icon = "assets/app.ico"
data_files = ["src/css", "src/ui"]
output_dir = "dist"
build_mode = "onedir"
windowed = true
hidden_imports = ["turtle", "PySide6.QtCore", "PySide6.QtGui", "PySide6.QtWidgets"]
collect_all = ["PySide6"]
```

### Known Issue: `ModuleNotFoundError: No module named 'editor'`

When running the built `.exe`:
```
from editor import CodeEditor
ModuleNotFoundError: No module named 'editor'
```

**Cause:** `pyside6-uic` generates a bare `from editor import CodeEditor`. Works from source but not inside the bundle.

**Fix:** In `src/qturtle/ui/Ui_MainWindow.py`, change line 23 to:
```python
from qturtle.editor import CodeEditor
```

**Permanent fix:** In Qt Designer → Edit → Promote Widgets → set CodeEditor's Header file to `qturtle.editor`. Future regenerations will produce the correct import.

---

## Briefcase

BeeWare tool for native desktop apps. Generates MSI installers and includes app icon.

### Installation
```bash
pip install briefcase
```

### Build
```bash
build_briefcase.bat
# or
briefcase create windows && briefcase build windows && briefcase package windows
```

Output: `build\qturtle\windows\app\src\QTurtle.exe`  
Installer: `dist\QTurtle-*.msi`

Copy output to `dist\QTurtle\` (same location as PyInstaller):
```bash
build_briefcase_to_dist.bat
```

### Configuration (`pyproject.toml`)
```toml
[tool.briefcase.app.qturtle]
formal_name = "QTurtle"
bundle = "org.qturtle"
version = "0.1.0"
sources = ["src/qturtle"]
requires = ["pyside6>=6.4.0"]

[tool.briefcase.app.qturtle.windows]
requires = ["pyside6>=6.4.0", "windows-curses; platform_system == 'Windows'"]
```

---

## Nuitka

Compiles Python to C, then to native machine code. Produces a smaller, faster binary but the first build takes significantly longer (downloads a C compiler).

### Installation
```bash
pip install nuitka
```

### Build
```bash
build_nuitka.bat
```

Output: `dist\QTurtleNuitka\QTurtle.exe`

### Notes
- First run downloads the MinGW C compiler — may take several minutes
- Subsequent builds are faster
- Uses `--standalone` + `--enable-plugin=pyside6` for full PySide6 support
- Excludes unused heavy packages (numpy, matplotlib, tkinter, etc.)

---

## cx_Freeze

Straightforward Python packager. Configuration lives in `setup_cxfreeze.py`.

### Installation
```bash
pip install cx-freeze
```

### Build
```bash
build_cxfreeze.bat
# or
python setup_cxfreeze.py build_exe
```

Output: `dist\QTurtleCxFreeze\QTurtle.exe`

### Configuration (`setup_cxfreeze.py`)
Key options:
```python
build_exe_options = {
    "packages": ["PySide6.QtCore", "PySide6.QtGui", "PySide6.QtWidgets", "qturtle", ...],
    "include_files": [("src/qturtle/css", "lib/qturtle/css"), ...],
    "excludes": ["PyQt6", "matplotlib", "numpy", "tkinter", ...],
    "optimize": 2,
}
```


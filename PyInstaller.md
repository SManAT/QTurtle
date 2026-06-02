# PyInstaller & Briefcase Build Guide

This guide explains how to use **PyInstaller** and **Briefcase** for packaging QTurtle into executable files.

## Quick Comparison

| Feature | PyInstaller | Briefcase |
|---------|-------------|-----------|
| **Startup Speed** | 🟡 Normal (~1-2s) | 🟡 Normal (~1-2s) |
| **Binary Size** | 📦 Medium (~150-200MB) | 📦 Medium (~200-250MB) |
| **Setup Complexity** | 🟢 Easy | 🟢 Easy |
| **Multi-platform** | ✅ Windows/Mac/Linux | ✅ Windows/Mac/Linux/iOS/Android |
| **Qt/PySide6 Support** | ✅ Good | ✅ Excellent |
| **Learning Curve** | 🟢 Gentle | 🟢 Gentle |
| **Config from TOML** | ✅ Yes | ✅ Yes |
| **Installer Support** | ❌ Manual setup | ✅ MSI/DMG/DEB |
| **Best For** | Quick development, testing | Professional releases, distribution |

---

## PyInstaller

**PyInstaller** is the current go-to tool for packaging Python applications. It's well-established, widely used, and easy to set up. QTurtle now reads all build configuration from `pyproject.toml`.

### Installation

```bash
# Install PyInstaller
pip install pyinstaller

# Install tomli for Python 3.10 and earlier (for TOML support)
pip install tomli
```

### Configuration (pyproject.toml)

All build settings are defined in `[tool.qturtle.build]`:

```toml
[tool.qturtle.build]
app_name = "QTurtle"
app_module = "src/qturtle.py"
icon = "assets/app.ico"
data_files = ["src/css", "src/ui"]
output_dir = "dist"
build_mode = "onedir"          # or "onefile"
clean = true
noconfirm = true
windowed = true
hidden_imports = [
    "turtle",
    "PySide6.QtCore",
    "PySide6.QtGui",
    "PySide6.QtWidgets",
]
collect_all = ["PySide6"]
```

### Building

```bash
# Use the batch file
build.bat

# Or run directly
python auto_build.py
```

### Output
- Executable: `dist/QTurtle/qturtle.exe` (Windows)
- Size: ~150-200MB
- Startup: Normal (~1-2 seconds)

### Pros
✅ Easiest to set up and use  
✅ Excellent documentation  
✅ Reads configuration from `pyproject.toml`  
✅ Works with all Python libraries  
✅ Fast build times  
✅ Most reliable for PySide6  

### Cons
❌ Larger binary size compared to alternatives  
❌ Can have issues with some complex packages  
❌ Not optimized for performance  

---

## Briefcase

**Briefcase** is a BeeWare project tool designed specifically for creating native desktop and mobile applications from Python. Excellent for GUI apps with Qt/PySide6.

### Installation

```bash
# Install Briefcase
pip install briefcase

# Verify installation
briefcase --version
```

### Setup for QTurtle

1. **Create Briefcase project** (interactive):
   ```bash
   briefcase create
   ```
   Answer the prompts:
   - Project name: `QTurtle`
   - App name: `qturtle`
   - Bundle identifier: `org.qturtle.app`
   - Author: `Stefan Hag`
   - License: `MIT`

2. **Project structure created**:
   ```
   src/
   ├── qturtle/
   │   ├── __main__.py          # Entry point
   │   ├── app.py               # Main application
   │   └── resources/
   │       ├── css/
   │       └── ui/
   ```

3. **Move your code** into the generated structure or update paths in configuration.

4. **Configure `pyproject.toml`**:
   ```toml
   [tool.briefcase.app.qturtle]
   formal_name = "QTurtle"
   bundle = "org.qturtle"
   version = "0.1.0"
   description = "Python IDE for turtle graphics"
   sources = ["src/qturtle"]
   requires = ["pyside6>=6.4.0"]
   
   [tool.briefcase.app.qturtle.windows]
   requires = ["pyside6>=6.4.0", "windows-curses; platform_system == 'Windows'"]
   ```

5. **Build**:
   ```bash
   # Create native project structure
   briefcase create windows
   
   # Build the executable
   briefcase build windows
   
   # Package for distribution
   briefcase package windows
   ```

### Output
- Executable: `build/qturtle/windows/app/QTurtle.exe`
- Size: ~200-250MB (includes Python + PySide6)
- Format: Installer (`.msi`) or directory

### Pros
✅ Designed for GUI applications  
✅ Excellent PySide6 integration  
✅ Multi-platform support (macOS, Linux, Windows, iOS, Android)  
✅ Simple configuration  
✅ Handles code signing and distribution  
✅ Active community and documentation  

### Cons
❌ Larger binary size  
❌ Slightly longer build times  
❌ More opinionated project structure  

---

## Usage Examples

### Building with PyInstaller

```bash
# Using batch file (recommended)
build_pyinstaller.bat

# Or directly
python auto_build.py

# Run the executable
dist\QTurtle\qturtle.exe

# To modify build settings, edit pyproject.toml [tool.qturtle.build]
```

### Building with Briefcase

```bash
# Using batch file
build_briefcase.bat

# Or directly
briefcase create windows
briefcase build windows
briefcase package windows

# Run the executable
build\qturtle\windows\app\src\QTurtle.exe

# Create MSI installer
briefcase package windows
```

---

## When to Use Which?

### Quick Decision Guide

**For development & quick testing?** → **PyInstaller**
- Fastest to set up and get a working executable
- Configuration already in `pyproject.toml`
- Run `build_pyinstaller.bat` and you're done
- Perfect for iterating and testing

**For professional distribution?** → **Briefcase**
- Generates MSI installers for Windows
- Excellent PySide6 integration
- Modern, actively maintained
- Better for releases and multi-platform support
- Includes app icon in executable

---

### Detailed Comparison

**Use PyInstaller if:**
- ✅ You want zero setup complexity (it's already configured)
- ✅ You need to build quickly for testing
- ✅ You're developing and iterating rapidly
- ✅ You want maximum library compatibility
- ✅ Fastest build times matter

**Use Briefcase if:**
- ✅ You need professional MSI installers
- ✅ You want excellent PySide6 integration
- ✅ You may distribute to end users
- ✅ You want long-term maintainability
- ✅ App icon and branding are important

---

## Resources

- **PyInstaller**: https://pyinstaller.org/
- **Briefcase**: https://briefcase.readthedocs.io/
- **BeeWare**: https://beeware.org/

# Installer.md - PyInstaller, PyOxidizer & Briefcase

This guide explains how to use **PyInstaller**, **PyOxidizer**, and **Briefcase** for packaging QTurtle into executable files.

## Quick Comparison

| Feature | PyInstaller | PyOxidizer | Briefcase |
|---------|-------------|-----------|-----------|
| **Speed** | 🟡 Normal startup | ⚡ Very fast startup | ⚡ Normal startup |
| **Binary Size** | 📦 Medium (~150-200MB) | 🔻 Smaller (~50-80MB) | 📦 Large (~200-250MB) |
| **Setup Complexity** | 🟢 Easy | 🟡 Medium | 🟢 Easy |
| **Multi-platform** | ✅ Windows/Mac/Linux | ✅ Windows/Mac/Linux | ✅ Windows/Mac/Linux/iOS/Android |
| **Qt/PySide6 Support** | ✅ Good | ✅ Good | ✅ Excellent |
| **Learning Curve** | 🟢 Gentle | 🟡 Steep | 🟢 Gentle |
| **Config from TOML** | ✅ Yes | ⚠️ Uses .bzl | ✅ Yes |
| **Best For** | Quick testing, simple builds | Performance, small binaries | Cross-platform, simplicity |

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
❌ Larger binary size  
❌ Slower startup than PyOxidizer  
❌ Can have issues with some complex packages  
❌ Not optimized for performance  

---

---

## PyOxidizer

**PyOxidizer** is a modern Rust-based tool that creates self-contained Python applications with faster startup times and smaller file sizes.

### Installation

```bash
# Install PyOxidizer
pip install pyoxidizer

# Or via Rust (recommended for development)
cargo install pyoxidizer
```

### Setup for QTurtle

1. **Initialize PyOxidizer project**:
   ```bash
   pyoxidizer init-rust-project QTurtle
   ```
   This creates a Rust project with a `pyoxidizer.bzl` configuration file.

2. **Configure `pyoxidizer.bzl`**:
   ```python
   def make_exe():
       return PythonExecutable(
           config=PythonConfig(
               version="3.11",
               optimization_level=2,
           ),
           entry_point=FileManifest(
               relative_path="qturtle",
               filesystem_relative_path="src/qturtle.py",
           ),
           include_resources=True,
           include_test=False,
       )

   def make_embedded_resources(exe):
       return FileManifest(
           relative_path="",
           filesystem_relative_path="src/css",
       )
   ```

3. **Build**:
   ```bash
   pyoxidizer build
   ```

### Output
- Executable: `target/release/qturtle.exe` (Windows) or `target/release/qturtle` (Unix)
- Size: ~60-80MB (includes full Python runtime)
- Startup: Very fast

### Pros
✅ Smallest binary size among alternatives  
✅ Fastest startup time  
✅ True native code execution  
✅ Production-grade reliability  

### Cons
❌ Requires Rust toolchain (adds build complexity)  
❌ Steeper learning curve  
❌ Less mature PySide6 integration compared to others  
❌ Longer initial setup time  

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
❌ Limited customization vs PyOxidizer  

---

## Usage Examples

### Building with PyInstaller

```bash
# Using batch file (recommended)
build.bat

# Or directly
python auto_build.py

# Run the executable
dist\QTurtle\qturtle.exe

# To modify build settings, edit pyproject.toml [tool.qturtle.build]
```

### Building with PyOxidizer

```bash
# Using batch file
build_pyoxidizer.bat

# Or directly
pyoxidizer build

# Run the executable
target\release\qturtle.exe
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
build\qturtle\windows\app\QTurtle.exe
```

---

## When to Use Which?

### Quick Decision Guide

**For immediate testing/development?** → **PyInstaller**
- Fastest to set up and get a working executable
- Configuration already in `pyproject.toml`
- Just run `build.bat`

**For performance-critical applications?** → **PyOxidizer**
- Smallest binary size (~50-80MB vs 150-200MB)
- Fastest startup times
- True native code execution
- Worth the setup investment if distribution size matters

**For cross-platform distribution?** → **Briefcase**
- Support for macOS, Linux, and even iOS/Android
- Excellent PySide6 integration
- Modern, actively maintained
- Best if you need professional multi-platform support

---

### Detailed Comparison

**Use PyInstaller if:**
- ✅ You want zero setup complexity (it's already configured)
- ✅ You need to build quickly and iterate
- ✅ You're happy with ~150-200MB binary size
- ✅ You need maximum library compatibility
- ✅ You want the fastest build times

**Use PyOxidizer if:**
- ✅ You want the smallest possible binary (~50-80MB)
- ✅ Performance and startup speed are critical
- ✅ You're comfortable with Rust toolchain setup
- ✅ Distribution size/bandwidth is a concern
- ✅ Targeting a single platform (Windows/Mac/Linux)

**Use Briefcase if:**
- ✅ You may distribute for multiple platforms (macOS, Linux, iOS, Android)
- ✅ You want a professional, structured approach
- ✅ You prefer clean, modern tooling
- ✅ You want excellent PySide6 integration out-of-the-box
- ✅ You need long-term maintainability

---

## Migration Path

If you want to try one of these alternatives:

1. **PyOxidizer**: Start with a test build, then migrate if satisfied
2. **Briefcase**: Generate a new project, copy your `src/` files into the structure, adjust imports
3. Keep `PyInstaller` as fallback while testing

---

## Resources

- **PyOxidizer**: https://pyoxidizer.readthedocs.io/
- **Briefcase**: https://briefcase.readthedocs.io/
- **BeeWare**: https://beeware.org/

#!/usr/bin/env python3
"""cx_Freeze build configuration for QTurtle"""

import atexit
import sys
from pathlib import Path
from cx_Freeze import setup, Executable

# Put the subprocess python.exe in runtime/ so its ._pth file does not land
# in the build root alongside QTurtle.exe.  If a python3XX._pth file sits
# next to QTurtle.exe, cx_Freeze's own __startup__ bootstrap can't be found
# (Python's prefix-search is replaced by the ._pth paths before cx_Freeze
# gets a chance to set things up).  Keeping it in runtime/ means only the
# subprocess interpreter is affected.
ver = f"{sys.version_info.major}{sys.version_info.minor}"
_pth_name = f"python{ver}._pth"
_pth_path = Path(_pth_name)
# cx_Freeze packs pure-Python stdlib modules (turtle, tkinter, …) into
# lib/library.zip by default.  Both paths are needed: the directory for
# extension modules (.pyd) and the zip for pure-Python modules.
_pth_path.write_text("../lib\n../lib/library.zip\nimport site\n", encoding="utf-8")


@atexit.register
def _cleanup_pth():
    try:
        _pth_path.unlink(missing_ok=True)
    except Exception:
        pass


# Tcl/Tk version numbers — needed for both DLL names and data-file paths.
import _tkinter

_tcl_ver = _tkinter.TCL_VERSION  # e.g. "8.6" or "9.0"
_tk_ver = _tkinter.TK_VERSION

# python.exe needs its own DLLs in its directory to start.
# Python 3.8+ ignores PATH when loading C-extension dependencies — it only
# searches the app directory (runtime/) and the .pyd's own directory (lib/).
# Tcl/Tk DLLs must therefore be in runtime/ so that _tkinter.pyd can load them.
_python_dir = Path(sys.executable).parent
_runtime_includes: list = [
    (sys.executable, "runtime/python.exe"),
    (str(_pth_path), f"runtime/{_pth_name}"),
]
for _dll_name in (
    f"python{ver}.dll",
    f"tcl{_tcl_ver.replace('.', '')}.dll",
    f"tk{_tk_ver.replace('.', '')}.dll",
):
    _dll = _python_dir / _dll_name
    if _dll.exists():
        _runtime_includes.append((str(_dll), f"runtime/{_dll_name}"))

# Explicitly copy Tcl/Tk library data files (init.tcl, tk.tcl, etc.) to
# tcl/ in the build output.  cx_Freeze copies the DLLs but often omits the
# data files, so the subprocess python.exe can't initialize Tcl without them.
def _find_tcltk_src():
    for base in (Path(sys.prefix), Path(getattr(sys, "base_prefix", sys.prefix))):
        tcl = base / "tcl" / f"tcl{_tcl_ver}"
        if tcl.exists():
            return tcl, base / "tcl" / f"tk{_tk_ver}"
    return None, None

_tcl_src, _tk_src = _find_tcltk_src()
_tcltk_includes: list = []
if _tcl_src and _tcl_src.exists():
    _tcltk_includes.append((str(_tcl_src), f"tcl/tcl{_tcl_ver}"))
if _tk_src and _tk_src.exists():
    _tcltk_includes.append((str(_tk_src), f"tcl/tk{_tk_ver}"))

build_exe_options = {
    "packages": [
        "PySide6.QtCore",
        "PySide6.QtGui",
        "PySide6.QtWidgets",
        "PySide6.QtPrintSupport",
        "tkinter",
        "turtle",
        "qturtle_app",
        "qturtle_app.editor",
        "qturtle_app.runner",
        "qturtle_app.svg_turtle_class",
        "qturtle_app.ui",
        "qturtle_app.ui.Ui_MainWindow",
    ],
    "include_files": [
        ("src/qturtle_app/css", "lib/qturtle_app/css"),
        ("src/qturtle_app/ui/Ui_MainWindow.ui", "lib/qturtle_app/ui/Ui_MainWindow.ui"),
        *_runtime_includes,
        *_tcltk_includes,
    ],
    "excludes": [
        "PyQt6",
        "matplotlib",
        "scipy",
        "numpy",
        "pandas",
        "PIL",
        "wx",
        "IPython",
        "jupyter",
        "notebook",
        "test",
        "unittest",
        "doctest",
        "pydoc",
        "xmlrpc",
        "ftplib",
        "poplib",
        "imaplib",
        "smtplib",
        "tzdata",
        "zoneinfo",
    ],
    "optimize": 2,
    "include_msvcr": True,
    "build_exe": "build/cxfreeze_temp",
}

icon_path = "src/assets/app.ico"

executables = [
    Executable(
        script="src/main.py",
        base="gui" if sys.platform == "win32" else None,
        target_name="QTurtle.exe" if sys.platform == "win32" else "QTurtle",
        icon=icon_path if (sys.platform == "win32" and Path(icon_path).exists()) else None,
    )
]

setup(
    name="QTurtle",
    version="1.0.0",
    description="Python IDE for turtle graphics scripts",
    options={"build_exe": build_exe_options},
    executables=executables,
)

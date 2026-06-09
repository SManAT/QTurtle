#!/usr/bin/env python3
"""cx_Freeze build configuration for QTurtle"""

import sys
from pathlib import Path
from cx_Freeze import setup, Executable

# ._pth file next to the bundled python.exe:
#   lib           → cx_Freeze package directory (turtle, tkinter, qturtle_app, …)
#   import site   → re-enables PYTHONPATH processing (._pth disables it by default)
_ver = f"{sys.version_info.major}{sys.version_info.minor}"
_pth_name = f"python{_ver}._pth"
_pth_path = Path(_pth_name)
_pth_path.write_text("lib\nimport site\n", encoding="utf-8")

build_exe_options = {
    "packages": [
        "PySide6.QtCore",
        "PySide6.QtGui",
        "PySide6.QtWidgets",
        "PySide6.QtPrintSupport",
        "tkinter",
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
        # Bundle python.exe so runner.py can launch scripts as subprocesses
        (sys.executable, "python.exe"),
        (str(_pth_path), _pth_name),
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

try:
    setup(
        name="QTurtle",
        version="1.0.0",
        description="Python IDE for turtle graphics scripts",
        options={"build_exe": build_exe_options},
        executables=executables,
    )
finally:
    _pth_path.unlink(missing_ok=True)

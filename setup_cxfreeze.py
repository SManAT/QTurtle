#!/usr/bin/env python3
"""cx_Freeze build configuration for QTurtle"""

import sys
from pathlib import Path
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": [
        "PySide6.QtCore",
        "PySide6.QtGui",
        "PySide6.QtWidgets",
        "PySide6.QtPrintSupport",
        "qturtle",
        "qturtle.editor",
        "qturtle.runner",
        "qturtle.svg_turtle_class",
        "qturtle.ui",
        "qturtle.ui.Ui_MainWindow",
    ],
    "include_files": [
        ("src/qturtle/css", "lib/qturtle/css"),
        ("src/qturtle/ui/Ui_MainWindow.ui", "lib/qturtle/ui/Ui_MainWindow.ui"),
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
        "tkinter",
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

icon_path = "assets/app.ico"

executables = [
    Executable(
        script="src/qturtle/__main__.py",
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

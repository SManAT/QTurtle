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

setup(
    name="QTurtle",
    version="1.0.0",
    description="Python IDE for turtle graphics scripts",
    options={"build_exe": build_exe_options},
    executables=executables,
)

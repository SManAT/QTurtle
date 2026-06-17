#!/usr/bin/env python3
"""cx_Freeze build configuration for QTurtle"""

import atexit
import shutil
import sys
from pathlib import Path
from cx_Freeze import setup, Executable
from cx_Freeze.command.build_exe import build_exe as _build_exe

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


# python.exe needs its own python3XX.dll next to it to start.
_python_dir = Path(sys.executable).parent
_runtime_includes: list = [
    (sys.executable, "runtime/python.exe"),
    (str(_pth_path), f"runtime/{_pth_name}"),
]
_python_dll = _python_dir / f"python{ver}.dll"
if _python_dll.exists():
    _runtime_includes.append((str(_python_dll), f"runtime/python{ver}.dll"))


# --- PySide6 slimming configuration -------------------------------------
# QTurtle only imports QtWidgets / QtGui / QtCore / QtPrintSupport.  cx_Freeze's
# PySide6 hook copies the *entire* PySide6 tree (every Qt module, all plugins
# and ~30 UI translations), so we prune the unused parts after the build.

# Keep only these UI languages; every other Qt .qm translation is dropped.
KEEP_TRANSLATIONS = ("de", "en")

# Qt6 feature DLLs the app never loads (QML engine, PDF viewer, OpenGL,
# networking, virtual keyboard, SVG rendering).
PRUNE_QT_DLLS = (
    "Qt6Quick", "Qt6Qml", "Qt6QmlModels", "Qt6QmlMeta", "Qt6QmlWorkerScript",
    "Qt6Pdf", "Qt6PdfQuick", "Qt6PdfWidgets",
    "Qt6OpenGL", "Qt6Network", "Qt6VirtualKeyboard", "Qt6Svg",
)

# Python binding modules (.pyd) that are never imported.
PRUNE_QT_PYDS = ("QtNetwork",)

# Whole plugin folders that are unused (no networking, QML, touch or IME).
PRUNE_PLUGIN_DIRS = (
    "tls", "networkinformation", "platforminputcontexts",
    "iconengines", "generic",
)

# Inside these kept plugin folders, only the listed files survive.
KEEP_PLUGINS = {
    "platforms": ("qwindows.dll",),                       # the only Windows QPA backend we need
    "imageformats": ("qico.dll", "qjpeg.dll", "qgif.dll"),  # app icon + common pixmaps
}


class BuildExe(_build_exe):
    """Custom build_exe that mirrors the Tcl/Tk data into runtime/ and prunes
    the unused PySide6 payload.

    cx_Freeze places the (version-matched) Tcl/Tk data files under
    <build>/share/tcl8.6 and share/tk8.6 for the main executable.  Our
    subprocess interpreter lives in runtime/python.exe, and Tcl's default
    search looks for init.tcl at runtime/share/tcl8.6 (relative to the exe)
    — TCL_LIBRARY is not honoured by this Tcl build.  Copying share/ into
    runtime/share/ puts the data exactly where Tcl looks, so tkinter/turtle
    work with no environment variables.
    """

    def run(self):
        super().run()
        out = Path(self.build_exe)
        src = out / "share"
        dst = out / "runtime" / "share"
        if src.is_dir():
            if dst.exists():
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
            print(f"  Copied Tcl/Tk data -> {dst}")
        else:
            print(f"  WARNING: {src} not found; tkinter/turtle may not work in subprocesses")

        self._slim_pyside6(out / "lib" / "PySide6")

    @staticmethod
    def _slim_pyside6(root: Path) -> None:
        """Delete the Qt modules, plugins and translations QTurtle never uses."""
        if not root.is_dir():
            print(f"  WARNING: {root} not found; skipping PySide6 slimming")
            return

        freed = 0

        def remove(path: Path) -> None:
            nonlocal freed
            if path.is_file():
                freed += path.stat().st_size
                path.unlink()
            elif path.is_dir():
                freed += sum(f.stat().st_size for f in path.rglob("*") if f.is_file())
                shutil.rmtree(path)

        # Drop translations for unwanted languages (e.g. qtbase_zh_CN.qm -> "zh").
        translations = root / "translations"
        if translations.is_dir():
            for qm in translations.glob("*.qm"):
                _, _, lang = qm.stem.partition("_")
                if lang.split("_", 1)[0] not in KEEP_TRANSLATIONS:
                    remove(qm)

        for name in PRUNE_QT_DLLS:
            remove(root / f"{name}.dll")
        for name in PRUNE_QT_PYDS:
            remove(root / f"{name}.pyd")

        for sub in PRUNE_PLUGIN_DIRS:
            remove(root / "plugins" / sub)

        for sub, keep in KEEP_PLUGINS.items():
            plugin_dir = root / "plugins" / sub
            if plugin_dir.is_dir():
                for entry in plugin_dir.iterdir():
                    if entry.name not in keep:
                        remove(entry)

        print(f"  Slimmed PySide6: freed {freed / 1024 / 1024:.1f} MB")


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
        # Window/taskbar icon: the app looks for it at <package>.parent/assets,
        # which is lib/assets in the frozen build (qturtle_app lives in lib/).
        ("src/assets", "lib/assets"),
        *_runtime_includes,
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
    cmdclass={"build_exe": BuildExe},
)

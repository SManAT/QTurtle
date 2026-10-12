import os
import shutil
import sys
import tempfile
from pathlib import Path
from PySide6.QtCore import QObject, QProcess, QProcessEnvironment, Signal


class ScriptRunner(QObject):
    output_received: Signal = Signal(str)
    error_received = Signal(str)
    finished_with_code = Signal(int)

    # Tracking code for turtle movements and timing
    TURTLE_TRACKING = """
import time as _qturtle_time
_qturtle_start = _qturtle_time.time()
_qturtle_forward_count = 0
_qturtle_backward_count = 0

def _qturtle_track_forward(self, distance):
    global _qturtle_forward_count
    _qturtle_forward_count += 1
    return _qturtle_original_forward(self, distance)

def _qturtle_track_backward(self, distance):
    global _qturtle_backward_count
    _qturtle_backward_count += 1
    return _qturtle_original_backward(self, distance)
"""

    # Epilog to keep turtle window open after script finishes
    TURTLE_EPILOG = """
import sys as _qturtle_sys
if 'turtle' in _qturtle_sys.modules:
    import turtle as _qturtle_t
    _qturtle_elapsed = _qturtle_time.time() - _qturtle_start
    _qturtle_total_lines = _qturtle_forward_count + _qturtle_backward_count
    print(f"--- Gezeichnet in {_qturtle_elapsed:.2f}s (Linien: {_qturtle_total_lines}) ---")
    try:
        _qturtle_t.done()
    except Exception:
        pass
"""

    # UTF-8 encoding setup for Windows compatibility
    UTF8_PREFIX = "import sys; sys.stdout.reconfigure(encoding='utf-8'); sys.stderr.reconfigure(encoding='utf-8')\n"

    # Excepthook that explains unknown commands/names in German and suggests
    # similar ones ("Meintest du ...?"). __QTURTLE_OFFSET__ is replaced with the
    # number of injected lines so the reported line matches the editor.
    ERROR_HINTS = r'''
import sys as _qturtle_sys

def _qturtle_excepthook(exc_type, exc, tb, _orig=_qturtle_sys.excepthook):
    if exc_type not in (AttributeError, NameError) or tb is None:
        return _orig(exc_type, exc, tb)
    try:
        import builtins, difflib, re, textwrap, types

        last = tb
        while last.tb_next is not None:
            last = last.tb_next
        # Only explain errors raised directly in the student's code
        if last.tb_frame.f_code.co_filename != __file__:
            return _orig(exc_type, exc, tb)

        name = getattr(exc, "name", None)
        if not name:
            match = re.search(r"(?:attribute|name) '(\w+)'", str(exc))
            name = match.group(1) if match else None
        if not name:
            return _orig(exc_type, exc, tb)

        line = last.tb_lineno - __QTURTLE_OFFSET__
        out = [f"Fehler in Zeile {line}: {exc_type.__name__}: {exc}"]

        if exc_type is AttributeError:
            obj = getattr(exc, "obj", None)
            if obj is None:
                out.append(f"Hinweis: Den Befehl '{name}' gibt es nicht.")
                print("\n".join(out), file=_qturtle_sys.stderr)
                return
            owner = obj.__name__ if isinstance(obj, types.ModuleType) else type(obj).__name__
            candidates = {n: callable(getattr(obj, n, None)) for n in dir(obj) if not n.startswith("_")}
            what = f"{owner} kennt den Befehl '{name}' nicht."
        else:
            frame = last.tb_frame
            names = set(frame.f_locals) | set(frame.f_globals) | set(dir(builtins))
            names = {n for n in names if not n.startswith("_")}
            candidates = {n: callable(frame.f_locals.get(n, frame.f_globals.get(n, getattr(builtins, n, None)))) for n in names}
            what = f"'{name}' ist nicht definiert."

        def label(n):
            return f"{n}()" if candidates[n] else n

        # Case-insensitive match first (e.g. "Forward" -> "forward"), then fuzzy
        lower = {n.lower(): n for n in candidates}
        similar = [lower[name.lower()]] if name.lower() in lower else []
        similar += [lower[n] for n in difflib.get_close_matches(name.lower(), lower, n=3, cutoff=0.6) if lower[n] not in similar]

        if similar:
            out.append(f"Hinweis: {what} Meintest du {' oder '.join(label(n) for n in similar[:3])}?")
        elif exc_type is AttributeError:
            commands = sorted(n for n in candidates if candidates[n])
            out.append(f"Hinweis: {what} Mögliche Befehle:")
            out.append(textwrap.fill(", ".join(f"{n}()" for n in commands), width=90, initial_indent="  ", subsequent_indent="  "))
        else:
            out.append(f"Hinweis: {what} Tippfehler, fehlender import oder Variable noch nicht zugewiesen?")
        print("\n".join(out), file=_qturtle_sys.stderr)
    except Exception:
        _orig(exc_type, exc, tb)

_qturtle_sys.excepthook = _qturtle_excepthook
'''

    # Loads every *.py file from the addons folder and copies its public
    # functions/classes/constants into the script's global namespace, so
    # students can call them directly without an import.
    # __QTURTLE_ADDONS_DIR__ is replaced with the folder found by _addons_dir().
    ADDON_LOADER = r'''
import os as _qturtle_os, sys as _qturtle_sys, types as _qturtle_types
import importlib.util as _qturtle_ilu

_qturtle_addons_dir = __QTURTLE_ADDONS_DIR__
if _qturtle_os.path.isdir(_qturtle_addons_dir):
    _qturtle_sys.path.insert(0, _qturtle_addons_dir)
    for _qturtle_file in sorted(_qturtle_os.listdir(_qturtle_addons_dir)):
        if not _qturtle_file.endswith(".py") or _qturtle_file.startswith("_"):
            continue
        _qturtle_name = _qturtle_file[:-3]
        try:
            _qturtle_path = _qturtle_os.path.join(_qturtle_addons_dir, _qturtle_file)
            _qturtle_spec = _qturtle_ilu.spec_from_file_location(_qturtle_name, _qturtle_path)
            if _qturtle_spec is None or _qturtle_spec.loader is None:
                continue
            _qturtle_mod = _qturtle_types.ModuleType(_qturtle_name)
            _qturtle_sys.modules[_qturtle_name] = _qturtle_mod
            _qturtle_spec.loader.exec_module(_qturtle_mod)
            for _n, _v in vars(_qturtle_mod).items():
                if _n.startswith("_") or isinstance(_v, _qturtle_types.ModuleType):
                    continue
                globals()[_n] = _v
        except Exception as _e:
            print(f"Warnung: Addon '{_qturtle_file}' konnte nicht geladen werden: {_e}",
                  file=_qturtle_sys.stderr)
'''

    def __init__(self, parent=None):
        super().__init__(parent)
        self._process = None
        self._temp_path = None

    def run(self, code: str):
        # Kill any existing process before starting a new one
        # This ensures old turtle windows are closed when running a new script or pressing F5 again
        if self.is_running:
            self._process.kill()
            if not self._process.waitForFinished(2000):
                # Force kill if graceful kill didn't work
                self._process.terminate()
                self._process.waitForFinished(1000)
            # Clean up temp file from killed process
            if self._temp_path and os.path.exists(self._temp_path):
                try:
                    os.remove(self._temp_path)
                except Exception:
                    pass
                self._temp_path = None

        # Detect if script uses turtle or SVGTurtle
        uses_turtle = "import turtle" in code or "from turtle" in code or "SVGTurtle" in code or "svg_turtle" in code

        # Build final code with UTF-8 setup and turtle epilog
        full_code = self.UTF8_PREFIX + self.ERROR_HINTS
        full_code += self.ADDON_LOADER.replace("__QTURTLE_ADDONS_DIR__", repr(str(self._addons_dir())))
        if uses_turtle:
            full_code += "\n" + self.TURTLE_TRACKING
            full_code += """
import turtle as _qturtle_t
_qturtle_original_forward = _qturtle_t.Turtle.forward
_qturtle_original_backward = _qturtle_t.Turtle.backward
_qturtle_t.Turtle.forward = _qturtle_track_forward
_qturtle_t.Turtle.backward = _qturtle_track_backward
_qturtle_t.Turtle.fd = _qturtle_track_forward
_qturtle_t.Turtle.bk = _qturtle_track_backward
_qturtle_t.Turtle.back = _qturtle_track_backward
_qturtle_t.Turtle.getX = _qturtle_t.Turtle.xcor
_qturtle_t.Turtle.getY = _qturtle_t.Turtle.ycor
_qturtle_t.Turtle.setX = _qturtle_t.Turtle.setx
_qturtle_t.Turtle.setY = _qturtle_t.Turtle.sety
"""
        full_code = full_code.replace("__QTURTLE_OFFSET__", str(full_code.count("\n")))
        full_code += code
        if uses_turtle:
            full_code += "\n" + self.TURTLE_EPILOG

        # Write to temp file
        try:
            fd, temp_path = tempfile.mkstemp(suffix=".py", prefix="qturtle_")
            os.write(fd, full_code.encode("utf-8"))
            os.close(fd)
            self._temp_path = temp_path
        except Exception as e:
            self.error_received.emit(f"Failed to create temp file: {e}")
            return

        # Create process
        self._process = QProcess(self)
        self._process.readyReadStandardOutput.connect(self._on_stdout)
        self._process.readyReadStandardError.connect(self._on_stderr)
        self._process.finished.connect(self._on_finished)

        python_exe = self._find_python()
        if not python_exe:
            self.error_received.emit("Python interpreter not found.")
            self._process = None
            return

        # Make qturtle package importable in the subprocess
        env = QProcessEnvironment.systemEnvironment()
        existing = env.value("PYTHONPATH", "")
        pkg_root = str(Path(__file__).parent.parent)
        extra = [pkg_root]
        if getattr(sys, "frozen", False):
            if hasattr(sys, "_MEIPASS"):
                extra.insert(0, sys._MEIPASS)  # pyright: ignore[reportAttributeAccessIssue]
            else:
                exe_dir = Path(sys.executable).parent
                extra.insert(0, str(exe_dir))
                # cx_Freeze stores packages in lib/ and lib/library.zip.
                # Both paths are needed: the directory for .pyd extensions,
                # the zip for pure-Python modules (turtle, tkinter, …).
                lib_dir = exe_dir / "lib"
                if lib_dir.exists():
                    extra.insert(0, str(lib_dir))
                    lib_zip = lib_dir / "library.zip"
                    if lib_zip.exists():
                        extra.insert(0, str(lib_zip))
                # Add build root to PATH so Windows DLL loader finds tcl/tk DLLs
                # when _tkinter.pyd (loaded from lib/) tries to import them.
                existing_path = env.value("PATH", "")
                env.insert("PATH", f"{str(exe_dir)};{existing_path}")
                # Note: Tcl finds its data via runtime/share/tcl8.6 (its default
                # search path relative to runtime/python.exe); no TCL_LIBRARY needed.
        pythonpath = ";".join(filter(None, extra + [existing]))
        env.insert("PYTHONPATH", pythonpath)
        self._process.setProcessEnvironment(env)

        # Start process
        try:
            self._process.start(python_exe, [temp_path])
        except Exception as e:
            self.error_received.emit(f"Failed to start process: {e}")
            self._process = None

    @staticmethod
    def _addons_dir() -> Path:
        """Folder with user-provided *.py files loaded into every script.

        In a frozen build the folder sits next to the app executable, so
        users can drop files there without touching the package. In source
        runs it is the repo root's addons/ folder.
        """
        if getattr(sys, "frozen", False):
            if hasattr(sys, "_MEIPASS"):
                base = Path(sys._MEIPASS)  # pyright: ignore[reportAttributeAccessIssue]
            else:
                base = Path(sys.executable).parent
        else:
            base = Path(__file__).resolve().parent.parent.parent
        return base / "addons"

    @staticmethod
    def _find_python() -> str:
        """Return a Python interpreter path safe for subprocess use.

        sys.executable is the app stub in PyInstaller, Nuitka, and Briefcase bundles,
        not the Python interpreter — launching it would open a second app window.
        """
        exe = Path(sys.executable)
        # Source / normal Python: executable is already python/pythonw
        if exe.stem.lower().startswith("python"):
            return str(exe)

        # PyInstaller onedir: check _MEIPASS for a bundled python.exe
        if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
            bundled = Path(sys._MEIPASS) / "python.exe"  # pyright: ignore[reportAttributeAccessIssue]
            if bundled.exists():
                return str(bundled)

        # Briefcase: support/python.exe sits one or two levels up from the launcher
        for base in (exe.parent, exe.parent.parent):
            candidate = base / "support" / "python.exe"
            if candidate.exists():
                return str(candidate)

        # cx_Freeze: python.exe in runtime/ subdirectory (has its own ._pth file)
        if getattr(sys, "frozen", False):
            candidate = exe.parent / "runtime" / "python.exe"
            if candidate.exists():
                return str(candidate)
            # Fallback: python.exe placed directly next to the app
            candidate = exe.parent / "python.exe"
            if candidate.exists():
                return str(candidate)

        # No bundled interpreter found; fall back to system Python
        return shutil.which("python") or shutil.which("python3") or ""

    def stop(self):
        if self._process is not None:
            self._process.kill()
            self._process.waitForFinished(2000)

    @property
    def is_running(self) -> bool:
        if self._process is None:
            return False
        return self._process.state() != QProcess.ProcessState.NotRunning

    def _on_stdout(self):
        if self._process is None:
            return
        data = self._process.readAllStandardOutput().data().decode("utf-8", errors="replace")  # pyright: ignore[reportAttributeAccessIssue]
        self.output_received.emit(data)

    def _on_stderr(self):
        if self._process is None:
            return
        data = self._process.readAllStandardError().data().decode("utf-8", errors="replace")  # pyright: ignore[reportAttributeAccessIssue]
        self.error_received.emit(data)

    def _on_finished(self, exit_code, exit_status):
        # Flush any remaining output that arrived with the exit signal
        if self._process is not None:
            remaining = self._process.readAllStandardOutput().data().decode("utf-8", errors="replace")  # pyright: ignore[reportAttributeAccessIssue]
            if remaining:
                self.output_received.emit(remaining)
            remaining_err = self._process.readAllStandardError().data().decode("utf-8", errors="replace")  # pyright: ignore[reportAttributeAccessIssue]
            if remaining_err:
                self.error_received.emit(remaining_err)

        self.finished_with_code.emit(exit_code)

        if self._temp_path and os.path.exists(self._temp_path):
            try:
                os.remove(self._temp_path)
            except Exception:
                pass
            self._temp_path = None

        self._process = None

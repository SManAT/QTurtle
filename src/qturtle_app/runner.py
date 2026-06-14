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
        full_code = self.UTF8_PREFIX
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
"""
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
                # Set Tcl/Tk library paths so tkinter can initialize in the subprocess.
                # cx_Freeze copies DLLs but not data files; we place those under tcl/.
                tcl_base = exe_dir / "tcl"
                for d in sorted(tcl_base.glob("tcl*")):
                    if d.is_dir() and (d / "init.tcl").exists():
                        env.insert("TCL_LIBRARY", str(d))
                        break
                for d in sorted(tcl_base.glob("tk*")):
                    if d.is_dir() and (d / "tk.tcl").exists():
                        env.insert("TK_LIBRARY", str(d))
                        break
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

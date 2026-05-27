import os
import sys
import tempfile
from pathlib import Path
from PySide6.QtCore import QObject, QProcess, Signal


class ScriptRunner(QObject):
    output_received = Signal(str)
    error_received = Signal(str)
    finished_with_code = Signal(int)

    # Epilog to keep turtle window open after script finishes
    TURTLE_EPILOG = """
import sys as _qturtle_sys
if 'turtle' in _qturtle_sys.modules:
    import turtle as _qturtle_t
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

        # Detect if script uses turtle
        uses_turtle = 'import turtle' in code or 'from turtle' in code

        # Build final code with UTF-8 setup and turtle epilog
        full_code = self.UTF8_PREFIX + code
        if uses_turtle:
            full_code += '\n' + self.TURTLE_EPILOG

        # Write to temp file
        try:
            fd, temp_path = tempfile.mkstemp(suffix='.py', prefix='qturtle_')
            os.write(fd, full_code.encode('utf-8'))
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

        # Start process
        try:
            self._process.start(sys.executable, [temp_path])
        except Exception as e:
            self.error_received.emit(f"Failed to start process: {e}")
            self._process = None

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
        data = self._process.readAllStandardOutput().data().decode('utf-8', errors='replace')
        self.output_received.emit(data)

    def _on_stderr(self):
        if self._process is None:
            return
        data = self._process.readAllStandardError().data().decode('utf-8', errors='replace')
        self.error_received.emit(data)

    def _on_finished(self, exit_code, exit_status):
        self.finished_with_code.emit(exit_code)

        # Clean up temp file
        if self._temp_path and os.path.exists(self._temp_path):
            try:
                os.remove(self._temp_path)
            except Exception:
                pass
            self._temp_path = None

        self._process = None

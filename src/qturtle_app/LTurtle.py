import json
import sys
import re
from pathlib import Path
from typing import Any

from PySide6 import QtCore
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QColor, QFont, QPixmap, QTextCharFormat
from PySide6.QtWidgets import QApplication, QFileDialog, QLabel, QMainWindow, QMessageBox
from qturtle_app.lib.L_system_class import LSystem

from qturtle_app.lib.responsive_window import ResponsiveMainWindow
from qturtle_app.ui.Ui_LTurtle import Ui_LTurtleWindow

from qturtle_app.runner import ScriptRunner

# Windows taskbar icon fix
if sys.platform == "win32":
    try:
        import ctypes

        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("QTurtle.App")
    except Exception:
        pass


_UMLAUT_MAP = {
    "ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss",
    "Ä": "Ae", "Ö": "Oe", "Ü": "Ue",
}


def sanitize_filename(name: str, default: str = "lsystem") -> str:
    """Return a safe ``*.svg`` filename for the given user input.

    - transliterates German umlauts (ä→ae, ö→oe, ü→ue, ß→ss),
    - replaces whitespace runs with a single underscore,
    - drops any remaining non-ASCII / filesystem-unsafe characters,
    - collapses repeated underscores and trims stray ``_``/``.`` at the ends,
    - always returns a name ending in ``.svg`` (falling back to *default*).
    """
    name = name.strip()
    for src, dst in _UMLAUT_MAP.items():
        name = name.replace(src, dst)

    # Work on the stem so the extension's dot survives the cleanup.
    stem = re.sub(r"\.svg$", "", name, flags=re.IGNORECASE)
    stem = re.sub(r"\s+", "_", stem)              # whitespace -> underscore
    stem = re.sub(r"[^A-Za-z0-9_-]", "", stem)    # strip unsafe / non-ASCII
    stem = re.sub(r"_+", "_", stem).strip("_.")   # tidy up

    return f"{stem or default}.svg"


class LSystemWorker(QThread):
    finished = Signal(str)
    error = Signal(str)

    def __init__(self, lsystem: LSystem):
        super().__init__()
        self.lsystem = lsystem

    def run(self):
        try:
            result = self.lsystem.getFinalString()
            self.finished.emit(result)
        except Exception as e:
            self.error.emit(str(e))


class LTurtleWindow(ResponsiveMainWindow):

    def __init__(self, main_window: QMainWindow, saveDir: Path):
        super().__init__()
        self.main_window = main_window
        self.rootDir = Path(__file__).parent
        self.current_file = None
        self.saveDir = saveDir
        self.lsystem_worker = None
        self.loader_spinner_index = 0

        # Setup UI
        self.ui = Ui_LTurtleWindow()
        self.ui.setupUi(self)
        self.ui.topSplitter.setSizes([300, 700])
        self.ui.mainSplitter.setSizes([450, 150])
        self.load_stylesheet("styles.css")

        # Create loader label
        self.loader_label = QLabel("⠋ Generating L-System...")
        self.loader_label.setStyleSheet("color: #6366f1; font-weight: bold; margin-left:10px;")
        self.loader_label.hide()
        self.ui.horizontalLayout.insertWidget(1, self.loader_label)

        # Configure console output
        self._setup_console()

        # Setup loader animation timer
        self.loader_timer = QtCore.QTimer()
        self.loader_timer.timeout.connect(self._update_loader_animation)

        # Setup script runner
        self.runner = ScriptRunner(self)
        self.runner.output_received.connect(self._on_runner_output)
        self.runner.error_received.connect(self._on_runner_error)
        self.runner.finished_with_code.connect(self._on_runner_finished)

        # Connect UI actions
        self._connect_actions()

        self._update_title()

        # permanent Widgets allways on right side
        copyright_label = QLabel("© S.Hagmann")
        self.ui.statusbar.addPermanentWidget(copyright_label)

        # Load window icon for taskbar
        self.apply_window_icon()

        self.setUpScreen()

        # show legend in console
        self.ui.consoleOutput.appendPlainText(LSystem.legend())

        self.show()

    def responsive_font_widgets(self):
        # Console scales with the window; the editor keeps its own Ctrl+/- zoom.
        return (self.ui.consoleOutput,)

    def initial_font_widgets(self):
        # Give the editor a screen-appropriate starting size at launch only.
        return (self.ui.codeEditor, self.ui.consoleOutput)

    def _setup_console(self):
        self.ui.consoleOutput.setReadOnly(True)
        palette = self.ui.consoleOutput.palette()
        palette.setColor(palette.ColorRole.Base, QColor("#FAFAFA"))
        palette.setColor(palette.ColorRole.Text, QColor("#383A42"))
        self.ui.consoleOutput.setPalette(palette)

    def _connect_actions(self):
        self.ui.actionNew.triggered.connect(self.new)
        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionSave.triggered.connect(self.save_file)
        self.ui.actionSave_As.triggered.connect(self.save_file_as)
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionRun.triggered.connect(self.run_script)
        self.ui.actionStop.triggered.connect(self.stop_script)
        # Buttons
        self.ui.openMainButton.clicked.connect(self.open_main_window)
        self.ui.btnRun.clicked.connect(self.run_script)

    def open_main_window(self):
        self.main_window.show()
        self.close()

    def _update_title(self):
        name = self.current_file.name if self.current_file else "Untitled"
        self.setWindowTitle(f"QTurtle (LTurtle) - {name}")

    def _generate_lsystem_code(self):
        angle = self.ui.winkel.value()
        iterations = self.ui.iterationen.value()
        length: int = self.ui.laenge.value()
        axiom = self.ui.axiom.text()
        rules: dict[Any, Any] = {}

        for char, widget in [("A", self.ui.ruleA), ("B", self.ui.ruleB), ("C", self.ui.ruleC), ("D", self.ui.ruleD), ("E", self.ui.ruleE)]:
            rule = widget.text()
            res = re.split(r"[>:]+", rule)
            if rule:
                rules[res[0].strip()] = res[1].strip()

        filename = sanitize_filename(self.ui.filename.text())
        self.ui.filename.setText(filename)  # reflect the sanitized name back

        lsys = LSystem(angle, iterations, axiom, rules)

        # Show loader and start worker thread
        self.ui.btnRun.setEnabled(False)
        self.loader_label.show()
        self.loader_spinner_index = 0
        self.loader_timer.start(100)

        self.lsystem_worker = LSystemWorker(lsys)
        self.lsystem_worker.finished.connect(lambda lstr: self._on_lsystem_generated(lstr, length, angle, iterations, filename))
        self.lsystem_worker.error.connect(self._on_lsystem_error)
        self.lsystem_worker.start()

    def _on_lsystem_generated(self, lstr, length, angle, iterations, filename):
        self.loader_timer.stop()
        self.loader_label.hide()
        self.ui.btnRun.setEnabled(True)

        code = f"""\
from qturtle_app.svg_turtle_class import SVGTurtle
from qturtle_app.lib.L_system_class import LSystem
import math

t = SVGTurtle(width=800, height=800, filename="{filename}", bgcolor="white")
t.speed(0)
L_str = "{lstr}"
t.drawLSystem(L_str, {length}, {angle}, {iterations})

t.save_svg()
"""
        self.ui.codeEditor.setPlainText(code)
        self.runner.run(code)

    def _on_lsystem_error(self, error_msg):
        self.loader_timer.stop()
        self.loader_label.hide()
        self.ui.btnRun.setEnabled(True)
        QMessageBox.critical(self, "Error", f"Failed to generate L-System: {error_msg}")

    def _on_modification_changed(self, changed):
        self._update_title()

    def new(self):
        if not self._maybe_save():
            return
        self.current_file = None
        self._update_title()

    def open_file(self):
        if not self._maybe_save():
            return

        path, _ = QFileDialog.getOpenFileName(self, "Open L-System File", str(self.saveDir), "L-System Files (*.lsys);;JSON Files (*.json);;All Files (*)")
        if not path:
            return

        try:
            data = json.loads(Path(path).read_text(encoding="utf-8"))
            self.ui.winkel.setValue(data.get("angle", 0))
            self.ui.iterationen.setValue(data.get("iterations", 1))
            self.ui.laenge.setValue(data.get("length", 10.0))
            self.ui.axiom.setText(data.get("axiom", "X"))
            self.ui.ruleA.setText(data.get("ruleA", ""))
            self.ui.ruleB.setText(data.get("ruleB", ""))
            self.ui.ruleC.setText(data.get("ruleC", ""))
            self.ui.ruleD.setText(data.get("ruleD", ""))
            self.ui.ruleE.setText(data.get("ruleE", ""))
            self.ui.filename.setText(data.get("filename", "lsystem.svg"))
            self.current_file = Path(path)
            self._update_title()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to open file: {e}")

    def save_file(self):
        if self.current_file is None:
            return self.save_file_as()

        try:
            data = {
                "angle": self.ui.winkel.value(),
                "iterations": self.ui.iterationen.value(),
                "length": self.ui.laenge.value(),
                "axiom": self.ui.axiom.text(),
                "ruleA": self.ui.ruleA.text(),
                "ruleB": self.ui.ruleB.text(),
                "ruleC": self.ui.ruleC.text(),
                "ruleD": self.ui.ruleD.text(),
                "ruleE": self.ui.ruleE.text(),
                "filename": self.ui.filename.text(),
            }
            self.current_file.write_text(json.dumps(data, indent=2), encoding="utf-8")
            self._update_title()
            return True
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save file: {e}")
            return False

    def save_file_as(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save L-System File", str(self.saveDir / "untitled.lsys"), "L-System Files (*.lsys);;JSON Files (*.json);;All Files (*)")
        if not path:
            return False

        self.current_file = Path(path)
        return self.save_file()

    def _maybe_save(self):
        return True

    def _update_loader_animation(self):
        spinners = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        self.loader_spinner_index = (self.loader_spinner_index + 1) % len(spinners)
        self.loader_label.setText(f"{spinners[self.loader_spinner_index]} Generating L-System...")

    def run_script(self):
        self.ui.consoleOutput.clear()
        self.ui.consoleOutput.appendPlainText("--- Running L-System ---\n")
        self._generate_lsystem_code()

    def stop_script(self):
        self.runner.stop()
        self.ui.consoleOutput.appendPlainText("\n--- Stopped ---")
        QApplication.processEvents()

    def _on_runner_output(self, text):
        self.ui.consoleOutput.moveCursor(self.ui.consoleOutput.textCursor().MoveOperation.End)
        self.ui.consoleOutput.insertPlainText(text)

    def _on_runner_error(self, text):
        cursor = self.ui.consoleOutput.textCursor()
        cursor.movePosition(cursor.MoveOperation.End)
        self.ui.consoleOutput.setTextCursor(cursor)

        fmt = QTextCharFormat()
        fmt.setForeground(QColor("#E45649"))
        cursor.insertText(text, fmt)

    def _on_runner_finished(self, exit_code):
        if exit_code != 0:
            self.ui.consoleOutput.appendPlainText(f"--- Done (exit code {exit_code}) ---")
        else:
            self.ui.consoleOutput.appendPlainText(f"--- Done ---")

    def closeEvent(self, event):
        if self._maybe_save():
            event.accept()
        else:
            event.ignore()

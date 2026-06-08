import json
import sys
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QFont, QIcon, QPixmap, QScreen, QTextCharFormat
from PySide6.QtWidgets import QApplication, QFileDialog, QLabel, QMainWindow, QMessageBox
from qturtle_app.ui.Ui_LTurtle import Ui_LTurtleWindow

from qturtle_app.runner import ScriptRunner

# Windows taskbar icon fix
if sys.platform == "win32":
    try:
        import ctypes

        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("QTurtle.App")
    except Exception:
        pass


class LTurtleWindow(QMainWindow):

    def __init__(self, main_window: QMainWindow):
        super().__init__()
        self.main_window = main_window
        self.rootDir = Path(__file__).parent
        self.current_file = None

        # Setup UI
        self.ui = Ui_LTurtleWindow()
        self.ui.setupUi(self)
        self.load_stylesheet("styles.css")

        # Configure console output
        self._setup_console()

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
        try:
            icon_path = self.rootDir.parent / "assets" / "app.ico"
            if icon_path.exists():
                appIcon = QIcon(str(icon_path))
                self.setWindowIcon(appIcon)
        except Exception:
            pass

        # center on screen
        screen = QApplication.primaryScreen()
        screen_h = screen.availableGeometry().height()
        screen_w = screen.availableGeometry().width()
        self.setGeometry(0, 0, int(screen_w * 0.75), int(screen_h * 0.75))
        self.center()

        self.show()

    def center(self):
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geo = self.frameGeometry()
        geo.moveCenter(center)
        self.move(geo.topLeft())

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

    def open_main_window(self):
        self.main_window.show()
        self.close()

    def _update_title(self):
        name = self.current_file.name if self.current_file else "Untitled"
        self.setWindowTitle(f"QTurtle (LTurtle) - {name}")

    def _generate_lsystem_code(self):
        angle = self.ui.winkel.value()
        iterations = self.ui.iterationen.value()
        length = self.ui.laenge.value()
        axiom = self.ui.axiom.text()
        rules = {}
        for char, widget in [("A", self.ui.ruleA), ("B", self.ui.ruleB), ("C", self.ui.ruleC), ("D", self.ui.ruleD), ("E", self.ui.ruleE), ("F", self.ui.ruleF)]:
            rule = widget.text()
            if rule:
                rules[char] = rule

        code = f"""\
from qturtle_app.svg_turtle_class import SVGTurtle
import math

t = SVGTurtle(width=800, height=800, filename="lsystem.svg", bgcolor="white")
t.speed(0)

axiom = "{axiom}"
rules = {rules}
angle = {angle}
length = {length}

current = axiom
for _ in range({iterations}):
    next_gen = ""
    for char in current:
        next_gen += rules.get(char, char)
    current = next_gen

stack = []
for char in current:
    if char == '+':
        t.right(90)
    elif char == '-':
        t.left(90)
    elif char == '[':
        stack.append((t.xcor(), t.ycor(), t.heading()))
    elif char == ']':
        if stack:
            x, y, heading = stack.pop()
            t.penup()
            t.goto(x, y)
            t.setheading(heading)
            t.pendown()
    elif char in rules:
        t.forward({length})

t.save_svg()
"""
        return code

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

        path, _ = QFileDialog.getOpenFileName(self, "Open L-System File", str(Path.home()), "L-System Files (*.lsys);;JSON Files (*.json);;All Files (*)")
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
            self.ui.ruleF.setText(data.get("ruleF", ""))
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
                "ruleF": self.ui.ruleF.text(),
            }
            self.current_file.write_text(json.dumps(data, indent=2), encoding="utf-8")
            self._update_title()
            return True
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save file: {e}")
            return False

    def save_file_as(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save L-System File", str(self.current_file or Path.home() / "untitled.lsys"), "L-System Files (*.lsys);;JSON Files (*.json);;All Files (*)")
        if not path:
            return False

        self.current_file = Path(path)
        return self.save_file()

    def _maybe_save(self):
        return True

    def run_script(self):
        self.ui.consoleOutput.clear()
        self.ui.consoleOutput.appendPlainText("--- Running L-System ---\n")
        code = self._generate_lsystem_code()
        self.runner.run(code)

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

    def load_stylesheet(self, file_path):
        css_path = Path.joinpath(self.rootDir, "css", file_path)
        try:
            with open(css_path, "r", encoding="utf-8") as file:
                stylesheet = file.read()
                self.setStyleSheet(stylesheet)
        except FileNotFoundError:
            print(f"CSS file '{css_path}' not found")

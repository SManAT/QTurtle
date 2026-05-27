import sys
from pathlib import Path

# Add src/ to path so Ui_MainWindow.py can import editor
sys.path.insert(0, str(Path(__file__).parent))

from PySide6.QtGui import QIcon, QPixmap, QFont, QTextCharFormat, QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PySide6.QtCore import Qt

from ui.Ui_MainWindow import Ui_MainWindow
from runner import ScriptRunner


DEFAULT_CODE = '''\
import turtle

t = turtle.Turtle()
t.speed(3)

for i in range(4):
    t.forward(100)
    t.right(90)
'''


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.rootDir = Path(__file__).parent
        self.current_file = None

        # Setup UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.load_stylesheet("styles.css")

        # Configure editor
        self.ui.codeEditor.setDefaultCode(DEFAULT_CODE)

        # Configure console output
        self._setup_console()

        # Setup script runner
        self.runner = ScriptRunner(self)
        self.runner.output_received.connect(self._on_runner_output)
        self.runner.error_received.connect(self._on_runner_error)
        self.runner.finished_with_code.connect(self._on_runner_finished)

        # Connect UI actions
        self._connect_actions()

        # Connect editor signals
        self.ui.codeEditor.document().modificationChanged.connect(self._on_modification_changed)
        self.ui.codeEditor.cursorPositionChanged.connect(self._update_status_bar)

        # Load window icon
        try:
            icon_path = self.rootDir.parent / 'assets' / 'app.ico'
            if icon_path.exists():
                appIcon = QIcon(str(icon_path))
                self.setWindowIcon(appIcon)
        except Exception:
            pass

        self._update_title()
        self.show()

    def _setup_console(self):
        self.ui.consoleOutput.setReadOnly(True)
        self.ui.consoleOutput.setFont(QFont("Consolas", 10))
        palette = self.ui.consoleOutput.palette()
        palette.setColor(palette.ColorRole.Base, QColor("#0C0C0C"))
        palette.setColor(palette.ColorRole.Text, QColor("#CCCCCC"))
        self.ui.consoleOutput.setPalette(palette)

    def _connect_actions(self):
        self.ui.actionNew.triggered.connect(self.new)
        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionSave.triggered.connect(self.save_file)
        self.ui.actionSave_As.triggered.connect(self.save_file_as)
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionCut.triggered.connect(self.ui.codeEditor.cut)
        self.ui.actionCopy.triggered.connect(self.ui.codeEditor.copy)
        self.ui.actionPaste.triggered.connect(self.ui.codeEditor.paste)
        self.ui.actionSelect_All.triggered.connect(self.ui.codeEditor.selectAll)
        self.ui.actionRun.triggered.connect(self.run_script)
        self.ui.actionStop.triggered.connect(self.stop_script)

    def _update_title(self):
        name = self.current_file.name if self.current_file else "Untitled"
        modified = " *" if self.ui.codeEditor.document().isModified() else ""
        self.setWindowTitle(f"QTurtle - {name}{modified}")

    def _update_status_bar(self):
        cursor = self.ui.codeEditor.textCursor()
        line = cursor.blockNumber() + 1
        col = cursor.columnNumber() + 1
        self.statusBar().showMessage(f"Line {line}, Col {col}")

    def _on_modification_changed(self, changed):
        self._update_title()

    def new(self):
        if not self._maybe_save():
            return
        self.ui.codeEditor.setDefaultCode(DEFAULT_CODE)
        self.current_file = None
        self._update_title()

    def open_file(self):
        if not self._maybe_save():
            return

        path, _ = QFileDialog.getOpenFileName(
            self,
            "Open Python File",
            str(Path.home()),
            "Python Files (*.py);;All Files (*)"
        )
        if not path:
            return

        try:
            text = Path(path).read_text(encoding='utf-8')
            self.ui.codeEditor.setPlainText(text)
            self.ui.codeEditor.document().setModified(False)
            self.current_file = Path(path)
            self._update_title()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to open file: {e}")

    def save_file(self):
        if self.current_file is None:
            return self.save_file_as()

        try:
            self.current_file.write_text(
                self.ui.codeEditor.toPlainText(),
                encoding='utf-8'
            )
            self.ui.codeEditor.document().setModified(False)
            self._update_title()
            return True
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save file: {e}")
            return False

    def save_file_as(self):
        path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Python File",
            str(self.current_file or Path.home() / "untitled.py"),
            "Python Files (*.py);;All Files (*)"
        )
        if not path:
            return False

        self.current_file = Path(path)
        return self.save_file()

    def _maybe_save(self):
        if not self.ui.codeEditor.document().isModified():
            return True

        reply = QMessageBox.warning(
            self,
            "Unsaved Changes",
            "The document has been modified.\nDo you want to save the changes?",
            QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.Cancel,
            QMessageBox.StandardButton.Save
        )

        if reply == QMessageBox.StandardButton.Save:
            return self.save_file()
        elif reply == QMessageBox.StandardButton.Discard:
            return True
        else:
            return False

    def run_script(self):
        if self.runner.is_running:
            return

        self.ui.consoleOutput.clear()
        self.ui.consoleOutput.appendPlainText("--- Running ---\n")
        code = self.ui.codeEditor.toPlainText()
        self.runner.run(code)
        self.ui.actionRun.setEnabled(False)
        self.ui.actionStop.setEnabled(True)

    def stop_script(self):
        self.runner.stop()

    def _on_runner_output(self, text):
        self.ui.consoleOutput.moveCursor(self.ui.consoleOutput.textCursor().MoveOperation.End)
        self.ui.consoleOutput.insertPlainText(text)

    def _on_runner_error(self, text):
        cursor = self.ui.consoleOutput.textCursor()
        cursor.movePosition(cursor.MoveOperation.End)
        self.ui.consoleOutput.setTextCursor(cursor)

        fmt = QTextCharFormat()
        fmt.setForeground(QColor("#FF6B6B"))
        cursor.insertText(text, fmt)

    def _on_runner_finished(self, exit_code):
        self.ui.consoleOutput.appendPlainText(f"\n--- Finished (exit code {exit_code}) ---")
        self.ui.actionRun.setEnabled(True)
        self.ui.actionStop.setEnabled(False)

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

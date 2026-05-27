#!/usr/bin/env python3
"""
Debug script to test keyboard key codes for zoom functionality.
Shows what key code is detected when you press Ctrl++, Ctrl+-, etc.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from PySide6.QtWidgets import QApplication, QMainWindow, QPlainTextEdit
from PySide6.QtCore import Qt


class KeyTestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Keyboard Key Code Tester")
        self.resize(600, 400)

        self.editor = QPlainTextEdit()
        self.editor.setPlainText("Press Ctrl++ and Ctrl+- to test key codes.\nKey events will appear below:\n\n")
        self.setCentralWidget(self.editor)

        # Override key event
        original_keyPressEvent = self.editor.keyPressEvent

        def keyPressEvent(event):
            if event.modifiers() & Qt.KeyboardModifier.ControlModifier:
                key = event.key()
                text = event.text()
                modifiers = event.modifiers()

                # Key code names
                key_names = {
                    Qt.Key.Key_Plus: "Key_Plus",
                    Qt.Key.Key_Equal: "Key_Equal",
                    Qt.Key.Key_Minus: "Key_Minus",
                    Qt.Key.Key_Asterisk: "Key_Asterisk",
                }
                key_name = key_names.get(key, f"Key({key})")

                msg = f"Ctrl+{text or '?'}: key={key_name} ({key}), text='{text}'\n"
                self.editor.appendPlainText(msg)
                print(msg)
                event.accept()
                return

            original_keyPressEvent(event)

        self.editor.keyPressEvent = keyPressEvent

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KeyTestWindow()
    print("\n" + "=" * 60)
    print("Keyboard Key Code Tester")
    print("=" * 60)
    print("\nPress Ctrl++ and Ctrl+- in the window.")
    print("Key codes will be displayed in the window and console.\n")
    print("For zoom to work, we need:")
    print("  Ctrl++ → should show Key_Plus, Key_Equal, or text='+'")
    print("  Ctrl+- → should show Key_Minus or text='-'")
    print("\n" + "=" * 60 + "\n")
    sys.exit(app.exec())

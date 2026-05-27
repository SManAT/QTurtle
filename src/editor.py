from PySide6.QtWidgets import QPlainTextEdit, QWidget, QTextEdit
from PySide6.QtCore import Qt, QRect, QSize, QRegularExpression, Signal
from PySide6.QtGui import (
    QColor, QPainter, QTextCharFormat, QFont, QSyntaxHighlighter,
    QPalette, QTextCursor
)


class PythonHighlighter(QSyntaxHighlighter):
    def __init__(self, document):
        super().__init__(document)
        self._rules = []

        # Keywords (blue)
        kw_format = QTextCharFormat()
        kw_format.setForeground(QColor("#569CD6"))
        kw_format.setFontWeight(QFont.Weight.Bold)
        keywords = [
            "False", "None", "True", "and", "as", "assert",
            "async", "await", "break", "class", "continue", "def",
            "del", "elif", "else", "except", "finally", "for",
            "from", "global", "if", "import", "in", "is", "lambda",
            "nonlocal", "not", "or", "pass", "raise", "return",
            "try", "while", "with", "yield"
        ]
        for kw in keywords:
            pattern = QRegularExpression(r"\b" + kw + r"\b")
            self._rules.append((pattern, kw_format))

        # Built-ins (cyan)
        builtin_format = QTextCharFormat()
        builtin_format.setForeground(QColor("#4EC9B0"))
        builtins = [
            "abs", "all", "any", "bin", "bool", "breakpoint", "bytearray",
            "bytes", "callable", "chr", "classmethod", "compile", "complex",
            "delattr", "dict", "dir", "divmod", "enumerate", "eval", "exec",
            "filter", "float", "format", "frozenset", "getattr", "globals",
            "hasattr", "hash", "help", "hex", "id", "input", "int",
            "isinstance", "issubclass", "iter", "len", "list", "locals",
            "map", "max", "memoryview", "min", "next", "object", "oct",
            "open", "ord", "pow", "print", "property", "range", "repr",
            "reversed", "round", "set", "setattr", "slice", "sorted",
            "staticmethod", "str", "sum", "super", "tuple", "type", "vars",
            "zip", "__init__", "__str__", "__repr__", "__len__"
        ]
        for b in builtins:
            pattern = QRegularExpression(r"\b" + b + r"\b")
            self._rules.append((pattern, builtin_format))

        # self/cls (light blue)
        self_format = QTextCharFormat()
        self_format.setForeground(QColor("#9CDCFE"))
        self._rules.append((QRegularExpression(r"\b(self|cls)\b"), self_format))

        # Numbers (light green)
        num_format = QTextCharFormat()
        num_format.setForeground(QColor("#B5CEA8"))
        self._rules.append((QRegularExpression(r"\b\d+\.?\d*\b"), num_format))

        # Strings (orange) - single and double quoted
        str_format = QTextCharFormat()
        str_format.setForeground(QColor("#CE9178"))
        self._rules.append((QRegularExpression(r'"[^"\\]*(\\.[^"\\]*)*"'), str_format))
        self._rules.append((QRegularExpression(r"'[^'\\]*(\\.[^'\\]*)*'"), str_format))

        # Comments (green) - must come last to override
        comment_format = QTextCharFormat()
        comment_format.setForeground(QColor("#6A9955"))
        comment_format.setFontItalic(True)
        self._rules.append((QRegularExpression(r"#[^\n]*"), comment_format))

        # Block states for triple-quoted strings
        self._tri_single = (QRegularExpression(r"'''"), 1, str_format)
        self._tri_double = (QRegularExpression(r'"""'), 2, str_format)

    def highlightBlock(self, text):
        # Apply single-line rules
        for pattern, fmt in self._rules:
            it = pattern.globalMatch(text)
            while it.hasNext():
                match = it.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), fmt)


class LineNumberArea(QWidget):
    def __init__(self, editor):
        super().__init__(editor)
        self.editor = editor

    def sizeHint(self):
        return QSize(self.editor.line_number_area_width(), 0)

    def paintEvent(self, event):
        self.editor.line_number_area_paint_event(event)


class CodeEditor(QPlainTextEdit):
    run_requested = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.line_number_area = LineNumberArea(self)

        # Connect signals for line number updates
        self.blockCountChanged.connect(self.update_line_number_area_width)
        self.updateRequest.connect(self.update_line_number_area)
        self.cursorPositionChanged.connect(self.highlight_current_line)

        # Set font - monospace
        font = QFont("Consolas", 12)
        font.setStyleStrategy(QFont.StyleStrategy.PreferAntialias)
        self.setFont(font)

        # Dark theme palette
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Base, QColor("#1E1E1E"))
        palette.setColor(QPalette.ColorRole.Text, QColor("#D4D4D4"))
        palette.setColor(QPalette.ColorRole.Highlight, QColor("#264F78"))
        palette.setColor(QPalette.ColorRole.HighlightedText, QColor("#D4D4D4"))
        self.setPalette(palette)

        # Tab stop = 4 spaces
        self.setTabStopDistance(self.fontMetrics().horizontalAdvance(' ' * 4))

        # Syntax highlighter
        PythonHighlighter(self.document())

        self.update_line_number_area_width(0)

        # Current line highlight color
        self._current_line_color = QColor("#2A2D2E")

    def line_number_area_width(self):
        digits = len(str(max(1, self.blockCount())))
        return 10 + self.fontMetrics().horizontalAdvance('9') * digits

    def update_line_number_area_width(self, _):
        self.setViewportMargins(self.line_number_area_width(), 0, 0, 0)

    def update_line_number_area(self, rect, dy):
        if dy:
            self.line_number_area.scroll(0, dy)
        else:
            self.line_number_area.update(0, rect.y(), self.line_number_area.width(), rect.height())

        if rect.contains(self.viewport().rect()):
            self.update_line_number_area_width(0)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        cr = self.contentsRect()
        self.line_number_area.setGeometry(
            QRect(cr.left(), cr.top(), self.line_number_area_width(), cr.height())
        )

    def line_number_area_paint_event(self, event):
        painter = QPainter(self.line_number_area)
        painter.fillRect(event.rect(), QColor("#2A2A2A"))

        block = self.firstVisibleBlock()
        block_number = block.blockNumber()
        top = round(self.blockBoundingGeometry(block).translated(self.contentOffset()).top())
        bottom = top + round(self.blockBoundingRect(block).height())

        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                painter.setPen(QColor("#858585"))
                painter.drawText(
                    0, top,
                    self.line_number_area.width() - 3,
                    round(self.blockBoundingRect(block).height()),
                    int(Qt.AlignmentFlag.AlignRight),
                    str(block_number + 1)
                )
            block = block.next()
            top = bottom
            bottom = top + round(self.blockBoundingRect(block).height())
            block_number += 1

    def highlight_current_line(self):
        if not self.isReadOnly():
            # Use a simple approach: highlight by color change on cursor move
            pass  # Current line highlighting handled via QPalette selection color

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter:
            self._handle_auto_indent()
            return
        elif event.key() == Qt.Key.Key_Tab:
            self.insertPlainText('    ')
            return
        elif event.key() == Qt.Key.Key_Backtab:
            self._handle_shift_tab()
            return
        elif event.key() == Qt.Key.Key_F5:
            self.run_requested.emit()
            return

        super().keyPressEvent(event)

    def _handle_auto_indent(self):
        cursor = self.textCursor()
        block = cursor.block()
        block_text = block.text()

        # Calculate current indentation
        indent = len(block_text) - len(block_text.lstrip())
        indent_str = block_text[:indent]

        # Check if line ends with colon (add extra indent)
        if block_text.rstrip().endswith(':'):
            indent_str += '    '

        # Insert newline + indentation
        super().keyPressEvent(
            __import__('PySide6.QtGui', fromlist=['QKeyEvent']).QKeyEvent(
                __import__('PySide6.QtCore', fromlist=['QEvent']).QEvent.Type.KeyPress,
                Qt.Key.Key_Return, Qt.KeyboardModifier.NoModifier
            )
        )
        self.insertPlainText(indent_str)

    def _handle_shift_tab(self):
        cursor = self.textCursor()
        block = cursor.block()
        text = block.text()

        if text.startswith('    '):
            # Remove 4 spaces from the beginning
            cursor.movePosition(QTextCursor.MoveOperation.StartOfBlock)
            cursor.movePosition(QTextCursor.MoveOperation.Right, QTextCursor.MoveMode.KeepAnchor, 4)
            cursor.removeSelectedText()

    def setDefaultCode(self, code: str):
        self.setPlainText(code)
        self.document().setModified(False)

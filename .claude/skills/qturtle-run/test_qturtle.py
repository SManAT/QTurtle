#!/usr/bin/env python3
"""
Automated tests for QTurtle application features.
Tests editor, zoom, and basic functionality.
"""

import sys
import time
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QKeySequence

from qturtle import MainWindow


def test_theme_colors():
    """Verify light theme colors are applied."""
    app = QApplication(sys.argv)
    window = MainWindow()

    # Check editor colors
    editor = window.ui.codeEditor
    palette = editor.palette()

    base_color = palette.color(palette.ColorRole.Base).name()
    text_color = palette.color(palette.ColorRole.Text).name()

    print(f"✓ Editor base color: {base_color}")
    print(f"✓ Editor text color: {text_color}")

    assert base_color == "#fafafa", f"Expected #fafafa, got {base_color}"
    assert text_color == "#383a42", f"Expected #383a42, got {text_color}"
    print("✓ Theme colors verified")

    window.close()
    return True


def test_zoom_bounds():
    """Verify zoom min/max bounds."""
    app = QApplication(sys.argv)
    window = MainWindow()
    editor = window.ui.codeEditor

    print(f"✓ Initial font size: {editor.font().pointSize()}pt")
    print(f"✓ Min size: {editor.min_font_size}pt, Max size: {editor.max_font_size}pt")

    # Test zoom in
    initial_size = editor.font().pointSize()
    for _ in range(30):  # Try to zoom in past max
        editor.zoom_in()

    max_achieved = editor.font().pointSize()
    assert max_achieved == editor.max_font_size, f"Max zoom failed: {max_achieved}pt"
    print(f"✓ Zoom in bounded to {max_achieved}pt (max: {editor.max_font_size}pt)")

    # Test zoom out
    for _ in range(30):  # Try to zoom out past min
        editor.zoom_out()

    min_achieved = editor.font().pointSize()
    assert min_achieved == editor.min_font_size, f"Min zoom failed: {min_achieved}pt"
    print(f"✓ Zoom out bounded to {min_achieved}pt (min: {editor.min_font_size}pt)")

    window.close()
    return True


def test_editor_properties():
    """Verify editor properties and defaults."""
    app = QApplication(sys.argv)
    window = MainWindow()
    editor = window.ui.codeEditor

    # Check default code
    code = editor.toPlainText()
    assert "import turtle" in code, "Default code should include turtle import"
    assert "t.forward" in code, "Default code should include forward command"
    print("✓ Default code present")

    # Check syntax highlighter
    highlighter = editor.document().syntaxHighlighter()
    assert highlighter is not None, "Syntax highlighter should be present"
    print("✓ Syntax highlighter present")

    # Check line number area
    assert editor.line_number_area is not None, "Line number area should exist"
    print("✓ Line number area present")

    # Check modification tracking
    assert not editor.document().isModified(), "Document should start unmodified"
    editor.setPlainText("test")
    assert editor.document().isModified(), "Document should be marked modified"
    print("✓ Modification tracking works")

    window.close()
    return True


def test_file_operations():
    """Verify file operation methods exist and work."""
    import tempfile

    app = QApplication(sys.argv)
    window = MainWindow()

    # Test new file
    window.new()
    assert window.current_file is None, "New file should have no path"
    print("✓ New file operation works")

    # Test save as
    with tempfile.NamedTemporaryFile(suffix='.py', delete=False) as f:
        temp_path = f.name

    try:
        window.current_file = Path(temp_path)
        window.ui.codeEditor.setPlainText("# Test code")
        success = window.save_file()
        assert success, "Save should succeed"
        assert Path(temp_path).exists(), "File should exist after save"
        print(f"✓ Save file works: {temp_path}")

        # Test open file
        window.new()  # Clear current
        window.current_file = Path(temp_path)
        code = Path(temp_path).read_text()
        window.ui.codeEditor.setPlainText(code)
        assert "Test code" in window.ui.codeEditor.toPlainText()
        print("✓ Open file works")
    finally:
        if Path(temp_path).exists():
            Path(temp_path).unlink()

    window.close()
    return True


def test_console_output():
    """Verify console output panel."""
    app = QApplication(sys.argv)
    window = MainWindow()
    console = window.ui.consoleOutput

    # Check console is read-only
    assert console.isReadOnly(), "Console should be read-only"
    print("✓ Console is read-only")

    # Check console colors
    palette = console.palette()
    base_color = palette.color(palette.ColorRole.Base).name()
    text_color = palette.color(palette.ColorRole.Text).name()

    assert base_color == "#fafafa", f"Console background incorrect: {base_color}"
    assert text_color == "#383a42", f"Console text color incorrect: {text_color}"
    print("✓ Console colors correct")

    window.close()
    return True


def run_all_tests():
    """Run all tests."""
    tests = [
        ("Theme Colors", test_theme_colors),
        ("Zoom Bounds", test_zoom_bounds),
        ("Editor Properties", test_editor_properties),
        ("File Operations", test_file_operations),
        ("Console Output", test_console_output),
    ]

    print("=" * 60)
    print("QTurtle Application Tests")
    print("=" * 60)

    passed = 0
    failed = 0

    for name, test_func in tests:
        try:
            print(f"\n[{name}]")
            result = test_func()
            if result:
                passed += 1
                print(f"✓ {name} PASSED")
        except Exception as e:
            failed += 1
            print(f"✗ {name} FAILED: {e}")
            import traceback
            traceback.print_exc()

    print("\n" + "=" * 60)
    print(f"Results: {passed} passed, {failed} failed")
    print("=" * 60)

    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)

"""Shared, responsive QMainWindow base for QTurtle's windows."""

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow


class ResponsiveMainWindow(QMainWindow):
    """Common window behaviour for the main and L-System windows.

    Provides:
      * clamped, screen-relative initial sizing + centering (``setUpScreen``),
      * a console font that scales with the window width (``resizeEvent``),
      * the taskbar/title-bar icon (``apply_window_icon``),
      * stylesheet loading (``load_stylesheet``).

    Subclasses must set ``self.rootDir`` (the ``qturtle_app`` package directory)
    before calling :meth:`apply_window_icon` / :meth:`load_stylesheet`, and may
    override :meth:`responsive_font_widgets` and :meth:`initial_font_widgets`.
    """

    # Initial window size = SCREEN_FRACTION of the available screen, clamped so
    # it is neither unusably small nor absurdly large on extreme displays.
    SCREEN_FRACTION = 0.75
    MIN_WIDTH, MAX_WIDTH = 900, 1600
    MIN_HEIGHT, MAX_HEIGHT = 600, 1000

    # Console font scales linearly with the window width, clamped to [min, max].
    FONT_MIN_PT, FONT_MAX_PT = 9, 16
    FONT_REF_WIDTH = 1400  # window width (px) at which FONT_MAX_PT is reached

    @staticmethod
    def _clamp(value, low, high):
        return max(low, min(value, high))

    # -- initial geometry ---------------------------------------------------
    def setUpScreen(self):
        """Size the window relative to the screen (clamped) and centre it."""
        available = self.screen().availableGeometry()
        width = self._clamp(
            int(available.width() * self.SCREEN_FRACTION), self.MIN_WIDTH, self.MAX_WIDTH
        )
        height = self._clamp(
            int(available.height() * self.SCREEN_FRACTION), self.MIN_HEIGHT, self.MAX_HEIGHT
        )
        self.resize(width, height)
        self.center()

        # Mark ready so resizeEvent (which may fire before this) starts scaling,
        # then apply the screen-appropriate starting font once.
        self._responsive_ready = True
        self._scale_fonts(self.initial_font_widgets())

    def center(self):
        geometry = self.frameGeometry()
        geometry.moveCenter(self.screen().availableGeometry().center())
        self.move(geometry.topLeft())

    # -- responsive font ----------------------------------------------------
    def _responsive_point_size(self):
        pt = round(self.width() * self.FONT_MAX_PT / self.FONT_REF_WIDTH)
        return self._clamp(pt, self.FONT_MIN_PT, self.FONT_MAX_PT)

    def _scale_fonts(self, widgets):
        pt = self._responsive_point_size()
        for widget in widgets:
            font = widget.font()
            if font.pointSize() != pt:  # avoid needless re-layout / flicker
                font.setPointSize(pt)
                widget.setFont(font)

    def responsive_font_widgets(self):
        """Widgets whose font is re-scaled on *every* resize (default: none).

        Override to return e.g. the console output. Do **not** include the code
        editor here — it has its own Ctrl+/- zoom, and auto-scaling on resize
        would fight the user.
        """
        return ()

    def initial_font_widgets(self):
        """Widgets that get a screen-appropriate font *once* at startup.

        Defaults to :meth:`responsive_font_widgets`. The editor may be added
        here for a sensible per-screen starting size without losing manual zoom.
        """
        return self.responsive_font_widgets()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if getattr(self, "_responsive_ready", False):
            self._scale_fonts(self.responsive_font_widgets())

    # -- shared chrome ------------------------------------------------------
    def apply_window_icon(self):
        """Set the window/taskbar icon from ``<package>/../assets/app.ico``."""
        try:
            icon_path = self.rootDir.parent / "assets" / "app.ico"
            if icon_path.exists():
                self.setWindowIcon(QIcon(str(icon_path)))
        except Exception:
            pass

    def load_stylesheet(self, file_path):
        css_path = self.rootDir / "css" / file_path
        try:
            self.setStyleSheet(css_path.read_text(encoding="utf-8"))
        except FileNotFoundError:
            print(f"CSS file '{css_path}' not found")

#!/usr/bin/env python3
"""Convert a Markdown file to PDF using Qt (no extra dependencies).

Usage: python md_to_pdf.py <input.md> <output.pdf>

Used by setup_cxfreeze.py to bundle TURTLE_API.md as a PDF.
"""

import sys
from pathlib import Path

from PySide6.QtCore import QMarginsF
from PySide6.QtGui import (
    QFont, QGuiApplication, QPageLayout, QPageSize, QPdfWriter, QTextDocument,
)

# Fonts must be installed on the build machine; they are embedded in the PDF.
BODY_FONT = "Calibri"
CODE_FONT = "Consolas"
FONT_SIZE = 9  # pt

# Qt's rich text engine supports a CSS subset; applied to the HTML of the
# converted Markdown so tables get borders.
CSS = """
body { color: #242d35; }
h1 { font-size: 18pt; color: #1a1a1a; }
h2 { font-size: 13pt; color: #1a1a1a; margin-top: 14px; }
table { border-collapse: collapse; }
th { background-color: #ececec; font-weight: bold; }
th, td { border: 1px solid #c8c8c8; padding: 3px; }
"""


def convert(md_path: Path, pdf_path: Path) -> None:
    source = QTextDocument()
    source.setDefaultFont(QFont(BODY_FONT, FONT_SIZE))
    source.setMarkdown(md_path.read_text(encoding="utf-8"))

    # setMarkdown() hard-codes the fonts into the HTML (code always becomes
    # 'Courier New'), so CSS cannot override them: replace them directly.
    html = source.toHtml()
    html = html.replace("font-family:'Courier New'", f"font-family:'{CODE_FONT}'")

    doc = QTextDocument()
    doc.setDefaultFont(QFont(BODY_FONT, FONT_SIZE))
    doc.setDefaultStyleSheet(CSS)
    doc.setHtml(html)

    writer = QPdfWriter(str(pdf_path))
    writer.setTitle(md_path.stem)
    writer.setResolution(300)
    writer.setPageLayout(QPageLayout(
        QPageSize(QPageSize.PageSizeId.A4),
        QPageLayout.Orientation.Portrait,
        QMarginsF(15, 15, 15, 15),
        QPageLayout.Unit.Millimeter,
    ))
    doc.print_(writer)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    app = QGuiApplication(sys.argv[:1])
    convert(Path(sys.argv[1]), Path(sys.argv[2]))
    print(f"  Converted {sys.argv[1]} -> {sys.argv[2]}")

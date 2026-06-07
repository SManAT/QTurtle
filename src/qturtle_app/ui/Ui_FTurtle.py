# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_FTurtle.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenu,
    QMenuBar, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSplitter, QStatusBar, QVBoxLayout,
    QWidget)

from qturtle_app.editor import CodeEditor

class Ui_FTurtleWindow(object):
    def setupUi(self, FTurtleWindow):
        if not FTurtleWindow.objectName():
            FTurtleWindow.setObjectName(u"FTurtleWindow")
        FTurtleWindow.resize(678, 427)
        self.actionNew = QAction(FTurtleWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(FTurtleWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(FTurtleWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_As = QAction(FTurtleWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionExit = QAction(FTurtleWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionCut = QAction(FTurtleWindow)
        self.actionCut.setObjectName(u"actionCut")
        self.actionCopy = QAction(FTurtleWindow)
        self.actionCopy.setObjectName(u"actionCopy")
        self.actionPaste = QAction(FTurtleWindow)
        self.actionPaste.setObjectName(u"actionPaste")
        self.actionSelect_All = QAction(FTurtleWindow)
        self.actionSelect_All.setObjectName(u"actionSelect_All")
        self.actionRun = QAction(FTurtleWindow)
        self.actionRun.setObjectName(u"actionRun")
        self.actionStop = QAction(FTurtleWindow)
        self.actionStop.setObjectName(u"actionStop")
        self.centralwidget = QWidget(FTurtleWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.btnRun = QPushButton(self.centralwidget)
        self.btnRun.setObjectName(u"btnRun")
        self.btnRun.setStyleSheet(u"background:\n"
"    QLinearGradient( spread:pad, x1: 0, y1: 0,\n"
"                     x2: 0, y2: 1,\n"
"                     stop: 0 #f0ff35,\n"
"                     stop: 1 #a9ff00\n"
"    ),\n"
"    QRadialGradient( cx: 0.5, cy: -0.4, radius: 2.0,\n"
"                     stop: 0 #b8ee36,\n"
"                     stop: 0.45 #b8ee36,\n"
"                     stop: 0.5 #80c800,\n"
"                     stop: 1 #80c800\n"
"    );\n"
"background-radius: 6, 5;\n"
"background-insets: 0, 1;\n"
"text-fill: #395306;\n"
"")

        self.horizontalLayout.addWidget(self.btnRun)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.openMainButton = QPushButton(self.centralwidget)
        self.openMainButton.setObjectName(u"openMainButton")
        self.openMainButton.setStyleSheet(u"background:\n"
"    QLinearGradient( spread:pad, x1: 0, y1: 0,\n"
"                     x2: 0, y2: 1,\n"
"                     stop: 0 #f0ff35,\n"
"                     stop: 1 #a9ff00\n"
"    ),\n"
"    QRadialGradient( cx: 0.5, cy: -0.4, radius: 2.0,\n"
"                     stop: 0 #b8ee36,\n"
"                     stop: 0.45 #b8ee36,\n"
"                     stop: 0.5 #80c800,\n"
"                     stop: 1 #80c800\n"
"    );\n"
"background-radius: 6, 5;\n"
"background-insets: 0, 1;\n"
"text-fill: #395306;\n"
"")

        self.horizontalLayout.addWidget(self.openMainButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.splitter.setChildrenCollapsible(False)
        self.codeEditor = CodeEditor(self.splitter)
        self.codeEditor.setObjectName(u"codeEditor")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.codeEditor.sizePolicy().hasHeightForWidth())
        self.codeEditor.setSizePolicy(sizePolicy)
        self.splitter.addWidget(self.codeEditor)
        self.consoleOutput = QPlainTextEdit(self.splitter)
        self.consoleOutput.setObjectName(u"consoleOutput")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.consoleOutput.sizePolicy().hasHeightForWidth())
        self.consoleOutput.setSizePolicy(sizePolicy1)
        self.consoleOutput.setReadOnly(True)
        self.splitter.addWidget(self.consoleOutput)

        self.verticalLayout.addWidget(self.splitter)

        FTurtleWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(FTurtleWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 678, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuRun = QMenu(self.menubar)
        self.menuRun.setObjectName(u"menuRun")
        FTurtleWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(FTurtleWindow)
        self.statusbar.setObjectName(u"statusbar")
        FTurtleWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSelect_All)
        self.menuRun.addAction(self.actionRun)
        self.menuRun.addAction(self.actionStop)

        self.retranslateUi(FTurtleWindow)

        QMetaObject.connectSlotsByName(FTurtleWindow)
    # setupUi

    def retranslateUi(self, FTurtleWindow):
        FTurtleWindow.setWindowTitle(QCoreApplication.translate("FTurtleWindow", u"QTurtle", None))
        self.actionNew.setText(QCoreApplication.translate("FTurtleWindow", u"&Neu", None))
#if QT_CONFIG(shortcut)
        self.actionNew.setShortcut(QCoreApplication.translate("FTurtleWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpen.setText(QCoreApplication.translate("FTurtleWindow", u"&\u00d6ffnen", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("FTurtleWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("FTurtleWindow", u"&Save", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("FTurtleWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave_As.setText(QCoreApplication.translate("FTurtleWindow", u"Save &As", None))
#if QT_CONFIG(shortcut)
        self.actionSave_As.setShortcut(QCoreApplication.translate("FTurtleWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionExit.setText(QCoreApplication.translate("FTurtleWindow", u"E&xit", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("FTurtleWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionCut.setText(QCoreApplication.translate("FTurtleWindow", u"Ausschneiden", None))
#if QT_CONFIG(shortcut)
        self.actionCut.setShortcut(QCoreApplication.translate("FTurtleWindow", u"Ctrl+X", None))
#endif // QT_CONFIG(shortcut)
        self.actionCopy.setText(QCoreApplication.translate("FTurtleWindow", u"Kopieren", None))
#if QT_CONFIG(shortcut)
        self.actionCopy.setShortcut(QCoreApplication.translate("FTurtleWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionPaste.setText(QCoreApplication.translate("FTurtleWindow", u"Einf\u00fcgen", None))
#if QT_CONFIG(shortcut)
        self.actionPaste.setShortcut(QCoreApplication.translate("FTurtleWindow", u"Ctrl+V", None))
#endif // QT_CONFIG(shortcut)
        self.actionSelect_All.setText(QCoreApplication.translate("FTurtleWindow", u"Select &All", None))
#if QT_CONFIG(shortcut)
        self.actionSelect_All.setShortcut(QCoreApplication.translate("FTurtleWindow", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.actionRun.setText(QCoreApplication.translate("FTurtleWindow", u"&Run Script", None))
#if QT_CONFIG(shortcut)
        self.actionRun.setShortcut(QCoreApplication.translate("FTurtleWindow", u"F5", None))
#endif // QT_CONFIG(shortcut)
        self.actionStop.setText(QCoreApplication.translate("FTurtleWindow", u"&Stop", None))
#if QT_CONFIG(shortcut)
        self.actionStop.setShortcut(QCoreApplication.translate("FTurtleWindow", u"Ctrl+F2", None))
#endif // QT_CONFIG(shortcut)
        self.btnRun.setText(QCoreApplication.translate("FTurtleWindow", u"Run Script", None))
        self.openMainButton.setText(QCoreApplication.translate("FTurtleWindow", u"Open Turtle", None))
        self.consoleOutput.setPlaceholderText(QCoreApplication.translate("FTurtleWindow", u"Console output...", None))
        self.menuFile.setTitle(QCoreApplication.translate("FTurtleWindow", u"&Datei", None))
        self.menuEdit.setTitle(QCoreApplication.translate("FTurtleWindow", u"&Bearbeiten", None))
        self.menuRun.setTitle(QCoreApplication.translate("FTurtleWindow", u"&Run", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_MainWindow.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(678, 427)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionCut = QAction(MainWindow)
        self.actionCut.setObjectName(u"actionCut")
        self.actionCopy = QAction(MainWindow)
        self.actionCopy.setObjectName(u"actionCopy")
        self.actionPaste = QAction(MainWindow)
        self.actionPaste.setObjectName(u"actionPaste")
        self.actionSelect_All = QAction(MainWindow)
        self.actionSelect_All.setObjectName(u"actionSelect_All")
        self.actionRun = QAction(MainWindow)
        self.actionRun.setObjectName(u"actionRun")
        self.actionStop = QAction(MainWindow)
        self.actionStop.setObjectName(u"actionStop")
        self.centralwidget = QWidget(MainWindow)
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
        self.btnRun.setStyleSheet(u"background: rgba(0,0,0,0.08),\n"
"           QLinearGradient(spread:pad, x1:0, y1:0, x2:0, y2:1,\n"
"                          stop:0 #9a9a9a, stop:1 #909090),\n"
"           QLinearGradient(spread:pad, x1:0, y1:0, x2:0, y2:1,\n"
"                          stop:0 white, stop:0.5 #f3f3f3,\n"
"                          stop:0.51 #ececec, stop:1 #f2f2f2);\n"
"background-insets: 0,0,1;\n"
"background-radius: 5,5,4;\n"
"padding: 3 30 3 30;\n"
"color: #242d35;\n"
"font-size: 12px;")

        self.horizontalLayout.addWidget(self.btnRun)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.openFTurtleButton = QPushButton(self.centralwidget)
        self.openFTurtleButton.setObjectName(u"openFTurtleButton")
        self.openFTurtleButton.setStyleSheet(u"background: rgba(0,0,0,0.08),\n"
"           QLinearGradient(spread:pad, x1:0, y1:0, x2:0, y2:1,\n"
"                          stop:0 #9a9a9a, stop:1 #909090),\n"
"           QLinearGradient(spread:pad, x1:0, y1:0, x2:0, y2:1,\n"
"                          stop:0 white, stop:0.5 #f3f3f3,\n"
"                          stop:0.51 #ececec, stop:1 #f2f2f2);\n"
"background-insets: 0,0,1;\n"
"background-radius: 5,5,4;\n"
"padding: 3 30 3 30;\n"
"color: #242d35;\n"
"font-size: 12px;")

        self.horizontalLayout.addWidget(self.openFTurtleButton)


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

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 678, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuRun = QMenu(self.menubar)
        self.menuRun.setObjectName(u"menuRun")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

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

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"QTurtle", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"&Neu", None))
#if QT_CONFIG(shortcut)
        self.actionNew.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"&\u00d6ffnen", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"&Save", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave_As.setText(QCoreApplication.translate("MainWindow", u"Save &As", None))
#if QT_CONFIG(shortcut)
        self.actionSave_As.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"E&xit", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionCut.setText(QCoreApplication.translate("MainWindow", u"Ausschneiden", None))
#if QT_CONFIG(shortcut)
        self.actionCut.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+X", None))
#endif // QT_CONFIG(shortcut)
        self.actionCopy.setText(QCoreApplication.translate("MainWindow", u"Kopieren", None))
#if QT_CONFIG(shortcut)
        self.actionCopy.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionPaste.setText(QCoreApplication.translate("MainWindow", u"Einf\u00fcgen", None))
#if QT_CONFIG(shortcut)
        self.actionPaste.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+V", None))
#endif // QT_CONFIG(shortcut)
        self.actionSelect_All.setText(QCoreApplication.translate("MainWindow", u"Select &All", None))
#if QT_CONFIG(shortcut)
        self.actionSelect_All.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.actionRun.setText(QCoreApplication.translate("MainWindow", u"&Run Script", None))
#if QT_CONFIG(shortcut)
        self.actionRun.setShortcut(QCoreApplication.translate("MainWindow", u"F5", None))
#endif // QT_CONFIG(shortcut)
        self.actionStop.setText(QCoreApplication.translate("MainWindow", u"&Stop", None))
#if QT_CONFIG(shortcut)
        self.actionStop.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+F2", None))
#endif // QT_CONFIG(shortcut)
        self.btnRun.setText(QCoreApplication.translate("MainWindow", u"Run Script", None))
        self.openFTurtleButton.setText(QCoreApplication.translate("MainWindow", u"Open FTurtle", None))
        self.consoleOutput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Console output...", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"&Datei", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"&Bearbeiten", None))
        self.menuRun.setTitle(QCoreApplication.translate("MainWindow", u"&Run", None))
    # retranslateUi


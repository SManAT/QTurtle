# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_LTurtle.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QSplitter,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_LTurtleWindow(object):
    def setupUi(self, LTurtleWindow):
        if not LTurtleWindow.objectName():
            LTurtleWindow.setObjectName(u"LTurtleWindow")
        LTurtleWindow.resize(700, 577)
        self.actionNew = QAction(LTurtleWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(LTurtleWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(LTurtleWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_As = QAction(LTurtleWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionExit = QAction(LTurtleWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionCut = QAction(LTurtleWindow)
        self.actionCut.setObjectName(u"actionCut")
        self.actionCopy = QAction(LTurtleWindow)
        self.actionCopy.setObjectName(u"actionCopy")
        self.actionPaste = QAction(LTurtleWindow)
        self.actionPaste.setObjectName(u"actionPaste")
        self.actionSelect_All = QAction(LTurtleWindow)
        self.actionSelect_All.setObjectName(u"actionSelect_All")
        self.actionRun = QAction(LTurtleWindow)
        self.actionRun.setObjectName(u"actionRun")
        self.actionStop = QAction(LTurtleWindow)
        self.actionStop.setObjectName(u"actionStop")
        self.centralwidget = QWidget(LTurtleWindow)
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
"padding: 3 30 3 30;\n"
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
"padding: 3 30 3 30;\n"
"")

        self.horizontalLayout.addWidget(self.openMainButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.mainSplitter = QSplitter(self.centralwidget)
        self.mainSplitter.setObjectName(u"mainSplitter")
        self.mainSplitter.setOrientation(Qt.Orientation.Vertical)
        self.mainSplitter.setHandleWidth(1)
        self.topSplitter = QSplitter(self.mainSplitter)
        self.topSplitter.setObjectName(u"topSplitter")
        self.topSplitter.setOrientation(Qt.Orientation.Horizontal)
        self.topSplitter.setHandleWidth(1)
        self.topSplitter.setChildrenCollapsible(False)
        self.widget = QWidget(self.topSplitter)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.LSystemForm = QGroupBox(self.widget)
        self.LSystemForm.setObjectName(u"LSystemForm")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.LSystemForm.sizePolicy().hasHeightForWidth())
        self.LSystemForm.setSizePolicy(sizePolicy)
        self.LSystemForm.setStyleSheet(u"font-size:11pt;")
        self.LSystemForm.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.formLayout = QFormLayout(self.LSystemForm)
        self.formLayout.setObjectName(u"formLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.label_rule_d = QLabel(self.LSystemForm)
        self.label_rule_d.setObjectName(u"label_rule_d")

        self.gridLayout.addWidget(self.label_rule_d, 8, 0, 1, 1)

        self.ruleA = QLineEdit(self.LSystemForm)
        self.ruleA.setObjectName(u"ruleA")

        self.gridLayout.addWidget(self.ruleA, 5, 1, 1, 1)

        self.ruleF = QLineEdit(self.LSystemForm)
        self.ruleF.setObjectName(u"ruleF")

        self.gridLayout.addWidget(self.ruleF, 10, 1, 1, 1)

        self.axiom = QLineEdit(self.LSystemForm)
        self.axiom.setObjectName(u"axiom")

        self.gridLayout.addWidget(self.axiom, 0, 1, 1, 1)

        self.ruleE = QLineEdit(self.LSystemForm)
        self.ruleE.setObjectName(u"ruleE")

        self.gridLayout.addWidget(self.ruleE, 9, 1, 1, 1)

        self.label_rule_c = QLabel(self.LSystemForm)
        self.label_rule_c.setObjectName(u"label_rule_c")

        self.gridLayout.addWidget(self.label_rule_c, 7, 0, 1, 1)

        self.iterationen = QSpinBox(self.LSystemForm)
        self.iterationen.setObjectName(u"iterationen")
        self.iterationen.setMinimum(2)
        self.iterationen.setMaximum(100)
        self.iterationen.setValue(5)

        self.gridLayout.addWidget(self.iterationen, 2, 1, 1, 1)

        self.ruleB = QLineEdit(self.LSystemForm)
        self.ruleB.setObjectName(u"ruleB")

        self.gridLayout.addWidget(self.ruleB, 6, 1, 1, 1)

        self.label_rule_e = QLabel(self.LSystemForm)
        self.label_rule_e.setObjectName(u"label_rule_e")

        self.gridLayout.addWidget(self.label_rule_e, 9, 0, 1, 1)

        self.label = QLabel(self.LSystemForm)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_length = QLabel(self.LSystemForm)
        self.label_length.setObjectName(u"label_length")

        self.gridLayout.addWidget(self.label_length, 3, 0, 1, 1)

        self.label_rule_a = QLabel(self.LSystemForm)
        self.label_rule_a.setObjectName(u"label_rule_a")

        self.gridLayout.addWidget(self.label_rule_a, 5, 0, 1, 1)

        self.label_iterations = QLabel(self.LSystemForm)
        self.label_iterations.setObjectName(u"label_iterations")

        self.gridLayout.addWidget(self.label_iterations, 2, 0, 1, 1)

        self.winkel = QSpinBox(self.LSystemForm)
        self.winkel.setObjectName(u"winkel")
        self.winkel.setMinimum(0)
        self.winkel.setMaximum(359)
        self.winkel.setValue(90)

        self.gridLayout.addWidget(self.winkel, 1, 1, 1, 1)

        self.label_angle = QLabel(self.LSystemForm)
        self.label_angle.setObjectName(u"label_angle")

        self.gridLayout.addWidget(self.label_angle, 1, 0, 1, 1)

        self.ruleC = QLineEdit(self.LSystemForm)
        self.ruleC.setObjectName(u"ruleC")

        self.gridLayout.addWidget(self.ruleC, 7, 1, 1, 1)

        self.label_rule_f = QLabel(self.LSystemForm)
        self.label_rule_f.setObjectName(u"label_rule_f")

        self.gridLayout.addWidget(self.label_rule_f, 10, 0, 1, 1)

        self.label_rules_header = QLabel(self.LSystemForm)
        self.label_rules_header.setObjectName(u"label_rules_header")

        self.gridLayout.addWidget(self.label_rules_header, 4, 0, 1, 2)

        self.ruleD = QLineEdit(self.LSystemForm)
        self.ruleD.setObjectName(u"ruleD")

        self.gridLayout.addWidget(self.ruleD, 8, 1, 1, 1)

        self.label_rule_b = QLabel(self.LSystemForm)
        self.label_rule_b.setObjectName(u"label_rule_b")

        self.gridLayout.addWidget(self.label_rule_b, 6, 0, 1, 1)

        self.laenge = QSpinBox(self.LSystemForm)
        self.laenge.setObjectName(u"laenge")
        self.laenge.setMaximum(500)
        self.laenge.setValue(100)

        self.gridLayout.addWidget(self.laenge, 3, 1, 1, 1)


        self.formLayout.setLayout(0, QFormLayout.ItemRole.SpanningRole, self.gridLayout)


        self.gridLayout_2.addWidget(self.LSystemForm, 0, 0, 1, 1)

        self.topSplitter.addWidget(self.widget)
        self.widget21 = QWidget(self.topSplitter)
        self.widget21.setObjectName(u"widget21")
        self.verticalLayout_2 = QVBoxLayout(self.widget21)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 18, -1, -1)
        self.codeEditor = QPlainTextEdit(self.widget21)
        self.codeEditor.setObjectName(u"codeEditor")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.codeEditor.sizePolicy().hasHeightForWidth())
        self.codeEditor.setSizePolicy(sizePolicy1)
        self.codeEditor.setStyleSheet(u"background:#ffffff; font-size:12pt;")

        self.verticalLayout_2.addWidget(self.codeEditor)

        self.topSplitter.addWidget(self.widget21)
        self.mainSplitter.addWidget(self.topSplitter)
        self.widget22 = QWidget(self.mainSplitter)
        self.widget22.setObjectName(u"widget22")
        self.horizontalLayout_2 = QHBoxLayout(self.widget22)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.consoleOutput = QPlainTextEdit(self.widget22)
        self.consoleOutput.setObjectName(u"consoleOutput")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.consoleOutput.sizePolicy().hasHeightForWidth())
        self.consoleOutput.setSizePolicy(sizePolicy2)
        self.consoleOutput.setAcceptDrops(False)
        self.consoleOutput.setStyleSheet(u"background:#ffffff;")
        self.consoleOutput.setUndoRedoEnabled(False)
        self.consoleOutput.setReadOnly(False)

        self.horizontalLayout_2.addWidget(self.consoleOutput)

        self.mainSplitter.addWidget(self.widget22)

        self.verticalLayout.addWidget(self.mainSplitter)

        LTurtleWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(LTurtleWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 700, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuRun = QMenu(self.menubar)
        self.menuRun.setObjectName(u"menuRun")
        LTurtleWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(LTurtleWindow)
        self.statusbar.setObjectName(u"statusbar")
        LTurtleWindow.setStatusBar(self.statusbar)

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

        self.retranslateUi(LTurtleWindow)

        QMetaObject.connectSlotsByName(LTurtleWindow)
    # setupUi

    def retranslateUi(self, LTurtleWindow):
        LTurtleWindow.setWindowTitle(QCoreApplication.translate("LTurtleWindow", u"QLTurtle", None))
        self.actionNew.setText(QCoreApplication.translate("LTurtleWindow", u"&Neu", None))
#if QT_CONFIG(shortcut)
        self.actionNew.setShortcut(QCoreApplication.translate("LTurtleWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpen.setText(QCoreApplication.translate("LTurtleWindow", u"&\u00d6ffnen", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("LTurtleWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("LTurtleWindow", u"&Save", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("LTurtleWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave_As.setText(QCoreApplication.translate("LTurtleWindow", u"Save &As", None))
#if QT_CONFIG(shortcut)
        self.actionSave_As.setShortcut(QCoreApplication.translate("LTurtleWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionExit.setText(QCoreApplication.translate("LTurtleWindow", u"E&xit", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("LTurtleWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionCut.setText(QCoreApplication.translate("LTurtleWindow", u"Ausschneiden", None))
#if QT_CONFIG(shortcut)
        self.actionCut.setShortcut(QCoreApplication.translate("LTurtleWindow", u"Ctrl+X", None))
#endif // QT_CONFIG(shortcut)
        self.actionCopy.setText(QCoreApplication.translate("LTurtleWindow", u"Kopieren", None))
#if QT_CONFIG(shortcut)
        self.actionCopy.setShortcut(QCoreApplication.translate("LTurtleWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionPaste.setText(QCoreApplication.translate("LTurtleWindow", u"Einf\u00fcgen", None))
#if QT_CONFIG(shortcut)
        self.actionPaste.setShortcut(QCoreApplication.translate("LTurtleWindow", u"Ctrl+V", None))
#endif // QT_CONFIG(shortcut)
        self.actionSelect_All.setText(QCoreApplication.translate("LTurtleWindow", u"Select &All", None))
#if QT_CONFIG(shortcut)
        self.actionSelect_All.setShortcut(QCoreApplication.translate("LTurtleWindow", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.actionRun.setText(QCoreApplication.translate("LTurtleWindow", u"&Run Script", None))
#if QT_CONFIG(shortcut)
        self.actionRun.setShortcut(QCoreApplication.translate("LTurtleWindow", u"F5", None))
#endif // QT_CONFIG(shortcut)
        self.actionStop.setText(QCoreApplication.translate("LTurtleWindow", u"&Stop", None))
#if QT_CONFIG(shortcut)
        self.actionStop.setShortcut(QCoreApplication.translate("LTurtleWindow", u"Ctrl+F2", None))
#endif // QT_CONFIG(shortcut)
        self.btnRun.setText(QCoreApplication.translate("LTurtleWindow", u"Run Script", None))
        self.openMainButton.setText(QCoreApplication.translate("LTurtleWindow", u"Open Turtle", None))
        self.LSystemForm.setTitle(QCoreApplication.translate("LTurtleWindow", u"Lindenmayer System", None))
        self.label_rule_d.setText(QCoreApplication.translate("LTurtleWindow", u"Rule D:", None))
        self.ruleA.setText(QCoreApplication.translate("LTurtleWindow", u"X > X+YF+", None))
        self.ruleA.setPlaceholderText(QCoreApplication.translate("LTurtleWindow", u"e.g., A", None))
        self.ruleF.setPlaceholderText("")
        self.axiom.setText(QCoreApplication.translate("LTurtleWindow", u"X", None))
        self.ruleE.setPlaceholderText("")
        self.label_rule_c.setText(QCoreApplication.translate("LTurtleWindow", u"Rule C:", None))
        self.ruleB.setText(QCoreApplication.translate("LTurtleWindow", u"Y > -FX-Y", None))
        self.ruleB.setPlaceholderText(QCoreApplication.translate("LTurtleWindow", u"e.g., B", None))
        self.label_rule_e.setText(QCoreApplication.translate("LTurtleWindow", u"Rule E:", None))
        self.label.setText(QCoreApplication.translate("LTurtleWindow", u"Axiom:", None))
        self.label_length.setText(QCoreApplication.translate("LTurtleWindow", u"Linienl\u00e4nge:", None))
        self.label_rule_a.setText(QCoreApplication.translate("LTurtleWindow", u"Rule A:", None))
        self.label_iterations.setText(QCoreApplication.translate("LTurtleWindow", u"Iterationen:", None))
        self.label_angle.setText(QCoreApplication.translate("LTurtleWindow", u"Winkel (\u00b0):", None))
        self.ruleC.setPlaceholderText("")
        self.label_rule_f.setText(QCoreApplication.translate("LTurtleWindow", u"Rule F:", None))
        self.label_rules_header.setText(QCoreApplication.translate("LTurtleWindow", u"Regeln: muss > beinhalten", None))
        self.ruleD.setPlaceholderText("")
        self.label_rule_b.setText(QCoreApplication.translate("LTurtleWindow", u"Rule B:", None))
        self.codeEditor.setPlainText("")
        self.codeEditor.setPlaceholderText(QCoreApplication.translate("LTurtleWindow", u"Final code shows up here ...", None))
        self.consoleOutput.setPlaceholderText(QCoreApplication.translate("LTurtleWindow", u"Console output...", None))
        self.menuFile.setTitle(QCoreApplication.translate("LTurtleWindow", u"&Datei", None))
        self.menuEdit.setTitle(QCoreApplication.translate("LTurtleWindow", u"&Bearbeiten", None))
        self.menuRun.setTitle(QCoreApplication.translate("LTurtleWindow", u"&Run", None))
    # retranslateUi


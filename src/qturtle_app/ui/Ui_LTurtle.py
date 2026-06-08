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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFormLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QSplitter,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_LTurtleWindow(object):
    def setupUi(self, LTurtleWindow):
        if not LTurtleWindow.objectName():
            LTurtleWindow.setObjectName(u"LTurtleWindow")
        LTurtleWindow.resize(678, 562)
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

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.splitter.setChildrenCollapsible(False)
        self.LSystemForm = QGroupBox(self.splitter)
        self.LSystemForm.setObjectName(u"LSystemForm")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.LSystemForm.sizePolicy().hasHeightForWidth())
        self.LSystemForm.setSizePolicy(sizePolicy)
        self.LSystemForm.setStyleSheet(u"font-size:11pt;")
        self.formLayout = QFormLayout(self.LSystemForm)
        self.formLayout.setObjectName(u"formLayout")
        self.winkel = QSpinBox(self.LSystemForm)
        self.winkel.setObjectName(u"winkel")
        self.winkel.setMinimum(0)
        self.winkel.setMaximum(359)
        self.winkel.setValue(90)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.winkel)

        self.label_iterations = QLabel(self.LSystemForm)
        self.label_iterations.setObjectName(u"label_iterations")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_iterations)

        self.iterationen = QSpinBox(self.LSystemForm)
        self.iterationen.setObjectName(u"iterationen")
        self.iterationen.setMinimum(2)
        self.iterationen.setMaximum(10)
        self.iterationen.setValue(2)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.iterationen)

        self.label_length = QLabel(self.LSystemForm)
        self.label_length.setObjectName(u"label_length")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_length)

        self.laenge = QDoubleSpinBox(self.LSystemForm)
        self.laenge.setObjectName(u"laenge")
        self.laenge.setDecimals(0)
        self.laenge.setMinimum(0.000000000000000)
        self.laenge.setMaximum(1000.000000000000000)
        self.laenge.setValue(10.000000000000000)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.laenge)

        self.label_rules_header = QLabel(self.LSystemForm)
        self.label_rules_header.setObjectName(u"label_rules_header")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.SpanningRole, self.label_rules_header)

        self.label_rule_a = QLabel(self.LSystemForm)
        self.label_rule_a.setObjectName(u"label_rule_a")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_rule_a)

        self.ruleA = QLineEdit(self.LSystemForm)
        self.ruleA.setObjectName(u"ruleA")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.ruleA)

        self.label_rule_b = QLabel(self.LSystemForm)
        self.label_rule_b.setObjectName(u"label_rule_b")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_rule_b)

        self.ruleB = QLineEdit(self.LSystemForm)
        self.ruleB.setObjectName(u"ruleB")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.ruleB)

        self.label_rule_c = QLabel(self.LSystemForm)
        self.label_rule_c.setObjectName(u"label_rule_c")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.label_rule_c)

        self.ruleC = QLineEdit(self.LSystemForm)
        self.ruleC.setObjectName(u"ruleC")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.ruleC)

        self.label_rule_d = QLabel(self.LSystemForm)
        self.label_rule_d.setObjectName(u"label_rule_d")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.label_rule_d)

        self.ruleD = QLineEdit(self.LSystemForm)
        self.ruleD.setObjectName(u"ruleD")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.ruleD)

        self.label_rule_e = QLabel(self.LSystemForm)
        self.label_rule_e.setObjectName(u"label_rule_e")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.LabelRole, self.label_rule_e)

        self.ruleE = QLineEdit(self.LSystemForm)
        self.ruleE.setObjectName(u"ruleE")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.FieldRole, self.ruleE)

        self.label_rule_f = QLabel(self.LSystemForm)
        self.label_rule_f.setObjectName(u"label_rule_f")

        self.formLayout.setWidget(10, QFormLayout.ItemRole.LabelRole, self.label_rule_f)

        self.ruleF = QLineEdit(self.LSystemForm)
        self.ruleF.setObjectName(u"ruleF")

        self.formLayout.setWidget(10, QFormLayout.ItemRole.FieldRole, self.ruleF)

        self.label_legend = QLabel(self.LSystemForm)
        self.label_legend.setObjectName(u"label_legend")
        self.label_legend.setWordWrap(True)

        self.formLayout.setWidget(11, QFormLayout.ItemRole.SpanningRole, self.label_legend)

        self.label_angle = QLabel(self.LSystemForm)
        self.label_angle.setObjectName(u"label_angle")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_angle)

        self.label = QLabel(self.LSystemForm)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.axiom = QLineEdit(self.LSystemForm)
        self.axiom.setObjectName(u"axiom")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.axiom)

        self.splitter.addWidget(self.LSystemForm)
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

        LTurtleWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(LTurtleWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 678, 33))
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
        self.label_iterations.setText(QCoreApplication.translate("LTurtleWindow", u"Iterationen:", None))
        self.label_length.setText(QCoreApplication.translate("LTurtleWindow", u"Linienl\u00e4nge:", None))
        self.label_rules_header.setText(QCoreApplication.translate("LTurtleWindow", u"Regeln: muss > beinhalten", None))
        self.label_rule_a.setText(QCoreApplication.translate("LTurtleWindow", u"Rule A:", None))
        self.ruleA.setText(QCoreApplication.translate("LTurtleWindow", u"X > X+YF+", None))
        self.ruleA.setPlaceholderText(QCoreApplication.translate("LTurtleWindow", u"e.g., A", None))
        self.label_rule_b.setText(QCoreApplication.translate("LTurtleWindow", u"Rule B:", None))
        self.ruleB.setText(QCoreApplication.translate("LTurtleWindow", u"Y > -FX-Y", None))
        self.ruleB.setPlaceholderText(QCoreApplication.translate("LTurtleWindow", u"e.g., B", None))
        self.label_rule_c.setText(QCoreApplication.translate("LTurtleWindow", u"Rule C:", None))
        self.ruleC.setPlaceholderText("")
        self.label_rule_d.setText(QCoreApplication.translate("LTurtleWindow", u"Rule D:", None))
        self.ruleD.setPlaceholderText("")
        self.label_rule_e.setText(QCoreApplication.translate("LTurtleWindow", u"Rule E:", None))
        self.ruleE.setPlaceholderText("")
        self.label_rule_f.setText(QCoreApplication.translate("LTurtleWindow", u"Rule F:", None))
        self.ruleF.setPlaceholderText("")
        self.label_legend.setStyleSheet(QCoreApplication.translate("LTurtleWindow", u"color: gray;", None))
        self.label_legend.setText(QCoreApplication.translate("LTurtleWindow", u"Legende:  + = Winkel\u00b0   - = -Winkel\u00b0   [ = push   ] = pop   F = forward", None))
        self.label_angle.setText(QCoreApplication.translate("LTurtleWindow", u"Winkel (\u00b0):", None))
        self.label.setText(QCoreApplication.translate("LTurtleWindow", u"Axiom:", None))
        self.axiom.setText(QCoreApplication.translate("LTurtleWindow", u"X", None))
        self.consoleOutput.setPlaceholderText(QCoreApplication.translate("LTurtleWindow", u"Console output...", None))
        self.menuFile.setTitle(QCoreApplication.translate("LTurtleWindow", u"&Datei", None))
        self.menuEdit.setTitle(QCoreApplication.translate("LTurtleWindow", u"&Bearbeiten", None))
        self.menuRun.setTitle(QCoreApplication.translate("LTurtleWindow", u"&Run", None))
    # retranslateUi


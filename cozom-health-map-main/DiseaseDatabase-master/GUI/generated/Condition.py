# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ConditionPage(object):
    def setupUi(self, ConditionPage):
        ConditionPage.setObjectName("ConditionPage")
        ConditionPage.resize(720, 360)
        self.centralWidget = QtWidgets.QWidget(ConditionPage)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.header.setFont(font)
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")
        self.verticalLayout.addWidget(self.header)
        self.conditionText = QtWidgets.QTextBrowser(self.centralWidget)
        self.conditionText.setObjectName("conditionText")
        self.verticalLayout.addWidget(self.conditionText)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.ok_button = QtWidgets.QPushButton(self.centralWidget)
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout.addWidget(self.ok_button)
        self.horizontalLayout.setStretch(0, 8)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 8)
        self.verticalLayout.setStretch(2, 1)
        self.header.raise_()
        self.conditionText.raise_()
        ConditionPage.setCentralWidget(self.centralWidget)

        self.retranslateUi(ConditionPage)
        QtCore.QMetaObject.connectSlotsByName(ConditionPage)

    def retranslateUi(self, ConditionPage):
        _translate = QtCore.QCoreApplication.translate
        ConditionPage.setWindowTitle(_translate("ConditionPage", "Condition Details - Cozom"))
        self.header.setText(_translate("ConditionPage", "Condition Details"))
        self.conditionText.setHtml(_translate("ConditionPage", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">
<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">
p, li { white-space: pre-wrap; }
</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Below are the details for the condition you selected, including the condition name, occurrence, and additional information.</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This information is provided by Cozom to assist you in understanding potential health conditions. Please consult with a licensed healthcare provider for any medical advice or diagnosis.</p></body></html>"))
        self.ok_button.setText(_translate("ConditionPage", "OK"))

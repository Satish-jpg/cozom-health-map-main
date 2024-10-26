# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AboutPage(object):
    def setupUi(self, AboutPage):
        AboutPage.setObjectName("AboutPage")
        AboutPage.resize(720, 360)
        self.centralWidget = QtWidgets.QWidget(AboutPage)
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
        self.licenseText = QtWidgets.QTextBrowser(self.centralWidget)
        self.licenseText.setObjectName("licenseText")
        self.verticalLayout.addWidget(self.licenseText)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.agree_button = QtWidgets.QPushButton(self.centralWidget)
        self.agree_button.setObjectName("agree_button")
        self.horizontalLayout.addWidget(self.agree_button)
        self.disagree_button = QtWidgets.QPushButton(self.centralWidget)
        self.disagree_button.setObjectName("disagree_button")
        self.horizontalLayout.addWidget(self.disagree_button)
        self.horizontalLayout.setStretch(0, 8)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 8)
        self.verticalLayout.setStretch(2, 1)
        self.header.raise_()
        self.licenseText.raise_()
        AboutPage.setCentralWidget(self.centralWidget)

        self.retranslateUi(AboutPage)
        QtCore.QMetaObject.connectSlotsByName(AboutPage)

    def retranslateUi(self, AboutPage):
        _translate = QtCore.QCoreApplication.translate
        AboutPage.setWindowTitle(_translate("AboutPage", "Cozom - About"))
        self.header.setText(_translate("AboutPage", "Cozom"))
        self.licenseText.setHtml(_translate("AboutPage", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Cozom is a health tech platform coded to help users identify symptoms and find specialist doctors. It uses the PyQt5 library for the graphical user interface, and requests library to retrieve data. All of the data used by this program is proprietary to Cozom. Usage of this data for commercial purposes; is permitted only with explicit permission from Cozom. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This software is intended to assist users in making informed decisions, but it is not a substitute for professional medical advice. Please consult with a licensed healthcare provider before making any decisions about your health. By using this software, you agree to these terms and conditions.</p></body></html>"))
        self.agree_button.setText(_translate("AboutPage", "I agree"))
        self.disagree_button.setText(_translate("AboutPage", "I disagree"))

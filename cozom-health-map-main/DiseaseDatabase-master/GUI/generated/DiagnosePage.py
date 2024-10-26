# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diagnosepage.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DiagnosePage(object):
    def setupUi(self, DiagnosePage):
        DiagnosePage.setObjectName("DiagnosePage")
        DiagnosePage.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(DiagnosePage)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.body_part_combo = QtWidgets.QComboBox(self.centralwidget)
        self.body_part_combo.setObjectName("body_part_combo")
        self.verticalLayout.addWidget(self.body_part_combo)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.symptom_combo = QtWidgets.QComboBox(self.centralwidget)
        self.symptom_combo.setObjectName("symptom_combo")
        self.verticalLayout_2.addWidget(self.symptom_combo)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.add_symptom_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_symptom_button.setObjectName("add_symptom_button")
        self.horizontalLayout_2.addWidget(self.add_symptom_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.symptom_list_view = QtWidgets.QListWidget(self.centralwidget)
        self.symptom_list_view.setObjectName("symptom_list_view")
        self.verticalLayout_4.addWidget(self.symptom_list_view)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.condition_list_view = QtWidgets.QListWidget(self.centralwidget)
        self.condition_list_view.setObjectName("condition_list_view")
        self.verticalLayout_5.addWidget(self.condition_list_view)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.horizontalLayout_3.setStretch(0, 25)
        self.horizontalLayout_3.setStretch(1, 75)
        DiagnosePage.setCentralWidget(self.centralwidget)

        self.retranslateUi(DiagnosePage)
        QtCore.QMetaObject.connectSlotsByName(DiagnosePage)

    def retranslateUi(self, DiagnosePage):
        _translate = QtCore.QCoreApplication.translate
        DiagnosePage.setWindowTitle(_translate("DiagnosePage", "Cozom - Symptom Diagnosis"))
        self.label.setText(_translate("DiagnosePage", "Select Body Part"))
        self.label_2.setText(_translate("DiagnosePage", "Select Symptom"))
        self.add_symptom_button.setText(_translate("DiagnosePage", "Add Selected Symptom"))
        self.label_3.setText(_translate("DiagnosePage", "Diagnosis Results"))
        self.label_4.setText(_translate("DiagnosePage", "Here are the most relevant conditions based on the symptoms you have selected."))

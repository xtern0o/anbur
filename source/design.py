# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\design.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(678, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("padding: 2px;")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout_2.addWidget(self.plainTextEdit, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setStyleSheet("padding: 2px;")
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.gridLayout.addWidget(self.plainTextEdit_2, 1, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout.addLayout(self.gridLayout_3, 2, 0, 1, 2)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "fdsfdsf\n"
"dffdssdfdsfdfds fd sf dsf dsf"))

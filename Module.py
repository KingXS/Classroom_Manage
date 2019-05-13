# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Module.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Module(object):
    def setupUi(self, Module):
        Module.setObjectName("Module")
        Module.resize(1040, 646)
        Module.setStyleSheet("background-image: url(:D:/PyQt/2.png);")
        self.label = QtWidgets.QLabel(Module)
        self.label.setGeometry(QtCore.QRect(320, 10, 661, 131))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Module)
        self.pushButton.setGeometry(QtCore.QRect(370, 140, 341, 61))
        self.pushButton.setStyleSheet("color:rgb(0, 170, 255);\n"
"font: 26pt \"Agency FB\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Module)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 250, 341, 61))
        self.pushButton_2.setStyleSheet("color:rgb(0, 170, 255);\n"
"font: 26pt \"Agency FB\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Module)
        self.pushButton_3.setGeometry(QtCore.QRect(370, 360, 341, 61))
        self.pushButton_3.setStyleSheet("color:rgb(0, 170, 255);\n"
"font: 26pt \"Agency FB\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Module)
        self.pushButton_4.setGeometry(QtCore.QRect(370, 470, 341, 61))
        self.pushButton_4.setStyleSheet("color:rgb(0, 170, 255);\n"
"font: 26pt \"Agency FB\";")
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Module)
        QtCore.QMetaObject.connectSlotsByName(Module)

    def retranslateUi(self, Module):
        _translate = QtCore.QCoreApplication.translate
        Module.setWindowTitle(_translate("Module", "模块选择"))
        self.label.setText(_translate("Module", "<html><head/><body><p><span style=\" font-size:26pt; font-weight:600; color:#00aaff;\">请选择你要操作的模块</span></p></body></html>"))
        self.pushButton.setText(_translate("Module", "教室管理"))
        self.pushButton_2.setText(_translate("Module", "课程管理"))
        self.pushButton_3.setText(_translate("Module", "班级管理"))
        self.pushButton_4.setText(_translate("Module", "教师管理"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(1040, 646)
        Main.setStyleSheet("background-image: url(:D:/PyQt/2.png);")
        self.label = QtWidgets.QLabel(Main)
        self.label.setGeometry(QtCore.QRect(300, 50, 591, 131))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Main)
        self.label_2.setGeometry(QtCore.QRect(340, 290, 151, 71))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Main)
        self.label_3.setGeometry(QtCore.QRect(370, 390, 151, 71))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Main)
        self.lineEdit.setGeometry(QtCore.QRect(530, 310, 181, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Main)
        self.lineEdit_2.setGeometry(QtCore.QRect(530, 410, 181, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Main)
        self.pushButton.setGeometry(QtCore.QRect(400, 520, 281, 61))
        self.pushButton.setStyleSheet("color:rgb(0, 170, 255);\n"
"font: 26pt \"Agency FB\";")
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(Main)
        self.label_4.setGeometry(QtCore.QRect(370, 190, 371, 71))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "登录窗口"))
        self.label.setText(_translate("Main", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600; color:#00aaff;\">教室管理信息系统</span></p></body></html>"))
        self.label_2.setText(_translate("Main", "<html><head/><body><p><span style=\" font-size:18pt; color:#00aaff;\">用户名：</span></p></body></html>"))
        self.label_3.setText(_translate("Main", "<html><head/><body><p><span style=\" font-size:18pt; color:#00aaff;\">密码：</span></p></body></html>"))
        self.pushButton.setText(_translate("Main", "登录"))
        self.label_4.setText(_translate("Main", "<html><head/><body><p><span style=\" font-size:14pt; color:#00aaff;\">信息安全1501 3150604023 王宪章</span></p></body></html>"))


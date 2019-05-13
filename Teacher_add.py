# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Teacher_add.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Teacher_add(object):
    def setupUi(self, Teacher_add):
        Teacher_add.setObjectName("Teacher_add")
        Teacher_add.resize(1040, 646)
        Teacher_add.setStyleSheet("background-image: url(:D:/PyQt/2.png);")
        self.label = QtWidgets.QLabel(Teacher_add)
        self.label.setGeometry(QtCore.QRect(410, 0, 661, 131))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Teacher_add)
        self.label_2.setGeometry(QtCore.QRect(320, 140, 211, 51))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Teacher_add)
        self.lineEdit.setGeometry(QtCore.QRect(500, 140, 251, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Teacher_add)
        self.label_3.setGeometry(QtCore.QRect(300, 230, 211, 51))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Teacher_add)
        self.pushButton.setGeometry(QtCore.QRect(480, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Teacher_add)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 570, 171, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Teacher_add)
        self.pushButton_3.setGeometry(QtCore.QRect(580, 570, 171, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(Teacher_add)
        self.label_4.setGeometry(QtCore.QRect(300, 320, 211, 51))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Teacher_add)
        self.label_5.setGeometry(QtCore.QRect(300, 400, 211, 51))
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(Teacher_add)
        self.lineEdit_2.setGeometry(QtCore.QRect(500, 240, 251, 31))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Teacher_add)
        self.lineEdit_3.setGeometry(QtCore.QRect(500, 320, 251, 31))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Teacher_add)
        self.lineEdit_4.setGeometry(QtCore.QRect(500, 410, 251, 31))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.retranslateUi(Teacher_add)
        QtCore.QMetaObject.connectSlotsByName(Teacher_add)

    def retranslateUi(self, Teacher_add):
        _translate = QtCore.QCoreApplication.translate
        Teacher_add.setWindowTitle(_translate("Teacher_add", "教师信息添加"))
        self.label.setText(_translate("Teacher_add", "<html><head/><body><p><span style=\" font-size:26pt; font-weight:600; color:#00aaff;\">教师信息添加</span></p></body></html>"))
        self.label_2.setText(_translate("Teacher_add", "<html><head/><body><p><span style=\" font-size:12pt; color:#00aaff;\">教师号：</span></p></body></html>"))
        self.label_3.setText(_translate("Teacher_add", "<html><head/><body><p><span style=\" font-size:12pt; color:#00aaff;\">教师姓名：</span></p></body></html>"))
        self.pushButton.setText(_translate("Teacher_add", "添加"))
        self.pushButton_2.setText(_translate("Teacher_add", "返回教师信息管理模块"))
        self.pushButton_3.setText(_translate("Teacher_add", "返回主菜单"))
        self.label_4.setText(_translate("Teacher_add", "<html><head/><body><p><span style=\" font-size:12pt; color:#00aaff;\">所在院系：</span></p></body></html>"))
        self.label_5.setText(_translate("Teacher_add", "<html><head/><body><p><span style=\" font-size:12pt; color:#00aaff;\">联系电话：</span></p></body></html>"))


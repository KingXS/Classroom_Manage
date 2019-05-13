# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Teacher_delete.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Teacher_delete(object):
    def setupUi(self, Teacher_delete):
        Teacher_delete.setObjectName("Teacher_delete")
        Teacher_delete.resize(1040, 646)
        Teacher_delete.setWindowOpacity(1.0)
        Teacher_delete.setStyleSheet("background-image: url(:D:/PyQt/2.png);")
        self.label = QtWidgets.QLabel(Teacher_delete)
        self.label.setGeometry(QtCore.QRect(400, 40, 661, 131))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Teacher_delete)
        self.label_2.setGeometry(QtCore.QRect(150, 270, 211, 51))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Teacher_delete)
        self.lineEdit.setGeometry(QtCore.QRect(410, 270, 251, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Teacher_delete)
        self.pushButton.setGeometry(QtCore.QRect(780, 270, 93, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Teacher_delete)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 487, 211, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Teacher_delete)
        self.pushButton_3.setGeometry(QtCore.QRect(640, 487, 201, 51))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Teacher_delete)
        QtCore.QMetaObject.connectSlotsByName(Teacher_delete)

    def retranslateUi(self, Teacher_delete):
        _translate = QtCore.QCoreApplication.translate
        Teacher_delete.setWindowTitle(_translate("Teacher_delete", "教师信息删除"))
        self.label.setText(_translate("Teacher_delete", "<html><head/><body><p><span style=\" font-size:26pt; font-weight:600; color:#00aaff;\">教师信息删除</span></p></body></html>"))
        self.label_2.setText(_translate("Teacher_delete", "<html><head/><body><p><span style=\" font-size:18pt; color:#00aaff;\">请输入教师号：</span></p></body></html>"))
        self.pushButton.setText(_translate("Teacher_delete", "删除"))
        self.pushButton_2.setText(_translate("Teacher_delete", "返回教师信息管理模块"))
        self.pushButton_3.setText(_translate("Teacher_delete", "返回主菜单"))


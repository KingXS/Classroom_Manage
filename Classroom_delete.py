# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Classroom_delete.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Classroom_delete(object):
    def setupUi(self, Classroom_delete):
        Classroom_delete.setObjectName("Classroom_delete")
        Classroom_delete.resize(1040, 646)
        Classroom_delete.setStyleSheet("background-image: url(:D:/PyQt/2.png);")
        self.label = QtWidgets.QLabel(Classroom_delete)
        self.label.setGeometry(QtCore.QRect(400, 40, 661, 131))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Classroom_delete)
        self.label_2.setGeometry(QtCore.QRect(150, 270, 211, 51))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Classroom_delete)
        self.lineEdit.setGeometry(QtCore.QRect(410, 270, 251, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Classroom_delete)
        self.pushButton.setGeometry(QtCore.QRect(780, 270, 93, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Classroom_delete)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 487, 211, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Classroom_delete)
        self.pushButton_3.setGeometry(QtCore.QRect(640, 487, 201, 51))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Classroom_delete)
        QtCore.QMetaObject.connectSlotsByName(Classroom_delete)

    def retranslateUi(self, Classroom_delete):
        _translate = QtCore.QCoreApplication.translate
        Classroom_delete.setWindowTitle(_translate("Classroom_delete", "教室信息删除"))
        self.label.setText(_translate("Classroom_delete", "<html><head/><body><p><span style=\" font-size:26pt; font-weight:600; color:#00aaff;\">教室信息删除</span></p></body></html>"))
        self.label_2.setText(_translate("Classroom_delete", "<html><head/><body><p><span style=\" font-size:18pt; color:#00aaff;\">请输入教室号：</span></p></body></html>"))
        self.pushButton.setText(_translate("Classroom_delete", "删除"))
        self.pushButton_2.setText(_translate("Classroom_delete", "返回教师信息管理模块"))
        self.pushButton_3.setText(_translate("Classroom_delete", "返回主菜单"))


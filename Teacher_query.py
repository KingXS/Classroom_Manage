# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Teacher_query.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Teacher_query(object):
    def setupUi(self, Teacher_query):
        Teacher_query.setObjectName("Teacher_query")
        Teacher_query.resize(1040, 646)
        Teacher_query.setStyleSheet("background-image: url(:D:/PyQt/2.png);")
        self.label = QtWidgets.QLabel(Teacher_query)
        self.label.setGeometry(QtCore.QRect(410, 0, 661, 131))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Teacher_query)
        self.label_2.setGeometry(QtCore.QRect(160, 120, 211, 51))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Teacher_query)
        self.lineEdit.setGeometry(QtCore.QRect(410, 130, 251, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Teacher_query)
        self.label_3.setGeometry(QtCore.QRect(220, 230, 211, 161))
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(Teacher_query)
        self.textEdit.setGeometry(QtCore.QRect(410, 240, 381, 221))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Teacher_query)
        self.pushButton.setGeometry(QtCore.QRect(790, 130, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Teacher_query)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 517, 161, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Teacher_query)
        self.pushButton_3.setGeometry(QtCore.QRect(640, 517, 171, 61))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Teacher_query)
        QtCore.QMetaObject.connectSlotsByName(Teacher_query)

    def retranslateUi(self, Teacher_query):
        _translate = QtCore.QCoreApplication.translate
        Teacher_query.setWindowTitle(_translate("Teacher_query", "教师信息查询"))
        self.label.setText(_translate("Teacher_query", "<html><head/><body><p><span style=\" font-size:26pt; font-weight:600; color:#00aaff;\">教师信息查询</span></p></body></html>"))
        self.label_2.setText(_translate("Teacher_query", "<html><head/><body><p><span style=\" font-size:18pt; color:#00aaff;\">请输入教师号：</span></p></body></html>"))
        self.label_3.setText(_translate("Teacher_query", "<html><head/><body><p><span style=\" font-size:18pt; color:#00aaff;\">结果显示：</span></p><p><span style=\" font-size:7pt; color:#00aaff;\">教师号</span></p><p><span style=\" font-size:7pt; color:#00aaff;\">教师姓名</span></p><p><span style=\" font-size:7pt; color:#00aaff;\">所在院系</span></p><p><span style=\" font-size:7pt; color:#00aaff;\">联系电话</span></p></body></html>"))
        self.pushButton.setText(_translate("Teacher_query", "查询"))
        self.pushButton_2.setText(_translate("Teacher_query", "返回教师信息管理模块"))
        self.pushButton_3.setText(_translate("Teacher_query", "返回主菜单"))


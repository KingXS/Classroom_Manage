# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Classroom_query.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Classroom_query(object):
    def setupUi(self, Classroom_query):
        Classroom_query.setObjectName("Classroom_query")
        Classroom_query.resize(1040, 646)
        Classroom_query.setStyleSheet("background-image: url(:D:/PyQt/2.png);")
        self.label = QtWidgets.QLabel(Classroom_query)
        self.label.setGeometry(QtCore.QRect(410, 0, 661, 131))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Classroom_query)
        self.label_2.setGeometry(QtCore.QRect(160, 120, 211, 51))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Classroom_query)
        self.lineEdit.setGeometry(QtCore.QRect(410, 130, 251, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Classroom_query)
        self.label_3.setGeometry(QtCore.QRect(220, 230, 211, 251))
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(Classroom_query)
        self.textEdit.setGeometry(QtCore.QRect(410, 240, 381, 221))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Classroom_query)
        self.pushButton.setGeometry(QtCore.QRect(790, 130, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Classroom_query)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 550, 171, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Classroom_query)
        self.pushButton_3.setGeometry(QtCore.QRect(640, 550, 171, 28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Classroom_query)
        QtCore.QMetaObject.connectSlotsByName(Classroom_query)

    def retranslateUi(self, Classroom_query):
        _translate = QtCore.QCoreApplication.translate
        Classroom_query.setWindowTitle(_translate("Classroom_query", "教室信息查询"))
        self.label.setText(_translate("Classroom_query", "<html><head/><body><p><span style=\" font-size:26pt; font-weight:600; color:#00aaff;\">教室信息查询</span></p></body></html>"))
        self.label_2.setText(_translate("Classroom_query", "<html><head/><body><p><span style=\" font-size:18pt; color:#00aaff;\">请输入教室号：</span></p></body></html>"))
        self.label_3.setText(_translate("Classroom_query", "<html><head/><body><p><span style=\" font-size:18pt; color:#00aaff;\">结果显示：</span></p><p><span style=\" font-size:7pt; color:#00aaff;\">教室号</span></p><p><span style=\" font-size:7pt; color:#00aaff;\">教室类型</span></p><p><span style=\" font-size:7pt; color:#00aaff;\">教室状态</span></p><p><span style=\" font-size:7pt; color:#00aaff;\">班级号</span></p><p><span style=\" font-size:7pt; color:#00aaff;\">管理员</span></p><p><span style=\" font-size:7pt; color:#00aaff;\">管理员电话</span></p><p><span style=\" font-size:7pt; color:#00aaff;\">容量</span></p></body></html>"))
        self.pushButton.setText(_translate("Classroom_query", "查询"))
        self.pushButton_2.setText(_translate("Classroom_query", "返回教室信息管理模块"))
        self.pushButton_3.setText(_translate("Classroom_query", "返回主菜单"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Course_delete.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Course_delete(object):
    def setupUi(self, Course_delete):
        Course_delete.setObjectName("Course_delete")
        Course_delete.resize(1040, 646)
        Course_delete.setStyleSheet("background-image: url(:D:/PyQt/2.png);")
        self.label = QtWidgets.QLabel(Course_delete)
        self.label.setGeometry(QtCore.QRect(400, 40, 661, 131))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Course_delete)
        self.label_2.setGeometry(QtCore.QRect(150, 270, 211, 51))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Course_delete)
        self.lineEdit.setGeometry(QtCore.QRect(410, 270, 251, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Course_delete)
        self.pushButton.setGeometry(QtCore.QRect(780, 270, 93, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Course_delete)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 487, 211, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Course_delete)
        self.pushButton_3.setGeometry(QtCore.QRect(640, 487, 201, 51))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Course_delete)
        QtCore.QMetaObject.connectSlotsByName(Course_delete)

    def retranslateUi(self, Course_delete):
        _translate = QtCore.QCoreApplication.translate
        Course_delete.setWindowTitle(_translate("Course_delete", "课程信息删除"))
        self.label.setText(_translate("Course_delete", "<html><head/><body><p><span style=\" font-size:26pt; font-weight:600; color:#00aaff;\">课程信息删除</span></p></body></html>"))
        self.label_2.setText(_translate("Course_delete", "<html><head/><body><p><span style=\" font-size:18pt; color:#00aaff;\">请输入课程号：</span></p></body></html>"))
        self.pushButton.setText(_translate("Course_delete", "删除"))
        self.pushButton_2.setText(_translate("Course_delete", "返回课程信息管理模块"))
        self.pushButton_3.setText(_translate("Course_delete", "返回主菜单"))


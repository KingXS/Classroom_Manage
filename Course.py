# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Course.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Course(object):
    def setupUi(self, Course):
        Course.setObjectName("Course")
        Course.resize(1040, 646)
        Course.setStyleSheet("background-image: url(:D:/PyQt/2.png);")
        self.label = QtWidgets.QLabel(Course)
        self.label.setGeometry(QtCore.QRect(360, 0, 661, 131))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Course)
        self.pushButton.setGeometry(QtCore.QRect(230, 150, 221, 121))
        self.pushButton.setStyleSheet("color:rgb(0, 170, 255);\n"
"font: 16pt \"Agency FB\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Course)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 150, 221, 121))
        self.pushButton_2.setStyleSheet("color:rgb(0, 170, 255);\n"
"font: 16pt \"Agency FB\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Course)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 340, 221, 121))
        self.pushButton_3.setStyleSheet("color:rgb(0, 170, 255);\n"
"font: 16pt \"Agency FB\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Course)
        self.pushButton_4.setGeometry(QtCore.QRect(580, 340, 221, 121))
        self.pushButton_4.setStyleSheet("color:rgb(0, 170, 255);\n"
"font: 16pt \"Agency FB\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Course)
        self.pushButton_5.setGeometry(QtCore.QRect(400, 520, 241, 51))
        self.pushButton_5.setObjectName("pushButton_5")

        self.retranslateUi(Course)
        QtCore.QMetaObject.connectSlotsByName(Course)

    def retranslateUi(self, Course):
        _translate = QtCore.QCoreApplication.translate
        Course.setWindowTitle(_translate("Course", "课程信息管理"))
        self.label.setText(_translate("Course", "<html><head/><body><p><span style=\" font-size:26pt; font-weight:600; color:#00aaff;\">课程信息管理模块</span></p></body></html>"))
        self.pushButton.setText(_translate("Course", "课程信息查询"))
        self.pushButton_2.setText(_translate("Course", "课程信息添加"))
        self.pushButton_3.setText(_translate("Course", "课程信息修改"))
        self.pushButton_4.setText(_translate("Course", "课程信息删除"))
        self.pushButton_5.setText(_translate("Course", "返回主菜单"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Course_add.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Course_add(object):
    def setupUi(self, Course_add):
        Course_add.setObjectName("Course_add")
        Course_add.resize(1040, 646)
        Course_add.setStyleSheet("background-image: url(:D:/PyQt/2.png);")
        self.label = QtWidgets.QLabel(Course_add)
        self.label.setGeometry(QtCore.QRect(410, 20, 661, 131))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Course_add)
        self.label_2.setGeometry(QtCore.QRect(320, 170, 211, 51))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Course_add)
        self.lineEdit.setGeometry(QtCore.QRect(500, 180, 251, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Course_add)
        self.label_3.setGeometry(QtCore.QRect(320, 240, 211, 51))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Course_add)
        self.pushButton.setGeometry(QtCore.QRect(480, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Course_add)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 570, 171, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Course_add)
        self.pushButton_3.setGeometry(QtCore.QRect(580, 570, 171, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(Course_add)
        self.label_4.setGeometry(QtCore.QRect(340, 310, 211, 51))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Course_add)
        self.label_5.setGeometry(QtCore.QRect(300, 380, 211, 51))
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(Course_add)
        self.lineEdit_2.setGeometry(QtCore.QRect(500, 250, 251, 31))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Course_add)
        self.lineEdit_3.setGeometry(QtCore.QRect(500, 320, 251, 31))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Course_add)
        self.lineEdit_4.setGeometry(QtCore.QRect(500, 390, 251, 31))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.retranslateUi(Course_add)
        QtCore.QMetaObject.connectSlotsByName(Course_add)

    def retranslateUi(self, Course_add):
        _translate = QtCore.QCoreApplication.translate
        Course_add.setWindowTitle(_translate("Course_add", "课程信息添加"))
        self.label.setText(_translate("Course_add", "<html><head/><body><p><span style=\" font-size:26pt; font-weight:600; color:#00aaff;\">课程信息添加</span></p></body></html>"))
        self.label_2.setText(_translate("Course_add", "<html><head/><body><p><span style=\" font-size:12pt; color:#00aaff;\">课程号：</span></p></body></html>"))
        self.label_3.setText(_translate("Course_add", "<html><head/><body><p><span style=\" font-size:12pt; color:#00aaff;\">课程名：</span></p></body></html>"))
        self.pushButton.setText(_translate("Course_add", "添加"))
        self.pushButton_2.setText(_translate("Course_add", "返回课程信息管理模块"))
        self.pushButton_3.setText(_translate("Course_add", "返回主菜单"))
        self.label_4.setText(_translate("Course_add", "<html><head/><body><p><span style=\" font-size:12pt; color:#00aaff;\">学分：</span></p></body></html>"))
        self.label_5.setText(_translate("Course_add", "<html><head/><body><p><span style=\" font-size:12pt; color:#00aaff;\">课程描述：</span></p></body></html>"))


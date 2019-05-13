from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Main import Ui_Main
from Module import Ui_Module
#引用教室管理各个模块
from Classroom import Ui_Classroom
from Classroom_query import Ui_Classroom_query
from Classroom_add import Ui_Classroom_add
from Classroom_change import Ui_Classroom_change
from Classroom_delete import Ui_Classroom_delete

#引用班级管理各个模块
from Class import Ui_Class
from Class_query import Ui_Class_query
from Class_add import Ui_Class_add
from Class_change import Ui_Class_change
from Class_delete import Ui_Class_delete

#引用课程管理各个模块
from Course import Ui_Course
from Course_query import Ui_Course_query
from Course_add import Ui_Course_add
from Course_change import Ui_Course_change
from Course_delete import Ui_Course_delete

#引用教师管理的各个模块
from Teacher import Ui_Teacher
from Teacher_query import Ui_Teacher_query
from Teacher_add import Ui_Teacher_add
from Teacher_change import Ui_Teacher_change
from Teacher_delete import Ui_Teacher_delete

import sys
import pymysql  # 导入 pymysql

#定义主窗口
class new_Main(QtWidgets.QWidget, Ui_Main):
    def __init__(self):
        super(new_Main,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Module_show)

#显示模块选择窗口
    def Module_show(self):
        user_name = self.lineEdit.text()
        user_password = self.lineEdit_2.text()
        if (user_name=="数据库课设") and (user_password=="123456"):
            Module.show()
            Main.hide()
        else:
            result=QMessageBox.warning(self,("警告"),("""用户名或密码有误！"""),
                                        QMessageBox.StandardButtons(QMessageBox.No|QMessageBox.Yes))

#定义模块选择窗口
class new_Module(QtWidgets.QWidget, Ui_Module):
    def __init__(self):
        super(new_Module,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Classroom_show)
        self.pushButton_2.clicked.connect(self.Course_show)
        self.pushButton_3.clicked.connect(self.Class_show)
        self.pushButton_4.clicked.connect(self.Teacher_show)


#教室管理窗口显示
    def Classroom_show(self):
        Classroom.show()
        Module.close()

    # 班级管理窗口显示
    def Class_show(self):
        Class.show()

    # 课程管理窗口显示
    def Course_show(self):
        Course.show()

    # 教师管理窗口显示
    def Teacher_show(self):
        Teacher.show()

#重载教室管理窗口
class new_Classroom(QtWidgets.QWidget, Ui_Classroom):
    def __init__(self):
        super(new_Classroom,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Classroom_query_show)
        self.pushButton_2.clicked.connect(self.Classroom_add_show)
        self.pushButton_3.clicked.connect(self.Classroom_change_show)
        self.pushButton_4.clicked.connect(self.Classroom_delete_show)
        self.pushButton_5.clicked.connect(self.Module_show)

    def Classroom_query_show(self):
        Classroom_query.show()
        Classroom.close()

    def Classroom_add_show(self):
        Classroom_add.show()
        Classroom.close()

    def Classroom_change_show(self):
        Classroom_change.show()
        Classroom.close()

    def Classroom_delete_show(self):
        Classroom_delete.show()
        Classroom.close()

    def Module_show(self):
        Classroom.close()
        Module.show()

 #教室信息查询窗口
class new_Classroom_query(QtWidgets.QWidget, Ui_Classroom_query):
    def __init__(self):
        super(new_Classroom_query,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.start_query)
        self.pushButton_2.clicked.connect(self.return_classroom)        #返回教室管理主界面
        self.pushButton_3.clicked.connect(self.return_module)       #返回主菜单

    def start_query(self):
        Classroom_num=self.lineEdit.text()
        # 使用cursor()方法获取操作游标
        cur = db.cursor()
        sql = "SELECT * FROM 教室管理.教室信息表"+" WHERE 教室号="+Classroom_num
        cur.execute(sql)  # 执行sql语句
        results = cur.fetchall()  # 获取查询的所有记录
        results_str=str(results)
        self.textEdit.setText(results_str)

    def return_classroom(self):
        Classroom_query.close()
        Classroom.show()

    def return_module(self):
        Classroom_query.close()
        Module.show()

#教室信息添加窗口
class new_Classroom_add(QtWidgets.QWidget, Ui_Classroom_add):
    def __init__(self):
        super(new_Classroom_add,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.classroom_add)  # 返回教室管理主界面
        self.pushButton_2.clicked.connect(self.return_classroom)  # 返回教室管理主界面
        self.pushButton_3.clicked.connect(self.return_module)  # 返回主菜单


    def classroom_add(self):
        Classroom_num=self.lineEdit.text()      #教室号
        Classroom_sort=self.lineEdit_2.text()       #教室种类
        Classroom_manager = self.comboBox.currentText()     #教室管理员
        if self.radioButton.isChecked():
            Classroom_state="被使用"       #教室状态
        if self.radioButton_2.isChecked():
            Classroom_state = "未被使用"
        Class_num=self.lineEdit_3.text()        #班级号
        Manager_phone=self.lineEdit_5.text()        #管理员电话
        print(type(Manager_phone))
        Classroom_hold=self.lineEdit_6.text()        #教室容量
        print(Classroom_hold)

        #插入语句
        cur1 = db.cursor()
        sql = "INSERT INTO 教室管理.教室信息表 (教室号,教室类型,教室状态,班级号,管理员,管理员电话,容量) "\
              "VALUES ('"+Classroom_num+"','"+Classroom_sort+"','"+Classroom_state+"','"+Class_num+"','"+Classroom_manager+"','"+Manager_phone+"','"+Classroom_hold+"')"
        print(sql)
        try:
            cur1.execute(sql)  # 执行sql语句
            #执行提交操作
            db.commit()
            reply = QMessageBox.information(self,
                                            "提示",
                                            "添加成功！",
                                            QMessageBox.Yes | QMessageBox.No)
        except:
            #回滚操作
            db.rollback()


    def return_classroom(self):
        Classroom_add.close()
        Classroom.show()

    def return_module(self):
        Classroom_add.close()
        Module.show()

#教室信息修改窗口
class new_Classroom_change(QtWidgets.QWidget, Ui_Classroom_change):
    def __init__(self):
        super(new_Classroom_change,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.start_change)
        self.pushButton_2.clicked.connect(self.return_classroom)  # 返回教室管理主界面
        self.pushButton_3.clicked.connect(self.return_module)  # 返回主菜单
        self.pushButton_4.clicked.connect(self.start_query)  # 返回主菜单

    def start_query(self):
        Classroom_num = self.lineEdit_4.text()
        # 使用cursor()方法获取操作游标
        cur = db.cursor()
        sql = "SELECT * FROM 教室管理.教室信息表" + " WHERE 教室号=" + Classroom_num
        cur.execute(sql)  # 执行sql语句
        results = cur.fetchall()  # 获取查询的所有记录
        results_str = str(results)
        self.textEdit.setText(results_str)

    def start_change(self):
        Classroom_num = self.lineEdit.text()  # 教室号
        Classroom_sort = self.lineEdit_2.text()  # 教室种类
        Classroom_manager = self.comboBox.currentText()  # 教室管理员
        if self.radioButton.isChecked():
            Classroom_state = "被使用"  # 教室状态
        if self.radioButton_2.isChecked():
            Classroom_state = "未被使用"
        Class_num = self.lineEdit_3.text()  # 班级号
        Manager_phone = self.lineEdit_5.text()  # 管理员电话
        print(type(Manager_phone))
        Classroom_hold = self.lineEdit_6.text()  # 教室容量
        print(Classroom_hold)

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 更新语句
        sql = "UPDATE  教室管理.教室信息表 SET 教室号='"+Classroom_num+"',教室类型='"+Classroom_sort+\
              "',教室状态='"+Classroom_state+"',班级号='"+Class_num+"',管理员='"+Classroom_manager+"',管理员电话='"+Manager_phone+"',容量='"+Classroom_hold+"' WHERE 教室号 ='"+Classroom_num+"'"
        print(sql)
              # 执行SQL语句
        try:
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            db.rollback()
        # 发生错误时回滚

        reply = QMessageBox.information(self,
                                        "提示",
                                        "修改成功！",
                                        QMessageBox.Yes | QMessageBox.No)


    def return_classroom(self):
        Classroom_change.close()
        Classroom.show()

    def return_module(self):
        Classroom_change.close()
        Module.show()

#教室信息删除模块
class new_Classroom_delete(QtWidgets.QWidget, Ui_Classroom_delete):
    def __init__(self):
        super(new_Classroom_delete,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.start_delete)  # 开始删除
        self.pushButton_2.clicked.connect(self.return_classroom)  # 返回教室管理主界面
        self.pushButton_3.clicked.connect(self.return_module)  # 返回主菜单

    def start_delete(self):
        Classroom_num=self.lineEdit.text()
        print(Classroom_num)
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # SQL 删除语句
        sql = "DELETE FROM 教室管理.教室信息表 WHERE 教室号='"+Classroom_num+"'"
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 提交修改
            db.commit()
            reply = QMessageBox.information(self,
                                            "提示",
                                            "删除成功！",
                                            QMessageBox.Yes | QMessageBox.No)

        except:
            # 发生错误时回滚
            db.rollback()


    def return_classroom(self):
        Classroom_delete.close()
        Classroom.show()

    def return_module(self):
        Classroom_delete.close()
        Module.show()


#班级信息管理模块
class new_Class(QtWidgets.QWidget, Ui_Class):
    def __init__(self):
        super(new_Class,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Class_query_show)      #班级信息查询窗口
        self.pushButton_2.clicked.connect(self.Class_add_show)  # 班级信息查询窗口
        self.pushButton_3.clicked.connect(self.Class_change_show)  # 班级信息查询窗口
        self.pushButton_4.clicked.connect(self.Class_delete_show)  # 班级信息查询窗口
        self.pushButton_5.clicked.connect(self.return_module)  # 班级信息查询窗口

    def Class_query_show(self):
        Class_query.show()
        Class.close()

    def Class_add_show(self):
        Class_add.show()
        Class.close()

    def Class_change_show(self):
        Class_change.show()
        Class.close()

    def Class_delete_show(self):
        Class_delete.show()
        Class.close()

    def return_module(self):
        Module.show()
        Class.close()

class new_Class_query(QtWidgets.QWidget, Ui_Class_query):
    def __init__(self):
        super(new_Class_query,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.start_query)       #开始查询
        self.pushButton_2.clicked.connect(self.return_class)  # 返回教室管理主界面
        self.pushButton_3.clicked.connect(self.return_module)  # 返回主菜单

    def start_query(self):
        Class_num = self.lineEdit.text()
        # 使用cursor()方法获取操作游标
        cur = db.cursor()
        sql = "SELECT * FROM 教室管理.班级信息表" + " WHERE 班级号=" + Class_num
        cur.execute(sql)  # 执行sql语句
        results = cur.fetchall()  # 获取查询的所有记录
        results_str = str(results)
        self.textEdit.setText(results_str)

    def return_class(self):
        Class_query.close()
        Class.show()

    def return_module(self):
        Class_query.close()
        Module.show()

class new_Class_add(QtWidgets.QWidget, Ui_Class_add):
    def __init__(self):
        super(new_Class_add,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.start_add)     #添加数据
        self.pushButton_2.clicked.connect(self.return_class)  # 返回教室管理主界面
        self.pushButton_3.clicked.connect(self.return_module)  # 返回主菜单

    def start_add(self):
        Class_num=self.lineEdit.text()      #班级号
        Class_=self.lineEdit_2.text()        #班级
        Class_teacher=self.lineEdit_3.text()        #班主任
        Teacher_num=self.lineEdit_4.text()      #教师号
        Classroom_num=self.lineEdit_5.text()        #教室号
        Partment=self.lineEdit_6.text()     #所在院系
        Course_num=self.lineEdit_7.text()       #课程号
 #       print(Class_num,Class,Class_teacher,Teacher_num,Classroom_num,Partment,Course_num)
        cur = db.cursor()
        sql = "INSERT INTO 教室管理.班级信息表 (班级号,班级,班主任,教师号,教室号,所在院系,课程号) " \
              "VALUES ('" + Class_num + "','" + Class_ + "','" + Class_teacher + "','" + Teacher_num + "','" + Classroom_num + "','" + Partment + "','" + Course_num + "')"
        print(sql)
        try:
            cur.execute(sql)  # 执行sql语句
            db.commit()
            reply = QMessageBox.information(self,
                                            "提示",
                                            "添加成功！",
                                            QMessageBox.Yes | QMessageBox.No)
        except:
            db.rollback()


    def return_class(self):
        Class_add.close()
        Class.show()

    def return_module(self):
        Class_add.close()
        Module.show()

class new_Class_change(QtWidgets.QWidget, Ui_Class_change):
    def __init__(self):
        super(new_Class_change,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.start_change)  # 开始修改
        self.pushButton_2.clicked.connect(self.return_class)  # 返回教室管理主界面
        self.pushButton_3.clicked.connect(self.return_module)  # 返回主菜单
        self.pushButton_4.clicked.connect(self.start_query)  # 开始查询


    def start_query(self):
        Class_num = self.lineEdit_8.text()
        # 使用cursor()方法获取操作游标
        cur = db.cursor()
        sql = "SELECT * FROM 教室管理.班级信息表" + " WHERE 班级号=" + Class_num
        cur.execute(sql)  # 执行sql语句
        results = cur.fetchall()  # 获取查询的所有记录
        results_str = str(results)
        self.textEdit.setText(results_str)

    def start_change(self):
        Class_num=self.lineEdit.text()      #班级号
        Class_=self.lineEdit_2.text()     #班级
        Class_manager=self.lineEdit_3.text()      #班主任
        Teacher_num=self.lineEdit_4.text()      #教师号
        Classroom_num=self.lineEdit_5.text()      #教室号
        Partment=self.lineEdit_6.text()     #所在院系
        Course_num=self.lineEdit_7.text()       #课程号

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 更新语句
        sql = "UPDATE  教室管理.班级信息表 SET 班级号='" + Class_num + "',班级='" + Class_ + \
              "',班主任='" + Class_manager + "',教师号='" + Teacher_num + "',教室号='" + Classroom_num + "',所在院系='" + Partment + "',课程号='" + Course_num + "' WHERE 班级号 ='" + Class_num + "'"
        print(sql)
        # 执行SQL语句
        try:
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            reply = QMessageBox.information(self,
                                            "提示",
                                            "修改成功！",
                                            QMessageBox.Yes | QMessageBox.No)

        except:

            db.rollback()

        # 发生错误时回滚


    def return_class(self):
        Class_change.close()
        Class.show()

    def return_module(self):
        Class_change.close()
        Module.show()

class new_Class_delete(QtWidgets.QWidget, Ui_Class_delete):
    def __init__(self):
        super(new_Class_delete,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.start_delete)  # 开始删除
        self.pushButton_2.clicked.connect(self.return_class)  # 返回教室管理主界面
        self.pushButton_3.clicked.connect(self.return_module)  # 返回主菜单

    def start_delete(self):
        Class_num = self.lineEdit.text()
        print(Class_num)
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 删除语句
        sql = "DELETE FROM 教室管理.班级信息表 WHERE 班级号='" + Class_num + "'"
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 提交修改
            db.commit()
            reply = QMessageBox.information(self,
                                            "提示",
                                            "删除成功！",
                                            QMessageBox.Yes | QMessageBox.No)
        except:
            # 发生错误时回滚
            db.rollback()


    def return_class(self):
        Class_delete.close()
        Class.show()

    def return_module(self):
        Class_delete.close()
        Module.show()


#课程信息管理模块
class new_Course(QtWidgets.QWidget, Ui_Course):
    def __init__(self):
        super(new_Course,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Course_query_show)  # 课程信息查询窗口
        self.pushButton_2.clicked.connect(self.Course_add_show)  # 课程信息添加窗口
        self.pushButton_3.clicked.connect(self.Course_change_show)  # 课程信息修改窗口
        self.pushButton_4.clicked.connect(self.Course_delete_show)  # 课程信息删除窗口

    def Course_query_show(self):
        Course_query.show()
        Course.close()

    def Course_add_show(self):
        Course_add.show()
        Course.close()

    def Course_change_show(self):
        Course_change.show()
        Course.close()

    def Course_delete_show(self):
        Course_delete.show()
        Course.close()

class new_Course_query(QtWidgets.QWidget, Ui_Course_query):
    def __init__(self):
        super(new_Course_query,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.start_query)
        self.pushButton_2.clicked.connect(self.return_course)  # 返回教室管理主界面
        self.pushButton_3.clicked.connect(self.return_module)  # 返回主菜单

    def start_query(self):
        Course_num = self.lineEdit.text()
        # 使用cursor()方法获取操作游标
        cur = db.cursor()
        sql = "SELECT * FROM 教室管理.课程基本信息表" + " WHERE 课程号=" + Course_num
        cur.execute(sql)  # 执行sql语句
        results = cur.fetchall()  # 获取查询的所有记录
        results_str = str(results)
        self.textEdit.setText(results_str)

    def return_course(self):
        Course_query.close()
        Course.show()

    def return_module(self):
        Course_query.close()
        Module.show()

class new_Course_add(QtWidgets.QWidget, Ui_Course_add):
    def __init__(self):
        super(new_Course_add,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.course_add)  # 开始添加信息
        self.pushButton_2.clicked.connect(self.return_course)  # 返回教室管理主界面
        self.pushButton_3.clicked.connect(self.return_module)  # 返回主菜单

    def course_add(self):
        Course_num=self.lineEdit.text()     #课程号
        Course_name=self.lineEdit_2.text()      #课程名
        Credit=self.lineEdit_3.text()       #学分
        Course_descript=self.lineEdit_4.text()      #课程描述

        # 插入语句
        cur1 = db.cursor()
        sql = "INSERT INTO 教室管理.课程基本信息表 (课程号,课程名,学分,课程描述) " \
              "VALUES ('" + Course_num + "','" + Course_name + "','" + Credit + "','" + Course_descript + "')"
        print(sql)
        try:
            cur1.execute(sql)  # 执行sql语句
            db.commit()
            reply = QMessageBox.information(self,
                                            "提示",
                                            "添加成功！",
                                            QMessageBox.Yes | QMessageBox.No)
        except:
            #发生错误回滚
            db.rollback()

    def return_course(self):
        Course_add.close()
        Course.show()

    def return_module(self):
        Course_add.close()
        Module.show()

class new_Course_change(QtWidgets.QWidget, Ui_Course_change):
    def __init__(self):
        super(new_Course_change,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.start_change)  # 开始修改
        self.pushButton_2.clicked.connect(self.return_course)  # 返回教室管理主界面
        self.pushButton_3.clicked.connect(self.return_module)  # 返回主菜单
        self.pushButton_4.clicked.connect(self.start_query)

    def start_query(self):
        Course_num = self.lineEdit_8.text()
        # 使用cursor()方法获取操作游标
        cur = db.cursor()
        sql = "SELECT * FROM 教室管理.课程基本信息表" + " WHERE 课程号=" + Course_num
        cur.execute(sql)  # 执行sql语句
        results = cur.fetchall()  # 获取查询的所有记录
        results_str = str(results)
        self.textEdit.setText(results_str)

    def start_change(self):
        Course_num = self.lineEdit.text()  # 课程号
        Course_name = self.lineEdit_2.text()  # 课程名
        Credit = self.lineEdit_3.text()  # 学分
        Course_descript = self.lineEdit_4.text()  #课程描述

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 更新语句
        sql = "UPDATE  教室管理.课程基本信息表 SET 课程号='" + Course_num + "',课程名='" + Course_name + \
                "',学分='" + Credit + "',课程描述='" + Course_descript + "' WHERE 课程号 ='" + Course_num + "'"
        print(sql)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        # 发生错误时回滚
            reply = QMessageBox.information(self,
                                            "提示",
                                            "修改成功！",
                                            QMessageBox.Yes | QMessageBox.No)
        except:
            #发生错误时回滚
            db.rollback()


    def return_course(self):
        Course_change.close()
        Course.show()

    def return_module(self):
        Course_change.close()
        Module.show()

class new_Course_delete(QtWidgets.QWidget, Ui_Course_delete):
    def __init__(self):
        super(new_Course_delete,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.start_delete)  # 开始删除
        self.pushButton_2.clicked.connect(self.return_course)  # 返回教室管理主界面
        self.pushButton_3.clicked.connect(self.return_module)  # 返回主菜单

    def start_delete(self):
        Course_num = self.lineEdit.text()
        print(Course_num)
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 删除语句
        sql = "DELETE FROM 教室管理.课程基本信息表 WHERE 课程号='" + Course_num + "'"
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 提交修改
            db.commit()
            reply = QMessageBox.information(self,
                                            "提示",
                                            "删除成功！",
                                            QMessageBox.Yes | QMessageBox.No)
        except:
            # 发生错误时回滚
            db.rollback()



    def return_course(self):
        Course_delete.close()
        Course.show()

    def return_module(self):
        Course_delete.close()
        Module.show()


#教师信息管理
class new_Teacher(QtWidgets.QWidget, Ui_Teacher):
    def __init__(self):
        super(new_Teacher,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Teacher_query_show)  # 课程信息查询窗口
        self.pushButton_2.clicked.connect(self.Teacher_add_show)  # 课程信息查询窗口
        self.pushButton_3.clicked.connect(self.Teacher_change_show)  # 课程信息查询窗口
        self.pushButton_4.clicked.connect(self.Teacher_delete_show)  # 课程信息查询窗口

    def Teacher_query_show(self):
        Teacher_query.show()
        Teacher.close()

    def Teacher_add_show(self):
        Teacher_add.show()
        Teacher.close()

    def Teacher_change_show(self):
        Teacher_change.show()
        Teacher.close()

    def Teacher_delete_show(self):
        Teacher_delete.show()
        Teacher.close()

class new_Teacher_query(QtWidgets.QWidget, Ui_Teacher_query):
    def __init__(self):
        super(new_Teacher_query,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.start_query)  # 开始查询
        self.pushButton_2.clicked.connect(self.return_teacher)  # 返回教室管理主界面
        self.pushButton_3.clicked.connect(self.return_module)  # 返回主菜单

    def start_query(self):
        Teacher_num = self.lineEdit.text()
        # 使用cursor()方法获取操作游标
        cur = db.cursor()
        sql = "SELECT * FROM 教室管理.教师信息表" + " WHERE 教师号=" + Teacher_num
        cur.execute(sql)  # 执行sql语句
        results = cur.fetchall()  # 获取查询的所有记录
        results_str = str(results)
        self.textEdit.setText(results_str)


    def return_teacher(self):
        Teacher_query.close()
        Teacher.show()

    def return_module(self):
        Teacher_query.close()
        Module.show()

class new_Teacher_add(QtWidgets.QWidget, Ui_Teacher_add):
    def __init__(self):
        super(new_Teacher_add,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.teacher_add)  # 开始添加信息
        self.pushButton_2.clicked.connect(self.return_teacher)  # 返回教室管理主界面
        self.pushButton_3.clicked.connect(self.return_module)  # 返回主菜单


    def teacher_add(self):
        Teacher_num=self.lineEdit.text()     #教师号
        Teacher_name=self.lineEdit_2.text()      #教师姓名
        Partment=self.lineEdit_3.text()       #所在院系
        Teacher_phone=self.lineEdit_4.text()      #联系电话

        # 插入语句
        cur1 = db.cursor()
        sql = "INSERT INTO 教室管理.教师信息表 (教师号,教师姓名,所在院系,联系电话) " \
              "VALUES ('" + Teacher_num + "','" + Teacher_name + "','" + Partment + "','" + Teacher_phone + "')"
        print(sql)
        try:
            cur1.execute(sql)  # 执行sql语句
            db.commit()
            reply = QMessageBox.information(self,
                                            "提示",
                                            "添加成功！",
                                            QMessageBox.Yes | QMessageBox.No)

        except:
            #发生错误时回滚
            db.rollback()

    def return_teacher(self):
        Teacher_add.close()
        Teacher.show()

    def return_module(self):
        Teacher_add.close()
        Module.show()

class new_Teacher_change(QtWidgets.QWidget, Ui_Teacher_change):
    def __init__(self):
        super(new_Teacher_change,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.start_change)      #开始修改
        self.pushButton_2.clicked.connect(self.return_teacher)  # 返回教室管理主界面
        self.pushButton_3.clicked.connect(self.return_module)  # 返回主菜单
        self.pushButton_4.clicked.connect(self.start_query)     #开始查询

    def start_query(self):
        Teacher_num = self.lineEdit_8.text()
        # 使用cursor()方法获取操作游标
        cur = db.cursor()
        sql = "SELECT * FROM 教室管理.教师信息表" + " WHERE 教师号=" + Teacher_num
        cur.execute(sql)  # 执行sql语句
        results = cur.fetchall()  # 获取查询的所有记录
        results_str = str(results)
        self.textEdit.setText(results_str)


    def return_teacher(self):
        Teacher_change.close()
        Teacher.show()

    def return_module(self):
        Teacher_change.close()
        Module.show()

    def start_change(self):
        Teacher_num = self.lineEdit.text()  # 教师号
        Teacher_name = self.lineEdit_2.text()  # 教师姓名
        Partment = self.lineEdit_3.text()  # 所在院系
        Teacher_phone = self.lineEdit_4.text()  #联系电话

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 更新语句
        sql = "UPDATE  教室管理.教师信息表 SET 教师号='" + Teacher_num + "',教师姓名='" + Teacher_name + \
                "',所在院系='" + Partment + "',联系电话='" + Teacher_phone + "' WHERE 教师号 ='" + Teacher_num + "'"
        print(sql)
        # 执行SQL语句
        try:
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            reply = QMessageBox.information(self,
                                            "提示",
                                            "修改成功！",
                                            QMessageBox.Yes | QMessageBox.No)

        except:
            db.rollback()

        # 发生错误时回滚

class new_Teacher_delete(QtWidgets.QWidget, Ui_Teacher_delete):
    def __init__(self):
        super(new_Teacher_delete,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.start_delete)  # 开始删除
        self.pushButton_2.clicked.connect(self.return_teacher)  # 返回教室管理主界面
        self.pushButton_3.clicked.connect(self.return_module)  # 返回主菜单

    def start_delete(self):
        Teacher_num = self.lineEdit.text()
        print(Teacher_num)
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 删除语句
        sql = "DELETE FROM 教室管理.教师信息表 WHERE 教师号='" + Teacher_num + "'"
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 提交修改
            db.commit()
            reply = QMessageBox.information(self,
                                            "提示",
                                            "删除成功！",
                                            QMessageBox.Yes | QMessageBox.No)

        except:
            # 发生错误时回滚
            db.rollback()



    def return_teacher(self):
        Teacher_delete.close()
        Teacher.show()

    def return_module(self):
        Teacher_delete.close()
        Module.show()

#主函数
if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    Main=new_Main()     #定义主窗口对象
    Module=new_Module()     #定义模块选择窗口对象
    Main.show()

    db = pymysql.connect(host="localhost", user="root",
                         password="", db="test", port=3306)

    Classroom=new_Classroom()       #定义教室管理对象
    Classroom_query=new_Classroom_query()       #定义教室信息查询窗口
    Classroom_add = new_Classroom_add()     #定义教室信息添加窗口
    Classroom_change = new_Classroom_change()  # 定义教室信息修改窗口
    Classroom_delete = new_Classroom_delete()  # 定义教室信息删除窗口

    Class = new_Class()  # 定义班级信息管理窗口
    Class_query = new_Class_query()  # 定义班级信息管理窗口
    Class_add = new_Class_add()  # 定义班级信息管理窗口
    Class_change = new_Class_change()  # 定义班级信息管理窗口
    Class_delete = new_Class_delete()  # 定义班级信息管理窗口

    Course = new_Course()  # 定义课程信息管理窗口
    Course_query = new_Course_query()  # 定义课程信息查询窗口
    Course_add = new_Course_add()  # 定义课程信息添加窗口
    Course_change = new_Course_change()  # 定义课程信息修改窗口
    Course_delete = new_Course_delete()  # 定义课程信息删除窗口

    Teacher=new_Teacher()#定义教师管理信息窗口
    Teacher_query = new_Teacher_query()  # 定义教师信息查询窗口
    Teacher_add = new_Teacher_add()  # 定义教师信息查询窗口
    Teacher_change = new_Teacher_change()  # 定义教师信息查询窗口
    Teacher_delete = new_Teacher_delete()  # 定义教师信息查询窗口
    sys.exit(app.exec_())
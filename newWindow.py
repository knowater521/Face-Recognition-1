# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\综合课设三\界面\new.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


import  sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class New_person_window(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(730, 468)
        Form.setMaximumSize(QtCore.QSize(730, 505))
        Form.setWindowIcon(QIcon('icons/love.png'))
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 721, 100))
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(20, 30, 61, 31))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(14)
        font.setUnderline(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox.setGeometry(QtCore.QRect(550, 20, 151, 48))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.male = QtWidgets.QCheckBox(self.groupBox)
        self.male.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.male.setObjectName("male")
        self.horizontalLayout_2.addWidget(self.male)
        self.female = QtWidgets.QCheckBox(self.groupBox)
        self.female.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.female.setObjectName("female")
        self.horizontalLayout_2.addWidget(self.female)
        self.name = QtWidgets.QLineEdit(self.groupBox_4)
        self.name.setGeometry(QtCore.QRect(90, 30, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(18)
        self.name.setFont(font)
        self.name.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.name.setObjectName("name")
        self.groupBox_5 = QtWidgets.QGroupBox(Form)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 120, 711, 100))
        self.groupBox_5.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_7 = QtWidgets.QLabel(self.groupBox_5)
        self.label_7.setGeometry(QtCore.QRect(330, 40, 41, 20))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_3.setGeometry(QtCore.QRect(510, 10, 191, 61))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.job = QtWidgets.QComboBox(self.groupBox_3)
        self.job.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.job.setObjectName("job")
        self.job.addItem("")
        self.job.addItem("")
        self.job.addItem("")
        self.horizontalLayout.addWidget(self.job)
        self.label_9 = QtWidgets.QLabel(self.groupBox_5)
        self.label_9.setGeometry(QtCore.QRect(20, 30, 101, 31))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(14)
        font.setUnderline(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.telephone = QtWidgets.QLineEdit(self.groupBox_5)
        self.telephone.setGeometry(QtCore.QRect(140, 30, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.telephone.setFont(font)
        self.telephone.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.telephone.setObjectName("telephone")
        self.groupBox_6 = QtWidgets.QGroupBox(Form)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 230, 711, 100))
        self.groupBox_6.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.address = QtWidgets.QLineEdit(self.groupBox_6)
        self.address.setGeometry(QtCore.QRect(80, 40, 611, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.address.setFont(font)
        self.address.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.address.setObjectName("address")
        self.label_10 = QtWidgets.QLabel(self.groupBox_6)
        self.label_10.setGeometry(QtCore.QRect(20, 40, 61, 31))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(14)
        font.setUnderline(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.confirm = QtWidgets.QPushButton(Form)
        self.confirm.setGeometry(QtCore.QRect(170, 370, 101, 31))
        self.confirm.setObjectName("confirm")
        self.cancel = QtWidgets.QPushButton(Form)
        self.cancel.setGeometry(QtCore.QRect(450, 370, 101, 31))
        self.cancel.setObjectName("cancel")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(320, 440, 101, 20))
        self.label_3.setObjectName("label_3")



        self.triggered()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def triggered(self):
        '''
        绑定一些事件
        :return:
        '''
        # self.backend = Backend()

        self.male.clicked.connect(lambda : self.female.setChecked(False))
        self.female.clicked.connect(lambda : self.male.setChecked(False))
        # self.confirm.clicked.connect(self.insert_data)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Sign in"))
        self.label_4.setText(_translate("Form", "姓名"))
        self.label_5.setText(_translate("Form", "性别"))
        self.male.setText(_translate("Form", "男"))
        self.female.setText(_translate("Form", "女"))
        self.label_2.setText(_translate("Form", "所在部门"))
        self.job.setItemText(0, _translate("Form", "技术部"))
        self.job.setItemText(1, _translate("Form", "研发部"))
        self.job.setItemText(2, _translate("Form", "人力资源部"))
        self.label_9.setText(_translate("Form", "联系电话"))
        self.label_10.setText(_translate("Form", "地址"))
        self.confirm.setText(_translate("Form", "确认"))
        self.cancel.setText(_translate("Form", "取消"))
        self.label_3.setText(_translate("Form", "Copyright@ysl"))

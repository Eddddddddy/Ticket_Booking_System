# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_main(object):
    def setupUi(self, Form_main):
        Form_main.setObjectName("Form_main")
        Form_main.resize(400, 300)
        self.frame = QtWidgets.QFrame(Form_main)
        self.frame.setGeometry(QtCore.QRect(50, 210, 295, 52))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_password = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.horizontalLayout.addWidget(self.lineEdit_password)
        self.pushButton_admin = QtWidgets.QPushButton(self.frame)
        self.pushButton_admin.setObjectName("pushButton_admin")
        self.horizontalLayout.addWidget(self.pushButton_admin)
        self.pushButton_user = QtWidgets.QPushButton(Form_main)
        self.pushButton_user.setGeometry(QtCore.QRect(110, 70, 181, 71))
        self.pushButton_user.setObjectName("pushButton_user")

        self.retranslateUi(Form_main)
        QtCore.QMetaObject.connectSlotsByName(Form_main)

    def retranslateUi(self, Form_main):
        _translate = QtCore.QCoreApplication.translate
        Form_main.setWindowTitle(_translate("Form_main", "Form"))
        self.pushButton_admin.setText(_translate("Form_main", "管理员登陆"))
        self.pushButton_user.setText(_translate("Form_main", "用户登录"))


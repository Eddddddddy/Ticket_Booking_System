# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_passenger.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1081, 176)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(30, 20, 1021, 45))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_ID = QtWidgets.QLabel(self.frame)
        self.label_ID.setObjectName("label_ID")
        self.horizontalLayout.addWidget(self.label_ID)
        self.lineEdit_ID = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_ID.setObjectName("lineEdit_ID")
        self.horizontalLayout.addWidget(self.lineEdit_ID)
        self.label_name = QtWidgets.QLabel(self.frame)
        self.label_name.setObjectName("label_name")
        self.horizontalLayout.addWidget(self.label_name)
        self.lineEdit_name = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.horizontalLayout.addWidget(self.lineEdit_name)
        self.label_sex = QtWidgets.QLabel(self.frame)
        self.label_sex.setObjectName("label_sex")
        self.horizontalLayout.addWidget(self.label_sex)
        self.lineEdit_sex = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_sex.setObjectName("lineEdit_sex")
        self.horizontalLayout.addWidget(self.lineEdit_sex)
        self.label_tel = QtWidgets.QLabel(self.frame)
        self.label_tel.setObjectName("label_tel")
        self.horizontalLayout.addWidget(self.label_tel)
        self.lineEdit_tel = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_tel.setObjectName("lineEdit_tel")
        self.horizontalLayout.addWidget(self.lineEdit_tel)
        self.label_nationality = QtWidgets.QLabel(self.frame)
        self.label_nationality.setObjectName("label_nationality")
        self.horizontalLayout.addWidget(self.label_nationality)
        self.lineEdit_nationality = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_nationality.setObjectName("lineEdit_nationality")
        self.horizontalLayout.addWidget(self.lineEdit_nationality)
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(410, 100, 267, 52))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_ok = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.horizontalLayout_2.addWidget(self.pushButton_ok)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_cancel = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_2.addWidget(self.pushButton_cancel)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_ID.setText(_translate("Dialog", "身份证号"))
        self.label_name.setText(_translate("Dialog", "姓名"))
        self.label_sex.setText(_translate("Dialog", "性别"))
        self.label_tel.setText(_translate("Dialog", "电话"))
        self.label_nationality.setText(_translate("Dialog", "国籍"))
        self.pushButton_ok.setText(_translate("Dialog", "确定"))
        self.pushButton_cancel.setText(_translate("Dialog", "取消"))


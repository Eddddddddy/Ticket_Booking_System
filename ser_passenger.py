# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ser_passenger.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_ser_passenger(object):
    def setupUi(self, Dialog_ser_passenger):
        Dialog_ser_passenger.setObjectName("Dialog_ser_passenger")
        Dialog_ser_passenger.resize(400, 82)
        self.frame = QtWidgets.QFrame(Dialog_ser_passenger)
        self.frame.setGeometry(QtCore.QRect(10, 20, 391, 52))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(12, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lineEdit_ser_passenger = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_ser_passenger.setMinimumSize(QtCore.QSize(160, 0))
        self.lineEdit_ser_passenger.setObjectName("lineEdit_ser_passenger")
        self.horizontalLayout.addWidget(self.lineEdit_ser_passenger)
        spacerItem1 = QtWidgets.QSpacerItem(23, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_ser_passenger = QtWidgets.QPushButton(self.frame)
        self.pushButton_ser_passenger.setObjectName("pushButton_ser_passenger")
        self.horizontalLayout.addWidget(self.pushButton_ser_passenger)

        self.retranslateUi(Dialog_ser_passenger)
        QtCore.QMetaObject.connectSlotsByName(Dialog_ser_passenger)

    def retranslateUi(self, Dialog_ser_passenger):
        _translate = QtCore.QCoreApplication.translate
        Dialog_ser_passenger.setWindowTitle(_translate("Dialog_ser_passenger", "Dialog"))
        self.label.setText(_translate("Dialog_ser_passenger", "身份证号"))
        self.pushButton_ser_passenger.setText(_translate("Dialog_ser_passenger", "搜索"))


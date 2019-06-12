# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ser_flight.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_ser_flight(object):
    def setupUi(self, Dialog_ser_flight):
        Dialog_ser_flight.setObjectName("Dialog_ser_flight")
        Dialog_ser_flight.resize(400, 83)
        self.frame = QtWidgets.QFrame(Dialog_ser_flight)
        self.frame.setGeometry(QtCore.QRect(10, 4, 391, 61))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(21, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lineEdit_ser_flight = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_ser_flight.setObjectName("lineEdit_ser_flight")
        self.horizontalLayout.addWidget(self.lineEdit_ser_flight)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_ser_flight = QtWidgets.QPushButton(self.frame)
        self.pushButton_ser_flight.setObjectName("pushButton_ser_flight")
        self.horizontalLayout.addWidget(self.pushButton_ser_flight)

        self.retranslateUi(Dialog_ser_flight)
        QtCore.QMetaObject.connectSlotsByName(Dialog_ser_flight)

    def retranslateUi(self, Dialog_ser_flight):
        _translate = QtCore.QCoreApplication.translate
        Dialog_ser_flight.setWindowTitle(_translate("Dialog_ser_flight", "Dialog"))
        self.label.setText(_translate("Dialog_ser_flight", "航班号"))
        self.pushButton_ser_flight.setText(_translate("Dialog_ser_flight", "搜索"))


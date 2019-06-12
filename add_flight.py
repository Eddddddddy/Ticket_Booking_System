# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_flight.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(680, 176)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(20, 20, 641, 73))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_time_l = QtWidgets.QLabel(self.frame)
        self.label_time_l.setObjectName("label_time_l")
        self.gridLayout.addWidget(self.label_time_l, 2, 2, 1, 1)
        self.lineEdit_time_a = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_time_a.setObjectName("lineEdit_time_a")
        self.gridLayout.addWidget(self.lineEdit_time_a, 2, 6, 1, 1)
        self.lineEdit_plane = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_plane.setObjectName("lineEdit_plane")
        self.gridLayout.addWidget(self.lineEdit_plane, 2, 1, 1, 1)
        self.lineEdit_time_l = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_time_l.setObjectName("lineEdit_time_l")
        self.gridLayout.addWidget(self.lineEdit_time_l, 2, 4, 1, 1)
        self.label_time_a = QtWidgets.QLabel(self.frame)
        self.label_time_a.setObjectName("label_time_a")
        self.gridLayout.addWidget(self.label_time_a, 2, 5, 1, 1)
        self.label_flight = QtWidgets.QLabel(self.frame)
        self.label_flight.setObjectName("label_flight")
        self.gridLayout.addWidget(self.label_flight, 0, 0, 1, 1)
        self.label_to_c = QtWidgets.QLabel(self.frame)
        self.label_to_c.setObjectName("label_to_c")
        self.gridLayout.addWidget(self.label_to_c, 0, 2, 1, 2)
        self.lineEdit_flight = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_flight.setObjectName("lineEdit_flight")
        self.gridLayout.addWidget(self.lineEdit_flight, 0, 1, 1, 1)
        self.label_plane = QtWidgets.QLabel(self.frame)
        self.label_plane.setObjectName("label_plane")
        self.gridLayout.addWidget(self.label_plane, 2, 0, 1, 1)
        self.lineEdit_to_c = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_to_c.setObjectName("lineEdit_to_c")
        self.gridLayout.addWidget(self.lineEdit_to_c, 0, 4, 1, 1)
        self.label_from_c = QtWidgets.QLabel(self.frame)
        self.label_from_c.setObjectName("label_from_c")
        self.gridLayout.addWidget(self.label_from_c, 0, 5, 1, 1)
        self.lineEdit_from_c = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_from_c.setObjectName("lineEdit_from_c")
        self.gridLayout.addWidget(self.lineEdit_from_c, 0, 6, 1, 1)
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(200, 110, 261, 52))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_ok = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.horizontalLayout.addWidget(self.pushButton_ok)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_cancel = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout.addWidget(self.pushButton_cancel)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_time_l.setText(_translate("Dialog", "出发时间"))
        self.label_time_a.setText(_translate("Dialog", "到达时间"))
        self.label_flight.setText(_translate("Dialog", "航班号"))
        self.label_to_c.setText(_translate("Dialog", "到达城市"))
        self.label_plane.setText(_translate("Dialog", "机型"))
        self.label_from_c.setText(_translate("Dialog", "出发城市"))
        self.pushButton_ok.setText(_translate("Dialog", "确定"))
        self.pushButton_cancel.setText(_translate("Dialog", "取消"))


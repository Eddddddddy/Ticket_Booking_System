# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1130, 817)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 1109, 802))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_left = QtWidgets.QFrame(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_left.sizePolicy().hasHeightForWidth())
        self.frame_left.setSizePolicy(sizePolicy)
        self.frame_left.setMinimumSize(QtCore.QSize(200, 800))
        self.frame_left.setMaximumSize(QtCore.QSize(200, 800))
        self.frame_left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left.setObjectName("frame_left")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_left)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_flight = QtWidgets.QPushButton(self.frame_left)
        self.button_flight.setMinimumSize(QtCore.QSize(0, 60))
        self.button_flight.setObjectName("button_flight")
        self.verticalLayout.addWidget(self.button_flight)
        self.button_passenger = QtWidgets.QPushButton(self.frame_left)
        self.button_passenger.setMinimumSize(QtCore.QSize(0, 60))
        self.button_passenger.setObjectName("button_passenger")
        self.verticalLayout.addWidget(self.button_passenger)
        self.button_seat = QtWidgets.QPushButton(self.frame_left)
        self.button_seat.setMinimumSize(QtCore.QSize(0, 60))
        self.button_seat.setObjectName("button_seat")
        self.verticalLayout.addWidget(self.button_seat)
        self.button_bill = QtWidgets.QPushButton(self.frame_left)
        self.button_bill.setMinimumSize(QtCore.QSize(0, 60))
        self.button_bill.setObjectName("button_bill")
        self.verticalLayout.addWidget(self.button_bill)
        self.horizontalLayout.addWidget(self.frame_left)
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.table_flight = QtWidgets.QTableWidget(self.page)
        self.table_flight.setGeometry(QtCore.QRect(20, 30, 851, 741))
        self.table_flight.setObjectName("table_flight")
        self.table_flight.setColumnCount(0)
        self.table_flight.setRowCount(0)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.table_passenger = QtWidgets.QTableWidget(self.page_2)
        self.table_passenger.setGeometry(QtCore.QRect(20, 30, 851, 741))
        self.table_passenger.setObjectName("table_passenger")
        self.table_passenger.setColumnCount(0)
        self.table_passenger.setRowCount(0)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.list_flight = QtWidgets.QListWidget(self.page_3)
        self.list_flight.setGeometry(QtCore.QRect(20, 30, 101, 741))
        self.list_flight.setObjectName("list_flight")
        self.frame_seat = QtWidgets.QFrame(self.page_3)
        self.frame_seat.setGeometry(QtCore.QRect(140, 30, 731, 741))
        self.frame_seat.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_seat.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_seat.setObjectName("frame_seat")
        self.frame_seat_l = QtWidgets.QFrame(self.frame_seat)
        self.frame_seat_l.setGeometry(QtCore.QRect(70, 150, 131, 455))
        self.frame_seat_l.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_seat_l.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_seat_l.setObjectName("frame_seat_l")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_seat_l)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_seat_l)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_13, 4, 1, 1, 1)
        self.pushButton_a3 = QtWidgets.QPushButton(self.frame_seat_l)
        self.pushButton_a3.setObjectName("pushButton_a3")
        self.gridLayout.addWidget(self.pushButton_a3, 4, 0, 1, 1)
        self.pushButton_a6 = QtWidgets.QPushButton(self.frame_seat_l)
        self.pushButton_a6.setObjectName("pushButton_a6")
        self.gridLayout.addWidget(self.pushButton_a6, 9, 0, 1, 1)
        self.pushButton_22 = QtWidgets.QPushButton(self.frame_seat_l)
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout.addWidget(self.pushButton_22, 9, 1, 1, 1)
        self.pushButton_B1 = QtWidgets.QPushButton(self.frame_seat_l)
        self.pushButton_B1.setObjectName("pushButton_B1")
        self.gridLayout.addWidget(self.pushButton_B1, 0, 1, 1, 1)
        self.pushButton_20 = QtWidgets.QPushButton(self.frame_seat_l)
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout.addWidget(self.pushButton_20, 8, 2, 1, 1)
        self.pushButton_25 = QtWidgets.QPushButton(self.frame_seat_l)
        self.pushButton_25.setObjectName("pushButton_25")
        self.gridLayout.addWidget(self.pushButton_25, 10, 1, 1, 1)
        self.pushButton_a1 = QtWidgets.QPushButton(self.frame_seat_l)
        self.pushButton_a1.setObjectName("pushButton_a1")
        self.gridLayout.addWidget(self.pushButton_a1, 0, 0, 1, 1)
        self.pushButton_23 = QtWidgets.QPushButton(self.frame_seat_l)
        self.pushButton_23.setObjectName("pushButton_23")
        self.gridLayout.addWidget(self.pushButton_23, 9, 2, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.frame_seat_l)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout.addWidget(self.pushButton_16, 6, 1, 1, 1)
        self.pushButton_a7 = QtWidgets.QPushButton(self.frame_seat_l)
        self.pushButton_a7.setObjectName("pushButton_a7")
        self.gridLayout.addWidget(self.pushButton_a7, 10, 0, 1, 1)
        self.pushButton_a2 = QtWidgets.QPushButton(self.frame_seat_l)
        self.pushButton_a2.setObjectName("pushButton_a2")
        self.gridLayout.addWidget(self.pushButton_a2, 2, 0, 1, 1)
        self.pushButton_a4 = QtWidgets.QPushButton(self.frame_seat_l)
        self.pushButton_a4.setObjectName("pushButton_a4")
        self.gridLayout.addWidget(self.pushButton_a4, 6, 0, 1, 1)
        self.pushButton_19 = QtWidgets.QPushButton(self.frame_seat_l)
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout.addWidget(self.pushButton_19, 8, 1, 1, 1)
        self.pushButton_a5 = QtWidgets.QPushButton(self.frame_seat_l)
        self.pushButton_a5.setObjectName("pushButton_a5")
        self.gridLayout.addWidget(self.pushButton_a5, 8, 0, 1, 1)
        self.pushButton_B2 = QtWidgets.QPushButton(self.frame_seat_l)
        self.pushButton_B2.setObjectName("pushButton_B2")
        self.gridLayout.addWidget(self.pushButton_B2, 2, 1, 1, 1)
        self.pushButton_a10 = QtWidgets.QPushButton(self.frame_seat_l)
        self.pushButton_a10.setObjectName("pushButton_a10")
        self.gridLayout.addWidget(self.pushButton_a10, 16, 0, 1, 1)
        self.pushButton_a9 = QtWidgets.QPushButton(self.frame_seat_l)
        self.pushButton_a9.setObjectName("pushButton_a9")
        self.gridLayout.addWidget(self.pushButton_a9, 15, 0, 1, 1)
        self.pushButton_37 = QtWidgets.QPushButton(self.frame_seat_l)
        self.pushButton_37.setObjectName("pushButton_37")
        self.gridLayout.addWidget(self.pushButton_37, 17, 1, 1, 1)
        self.pushButton_a11 = QtWidgets.QPushButton(self.frame_seat_l)
        self.pushButton_a11.setObjectName("pushButton_a11")
        self.gridLayout.addWidget(self.pushButton_a11, 17, 0, 1, 1)
        self.pushButton_34 = QtWidgets.QPushButton(self.frame_seat_l)
        self.pushButton_34.setObjectName("pushButton_34")
        self.gridLayout.addWidget(self.pushButton_34, 16, 1, 1, 1)
        self.pushButton_28 = QtWidgets.QPushButton(self.frame_seat_l)
        self.pushButton_28.setObjectName("pushButton_28")
        self.gridLayout.addWidget(self.pushButton_28, 13, 1, 1, 1)
        self.pushButton_31 = QtWidgets.QPushButton(self.frame_seat_l)
        self.pushButton_31.setObjectName("pushButton_31")
        self.gridLayout.addWidget(self.pushButton_31, 15, 1, 1, 1)
        self.pushButton_C2 = QtWidgets.QPushButton(self.frame_seat_l)
        self.pushButton_C2.setObjectName("pushButton_C2")
        self.gridLayout.addWidget(self.pushButton_C2, 2, 2, 1, 1)
        self.pushButton_a8 = QtWidgets.QPushButton(self.frame_seat_l)
        self.pushButton_a8.setObjectName("pushButton_a8")
        self.gridLayout.addWidget(self.pushButton_a8, 13, 0, 1, 1)
        self.pushButton_26 = QtWidgets.QPushButton(self.frame_seat_l)
        self.pushButton_26.setObjectName("pushButton_26")
        self.gridLayout.addWidget(self.pushButton_26, 10, 2, 1, 1)
        self.pushButton_29 = QtWidgets.QPushButton(self.frame_seat_l)
        self.pushButton_29.setObjectName("pushButton_29")
        self.gridLayout.addWidget(self.pushButton_29, 13, 2, 1, 1)
        self.pushButton_32 = QtWidgets.QPushButton(self.frame_seat_l)
        self.pushButton_32.setObjectName("pushButton_32")
        self.gridLayout.addWidget(self.pushButton_32, 15, 2, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.frame_seat_l)
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout.addWidget(self.pushButton_17, 6, 2, 1, 1)
        self.pushButton_35 = QtWidgets.QPushButton(self.frame_seat_l)
        self.pushButton_35.setObjectName("pushButton_35")
        self.gridLayout.addWidget(self.pushButton_35, 16, 2, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_seat_l)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout.addWidget(self.pushButton_14, 4, 2, 1, 1)
        self.pushButton_38 = QtWidgets.QPushButton(self.frame_seat_l)
        self.pushButton_38.setObjectName("pushButton_38")
        self.gridLayout.addWidget(self.pushButton_38, 17, 2, 1, 1)
        self.pushButton_C1 = QtWidgets.QPushButton(self.frame_seat_l)
        self.pushButton_C1.setObjectName("pushButton_C1")
        self.gridLayout.addWidget(self.pushButton_C1, 0, 2, 1, 1)
        self.frame_seat_c = QtWidgets.QFrame(self.frame_seat)
        self.frame_seat_c.setGeometry(QtCore.QRect(280, 150, 171, 451))
        self.frame_seat_c.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_seat_c.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_seat_c.setObjectName("frame_seat_c")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_seat_c)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_72 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_72.setObjectName("pushButton_72")
        self.gridLayout_2.addWidget(self.pushButton_72, 8, 1, 1, 1)
        self.pushButton_73 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_73.setObjectName("pushButton_73")
        self.gridLayout_2.addWidget(self.pushButton_73, 8, 2, 1, 1)
        self.pushButton_76 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_76.setObjectName("pushButton_76")
        self.gridLayout_2.addWidget(self.pushButton_76, 9, 1, 1, 1)
        self.pushButton_74 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_74.setObjectName("pushButton_74")
        self.gridLayout_2.addWidget(self.pushButton_74, 8, 3, 1, 1)
        self.pushButton_78 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_78.setObjectName("pushButton_78")
        self.gridLayout_2.addWidget(self.pushButton_78, 9, 3, 1, 1)
        self.pushButton_75 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_75.setObjectName("pushButton_75")
        self.gridLayout_2.addWidget(self.pushButton_75, 9, 0, 1, 1)
        self.pushButton_77 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_77.setObjectName("pushButton_77")
        self.gridLayout_2.addWidget(self.pushButton_77, 9, 2, 1, 1)
        self.pushButton_63 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_63.setObjectName("pushButton_63")
        self.gridLayout_2.addWidget(self.pushButton_63, 6, 0, 1, 1)
        self.pushButton_43 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_43.setObjectName("pushButton_43")
        self.gridLayout_2.addWidget(self.pushButton_43, 1, 1, 1, 1)
        self.pushButton_49 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_49.setObjectName("pushButton_49")
        self.gridLayout_2.addWidget(self.pushButton_49, 1, 3, 1, 1)
        self.pushButton_71 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_71.setObjectName("pushButton_71")
        self.gridLayout_2.addWidget(self.pushButton_71, 8, 0, 1, 1)
        self.pushButton_50 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_50.setObjectName("pushButton_50")
        self.gridLayout_2.addWidget(self.pushButton_50, 2, 2, 1, 1)
        self.pushButton_69 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_69.setObjectName("pushButton_69")
        self.gridLayout_2.addWidget(self.pushButton_69, 7, 2, 1, 1)
        self.pushButton_44 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_44.setObjectName("pushButton_44")
        self.gridLayout_2.addWidget(self.pushButton_44, 2, 1, 1, 1)
        self.pushButton_45 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_45.setObjectName("pushButton_45")
        self.gridLayout_2.addWidget(self.pushButton_45, 3, 0, 1, 1)
        self.pushButton_46 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_46.setObjectName("pushButton_46")
        self.gridLayout_2.addWidget(self.pushButton_46, 0, 2, 1, 1)
        self.pushButton_47 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_47.setObjectName("pushButton_47")
        self.gridLayout_2.addWidget(self.pushButton_47, 0, 3, 1, 1)
        self.pushButton_68 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_68.setObjectName("pushButton_68")
        self.gridLayout_2.addWidget(self.pushButton_68, 7, 1, 1, 1)
        self.pushButton_59 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_59.setObjectName("pushButton_59")
        self.gridLayout_2.addWidget(self.pushButton_59, 5, 0, 1, 1)
        self.pushButton_51 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_51.setObjectName("pushButton_51")
        self.gridLayout_2.addWidget(self.pushButton_51, 2, 3, 1, 1)
        self.pushButton_54 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_54.setObjectName("pushButton_54")
        self.gridLayout_2.addWidget(self.pushButton_54, 3, 3, 1, 1)
        self.pushButton_52 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_52.setObjectName("pushButton_52")
        self.gridLayout_2.addWidget(self.pushButton_52, 3, 1, 1, 1)
        self.pushButton_58 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_58.setObjectName("pushButton_58")
        self.gridLayout_2.addWidget(self.pushButton_58, 4, 3, 1, 1)
        self.pushButton_53 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_53.setObjectName("pushButton_53")
        self.gridLayout_2.addWidget(self.pushButton_53, 3, 2, 1, 1)
        self.pushButton_55 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_55.setObjectName("pushButton_55")
        self.gridLayout_2.addWidget(self.pushButton_55, 4, 0, 1, 1)
        self.pushButton_57 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_57.setObjectName("pushButton_57")
        self.gridLayout_2.addWidget(self.pushButton_57, 4, 2, 1, 1)
        self.pushButton_56 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_56.setObjectName("pushButton_56")
        self.gridLayout_2.addWidget(self.pushButton_56, 4, 1, 1, 1)
        self.pushButton_64 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_64.setObjectName("pushButton_64")
        self.gridLayout_2.addWidget(self.pushButton_64, 6, 1, 1, 1)
        self.pushButton_61 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_61.setObjectName("pushButton_61")
        self.gridLayout_2.addWidget(self.pushButton_61, 5, 2, 1, 1)
        self.pushButton_60 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_60.setObjectName("pushButton_60")
        self.gridLayout_2.addWidget(self.pushButton_60, 5, 1, 1, 1)
        self.pushButton_62 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_62.setObjectName("pushButton_62")
        self.gridLayout_2.addWidget(self.pushButton_62, 5, 3, 1, 1)
        self.pushButton_48 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_48.setObjectName("pushButton_48")
        self.gridLayout_2.addWidget(self.pushButton_48, 1, 2, 1, 1)
        self.pushButton_65 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_65.setObjectName("pushButton_65")
        self.gridLayout_2.addWidget(self.pushButton_65, 6, 2, 1, 1)
        self.pushButton_40 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_40.setObjectName("pushButton_40")
        self.gridLayout_2.addWidget(self.pushButton_40, 1, 0, 1, 1)
        self.pushButton_42 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_42.setObjectName("pushButton_42")
        self.gridLayout_2.addWidget(self.pushButton_42, 0, 1, 1, 1)
        self.pushButton_39 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_39.setObjectName("pushButton_39")
        self.gridLayout_2.addWidget(self.pushButton_39, 0, 0, 1, 1)
        self.pushButton_66 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_66.setObjectName("pushButton_66")
        self.gridLayout_2.addWidget(self.pushButton_66, 6, 3, 1, 1)
        self.pushButton_41 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_41.setObjectName("pushButton_41")
        self.gridLayout_2.addWidget(self.pushButton_41, 2, 0, 1, 1)
        self.pushButton_70 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_70.setObjectName("pushButton_70")
        self.gridLayout_2.addWidget(self.pushButton_70, 7, 3, 1, 1)
        self.pushButton_67 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_67.setObjectName("pushButton_67")
        self.gridLayout_2.addWidget(self.pushButton_67, 7, 0, 1, 1)
        self.pushButton_79 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_79.setObjectName("pushButton_79")
        self.gridLayout_2.addWidget(self.pushButton_79, 10, 0, 1, 1)
        self.pushButton_80 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_80.setObjectName("pushButton_80")
        self.gridLayout_2.addWidget(self.pushButton_80, 10, 1, 1, 1)
        self.pushButton_81 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_81.setObjectName("pushButton_81")
        self.gridLayout_2.addWidget(self.pushButton_81, 10, 2, 1, 1)
        self.pushButton_82 = QtWidgets.QPushButton(self.frame_seat_c)
        self.pushButton_82.setObjectName("pushButton_82")
        self.gridLayout_2.addWidget(self.pushButton_82, 10, 3, 1, 1)
        self.frame_seat_r = QtWidgets.QFrame(self.frame_seat)
        self.frame_seat_r.setGeometry(QtCore.QRect(530, 150, 131, 451))
        self.frame_seat_r.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_seat_r.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_seat_r.setObjectName("frame_seat_r")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_seat_r)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_83 = QtWidgets.QPushButton(self.frame_seat_r)
        self.pushButton_83.setObjectName("pushButton_83")
        self.gridLayout_3.addWidget(self.pushButton_83, 0, 0, 1, 1)
        self.pushButton_85 = QtWidgets.QPushButton(self.frame_seat_r)
        self.pushButton_85.setObjectName("pushButton_85")
        self.gridLayout_3.addWidget(self.pushButton_85, 1, 0, 1, 1)
        self.pushButton_95 = QtWidgets.QPushButton(self.frame_seat_r)
        self.pushButton_95.setObjectName("pushButton_95")
        self.gridLayout_3.addWidget(self.pushButton_95, 8, 0, 1, 1)
        self.pushButton_90 = QtWidgets.QPushButton(self.frame_seat_r)
        self.pushButton_90.setObjectName("pushButton_90")
        self.gridLayout_3.addWidget(self.pushButton_90, 3, 0, 1, 1)
        self.pushButton_92 = QtWidgets.QPushButton(self.frame_seat_r)
        self.pushButton_92.setObjectName("pushButton_92")
        self.gridLayout_3.addWidget(self.pushButton_92, 5, 0, 1, 1)
        self.pushButton_86 = QtWidgets.QPushButton(self.frame_seat_r)
        self.pushButton_86.setObjectName("pushButton_86")
        self.gridLayout_3.addWidget(self.pushButton_86, 1, 1, 1, 1)
        self.pushButton_93 = QtWidgets.QPushButton(self.frame_seat_r)
        self.pushButton_93.setObjectName("pushButton_93")
        self.gridLayout_3.addWidget(self.pushButton_93, 6, 0, 1, 1)
        self.pushButton_91 = QtWidgets.QPushButton(self.frame_seat_r)
        self.pushButton_91.setObjectName("pushButton_91")
        self.gridLayout_3.addWidget(self.pushButton_91, 4, 0, 1, 1)
        self.pushButton_89 = QtWidgets.QPushButton(self.frame_seat_r)
        self.pushButton_89.setObjectName("pushButton_89")
        self.gridLayout_3.addWidget(self.pushButton_89, 2, 0, 1, 1)
        self.pushButton_94 = QtWidgets.QPushButton(self.frame_seat_r)
        self.pushButton_94.setObjectName("pushButton_94")
        self.gridLayout_3.addWidget(self.pushButton_94, 7, 0, 1, 1)
        self.pushButton_88 = QtWidgets.QPushButton(self.frame_seat_r)
        self.pushButton_88.setObjectName("pushButton_88")
        self.gridLayout_3.addWidget(self.pushButton_88, 1, 2, 1, 1)
        self.pushButton_84 = QtWidgets.QPushButton(self.frame_seat_r)
        self.pushButton_84.setObjectName("pushButton_84")
        self.gridLayout_3.addWidget(self.pushButton_84, 0, 1, 1, 1)
        self.pushButton_87 = QtWidgets.QPushButton(self.frame_seat_r)
        self.pushButton_87.setObjectName("pushButton_87")
        self.gridLayout_3.addWidget(self.pushButton_87, 0, 2, 1, 1)
        self.pushButton_96 = QtWidgets.QPushButton(self.frame_seat_r)
        self.pushButton_96.setObjectName("pushButton_96")
        self.gridLayout_3.addWidget(self.pushButton_96, 9, 0, 1, 1)
        self.pushButton_97 = QtWidgets.QPushButton(self.frame_seat_r)
        self.pushButton_97.setObjectName("pushButton_97")
        self.gridLayout_3.addWidget(self.pushButton_97, 10, 0, 1, 1)
        self.pushButton_98 = QtWidgets.QPushButton(self.frame_seat_r)
        self.pushButton_98.setObjectName("pushButton_98")
        self.gridLayout_3.addWidget(self.pushButton_98, 2, 1, 1, 1)
        self.pushButton_99 = QtWidgets.QPushButton(self.frame_seat_r)
        self.pushButton_99.setObjectName("pushButton_99")
        self.gridLayout_3.addWidget(self.pushButton_99, 2, 2, 1, 1)
        self.pushButton_100 = QtWidgets.QPushButton(self.frame_seat_r)
        self.pushButton_100.setObjectName("pushButton_100")
        self.gridLayout_3.addWidget(self.pushButton_100, 3, 1, 1, 1)
        self.pushButton_101 = QtWidgets.QPushButton(self.frame_seat_r)
        self.pushButton_101.setObjectName("pushButton_101")
        self.gridLayout_3.addWidget(self.pushButton_101, 3, 2, 1, 1)
        self.pushButton_102 = QtWidgets.QPushButton(self.frame_seat_r)
        self.pushButton_102.setObjectName("pushButton_102")
        self.gridLayout_3.addWidget(self.pushButton_102, 4, 1, 1, 1)
        self.pushButton_103 = QtWidgets.QPushButton(self.frame_seat_r)
        self.pushButton_103.setObjectName("pushButton_103")
        self.gridLayout_3.addWidget(self.pushButton_103, 4, 2, 1, 1)
        self.pushButton_104 = QtWidgets.QPushButton(self.frame_seat_r)
        self.pushButton_104.setObjectName("pushButton_104")
        self.gridLayout_3.addWidget(self.pushButton_104, 5, 1, 1, 1)
        self.pushButton_105 = QtWidgets.QPushButton(self.frame_seat_r)
        self.pushButton_105.setObjectName("pushButton_105")
        self.gridLayout_3.addWidget(self.pushButton_105, 5, 2, 1, 1)
        self.pushButton_106 = QtWidgets.QPushButton(self.frame_seat_r)
        self.pushButton_106.setObjectName("pushButton_106")
        self.gridLayout_3.addWidget(self.pushButton_106, 6, 1, 1, 1)
        self.pushButton_107 = QtWidgets.QPushButton(self.frame_seat_r)
        self.pushButton_107.setObjectName("pushButton_107")
        self.gridLayout_3.addWidget(self.pushButton_107, 6, 2, 1, 1)
        self.pushButton_108 = QtWidgets.QPushButton(self.frame_seat_r)
        self.pushButton_108.setObjectName("pushButton_108")
        self.gridLayout_3.addWidget(self.pushButton_108, 7, 1, 1, 1)
        self.pushButton_109 = QtWidgets.QPushButton(self.frame_seat_r)
        self.pushButton_109.setObjectName("pushButton_109")
        self.gridLayout_3.addWidget(self.pushButton_109, 7, 2, 1, 1)
        self.pushButton_110 = QtWidgets.QPushButton(self.frame_seat_r)
        self.pushButton_110.setObjectName("pushButton_110")
        self.gridLayout_3.addWidget(self.pushButton_110, 8, 1, 1, 1)
        self.pushButton_111 = QtWidgets.QPushButton(self.frame_seat_r)
        self.pushButton_111.setObjectName("pushButton_111")
        self.gridLayout_3.addWidget(self.pushButton_111, 8, 2, 1, 1)
        self.pushButton_112 = QtWidgets.QPushButton(self.frame_seat_r)
        self.pushButton_112.setObjectName("pushButton_112")
        self.gridLayout_3.addWidget(self.pushButton_112, 9, 1, 1, 1)
        self.pushButton_113 = QtWidgets.QPushButton(self.frame_seat_r)
        self.pushButton_113.setObjectName("pushButton_113")
        self.gridLayout_3.addWidget(self.pushButton_113, 9, 2, 1, 1)
        self.pushButton_114 = QtWidgets.QPushButton(self.frame_seat_r)
        self.pushButton_114.setObjectName("pushButton_114")
        self.gridLayout_3.addWidget(self.pushButton_114, 10, 1, 1, 1)
        self.pushButton_115 = QtWidgets.QPushButton(self.frame_seat_r)
        self.pushButton_115.setObjectName("pushButton_115")
        self.gridLayout_3.addWidget(self.pushButton_115, 10, 2, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.table_bill = QtWidgets.QTableWidget(self.page_4)
        self.table_bill.setGeometry(QtCore.QRect(20, 30, 851, 741))
        self.table_bill.setObjectName("table_bill")
        self.table_bill.setColumnCount(0)
        self.table_bill.setRowCount(0)
        self.stackedWidget.addWidget(self.page_4)
        self.horizontalLayout.addWidget(self.stackedWidget)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.button_flight.setText(_translate("Form", "航班信息"))
        self.button_passenger.setText(_translate("Form", "乘客信息"))
        self.button_seat.setText(_translate("Form", "座位情况"))
        self.button_bill.setText(_translate("Form", "付款信息"))
        self.pushButton_13.setText(_translate("Form", "PushButton"))
        self.pushButton_a3.setText(_translate("Form", "PushButton"))
        self.pushButton_a6.setText(_translate("Form", "PushButton"))
        self.pushButton_22.setText(_translate("Form", "PushButton"))
        self.pushButton_B1.setText(_translate("Form", "PushButton"))
        self.pushButton_20.setText(_translate("Form", "PushButton"))
        self.pushButton_25.setText(_translate("Form", "PushButton"))
        self.pushButton_a1.setText(_translate("Form", "PushButton"))
        self.pushButton_23.setText(_translate("Form", "PushButton"))
        self.pushButton_16.setText(_translate("Form", "PushButton"))
        self.pushButton_a7.setText(_translate("Form", "PushButton"))
        self.pushButton_a2.setText(_translate("Form", "PushButton"))
        self.pushButton_a4.setText(_translate("Form", "PushButton"))
        self.pushButton_19.setText(_translate("Form", "PushButton"))
        self.pushButton_a5.setText(_translate("Form", "PushButton"))
        self.pushButton_B2.setText(_translate("Form", "PushButton"))
        self.pushButton_a10.setText(_translate("Form", "PushButton"))
        self.pushButton_a9.setText(_translate("Form", "PushButton"))
        self.pushButton_37.setText(_translate("Form", "PushButton"))
        self.pushButton_a11.setText(_translate("Form", "PushButton"))
        self.pushButton_34.setText(_translate("Form", "PushButton"))
        self.pushButton_28.setText(_translate("Form", "PushButton"))
        self.pushButton_31.setText(_translate("Form", "PushButton"))
        self.pushButton_C2.setText(_translate("Form", "PushButton"))
        self.pushButton_a8.setText(_translate("Form", "PushButton"))
        self.pushButton_26.setText(_translate("Form", "PushButton"))
        self.pushButton_29.setText(_translate("Form", "PushButton"))
        self.pushButton_32.setText(_translate("Form", "PushButton"))
        self.pushButton_17.setText(_translate("Form", "PushButton"))
        self.pushButton_35.setText(_translate("Form", "PushButton"))
        self.pushButton_14.setText(_translate("Form", "PushButton"))
        self.pushButton_38.setText(_translate("Form", "PushButton"))
        self.pushButton_C1.setText(_translate("Form", "PushButton"))
        self.pushButton_72.setText(_translate("Form", "PushButton"))
        self.pushButton_73.setText(_translate("Form", "PushButton"))
        self.pushButton_76.setText(_translate("Form", "PushButton"))
        self.pushButton_74.setText(_translate("Form", "PushButton"))
        self.pushButton_78.setText(_translate("Form", "PushButton"))
        self.pushButton_75.setText(_translate("Form", "PushButton"))
        self.pushButton_77.setText(_translate("Form", "PushButton"))
        self.pushButton_63.setText(_translate("Form", "PushButton"))
        self.pushButton_43.setText(_translate("Form", "PushButton"))
        self.pushButton_49.setText(_translate("Form", "PushButton"))
        self.pushButton_71.setText(_translate("Form", "PushButton"))
        self.pushButton_50.setText(_translate("Form", "PushButton"))
        self.pushButton_69.setText(_translate("Form", "PushButton"))
        self.pushButton_44.setText(_translate("Form", "PushButton"))
        self.pushButton_45.setText(_translate("Form", "PushButton"))
        self.pushButton_46.setText(_translate("Form", "PushButton"))
        self.pushButton_47.setText(_translate("Form", "PushButton"))
        self.pushButton_68.setText(_translate("Form", "PushButton"))
        self.pushButton_59.setText(_translate("Form", "PushButton"))
        self.pushButton_51.setText(_translate("Form", "PushButton"))
        self.pushButton_54.setText(_translate("Form", "PushButton"))
        self.pushButton_52.setText(_translate("Form", "PushButton"))
        self.pushButton_58.setText(_translate("Form", "PushButton"))
        self.pushButton_53.setText(_translate("Form", "PushButton"))
        self.pushButton_55.setText(_translate("Form", "PushButton"))
        self.pushButton_57.setText(_translate("Form", "PushButton"))
        self.pushButton_56.setText(_translate("Form", "PushButton"))
        self.pushButton_64.setText(_translate("Form", "PushButton"))
        self.pushButton_61.setText(_translate("Form", "PushButton"))
        self.pushButton_60.setText(_translate("Form", "PushButton"))
        self.pushButton_62.setText(_translate("Form", "PushButton"))
        self.pushButton_48.setText(_translate("Form", "PushButton"))
        self.pushButton_65.setText(_translate("Form", "PushButton"))
        self.pushButton_40.setText(_translate("Form", "PushButton"))
        self.pushButton_42.setText(_translate("Form", "PushButton"))
        self.pushButton_39.setText(_translate("Form", "PushButton"))
        self.pushButton_66.setText(_translate("Form", "PushButton"))
        self.pushButton_41.setText(_translate("Form", "PushButton"))
        self.pushButton_70.setText(_translate("Form", "PushButton"))
        self.pushButton_67.setText(_translate("Form", "PushButton"))
        self.pushButton_79.setText(_translate("Form", "PushButton"))
        self.pushButton_80.setText(_translate("Form", "PushButton"))
        self.pushButton_81.setText(_translate("Form", "PushButton"))
        self.pushButton_82.setText(_translate("Form", "PushButton"))
        self.pushButton_83.setText(_translate("Form", "PushButton"))
        self.pushButton_85.setText(_translate("Form", "PushButton"))
        self.pushButton_95.setText(_translate("Form", "PushButton"))
        self.pushButton_90.setText(_translate("Form", "PushButton"))
        self.pushButton_92.setText(_translate("Form", "PushButton"))
        self.pushButton_86.setText(_translate("Form", "PushButton"))
        self.pushButton_93.setText(_translate("Form", "PushButton"))
        self.pushButton_91.setText(_translate("Form", "PushButton"))
        self.pushButton_89.setText(_translate("Form", "PushButton"))
        self.pushButton_94.setText(_translate("Form", "PushButton"))
        self.pushButton_88.setText(_translate("Form", "PushButton"))
        self.pushButton_84.setText(_translate("Form", "PushButton"))
        self.pushButton_87.setText(_translate("Form", "PushButton"))
        self.pushButton_96.setText(_translate("Form", "PushButton"))
        self.pushButton_97.setText(_translate("Form", "PushButton"))
        self.pushButton_98.setText(_translate("Form", "PushButton"))
        self.pushButton_99.setText(_translate("Form", "PushButton"))
        self.pushButton_100.setText(_translate("Form", "PushButton"))
        self.pushButton_101.setText(_translate("Form", "PushButton"))
        self.pushButton_102.setText(_translate("Form", "PushButton"))
        self.pushButton_103.setText(_translate("Form", "PushButton"))
        self.pushButton_104.setText(_translate("Form", "PushButton"))
        self.pushButton_105.setText(_translate("Form", "PushButton"))
        self.pushButton_106.setText(_translate("Form", "PushButton"))
        self.pushButton_107.setText(_translate("Form", "PushButton"))
        self.pushButton_108.setText(_translate("Form", "PushButton"))
        self.pushButton_109.setText(_translate("Form", "PushButton"))
        self.pushButton_110.setText(_translate("Form", "PushButton"))
        self.pushButton_111.setText(_translate("Form", "PushButton"))
        self.pushButton_112.setText(_translate("Form", "PushButton"))
        self.pushButton_113.setText(_translate("Form", "PushButton"))
        self.pushButton_114.setText(_translate("Form", "PushButton"))
        self.pushButton_115.setText(_translate("Form", "PushButton"))

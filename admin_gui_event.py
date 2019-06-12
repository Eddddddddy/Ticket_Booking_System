from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

from admin import Ui_Form
from add_flight import Ui_Dialog
from add_passenger import Ui_Dialog_2
import sql
import time
import datetime


class add_passenger_window(QtWidgets.QWidget,Ui_Dialog_2):
    def __init__(self):
        super(add_passenger_window,self).__init__()
        self.setupUi(self)
        self.pushButton_cancel.clicked.connect(self.button_cancel)

    def button_cancel(self):
        self.hide()

class add_flight_window(QtWidgets.QWidget,Ui_Dialog):
    def __init__(self):
        super(add_flight_window,self).__init__()
        self.setupUi(self)
        self.pushButton_cancel.clicked.connect(self.button_cancel)

    def button_cancel(self):
        self.hide()


class admin_window(QtWidgets.QWidget, Ui_Form):
    flight_item = ''
    def __init__(self):
        super(admin_window, self).__init__()

        self.setupUi(self)

        self.table_flight.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_flight.setHorizontalHeaderLabels(['航班号', '到达城市', '出发城市', '机型', '出发时间', '到达时间', '满座率'])
        self.table_flight.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_passenger.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_passenger.setHorizontalHeaderLabels(['身份证号', '姓名', '性别', '电话', '国籍'])
        self.table_passenger.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_bill.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_bill.setHorizontalHeaderLabels(['身份证号', '姓名', '航班', '价格', '是否付款'])
        self.table_bill.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.button_flight.clicked.connect(self.stackedWidget_1)
        self.button_passenger.clicked.connect(self.stackedWidget_2)
        self.button_seat.clicked.connect(self.stackedWidget_3)
        self.button_bill.clicked.connect(self.stackedWidget_4)
        self.list_flight.itemClicked.connect(self.add_seatMap)
        self.pushButton_a1.clicked.connect(self.seat_button_a1)
        self.pushButton_a2.clicked.connect(self.seat_button_a2)
        self.pushButton_a3.clicked.connect(self.seat_button_a3)
        self.pushButton_a4.clicked.connect(self.seat_button_a4)
        self.pushButton_b1.clicked.connect(self.seat_button_b1)
        self.pushButton_b2.clicked.connect(self.seat_button_b2)
        self.pushButton_b3.clicked.connect(self.seat_button_b3)
        self.pushButton_b4.clicked.connect(self.seat_button_b4)
        self.pushButton_c1.clicked.connect(self.seat_button_c1)
        self.pushButton_c2.clicked.connect(self.seat_button_c2)
        self.pushButton_c3.clicked.connect(self.seat_button_c3)
        self.pushButton_c4.clicked.connect(self.seat_button_c4)
        self.pushButton_e1.clicked.connect(self.seat_button_e1)
        self.pushButton_e2.clicked.connect(self.seat_button_e2)
        self.pushButton_e3.clicked.connect(self.seat_button_e3)
        self.pushButton_e4.clicked.connect(self.seat_button_e4)
        self.pushButton_f1.clicked.connect(self.seat_button_f1)
        self.pushButton_f2.clicked.connect(self.seat_button_f2)
        self.pushButton_f3.clicked.connect(self.seat_button_f3)
        self.pushButton_f4.clicked.connect(self.seat_button_f4)
        self.pushButton_g1.clicked.connect(self.seat_button_g1)
        self.pushButton_g2.clicked.connect(self.seat_button_g2)
        self.pushButton_g3.clicked.connect(self.seat_button_g3)
        self.pushButton_g4.clicked.connect(self.seat_button_g4)
        self.pushButton_h1.clicked.connect(self.seat_button_h1)
        self.pushButton_h2.clicked.connect(self.seat_button_h2)
        self.pushButton_h3.clicked.connect(self.seat_button_h3)
        self.pushButton_h4.clicked.connect(self.seat_button_h4)
        self.pushButton_j1.clicked.connect(self.seat_button_j1)
        self.pushButton_j2.clicked.connect(self.seat_button_j2)
        self.pushButton_j3.clicked.connect(self.seat_button_j3)
        self.pushButton_j4.clicked.connect(self.seat_button_j4)
        self.pushButton_k1.clicked.connect(self.seat_button_k1)
        self.pushButton_k2.clicked.connect(self.seat_button_k2)
        self.pushButton_k3.clicked.connect(self.seat_button_k3)
        self.pushButton_k4.clicked.connect(self.seat_button_k4)
        self.pushButton_l1.clicked.connect(self.seat_button_l1)
        self.pushButton_l2.clicked.connect(self.seat_button_l2)
        self.pushButton_l3.clicked.connect(self.seat_button_l3)
        self.pushButton_l4.clicked.connect(self.seat_button_l4)
        self.pushButton_a5.clicked.connect(self.seat_button_a5)
        self.pushButton_a6.clicked.connect(self.seat_button_a6)
        self.pushButton_a7.clicked.connect(self.seat_button_a7)
        self.pushButton_a8.clicked.connect(self.seat_button_a8)
        self.pushButton_a9.clicked.connect(self.seat_button_a9)
        self.pushButton_b5.clicked.connect(self.seat_button_b5)
        self.pushButton_b6.clicked.connect(self.seat_button_b6)
        self.pushButton_b7.clicked.connect(self.seat_button_b7)
        self.pushButton_b8.clicked.connect(self.seat_button_b8)
        self.pushButton_b9.clicked.connect(self.seat_button_b9)
        self.pushButton_c5.clicked.connect(self.seat_button_c5)
        self.pushButton_c6.clicked.connect(self.seat_button_c6)
        self.pushButton_c7.clicked.connect(self.seat_button_c7)
        self.pushButton_c8.clicked.connect(self.seat_button_c8)
        self.pushButton_c9.clicked.connect(self.seat_button_c9)
        self.pushButton_e5.clicked.connect(self.seat_button_e5)
        self.pushButton_e6.clicked.connect(self.seat_button_e6)
        self.pushButton_e7.clicked.connect(self.seat_button_e7)
        self.pushButton_e8.clicked.connect(self.seat_button_e8)
        self.pushButton_e9.clicked.connect(self.seat_button_e9)
        self.pushButton_f5.clicked.connect(self.seat_button_f5)
        self.pushButton_f6.clicked.connect(self.seat_button_f6)
        self.pushButton_f7.clicked.connect(self.seat_button_f7)
        self.pushButton_f8.clicked.connect(self.seat_button_f8)
        self.pushButton_f9.clicked.connect(self.seat_button_f9)
        self.pushButton_g5.clicked.connect(self.seat_button_g5)
        self.pushButton_g6.clicked.connect(self.seat_button_g6)
        self.pushButton_g7.clicked.connect(self.seat_button_g7)
        self.pushButton_g8.clicked.connect(self.seat_button_g8)
        self.pushButton_g9.clicked.connect(self.seat_button_g9)
        self.pushButton_h5.clicked.connect(self.seat_button_h5)
        self.pushButton_h6.clicked.connect(self.seat_button_h6)
        self.pushButton_h7.clicked.connect(self.seat_button_h7)
        self.pushButton_h8.clicked.connect(self.seat_button_h8)
        self.pushButton_h9.clicked.connect(self.seat_button_h9)
        self.pushButton_j5.clicked.connect(self.seat_button_j5)
        self.pushButton_j6.clicked.connect(self.seat_button_j6)
        self.pushButton_j7.clicked.connect(self.seat_button_j7)
        self.pushButton_j8.clicked.connect(self.seat_button_j8)
        self.pushButton_j9.clicked.connect(self.seat_button_j9)
        self.pushButton_k5.clicked.connect(self.seat_button_k5)
        self.pushButton_k6.clicked.connect(self.seat_button_k6)
        self.pushButton_k7.clicked.connect(self.seat_button_k7)
        self.pushButton_k8.clicked.connect(self.seat_button_k8)
        self.pushButton_k9.clicked.connect(self.seat_button_k9)
        self.pushButton_l5.clicked.connect(self.seat_button_l5)
        self.pushButton_l6.clicked.connect(self.seat_button_l6)
        self.pushButton_l7.clicked.connect(self.seat_button_l7)
        self.pushButton_l8.clicked.connect(self.seat_button_l8)
        self.pushButton_l9.clicked.connect(self.seat_button_l9)
        self.pushButton_l10.clicked.connect(self.seat_button_l10)
        self.pushButton_l11.clicked.connect(self.seat_button_l11)
        self.pushButton_k10.clicked.connect(self.seat_button_k10)
        self.pushButton_k11.clicked.connect(self.seat_button_k11)
        self.pushButton_j10.clicked.connect(self.seat_button_j10)
        self.pushButton_j11.clicked.connect(self.seat_button_j11)
        self.pushButton_h10.clicked.connect(self.seat_button_h10)
        self.pushButton_h11.clicked.connect(self.seat_button_h11)
        self.pushButton_g10.clicked.connect(self.seat_button_g10)
        self.pushButton_g11.clicked.connect(self.seat_button_g11)
        self.pushButton_f10.clicked.connect(self.seat_button_f10)
        self.pushButton_f11.clicked.connect(self.seat_button_f11)
        self.pushButton_e10.clicked.connect(self.seat_button_e10)
        self.pushButton_e11.clicked.connect(self.seat_button_e11)
        self.pushButton_c10.clicked.connect(self.seat_button_c10)
        self.pushButton_c11.clicked.connect(self.seat_button_c11)
        self.pushButton_b10.clicked.connect(self.seat_button_b10)
        self.pushButton_b11.clicked.connect(self.seat_button_b11)
        self.pushButton_a10.clicked.connect(self.seat_button_a10)
        self.pushButton_a11.clicked.connect(self.seat_button_a11)
        self.pushButton_flight_del.clicked.connect(self.flight_del)
        self.pushButton_flight_mod.clicked.connect(self.flight_mod)
        self.pushButton_flight_add.clicked.connect(self.flight_add)

        #self.pushButton_flight_ser.clicked.connect(self.flight_ser)
        self.pushButton_passenger_del.clicked.connect(self.passenger_del)
        self.pushButton_passenger_mod.clicked.connect(self.passenger_mod)
        #self.pushButton_passenger_add.clicked.connect(self.passenger_add)
        #self.pushButton_passenger_ser.clicked.connect(self.passenger_ser)

        self.S = sql.SQL()
        self.add_table_flight()
        self.add_table_passenger()
        self.add_table_bill()
        self.add_list_flight()

    def stackedWidget_1(self):
        self.stackedWidget.setCurrentIndex(0)

    def stackedWidget_2(self):
        self.stackedWidget.setCurrentIndex(1)

    def stackedWidget_3(self):
        self.stackedWidget.setCurrentIndex(2)

    def stackedWidget_4(self):
        self.stackedWidget.setCurrentIndex(3)

    def add_table_flight(self):
        results = self.S.airplane_getAll()
        i = 0
        self.table_flight.clear()
        for row in results:
            self.table_flight.setItem(i, 0, QTableWidgetItem(row[0]))
            self.table_flight.setItem(i, 1, QTableWidgetItem(row[1]))
            self.table_flight.setItem(i, 2, QTableWidgetItem(row[2]))
            self.table_flight.setItem(i, 3, QTableWidgetItem(row[3]))
            self.table_flight.setItem(i, 4, QTableWidgetItem(row[4].strftime("%Y-%m-%d %H:%M:%S")))
            self.table_flight.setItem(i, 5, QTableWidgetItem(row[5].strftime("%Y-%m-%d %H:%M:%S")))
            i = i + 1

    def add_table_passenger(self):
        results = self.S.passenger_getAll()
        i = 0
        self.table_passenger.clear()
        for row in results:
            self.table_passenger.setItem(i, 0, QTableWidgetItem(row[0]))
            self.table_passenger.setItem(i, 1, QTableWidgetItem(row[1]))
            self.table_passenger.setItem(i, 2, QTableWidgetItem(row[2]))
            self.table_passenger.setItem(i, 3, QTableWidgetItem(row[3]))
            self.table_passenger.setItem(i, 4, QTableWidgetItem(row[4]))
            i = i + 1

    def add_table_bill(self):
        result_bill = self.S.bill_getAll()
        i = 0
        self.table_bill.clear()
        for row in result_bill:
            result_flight_no = self.S.reservation_get_backFlight_no(row[0])
            str = ''
            j = 0
            for row_1 in result_flight_no:
                str = str + row_1[j] + ' '
                j = j + 1
            result_name = self.S.passenger_get(row[0])
            for row_1 in result_name:
                str_1 = row_1[1]
            self.table_bill.setItem(i, 0, QTableWidgetItem(row[0]))
            self.table_bill.setItem(i, 1, QTableWidgetItem(str_1))
            self.table_bill.setItem(i, 2, QTableWidgetItem(str))
            self.table_bill.setItem(i, 3, QTableWidgetItem(row[1]))
            self.table_bill.setItem(i, 4, QTableWidgetItem(row[2]))
            i = i + 1

    def add_list_flight(self):
        results = self.S.airplane_getAll()
        self.list_flight.clear()
        for row in results:
            self.list_flight.addItem(row[0])

    def flash_admin(self):
        self.add_list_flight()
        self.add_table_bill()
        self.add_table_passenger()
        self.add_table_flight()

    def add_seatMap(self, item):
        result = self.S.seat_get(item.text())
        self.flight_item = item.text()
        for row in result:
            array = []
            for c in row[1]:
                array.append(c)
            print(array)
            self.pushButton_a1.setText("1") if array[0] == '1' else self.pushButton_a1.setText('0')
            self.pushButton_a2.setText("1") if array[1] == '1' else self.pushButton_a2.setText('0')
            self.pushButton_a3.setText("1") if array[2] == '1' else self.pushButton_a3.setText('0')
            self.pushButton_a4.setText("1") if array[3] == '1' else self.pushButton_a4.setText('0')
            self.pushButton_b1.setText("1") if array[4] == '1' else self.pushButton_b1.setText('0')
            self.pushButton_b2.setText("1") if array[5] == '1' else self.pushButton_b2.setText('0')
            self.pushButton_b3.setText("1") if array[6] == '1' else self.pushButton_b3.setText('0')
            self.pushButton_b4.setText("1") if array[7] == '1' else self.pushButton_b4.setText('0')
            self.pushButton_c1.setText("1") if array[8] == '1' else self.pushButton_c1.setText('0')
            self.pushButton_c2.setText("1") if array[9] == '1' else self.pushButton_c2.setText('0')
            self.pushButton_c3.setText("1") if array[10] == '1' else self.pushButton_c3.setText('0')
            self.pushButton_c4.setText("1") if array[11] == '1' else self.pushButton_c4.setText('0')
            self.pushButton_e1.setText("1") if array[12] == '1' else self.pushButton_e1.setText('0')
            self.pushButton_e2.setText("1") if array[13] == '1' else self.pushButton_e2.setText('0')
            self.pushButton_e3.setText("1") if array[14] == '1' else self.pushButton_e3.setText('0')
            self.pushButton_e4.setText("1") if array[15] == '1' else self.pushButton_e4.setText('0')
            self.pushButton_f1.setText("1") if array[16] == '1' else self.pushButton_f1.setText('0')
            self.pushButton_f2.setText("1") if array[17] == '1' else self.pushButton_f2.setText('0')
            self.pushButton_f3.setText("1") if array[18] == '1' else self.pushButton_f3.setText('0')
            self.pushButton_f4.setText("1") if array[19] == '1' else self.pushButton_f4.setText('0')
            self.pushButton_g1.setText("1") if array[20] == '1' else self.pushButton_g1.setText('0')
            self.pushButton_g2.setText("1") if array[21] == '1' else self.pushButton_g2.setText('0')
            self.pushButton_g3.setText("1") if array[22] == '1' else self.pushButton_g3.setText('0')
            self.pushButton_g4.setText("1") if array[23] == '1' else self.pushButton_g4.setText('0')
            self.pushButton_h1.setText("1") if array[24] == '1' else self.pushButton_h1.setText('0')
            self.pushButton_h2.setText("1") if array[25] == '1' else self.pushButton_h2.setText('0')
            self.pushButton_h3.setText("1") if array[26] == '1' else self.pushButton_h3.setText('0')
            self.pushButton_h4.setText("1") if array[27] == '1' else self.pushButton_h4.setText('0')
            self.pushButton_j1.setText("1") if array[28] == '1' else self.pushButton_j1.setText('0')
            self.pushButton_j2.setText("1") if array[29] == '1' else self.pushButton_j2.setText('0')
            self.pushButton_j3.setText("1") if array[30] == '1' else self.pushButton_j3.setText('0')
            self.pushButton_j4.setText("1") if array[31] == '1' else self.pushButton_j4.setText('0')
            self.pushButton_k1.setText("1") if array[32] == '1' else self.pushButton_k1.setText('0')
            self.pushButton_k2.setText("1") if array[33] == '1' else self.pushButton_k2.setText('0')
            self.pushButton_k3.setText("1") if array[34] == '1' else self.pushButton_k3.setText('0')
            self.pushButton_k4.setText("1") if array[35] == '1' else self.pushButton_k4.setText('0')
            self.pushButton_l1.setText("1") if array[36] == '1' else self.pushButton_l1.setText('0')
            self.pushButton_l2.setText("1") if array[37] == '1' else self.pushButton_l2.setText('0')
            self.pushButton_l3.setText("1") if array[38] == '1' else self.pushButton_l3.setText('0')
            self.pushButton_l4.setText("1") if array[39] == '1' else self.pushButton_l4.setText('0')
            array = []
            for c in row[2]:
                array.append(c)
            print(array)
            self.pushButton_a5.setText("1") if array[0] == '1' else self.pushButton_a5.setText('0')
            self.pushButton_a6.setText("1") if array[1] == '1' else self.pushButton_a6.setText('0')
            self.pushButton_a7.setText("1") if array[2] == '1' else self.pushButton_a7.setText('0')
            self.pushButton_a8.setText("1") if array[3] == '1' else self.pushButton_a8.setText('0')
            self.pushButton_a9.setText("1") if array[4] == '1' else self.pushButton_a9.setText('0')
            self.pushButton_a10.setText("1") if array[5] == '1' else self.pushButton_a10.setText('0')
            self.pushButton_a11.setText("1") if array[6] == '1' else self.pushButton_a11.setText('0')
            self.pushButton_b5.setText("1") if array[7] == '1' else self.pushButton_b5.setText('0')
            self.pushButton_b6.setText("1") if array[8] == '1' else self.pushButton_b6.setText('0')
            self.pushButton_b7.setText("1") if array[9] == '1' else self.pushButton_b7.setText('0')
            self.pushButton_b8.setText("1") if array[10] == '1' else self.pushButton_b8.setText('0')
            self.pushButton_b9.setText("1") if array[11] == '1' else self.pushButton_b9.setText('0')
            self.pushButton_b10.setText("1") if array[12] == '1' else self.pushButton_b10.setText('0')
            self.pushButton_b11.setText("1") if array[13] == '1' else self.pushButton_b11.setText('0')
            self.pushButton_c5.setText("1") if array[14] == '1' else self.pushButton_c5.setText('0')
            self.pushButton_c6.setText("1") if array[15] == '1' else self.pushButton_c6.setText('0')
            self.pushButton_c7.setText("1") if array[16] == '1' else self.pushButton_c7.setText('0')
            self.pushButton_c8.setText("1") if array[17] == '1' else self.pushButton_c8.setText('0')
            self.pushButton_c9.setText("1") if array[18] == '1' else self.pushButton_c9.setText('0')
            self.pushButton_c10.setText("1") if array[19] == '1' else self.pushButton_c10.setText('0')
            self.pushButton_c11.setText("1") if array[20] == '1' else self.pushButton_c11.setText('0')
            self.pushButton_e5.setText("1") if array[21] == '1' else self.pushButton_e5.setText('0')
            self.pushButton_e6.setText("1") if array[22] == '1' else self.pushButton_e6.setText('0')
            self.pushButton_e7.setText("1") if array[23] == '1' else self.pushButton_e7.setText('0')
            self.pushButton_e8.setText("1") if array[24] == '1' else self.pushButton_e8.setText('0')
            self.pushButton_e9.setText("1") if array[25] == '1' else self.pushButton_e9.setText('0')
            self.pushButton_e10.setText("1") if array[26] == '1' else self.pushButton_e10.setText('0')
            self.pushButton_e11.setText("1") if array[27] == '1' else self.pushButton_e11.setText('0')
            self.pushButton_f5.setText("1") if array[28] == '1' else self.pushButton_f5.setText('0')
            self.pushButton_f6.setText("1") if array[29] == '1' else self.pushButton_f6.setText('0')
            self.pushButton_f7.setText("1") if array[30] == '1' else self.pushButton_f7.setText('0')
            self.pushButton_f8.setText("1") if array[31] == '1' else self.pushButton_f8.setText('0')
            self.pushButton_f9.setText("1") if array[32] == '1' else self.pushButton_f9.setText('0')
            self.pushButton_f10.setText("1") if array[33] == '1' else self.pushButton_f10.setText('0')
            self.pushButton_f11.setText("1") if array[34] == '1' else self.pushButton_f11.setText('0')
            self.pushButton_g5.setText("1") if array[35] == '1' else self.pushButton_g5.setText('0')
            self.pushButton_g6.setText("1") if array[36] == '1' else self.pushButton_g6.setText('0')
            self.pushButton_g7.setText("1") if array[37] == '1' else self.pushButton_g7.setText('0')
            self.pushButton_g8.setText("1") if array[38] == '1' else self.pushButton_g8.setText('0')
            self.pushButton_g9.setText("1") if array[39] == '1' else self.pushButton_g9.setText('0')
            self.pushButton_g10.setText("1") if array[40] == '1' else self.pushButton_g10.setText('0')
            self.pushButton_g11.setText("1") if array[41] == '1' else self.pushButton_g11.setText('0')
            self.pushButton_h5.setText("1") if array[42] == '1' else self.pushButton_h5.setText('0')
            self.pushButton_h6.setText("1") if array[43] == '1' else self.pushButton_h6.setText('0')
            self.pushButton_h7.setText("1") if array[44] == '1' else self.pushButton_h7.setText('0')
            self.pushButton_h8.setText("1") if array[45] == '1' else self.pushButton_h8.setText('0')
            self.pushButton_h9.setText("1") if array[46] == '1' else self.pushButton_h9.setText('0')
            self.pushButton_h10.setText("1") if array[47] == '1' else self.pushButton_h10.setText('0')
            self.pushButton_h11.setText("1") if array[48] == '1' else self.pushButton_h11.setText('0')
            self.pushButton_j5.setText("1") if array[49] == '1' else self.pushButton_j5.setText('0')
            self.pushButton_j6.setText("1") if array[50] == '1' else self.pushButton_j6.setText('0')
            self.pushButton_j7.setText("1") if array[51] == '1' else self.pushButton_j7.setText('0')
            self.pushButton_j8.setText("1") if array[52] == '1' else self.pushButton_j8.setText('0')
            self.pushButton_j9.setText("1") if array[53] == '1' else self.pushButton_j9.setText('0')
            self.pushButton_j10.setText("1") if array[54] == '1' else self.pushButton_j10.setText('0')
            self.pushButton_j11.setText("1") if array[55] == '1' else self.pushButton_j11.setText('0')
            self.pushButton_k5.setText("1") if array[56] == '1' else self.pushButton_k5.setText('0')
            self.pushButton_k6.setText("1") if array[57] == '1' else self.pushButton_k6.setText('0')
            self.pushButton_k7.setText("1") if array[58] == '1' else self.pushButton_k7.setText('0')
            self.pushButton_k8.setText("1") if array[59] == '1' else self.pushButton_k8.setText('0')
            self.pushButton_k9.setText("1") if array[60] == '1' else self.pushButton_k9.setText('0')
            self.pushButton_k10.setText("1") if array[61] == '1' else self.pushButton_k10.setText('0')
            self.pushButton_k11.setText("1") if array[62] == '1' else self.pushButton_k11.setText('0')
            self.pushButton_l5.setText("1") if array[63] == '1' else self.pushButton_l5.setText('0')
            self.pushButton_l6.setText("1") if array[64] == '1' else self.pushButton_l6.setText('0')
            self.pushButton_l7.setText("1") if array[65] == '1' else self.pushButton_l7.setText('0')
            self.pushButton_l8.setText("1") if array[66] == '1' else self.pushButton_l8.setText('0')
            self.pushButton_l9.setText("1") if array[67] == '1' else self.pushButton_l9.setText('0')
            self.pushButton_l10.setText("1") if array[68] == '1' else self.pushButton_l10.setText('0')
            self.pushButton_l11.setText("1") if array[69] == '1' else self.pushButton_l11.setText('0')

    def saveSeat(self):
        array_a = []
        array_b = []
        array_a.append(self.pushButton_a1.text())
        array_a.append(self.pushButton_a2.text())
        array_a.append(self.pushButton_a3.text())
        array_a.append(self.pushButton_a4.text())
        array_a.append(self.pushButton_b1.text())
        array_a.append(self.pushButton_b2.text())
        array_a.append(self.pushButton_b3.text())
        array_a.append(self.pushButton_b4.text())
        array_a.append(self.pushButton_c1.text())
        array_a.append(self.pushButton_c2.text())
        array_a.append(self.pushButton_c3.text())
        array_a.append(self.pushButton_c4.text())
        array_a.append(self.pushButton_e1.text())
        array_a.append(self.pushButton_e2.text())
        array_a.append(self.pushButton_e3.text())
        array_a.append(self.pushButton_e4.text())
        array_a.append(self.pushButton_f1.text())
        array_a.append(self.pushButton_f2.text())
        array_a.append(self.pushButton_f3.text())
        array_a.append(self.pushButton_f4.text())
        array_a.append(self.pushButton_g1.text())
        array_a.append(self.pushButton_g2.text())
        array_a.append(self.pushButton_g3.text())
        array_a.append(self.pushButton_g4.text())
        array_a.append(self.pushButton_h1.text())
        array_a.append(self.pushButton_h2.text())
        array_a.append(self.pushButton_h3.text())
        array_a.append(self.pushButton_h4.text())
        array_a.append(self.pushButton_j1.text())
        array_a.append(self.pushButton_j2.text())
        array_a.append(self.pushButton_j3.text())
        array_a.append(self.pushButton_j4.text())
        array_a.append(self.pushButton_k1.text())
        array_a.append(self.pushButton_k2.text())
        array_a.append(self.pushButton_k3.text())
        array_a.append(self.pushButton_k4.text())
        array_a.append(self.pushButton_l1.text())
        array_a.append(self.pushButton_l2.text())
        array_a.append(self.pushButton_l3.text())
        array_a.append(self.pushButton_l4.text())
        array_b.append(self.pushButton_a5.text())
        array_b.append(self.pushButton_a6.text())
        array_b.append(self.pushButton_a7.text())
        array_b.append(self.pushButton_a8.text())
        array_b.append(self.pushButton_a9.text())
        array_b.append(self.pushButton_a10.text())
        array_b.append(self.pushButton_a11.text())
        array_b.append(self.pushButton_b5.text())
        array_b.append(self.pushButton_b6.text())
        array_b.append(self.pushButton_b7.text())
        array_b.append(self.pushButton_b8.text())
        array_b.append(self.pushButton_b9.text())
        array_b.append(self.pushButton_b10.text())
        array_b.append(self.pushButton_b11.text())
        array_b.append(self.pushButton_c5.text())
        array_b.append(self.pushButton_c6.text())
        array_b.append(self.pushButton_c7.text())
        array_b.append(self.pushButton_c8.text())
        array_b.append(self.pushButton_c9.text())
        array_b.append(self.pushButton_c10.text())
        array_b.append(self.pushButton_c11.text())
        array_b.append(self.pushButton_e5.text())
        array_b.append(self.pushButton_e6.text())
        array_b.append(self.pushButton_e7.text())
        array_b.append(self.pushButton_e8.text())
        array_b.append(self.pushButton_e9.text())
        array_b.append(self.pushButton_e10.text())
        array_b.append(self.pushButton_e11.text())
        array_b.append(self.pushButton_f5.text())
        array_b.append(self.pushButton_f6.text())
        array_b.append(self.pushButton_f7.text())
        array_b.append(self.pushButton_f8.text())
        array_b.append(self.pushButton_f9.text())
        array_b.append(self.pushButton_f10.text())
        array_b.append(self.pushButton_f11.text())
        array_b.append(self.pushButton_g5.text())
        array_b.append(self.pushButton_g6.text())
        array_b.append(self.pushButton_g7.text())
        array_b.append(self.pushButton_g8.text())
        array_b.append(self.pushButton_g9.text())
        array_b.append(self.pushButton_g10.text())
        array_b.append(self.pushButton_g11.text())
        array_b.append(self.pushButton_h5.text())
        array_b.append(self.pushButton_h6.text())
        array_b.append(self.pushButton_h7.text())
        array_b.append(self.pushButton_h8.text())
        array_b.append(self.pushButton_h9.text())
        array_b.append(self.pushButton_h10.text())
        array_b.append(self.pushButton_h11.text())
        array_b.append(self.pushButton_j5.text())
        array_b.append(self.pushButton_j6.text())
        array_b.append(self.pushButton_j7.text())
        array_b.append(self.pushButton_j8.text())
        array_b.append(self.pushButton_j9.text())
        array_b.append(self.pushButton_j10.text())
        array_b.append(self.pushButton_j11.text())
        array_b.append(self.pushButton_k5.text())
        array_b.append(self.pushButton_k6.text())
        array_b.append(self.pushButton_k7.text())
        array_b.append(self.pushButton_k8.text())
        array_b.append(self.pushButton_k9.text())
        array_b.append(self.pushButton_k10.text())
        array_b.append(self.pushButton_k11.text())
        array_b.append(self.pushButton_l5.text())
        array_b.append(self.pushButton_l6.text())
        array_b.append(self.pushButton_l7.text())
        array_b.append(self.pushButton_l8.text())
        array_b.append(self.pushButton_l9.text())
        array_b.append(self.pushButton_l10.text())
        array_b.append(self.pushButton_l11.text())

        s_a = ''.join('%s' % a for a in array_a)
        s_b = ''.join('%s' % a for a in array_b)
        self.S.save_seat(self.flight_item, s_a, s_b)

    def flight_del(self):
        row = self.table_flight.currentRow()
        print(self.table_flight.item(row, 0).text())
        self.S.del_flight(self.table_flight.item(row, 0).text())
        self.flash_admin()

    def flight_mod(self):
        row = self.table_flight.currentRow()
        self.S.mod_flight(self.table_flight.item(row, 0).text(),
                          self.table_flight.item(row, 1).text(),
                          self.table_flight.item(row, 2).text(),
                          self.table_flight.item(row, 3).text(),
                          self.table_flight.item(row, 4).text(),
                          self.table_flight.item(row, 5).text())
        self.flash_admin()

    def in_flight_win(self,flight_win):
        self.add_flight_win=flight_win

    def in_passenger_win(self,passenger_win):
        self.add_passenger_win=passenger_win

    def flight_add(self):
        self.add_flight_win.lineEdit_time_a.clear()
        self.add_flight_win.lineEdit_time_l.clear()
        self.add_flight_win.lineEdit_plane.clear()
        self.add_flight_win.lineEdit_from_c.clear()
        self.add_flight_win.lineEdit_to_c.clear()
        self.add_flight_win.lineEdit_flight.clear()
        self.add_flight_win.show()
        self.add_flight_win.pushButton_ok.clicked.connect(self.flight_add_2)

    def flight_add_2(self):
        self.S.airplane_add(self.add_flight_win.lineEdit_flight.text(),
                            self.add_flight_win.lineEdit_to_c.text(),
                            self.add_flight_win.lineEdit_from_c.text(),
                            self.add_flight_win.lineEdit_plane.text(),
                            self.add_flight_win.lineEdit_time_l.text(),
                            self.add_flight_win.lineEdit_time_a.text())
        self.S.seat_add(self.add_flight_win.lineEdit_flight.text(),
                        '0000011000000001011100010000000011110000',
                        '0000000000000000000000100000001111000000000000000000000000000000000000',
                        '2600',
                        '2800')
        self.add_flight_win.hide()
        self.flash_admin()

    def passenger_del(self):
        row = self.table_passenger.currentRow()
        print(self.table_passenger.item(row, 0).text())
        self.S.del_passenger(self.table_passenger.item(row, 0).text())
        self.flash_admin()

    def passenger_mod(self):
        row = self.table_passenger.currentRow()
        self.S.mod_passenger(self.table_passenger.item(row, 0).text(),
                             self.table_passenger.item(row, 1).text(),
                             self.table_passenger.item(row, 2).text(),
                             self.table_passenger.item(row, 3).text(),
                             self.table_passenger.item(row, 4).text(),
                             self.table_passenger.item(row, 5).text())
        self.flash_admin()

    def seat_button_a1(self):
        self.pushButton_a1.setText("0") if self.pushButton_a1.text() == '1' else self.pushButton_a1.setText('1')
        self.saveSeat()

    def seat_button_a2(self):
        self.pushButton_a2.setText("0") if self.pushButton_a2.text() == '1' else self.pushButton_a2.setText('1')
        self.saveSeat()

    def seat_button_a3(self):
        self.pushButton_a3.setText("0") if self.pushButton_a3.text() == '1' else self.pushButton_a3.setText('1')
        self.saveSeat()

    def seat_button_a4(self):
        self.pushButton_a4.setText("0") if self.pushButton_a4.text() == '1' else self.pushButton_a4.setText('1')
        self.saveSeat()

    def seat_button_a5(self):
        self.pushButton_a5.setText("0") if self.pushButton_a5.text() == '1' else self.pushButton_a5.setText('1')
        self.saveSeat()

    def seat_button_a6(self):
        self.pushButton_a6.setText("0") if self.pushButton_a6.text() == '1' else self.pushButton_a6.setText('1')
        self.saveSeat()

    def seat_button_a7(self):
        self.pushButton_a7.setText("0") if self.pushButton_a7.text() == '1' else self.pushButton_a7.setText('1')
        self.saveSeat()

    def seat_button_a8(self):
        self.pushButton_a8.setText("0") if self.pushButton_a8.text() == '1' else self.pushButton_a8.setText('1')
        self.saveSeat()

    def seat_button_a9(self):
        self.pushButton_a9.setText("0") if self.pushButton_a9.text() == '1' else self.pushButton_a9.setText('1')
        self.saveSeat()

    def seat_button_a10(self):
        self.pushButton_a10.setText("0") if self.pushButton_a10.text() == '1' else self.pushButton_a10.setText('1')
        self.saveSeat()

    def seat_button_a11(self):
        self.pushButton_a11.setText("0") if self.pushButton_a11.text() == '1' else self.pushButton_a11.setText('1')
        self.saveSeat()

    def seat_button_b1(self):
        self.pushButton_b1.setText("0") if self.pushButton_b1.text() == '1' else self.pushButton_b1.setText('1')
        self.saveSeat()

    def seat_button_b2(self):
        self.pushButton_b2.setText("0") if self.pushButton_b2.text() == '1' else self.pushButton_b2.setText('1')
        self.saveSeat()

    def seat_button_b3(self):
        self.pushButton_b3.setText("0") if self.pushButton_b3.text() == '1' else self.pushButton_b3.setText('1')
        self.saveSeat()

    def seat_button_b4(self):
        self.pushButton_b4.setText("0") if self.pushButton_b4.text() == '1' else self.pushButton_b4.setText('1')
        self.saveSeat()

    def seat_button_b5(self):
        self.pushButton_b5.setText("0") if self.pushButton_b5.text() == '1' else self.pushButton_b5.setText('1')
        self.saveSeat()

    def seat_button_b6(self):
        self.pushButton_b6.setText("0") if self.pushButton_b6.text() == '1' else self.pushButton_b6.setText('1')
        self.saveSeat()

    def seat_button_b7(self):
        self.pushButton_b7.setText("0") if self.pushButton_b7.text() == '1' else self.pushButton_b7.setText('1')
        self.saveSeat()

    def seat_button_b8(self):
        self.pushButton_b8.setText("0") if self.pushButton_b8.text() == '1' else self.pushButton_b8.setText('1')
        self.saveSeat()

    def seat_button_b9(self):
        self.pushButton_b9.setText("0") if self.pushButton_b9.text() == '1' else self.pushButton_b9.setText('1')
        self.saveSeat()

    def seat_button_b10(self):
        self.pushButton_b10.setText("0") if self.pushButton_b10.text() == '1' else self.pushButton_b10.setText('1')
        self.saveSeat()

    def seat_button_b11(self):
        self.pushButton_b11.setText("0") if self.pushButton_b11.text() == '1' else self.pushButton_b11.setText('1')
        self.saveSeat()

    def seat_button_c1(self):
        self.pushButton_c1.setText("0") if self.pushButton_c1.text() == '1' else self.pushButton_c1.setText('1')
        self.saveSeat()

    def seat_button_c2(self):
        self.pushButton_c2.setText("0") if self.pushButton_c2.text() == '1' else self.pushButton_c2.setText('1')
        self.saveSeat()

    def seat_button_c3(self):
        self.pushButton_c3.setText("0") if self.pushButton_c3.text() == '1' else self.pushButton_c3.setText('1')
        self.saveSeat()

    def seat_button_c4(self):
        self.pushButton_c4.setText("0") if self.pushButton_c4.text() == '1' else self.pushButton_c4.setText('1')
        self.saveSeat()

    def seat_button_c5(self):
        self.pushButton_c5.setText("0") if self.pushButton_c5.text() == '1' else self.pushButton_c5.setText('1')
        self.saveSeat()

    def seat_button_c6(self):
        self.pushButton_c6.setText("0") if self.pushButton_c6.text() == '1' else self.pushButton_c6.setText('1')
        self.saveSeat()

    def seat_button_c7(self):
        self.pushButton_c7.setText("0") if self.pushButton_c7.text() == '1' else self.pushButton_c7.setText('1')
        self.saveSeat()

    def seat_button_c8(self):
        self.pushButton_c8.setText("0") if self.pushButton_c8.text() == '1' else self.pushButton_c8.setText('1')
        self.saveSeat()

    def seat_button_c9(self):
        self.pushButton_c9.setText("0") if self.pushButton_c9.text() == '1' else self.pushButton_c9.setText('1')
        self.saveSeat()

    def seat_button_c10(self):
        self.pushButton_c10.setText("0") if self.pushButton_c10.text() == '1' else self.pushButton_c10.setText('1')
        self.saveSeat()

    def seat_button_c11(self):
        self.pushButton_c11.setText("0") if self.pushButton_c11.text() == '1' else self.pushButton_c11.setText('1')
        self.saveSeat()

    def seat_button_e1(self):
        self.pushButton_e1.setText("0") if self.pushButton_e1.text() == '1' else self.pushButton_e1.setText('1')
        self.saveSeat()

    def seat_button_e2(self):
        self.pushButton_e2.setText("0") if self.pushButton_e2.text() == '1' else self.pushButton_e2.setText('1')
        self.saveSeat()

    def seat_button_e3(self):
        self.pushButton_e3.setText("0") if self.pushButton_e3.text() == '1' else self.pushButton_e3.setText('1')
        self.saveSeat()

    def seat_button_e4(self):
        self.pushButton_e4.setText("0") if self.pushButton_e4.text() == '1' else self.pushButton_e4.setText('1')
        self.saveSeat()

    def seat_button_e5(self):
        self.pushButton_e5.setText("0") if self.pushButton_e5.text() == '1' else self.pushButton_e5.setText('1')
        self.saveSeat()

    def seat_button_e6(self):
        self.pushButton_e6.setText("0") if self.pushButton_e6.text() == '1' else self.pushButton_e6.setText('1')
        self.saveSeat()

    def seat_button_e7(self):
        self.pushButton_e7.setText("0") if self.pushButton_e7.text() == '1' else self.pushButton_e7.setText('1')
        self.saveSeat()

    def seat_button_e8(self):
        self.pushButton_e8.setText("0") if self.pushButton_e8.text() == '1' else self.pushButton_e8.setText('1')
        self.saveSeat()

    def seat_button_e9(self):
        self.pushButton_e9.setText("0") if self.pushButton_e9.text() == '1' else self.pushButton_e9.setText('1')
        self.saveSeat()

    def seat_button_e10(self):
        self.pushButton_e10.setText("0") if self.pushButton_e10.text() == '1' else self.pushButton_e10.setText('1')
        self.saveSeat()

    def seat_button_e11(self):
        self.pushButton_e11.setText("0") if self.pushButton_e11.text() == '1' else self.pushButton_e11.setText('1')
        self.saveSeat()

    def seat_button_f1(self):
        self.pushButton_f1.setText("0") if self.pushButton_f1.text() == '1' else self.pushButton_f1.setText('1')
        self.saveSeat()

    def seat_button_f2(self):
        self.pushButton_f2.setText("0") if self.pushButton_f2.text() == '1' else self.pushButton_f2.setText('1')
        self.saveSeat()

    def seat_button_f3(self):
        self.pushButton_f3.setText("0") if self.pushButton_f3.text() == '1' else self.pushButton_f3.setText('1')
        self.saveSeat()

    def seat_button_f4(self):
        self.pushButton_f4.setText("0") if self.pushButton_f4.text() == '1' else self.pushButton_f4.setText('1')
        self.saveSeat()

    def seat_button_f5(self):
        self.pushButton_f5.setText("0") if self.pushButton_f5.text() == '1' else self.pushButton_f5.setText('1')
        self.saveSeat()

    def seat_button_f6(self):
        self.pushButton_f6.setText("0") if self.pushButton_f6.text() == '1' else self.pushButton_f6.setText('1')
        self.saveSeat()

    def seat_button_f7(self):
        self.pushButton_f7.setText("0") if self.pushButton_f7.text() == '1' else self.pushButton_f7.setText('1')
        self.saveSeat()

    def seat_button_f8(self):
        self.pushButton_f8.setText("0") if self.pushButton_f8.text() == '1' else self.pushButton_f8.setText('1')
        self.saveSeat()

    def seat_button_f9(self):
        self.pushButton_f9.setText("0") if self.pushButton_f9.text() == '1' else self.pushButton_f9.setText('1')
        self.saveSeat()

    def seat_button_f10(self):
        self.pushButton_f10.setText("0") if self.pushButton_f10.text() == '1' else self.pushButton_f10.setText('1')
        self.saveSeat()

    def seat_button_f11(self):
        self.pushButton_f11.setText("0") if self.pushButton_f11.text() == '1' else self.pushButton_f11.setText('1')
        self.saveSeat()

    def seat_button_g1(self):
        self.pushButton_g1.setText("0") if self.pushButton_g1.text() == '1' else self.pushButton_g1.setText('1')
        self.saveSeat()

    def seat_button_g2(self):
        self.pushButton_g2.setText("0") if self.pushButton_g2.text() == '1' else self.pushButton_g2.setText('1')
        self.saveSeat()

    def seat_button_g3(self):
        self.pushButton_g3.setText("0") if self.pushButton_g3.text() == '1' else self.pushButton_g3.setText('1')
        self.saveSeat()

    def seat_button_g4(self):
        self.pushButton_g4.setText("0") if self.pushButton_g4.text() == '1' else self.pushButton_g4.setText('1')
        self.saveSeat()

    def seat_button_g5(self):
        self.pushButton_g5.setText("0") if self.pushButton_g5.text() == '1' else self.pushButton_g5.setText('1')
        self.saveSeat()

    def seat_button_g6(self):
        self.pushButton_g6.setText("0") if self.pushButton_g6.text() == '1' else self.pushButton_g6.setText('1')
        self.saveSeat()

    def seat_button_g7(self):
        self.pushButton_g7.setText("0") if self.pushButton_g7.text() == '1' else self.pushButton_g7.setText('1')
        self.saveSeat()

    def seat_button_g8(self):
        self.pushButton_g8.setText("0") if self.pushButton_g8.text() == '1' else self.pushButton_g8.setText('1')
        self.saveSeat()

    def seat_button_g9(self):
        self.pushButton_g9.setText("0") if self.pushButton_g9.text() == '1' else self.pushButton_g9.setText('1')
        self.saveSeat()

    def seat_button_g10(self):
        self.pushButton_g10.setText("0") if self.pushButton_g10.text() == '1' else self.pushButton_g10.setText('1')
        self.saveSeat()

    def seat_button_g11(self):
        self.pushButton_g11.setText("0") if self.pushButton_g11.text() == '1' else self.pushButton_g11.setText('1')
        self.saveSeat()

    def seat_button_h1(self):
        self.pushButton_h1.setText("0") if self.pushButton_h1.text() == '1' else self.pushButton_h1.setText('1')
        self.saveSeat()

    def seat_button_h2(self):
        self.pushButton_h2.setText("0") if self.pushButton_h2.text() == '1' else self.pushButton_h2.setText('1')
        self.saveSeat()

    def seat_button_h3(self):
        self.pushButton_h3.setText("0") if self.pushButton_h3.text() == '1' else self.pushButton_h3.setText('1')
        self.saveSeat()

    def seat_button_h4(self):
        self.pushButton_h4.setText("0") if self.pushButton_h4.text() == '1' else self.pushButton_h4.setText('1')
        self.saveSeat()

    def seat_button_h5(self):
        self.pushButton_h5.setText("0") if self.pushButton_h5.text() == '1' else self.pushButton_h5.setText('1')
        self.saveSeat()

    def seat_button_h6(self):
        self.pushButton_h6.setText("0") if self.pushButton_h6.text() == '1' else self.pushButton_h6.setText('1')
        self.saveSeat()

    def seat_button_h7(self):
        self.pushButton_h7.setText("0") if self.pushButton_h7.text() == '1' else self.pushButton_h7.setText('1')
        self.saveSeat()

    def seat_button_h8(self):
        self.pushButton_h8.setText("0") if self.pushButton_h8.text() == '1' else self.pushButton_h8.setText('1')
        self.saveSeat()

    def seat_button_h9(self):
        self.pushButton_h9.setText("0") if self.pushButton_h9.text() == '1' else self.pushButton_h9.setText('1')
        self.saveSeat()

    def seat_button_h10(self):
        self.pushButton_h10.setText("0") if self.pushButton_h10.text() == '1' else self.pushButton_h10.setText('1')
        self.saveSeat()

    def seat_button_h11(self):
        self.pushButton_h11.setText("0") if self.pushButton_h11.text() == '1' else self.pushButton_h11.setText('1')
        self.saveSeat()

    def seat_button_j1(self):
        self.pushButton_j1.setText("0") if self.pushButton_j1.text() == '1' else self.pushButton_j1.setText('1')
        self.saveSeat()

    def seat_button_j2(self):
        self.pushButton_j2.setText("0") if self.pushButton_j2.text() == '1' else self.pushButton_j2.setText('1')
        self.saveSeat()

    def seat_button_j3(self):
        self.pushButton_j3.setText("0") if self.pushButton_j3.text() == '1' else self.pushButton_j3.setText('1')
        self.saveSeat()

    def seat_button_j4(self):
        self.pushButton_j4.setText("0") if self.pushButton_j4.text() == '1' else self.pushButton_j4.setText('1')
        self.saveSeat()

    def seat_button_j5(self):
        self.pushButton_j5.setText("0") if self.pushButton_j5.text() == '1' else self.pushButton_j5.setText('1')
        self.saveSeat()

    def seat_button_j6(self):
        self.pushButton_j6.setText("0") if self.pushButton_j6.text() == '1' else self.pushButton_j6.setText('1')
        self.saveSeat()

    def seat_button_j7(self):
        self.pushButton_j7.setText("0") if self.pushButton_j7.text() == '1' else self.pushButton_j7.setText('1')
        self.saveSeat()

    def seat_button_j8(self):
        self.pushButton_j8.setText("0") if self.pushButton_j8.text() == '1' else self.pushButton_j8.setText('1')
        self.saveSeat()

    def seat_button_j9(self):
        self.pushButton_j9.setText("0") if self.pushButton_j9.text() == '1' else self.pushButton_j9.setText('1')
        self.saveSeat()

    def seat_button_j10(self):
        self.pushButton_j10.setText("0") if self.pushButton_j10.text() == '1' else self.pushButton_j10.setText('1')
        self.saveSeat()

    def seat_button_j11(self):
        self.pushButton_j11.setText("0") if self.pushButton_j11.text() == '1' else self.pushButton_j11.setText('1')
        self.saveSeat()

    def seat_button_k1(self):
        self.pushButton_k1.setText("0") if self.pushButton_k1.text() == '1' else self.pushButton_k1.setText('1')
        self.saveSeat()

    def seat_button_k2(self):
        self.pushButton_k2.setText("0") if self.pushButton_k2.text() == '1' else self.pushButton_k2.setText('1')
        self.saveSeat()

    def seat_button_k3(self):
        self.pushButton_k3.setText("0") if self.pushButton_k3.text() == '1' else self.pushButton_k3.setText('1')
        self.saveSeat()

    def seat_button_k4(self):
        self.pushButton_k4.setText("0") if self.pushButton_k4.text() == '1' else self.pushButton_k4.setText('1')
        self.saveSeat()

    def seat_button_k5(self):
        self.pushButton_k5.setText("0") if self.pushButton_k5.text() == '1' else self.pushButton_k5.setText('1')
        self.saveSeat()

    def seat_button_k6(self):
        self.pushButton_k6.setText("0") if self.pushButton_k6.text() == '1' else self.pushButton_k6.setText('1')
        self.saveSeat()

    def seat_button_k7(self):
        self.pushButton_k7.setText("0") if self.pushButton_k7.text() == '1' else self.pushButton_k7.setText('1')
        self.saveSeat()

    def seat_button_k8(self):
        self.pushButton_k8.setText("0") if self.pushButton_k8.text() == '1' else self.pushButton_k8.setText('1')
        self.saveSeat()

    def seat_button_k9(self):
        self.pushButton_k9.setText("0") if self.pushButton_k9.text() == '1' else self.pushButton_k9.setText('1')
        self.saveSeat()

    def seat_button_k10(self):
        self.pushButton_k10.setText("0") if self.pushButton_k10.text() == '1' else self.pushButton_k10.setText('1')
        self.saveSeat()

    def seat_button_k11(self):
        self.pushButton_k11.setText("0") if self.pushButton_k11.text() == '1' else self.pushButton_k11.setText('1')
        self.saveSeat()

    def seat_button_l1(self):
        self.pushButton_l1.setText("0") if self.pushButton_l1.text() == '1' else self.pushButton_l1.setText('1')
        self.saveSeat()

    def seat_button_l2(self):
        self.pushButton_l2.setText("0") if self.pushButton_l2.text() == '1' else self.pushButton_l2.setText('1')
        self.saveSeat()

    def seat_button_l3(self):
        self.pushButton_l3.setText("0") if self.pushButton_l3.text() == '1' else self.pushButton_l3.setText('1')
        self.saveSeat()

    def seat_button_l4(self):
        self.pushButton_l4.setText("0") if self.pushButton_l4.text() == '1' else self.pushButton_l4.setText('1')
        self.saveSeat()

    def seat_button_l5(self):
        self.pushButton_l5.setText("0") if self.pushButton_l5.text() == '1' else self.pushButton_l5.setText('1')
        self.saveSeat()

    def seat_button_l6(self):
        self.pushButton_l6.setText("0") if self.pushButton_l6.text() == '1' else self.pushButton_l6.setText('1')
        self.saveSeat()

    def seat_button_l7(self):
        self.pushButton_l7.setText("0") if self.pushButton_l7.text() == '1' else self.pushButton_l7.setText('1')
        self.saveSeat()

    def seat_button_l8(self):
        self.pushButton_l8.setText("0") if self.pushButton_l8.text() == '1' else self.pushButton_l8.setText('1')
        self.saveSeat()

    def seat_button_l9(self):
        self.pushButton_l9.setText("0") if self.pushButton_l9.text() == '1' else self.pushButton_l9.setText('1')
        self.saveSeat()

    def seat_button_l10(self):
        self.pushButton_l10.setText("0") if self.pushButton_l10.text() == '1' else self.pushButton_l10.setText('1')
        self.saveSeat()

    def seat_button_l11(self):
        self.pushButton_l11.setText("0") if self.pushButton_l11.text() == '1' else self.pushButton_l11.setText('1')
        self.saveSeat()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    admin_win = admin_window()
    add_flight_win=add_flight_window()
    add_passenger_win=add_passenger_window()

    admin_win.show()
    admin_win.in_flight_win(add_flight_win)
    admin_win.in_passenger_win(add_passenger_win)

    sys.exit(app.exec_())

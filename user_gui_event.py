from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

from user import Ui_Form_user
from ser_flight import Ui_Dialog_ser_flight
import sql
import time
import datetime


class ser_flight_window(QtWidgets.QWidget, Ui_Dialog_ser_flight):
    def __init__(self):
        super(ser_flight_window, self).__init__()
        self.setupUi(self)


class user_window(QtWidgets.QWidget, Ui_Form_user):
    flight_item = ''
    state = '0'
    inf_name = ''
    inf_ID = ''
    inf_sex = ''
    inf_tel = ''
    inf_nationality = ''

    def __init__(self):
        super(user_window, self).__init__()

        self.setupUi(self)

        self.table_flight.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_flight.setHorizontalHeaderLabels(['航班号', '到达城市', '出发城市', '机型', '出发时间', '到达时间', '满座率'])
        self.table_flight.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.stackedWidget_4()

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
        self.pushButton_flight_ser.clicked.connect(self.flight_ser)
        self.pushButton_buy_submit.clicked.connect(self.buy_submit)
        self.pushButton_inf_submit.clicked.connect(self.inf_submit)

        self.S = sql.SQL()
        self.add_table_flight()

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
            seat = self.S.seat_get(row[0])
            seat_ab = 0
            print(seat)
            for row_seat in seat:
                for c in row_seat[1]:
                    if c == '1':
                        seat_ab = seat_ab + 1
                for c in row_seat[2]:
                    if c == '1':
                        seat_ab = seat_ab + 1
            self.table_flight.setItem(i, 6, QTableWidgetItem(str(int(seat_ab * 100 / 110)) + '%'))
            print(seat_ab)
            i = i + 1

    def add_list_flight(self):
        results = self.S.airplane_getAll()
        self.list_flight.clear()
        for row in results:
            self.list_flight.addItem(row[0])

    def flash_admin(self):
        self.add_list_flight()
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

    def in_flight_ser_win(self, flight_ser_win):
        self.ser_flight_win = flight_ser_win

    def flight_ser(self):
        self.ser_flight_win.show()
        self.ser_flight_win.pushButton_ser_flight.clicked.connect(self.flight_ser_2)

    def flight_ser_2(self):
        i = 0
        str = self.ser_flight_win.lineEdit_ser_flight.text()
        while i < 100:
            if str == self.table_flight.item(i, 0).text():
                self.table_flight.selectRow(i)
                break
            i = i + 1
        self.ser_flight_win.hide()

    def buy_submit(self):

        try:
            self.S.reservation_add(self.lineEdit_inf_ID.text(), self.flight_item, self.state)
        except Exception:
            pass

        print(self.lineEdit_inf_ID.text())
        # try:
        #     self.S.mod_reservation(self.lineEdit_inf_ID.text(), self.flight_item, self.state)
        # except Exception:
        #     self.S.reservation_add(self.lineEdit_inf_ID.text(), self.flight_item, self.state)
        self.print_bill()
        self.add_table_flight()

    def inf_submit(self):
        self.inf_name = self.lineEdit_inf_name.text()
        self.inf_ID = self.lineEdit_inf_ID.text()
        self.inf_sex = self.lineEdit_inf_sex.text()
        self.inf_tel = self.lineEdit_inf_tel.text()
        self.inf_nationality = self.lineEdit_inf_nationality
        try:
            self.S.passenger_add(self.inf_ID, self.inf_name, self.inf_sex, self.inf_tel, self.inf_nationality)
        except Exception:
            pass
        self.print_bill()

    def print_bill(self):
        self.label_notice_name.setText(self.inf_name)
        self.label_notice_tel.setText(self.inf_tel)
        print(((self.S.get_reservation_bill(self.inf_ID))[0])[0])
        self.label_notice_total.setText(str(((self.S.get_reservation_bill(self.inf_ID))[0])[0]))
        strr=''
        for a in (self.S.reservation_get_backFlight_no_seat(self.inf_ID)):
            strr=strr+str(a)+' '
        self.label_notice_flight.setText(strr)


    def seat_button_a1(self):
        if self.state == 'A1':
            self.pushButton_a1.setText("0") if self.pushButton_a1.text() == '1' else self.pushButton_a1.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_a1.setText("0") if self.pushButton_a1.text() == '1' else self.pushButton_a1.setText('1')
            self.saveSeat()
            self.state = 'A1'

    def seat_button_a2(self):
        if self.state == 'A2':
            self.pushButton_a2.setText("0") if self.pushButton_a2.text() == '1' else self.pushButton_a2.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_a2.setText("0") if self.pushButton_a2.text() == '1' else self.pushButton_a2.setText('1')
            self.saveSeat()
            self.state = 'A2'

    def seat_button_a3(self):
        if self.state == 'A3':
            self.pushButton_a3.setText("0") if self.pushButton_a3.text() == '1' else self.pushButton_a3.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_a3.setText("0") if self.pushButton_a3.text() == '1' else self.pushButton_a3.setText('1')
            self.saveSeat()
            self.state = 'A3'

    def seat_button_a4(self):
        if self.state == 'A4':
            self.pushButton_a4.setText("0") if self.pushButton_a4.text() == '1' else self.pushButton_a4.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_a4.setText("0") if self.pushButton_a4.text() == '1' else self.pushButton_a4.setText('1')
            self.saveSeat()
            self.state = 'A4'

    def seat_button_a5(self):
        if self.state == 'A5':
            self.pushButton_a5.setText("0") if self.pushButton_a5.text() == '1' else self.pushButton_a5.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_a5.setText("0") if self.pushButton_a5.text() == '1' else self.pushButton_a5.setText('1')
            self.saveSeat()
            self.state = 'A5'

    def seat_button_a6(self):
        if self.state == 'A6':
            self.pushButton_a6.setText("0") if self.pushButton_a6.text() == '1' else self.pushButton_a6.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_a6.setText("0") if self.pushButton_a6.text() == '1' else self.pushButton_a6.setText('1')
            self.saveSeat()
            self.state = 'A6'

    def seat_button_a7(self):
        if self.state == 'A7':
            self.pushButton_a7.setText("0") if self.pushButton_a7.text() == '1' else self.pushButton_a7.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_a7.setText("0") if self.pushButton_a7.text() == '1' else self.pushButton_a7.setText('1')
            self.saveSeat()
            self.state = 'A7'

    def seat_button_a8(self):
        if self.state == 'A8':
            self.pushButton_a8.setText("0") if self.pushButton_a8.text() == '1' else self.pushButton_a8.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_a8.setText("0") if self.pushButton_a8.text() == '1' else self.pushButton_a8.setText('1')
            self.saveSeat()
            self.state = 'A8'

    def seat_button_a9(self):
        if self.state == 'A9':
            self.pushButton_a9.setText("0") if self.pushButton_a9.text() == '1' else self.pushButton_a9.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_a9.setText("0") if self.pushButton_a9.text() == '1' else self.pushButton_a9.setText('1')
            self.saveSeat()
            self.state = 'A9'

    def seat_button_a10(self):
        if self.state == 'A10':
            self.pushButton_a10.setText("0") if self.pushButton_a10.text() == '1' else self.pushButton_a10.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_a10.setText("0") if self.pushButton_a10.text() == '1' else self.pushButton_a10.setText('1')
            self.saveSeat()
            self.state = 'A10'

    def seat_button_a11(self):
        if self.state == 'A11':
            self.pushButton_a11.setText("0") if self.pushButton_a11.text() == '1' else self.pushButton_a11.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_a11.setText("0") if self.pushButton_a11.text() == '1' else self.pushButton_a11.setText('1')
            self.saveSeat()
            self.state = 'A11'

    def seat_button_b1(self):
        if self.state == 'B1':
            self.pushButton_b1.setText("0") if self.pushButton_b1.text() == '1' else self.pushButton_b1.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_b1.setText("0") if self.pushButton_b1.text() == '1' else self.pushButton_b1.setText('1')
            self.saveSeat()
            self.state = 'B1'

    def seat_button_b2(self):
        if self.state == 'B2':
            self.pushButton_b2.setText("0") if self.pushButton_b2.text() == '1' else self.pushButton_b2.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_b2.setText("0") if self.pushButton_b2.text() == '1' else self.pushButton_b2.setText('1')
            self.saveSeat()
            self.state = 'B2'

    def seat_button_b3(self):
        if self.state == 'B3':
            self.pushButton_b3.setText("0") if self.pushButton_b3.text() == '1' else self.pushButton_b3.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_b3.setText("0") if self.pushButton_b3.text() == '1' else self.pushButton_b3.setText('1')
            self.saveSeat()
            self.state = 'B3'

    def seat_button_b4(self):
        if self.state == 'B4':
            self.pushButton_b4.setText("0") if self.pushButton_b4.text() == '1' else self.pushButton_b4.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_b4.setText("0") if self.pushButton_b4.text() == '1' else self.pushButton_b4.setText('1')
            self.saveSeat()
            self.state = 'B4'

    def seat_button_b5(self):
        if self.state == 'B5':
            self.pushButton_b5.setText("0") if self.pushButton_b5.text() == '1' else self.pushButton_b5.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_b5.setText("0") if self.pushButton_b5.text() == '1' else self.pushButton_b5.setText('1')
            self.saveSeat()
            self.state = 'B5'

    def seat_button_b6(self):
        if self.state == 'B6':
            self.pushButton_b6.setText("0") if self.pushButton_b6.text() == '1' else self.pushButton_b6.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_b6.setText("0") if self.pushButton_b6.text() == '1' else self.pushButton_b6.setText('1')
            self.saveSeat()
            self.state = 'B6'

    def seat_button_b7(self):
        if self.state == 'B7':
            self.pushButton_b7.setText("0") if self.pushButton_b7.text() == '1' else self.pushButton_b7.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_b7.setText("0") if self.pushButton_b7.text() == '1' else self.pushButton_b7.setText('1')
            self.saveSeat()
            self.state = 'B7'

    def seat_button_b8(self):
        if self.state == 'B8':
            self.pushButton_b8.setText("0") if self.pushButton_b8.text() == '1' else self.pushButton_b8.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_b8.setText("0") if self.pushButton_b8.text() == '1' else self.pushButton_b8.setText('1')
            self.saveSeat()
            self.state = 'B8'

    def seat_button_b9(self):
        if self.state == 'B9':
            self.pushButton_b9.setText("0") if self.pushButton_b9.text() == '1' else self.pushButton_b9.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_b9.setText("0") if self.pushButton_b9.text() == '1' else self.pushButton_b9.setText('1')
            self.saveSeat()
            self.state = 'B9'

    def seat_button_b10(self):
        if self.state == 'B10':
            self.pushButton_b10.setText("0") if self.pushButton_b10.text() == '1' else self.pushButton_b10.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_b10.setText("0") if self.pushButton_b10.text() == '1' else self.pushButton_b10.setText('1')
            self.saveSeat()
            self.state = 'B10'

    def seat_button_b11(self):
        if self.state == 'B11':
            self.pushButton_b11.setText("0") if self.pushButton_b11.text() == '1' else self.pushButton_b11.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_b11.setText("0") if self.pushButton_b11.text() == '1' else self.pushButton_b11.setText('1')
            self.saveSeat()
            self.state = 'B11'

    def seat_button_c1(self):
        if self.state == 'C1':
            self.pushButton_c1.setText("0") if self.pushButton_c1.text() == '1' else self.pushButton_c1.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_c1.setText("0") if self.pushButton_c1.text() == '1' else self.pushButton_c1.setText('1')
            self.saveSeat()
            self.state = 'C1'

    def seat_button_c2(self):
        if self.state == 'C2':
            self.pushButton_c2.setText("0") if self.pushButton_c2.text() == '1' else self.pushButton_c2.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_c2.setText("0") if self.pushButton_c2.text() == '1' else self.pushButton_c2.setText('1')
            self.saveSeat()
            self.state = 'C2'

    def seat_button_c3(self):
        if self.state == 'C3':
            self.pushButton_c3.setText("0") if self.pushButton_c3.text() == '1' else self.pushButton_c3.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_c3.setText("0") if self.pushButton_c3.text() == '1' else self.pushButton_c3.setText('1')
            self.saveSeat()
            self.state = 'C3'

    def seat_button_c4(self):
        if self.state == 'C4':
            self.pushButton_c4.setText("0") if self.pushButton_c4.text() == '1' else self.pushButton_c4.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_c4.setText("0") if self.pushButton_c4.text() == '1' else self.pushButton_c4.setText('1')
            self.saveSeat()
            self.state = 'C4'

    def seat_button_c5(self):
        if self.state == 'C5':
            self.pushButton_c5.setText("0") if self.pushButton_c5.text() == '1' else self.pushButton_c5.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_c5.setText("0") if self.pushButton_c5.text() == '1' else self.pushButton_c5.setText('1')
            self.saveSeat()
            self.state = 'C5'

    def seat_button_c6(self):
        if self.state == 'C6':
            self.pushButton_c6.setText("0") if self.pushButton_c6.text() == '1' else self.pushButton_c6.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_c6.setText("0") if self.pushButton_c6.text() == '1' else self.pushButton_c6.setText('1')
            self.saveSeat()
            self.state = 'C6'

    def seat_button_c7(self):
        if self.state == 'C7':
            self.pushButton_c7.setText("0") if self.pushButton_c7.text() == '1' else self.pushButton_c7.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_c7.setText("0") if self.pushButton_c7.text() == '1' else self.pushButton_c7.setText('1')
            self.saveSeat()
            self.state = 'C7'

    def seat_button_c8(self):
        if self.state == 'C8':
            self.pushButton_c8.setText("0") if self.pushButton_c8.text() == '1' else self.pushButton_c8.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_c8.setText("0") if self.pushButton_c8.text() == '1' else self.pushButton_c8.setText('1')
            self.saveSeat()
            self.state = 'C8'

    def seat_button_c9(self):
        if self.state == 'C9':
            self.pushButton_c9.setText("0") if self.pushButton_c9.text() == '1' else self.pushButton_c9.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_c9.setText("0") if self.pushButton_c9.text() == '1' else self.pushButton_c9.setText('1')
            self.saveSeat()
            self.state = 'C9'

    def seat_button_c10(self):
        if self.state == 'C10':
            self.pushButton_c10.setText("0") if self.pushButton_c10.text() == '1' else self.pushButton_c10.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_c10.setText("0") if self.pushButton_c10.text() == '1' else self.pushButton_c10.setText('1')
            self.saveSeat()
            self.state = 'C10'

    def seat_button_c11(self):
        if self.state == 'C11':
            self.pushButton_c11.setText("0") if self.pushButton_c11.text() == '1' else self.pushButton_c11.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_c11.setText("0") if self.pushButton_c11.text() == '1' else self.pushButton_c11.setText('1')
            self.saveSeat()
            self.state = 'C11'

    def seat_button_e1(self):
        if self.state == 'E1':
            self.pushButton_e1.setText("0") if self.pushButton_e1.text() == '1' else self.pushButton_e1.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_e1.setText("0") if self.pushButton_e1.text() == '1' else self.pushButton_e1.setText('1')
            self.saveSeat()
            self.state = 'E1'

    def seat_button_e2(self):
        if self.state == 'E2':
            self.pushButton_e2.setText("0") if self.pushButton_e2.text() == '1' else self.pushButton_e2.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_e2.setText("0") if self.pushButton_e2.text() == '1' else self.pushButton_e2.setText('1')
            self.saveSeat()
            self.state = 'E2'

    def seat_button_e3(self):
        if self.state == 'E3':
            self.pushButton_e3.setText("0") if self.pushButton_e3.text() == '1' else self.pushButton_e3.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_e3.setText("0") if self.pushButton_e3.text() == '1' else self.pushButton_e3.setText('1')
            self.saveSeat()
            self.state = 'E3'

    def seat_button_e4(self):
        if self.state == 'E4':
            self.pushButton_e4.setText("0") if self.pushButton_e4.text() == '1' else self.pushButton_e4.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_e4.setText("0") if self.pushButton_e4.text() == '1' else self.pushButton_e4.setText('1')
            self.saveSeat()
            self.state = 'E4'

    def seat_button_e5(self):
        if self.state == 'E5':
            self.pushButton_e5.setText("0") if self.pushButton_e5.text() == '1' else self.pushButton_e5.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_e5.setText("0") if self.pushButton_e5.text() == '1' else self.pushButton_e5.setText('1')
            self.saveSeat()
            self.state = 'E5'

    def seat_button_e6(self):
        if self.state == 'E6':
            self.pushButton_e6.setText("0") if self.pushButton_e6.text() == '1' else self.pushButton_e6.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_e6.setText("0") if self.pushButton_e6.text() == '1' else self.pushButton_e6.setText('1')
            self.saveSeat()
            self.state = 'E6'

    def seat_button_e7(self):
        if self.state == 'E7':
            self.pushButton_e7.setText("0") if self.pushButton_e7.text() == '1' else self.pushButton_e7.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_e7.setText("0") if self.pushButton_e7.text() == '1' else self.pushButton_e7.setText('1')
            self.saveSeat()
            self.state = 'E7'

    def seat_button_e8(self):
        if self.state == 'E8':
            self.pushButton_e8.setText("0") if self.pushButton_e8.text() == '1' else self.pushButton_e8.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_e8.setText("0") if self.pushButton_e8.text() == '1' else self.pushButton_e8.setText('1')
            self.saveSeat()
            self.state = 'E8'

    def seat_button_e9(self):
        if self.state == 'E9':
            self.pushButton_e9.setText("0") if self.pushButton_e9.text() == '1' else self.pushButton_e9.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_e9.setText("0") if self.pushButton_e9.text() == '1' else self.pushButton_e9.setText('1')
            self.saveSeat()
            self.state = 'E9'

    def seat_button_e10(self):
        if self.state == 'E10':
            self.pushButton_e10.setText("0") if self.pushButton_e10.text() == '1' else self.pushButton_e10.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_e10.setText("0") if self.pushButton_e10.text() == '1' else self.pushButton_e10.setText('1')
            self.saveSeat()
            self.state = 'E10'

    def seat_button_e11(self):
        if self.state == 'E11':
            self.pushButton_e11.setText("0") if self.pushButton_e11.text() == '1' else self.pushButton_e11.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_e11.setText("0") if self.pushButton_e11.text() == '1' else self.pushButton_e11.setText('1')
            self.saveSeat()
            self.state = 'E11'

    def seat_button_f1(self):
        if self.state == 'F1':
            self.pushButton_f1.setText("0") if self.pushButton_f1.text() == '1' else self.pushButton_f1.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_f1.setText("0") if self.pushButton_f1.text() == '1' else self.pushButton_f1.setText('1')
            self.saveSeat()
            self.state = 'F1'

    def seat_button_f2(self):
        if self.state == 'F2':
            self.pushButton_f2.setText("0") if self.pushButton_f2.text() == '1' else self.pushButton_f2.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_f2.setText("0") if self.pushButton_f2.text() == '1' else self.pushButton_f2.setText('1')
            self.saveSeat()
            self.state = 'F2'

    def seat_button_f3(self):
        if self.state == 'F3':
            self.pushButton_f3.setText("0") if self.pushButton_f3.text() == '1' else self.pushButton_f3.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_f3.setText("0") if self.pushButton_f3.text() == '1' else self.pushButton_f3.setText('1')
            self.saveSeat()
            self.state = 'F3'

    def seat_button_f4(self):
        if self.state == 'F4':
            self.pushButton_f4.setText("0") if self.pushButton_f4.text() == '1' else self.pushButton_f4.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_f4.setText("0") if self.pushButton_f4.text() == '1' else self.pushButton_f4.setText('1')
            self.saveSeat()
            self.state = 'F4'

    def seat_button_f5(self):
        if self.state == 'F5':
            self.pushButton_f5.setText("0") if self.pushButton_f5.text() == '1' else self.pushButton_f5.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_f5.setText("0") if self.pushButton_f5.text() == '1' else self.pushButton_f5.setText('1')
            self.saveSeat()
            self.state = 'F5'

    def seat_button_f6(self):
        if self.state == 'F6':
            self.pushButton_f6.setText("0") if self.pushButton_f6.text() == '1' else self.pushButton_f6.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_f6.setText("0") if self.pushButton_f6.text() == '1' else self.pushButton_f6.setText('1')
            self.saveSeat()
            self.state = 'F6'

    def seat_button_f7(self):
        if self.state == 'F7':
            self.pushButton_f7.setText("0") if self.pushButton_f7.text() == '1' else self.pushButton_f7.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_f7.setText("0") if self.pushButton_f7.text() == '1' else self.pushButton_f7.setText('1')
            self.saveSeat()
            self.state = 'F7'

    def seat_button_f8(self):
        if self.state == 'F8':
            self.pushButton_f8.setText("0") if self.pushButton_f8.text() == '1' else self.pushButton_f8.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_f8.setText("0") if self.pushButton_f8.text() == '1' else self.pushButton_f8.setText('1')
            self.saveSeat()
            self.state = 'F8'

    def seat_button_f9(self):
        if self.state == 'F9':
            self.pushButton_f9.setText("0") if self.pushButton_f9.text() == '1' else self.pushButton_f9.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_f9.setText("0") if self.pushButton_f9.text() == '1' else self.pushButton_f9.setText('1')
            self.saveSeat()
            self.state = 'F9'

    def seat_button_f10(self):
        if self.state == 'F10':
            self.pushButton_f10.setText("0") if self.pushButton_f10.text() == '1' else self.pushButton_f10.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_f10.setText("0") if self.pushButton_f10.text() == '1' else self.pushButton_f10.setText('1')
            self.saveSeat()
            self.state = 'F10'

    def seat_button_f11(self):
        if self.state == 'F11':
            self.pushButton_f11.setText("0") if self.pushButton_f11.text() == '1' else self.pushButton_f11.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_f11.setText("0") if self.pushButton_f11.text() == '1' else self.pushButton_f11.setText('1')
            self.saveSeat()
            self.state = 'F11'

    def seat_button_g1(self):
        if self.state == 'G1':
            self.pushButton_g1.setText("0") if self.pushButton_g1.text() == '1' else self.pushButton_g1.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_g1.setText("0") if self.pushButton_g1.text() == '1' else self.pushButton_g1.setText('1')
            self.saveSeat()
            self.state = 'G1'

    def seat_button_g2(self):
        if self.state == 'G2':
            self.pushButton_g2.setText("0") if self.pushButton_g2.text() == '1' else self.pushButton_g2.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_g2.setText("0") if self.pushButton_g2.text() == '1' else self.pushButton_g2.setText('1')
            self.saveSeat()
            self.state = 'G2'

    def seat_button_g3(self):
        if self.state == 'G3':
            self.pushButton_g3.setText("0") if self.pushButton_g3.text() == '1' else self.pushButton_g3.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_g3.setText("0") if self.pushButton_g3.text() == '1' else self.pushButton_g3.setText('1')
            self.saveSeat()
            self.state = 'G3'

    def seat_button_g4(self):
        if self.state == 'G4':
            self.pushButton_g4.setText("0") if self.pushButton_g4.text() == '1' else self.pushButton_g4.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_g4.setText("0") if self.pushButton_g4.text() == '1' else self.pushButton_g4.setText('1')
            self.saveSeat()
            self.state = 'G4'

    def seat_button_g5(self):
        if self.state == 'G5':
            self.pushButton_g5.setText("0") if self.pushButton_g5.text() == '1' else self.pushButton_g5.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_g5.setText("0") if self.pushButton_g5.text() == '1' else self.pushButton_g5.setText('1')
            self.saveSeat()
            self.state = 'G5'

    def seat_button_g6(self):
        if self.state == 'G6':
            self.pushButton_g6.setText("0") if self.pushButton_g6.text() == '1' else self.pushButton_g6.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_g6.setText("0") if self.pushButton_g6.text() == '1' else self.pushButton_g6.setText('1')
            self.saveSeat()
            self.state = 'G6'

    def seat_button_g7(self):
        if self.state == 'G7':
            self.pushButton_g7.setText("0") if self.pushButton_g7.text() == '1' else self.pushButton_g7.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_g7.setText("0") if self.pushButton_g7.text() == '1' else self.pushButton_g7.setText('1')
            self.saveSeat()
            self.state = 'G7'

    def seat_button_g8(self):
        if self.state == 'G8':
            self.pushButton_g8.setText("0") if self.pushButton_g8.text() == '1' else self.pushButton_g8.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_g8.setText("0") if self.pushButton_g8.text() == '1' else self.pushButton_g8.setText('1')
            self.saveSeat()
            self.state = 'G8'

    def seat_button_g9(self):
        if self.state == 'G9':
            self.pushButton_g9.setText("0") if self.pushButton_g9.text() == '1' else self.pushButton_g9.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_g9.setText("0") if self.pushButton_g9.text() == '1' else self.pushButton_g9.setText('1')
            self.saveSeat()
            self.state = 'G9'

    def seat_button_g10(self):
        if self.state == 'G10':
            self.pushButton_g10.setText("0") if self.pushButton_g10.text() == '1' else self.pushButton_g10.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_g10.setText("0") if self.pushButton_g10.text() == '1' else self.pushButton_g10.setText('1')
            self.saveSeat()
            self.state = 'G10'

    def seat_button_g11(self):
        if self.state == 'G11':
            self.pushButton_g11.setText("0") if self.pushButton_g11.text() == '1' else self.pushButton_g11.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_g11.setText("0") if self.pushButton_g11.text() == '1' else self.pushButton_g11.setText('1')
            self.saveSeat()
            self.state = 'G11'

    def seat_button_h1(self):
        if self.state == 'H1':
            self.pushButton_h1.setText("0") if self.pushButton_h1.text() == '1' else self.pushButton_h1.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_h1.setText("0") if self.pushButton_h1.text() == '1' else self.pushButton_h1.setText('1')
            self.saveSeat()
            self.state = 'H1'

    def seat_button_h2(self):
        if self.state == 'H2':
            self.pushButton_h2.setText("0") if self.pushButton_h2.text() == '1' else self.pushButton_h2.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_h2.setText("0") if self.pushButton_h2.text() == '1' else self.pushButton_h2.setText('1')
            self.saveSeat()
            self.state = 'H2'

    def seat_button_h3(self):
        if self.state == 'H3':
            self.pushButton_h3.setText("0") if self.pushButton_h3.text() == '1' else self.pushButton_h3.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_h3.setText("0") if self.pushButton_h3.text() == '1' else self.pushButton_h3.setText('1')
            self.saveSeat()
            self.state = 'H3'

    def seat_button_h4(self):
        if self.state == 'H4':
            self.pushButton_h4.setText("0") if self.pushButton_h4.text() == '1' else self.pushButton_h4.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_h4.setText("0") if self.pushButton_h4.text() == '1' else self.pushButton_h4.setText('1')
            self.saveSeat()
            self.state = 'H4'

    def seat_button_h5(self):
        if self.state == 'H5':
            self.pushButton_h5.setText("0") if self.pushButton_h5.text() == '1' else self.pushButton_h5.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_h5.setText("0") if self.pushButton_h5.text() == '1' else self.pushButton_h5.setText('1')
            self.saveSeat()
            self.state = 'H5'

    def seat_button_h6(self):
        if self.state == 'H6':
            self.pushButton_h6.setText("0") if self.pushButton_h6.text() == '1' else self.pushButton_h6.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_h6.setText("0") if self.pushButton_h6.text() == '1' else self.pushButton_h6.setText('1')
            self.saveSeat()
            self.state = 'H6'

    def seat_button_h7(self):
        if self.state == 'H7':
            self.pushButton_h7.setText("0") if self.pushButton_h7.text() == '1' else self.pushButton_h7.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_h7.setText("0") if self.pushButton_h7.text() == '1' else self.pushButton_h7.setText('1')
            self.saveSeat()
            self.state = 'H7'

    def seat_button_h8(self):
        if self.state == 'H8':
            self.pushButton_h8.setText("0") if self.pushButton_h8.text() == '1' else self.pushButton_h8.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_h8.setText("0") if self.pushButton_h8.text() == '1' else self.pushButton_h8.setText('1')
            self.saveSeat()
            self.state = 'H8'

    def seat_button_h9(self):
        if self.state == 'H9':
            self.pushButton_h9.setText("0") if self.pushButton_h9.text() == '1' else self.pushButton_h9.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_h9.setText("0") if self.pushButton_h9.text() == '1' else self.pushButton_h9.setText('1')
            self.saveSeat()
            self.state = 'H9'

    def seat_button_h10(self):
        if self.state == 'H10':
            self.pushButton_h10.setText("0") if self.pushButton_h10.text() == '1' else self.pushButton_h10.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_h10.setText("0") if self.pushButton_h10.text() == '1' else self.pushButton_h10.setText('1')
            self.saveSeat()
            self.state = 'H10'

    def seat_button_h11(self):
        if self.state == 'H11':
            self.pushButton_h11.setText("0") if self.pushButton_h11.text() == '1' else self.pushButton_h11.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_h11.setText("0") if self.pushButton_h11.text() == '1' else self.pushButton_h11.setText('1')
            self.saveSeat()
            self.state = 'H11'

    def seat_button_j1(self):
        if self.state == 'J1':
            self.pushButton_j1.setText("0") if self.pushButton_j1.text() == '1' else self.pushButton_j1.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_j1.setText("0") if self.pushButton_j1.text() == '1' else self.pushButton_j1.setText('1')
            self.saveSeat()
            self.state = 'J1'

    def seat_button_j2(self):
        if self.state == 'J2':
            self.pushButton_j2.setText("0") if self.pushButton_j2.text() == '1' else self.pushButton_j2.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_j2.setText("0") if self.pushButton_j2.text() == '1' else self.pushButton_j2.setText('1')
            self.saveSeat()
            self.state = 'J2'

    def seat_button_j3(self):
        if self.state == 'J3':
            self.pushButton_j3.setText("0") if self.pushButton_j3.text() == '1' else self.pushButton_j3.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_j3.setText("0") if self.pushButton_j3.text() == '1' else self.pushButton_j3.setText('1')
            self.saveSeat()
            self.state = 'J3'

    def seat_button_j4(self):
        if self.state == 'J4':
            self.pushButton_j4.setText("0") if self.pushButton_j4.text() == '1' else self.pushButton_j4.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_j4.setText("0") if self.pushButton_j4.text() == '1' else self.pushButton_j4.setText('1')
            self.saveSeat()
            self.state = 'J4'

    def seat_button_j5(self):
        if self.state == 'J5':
            self.pushButton_j5.setText("0") if self.pushButton_j5.text() == '1' else self.pushButton_j5.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_j5.setText("0") if self.pushButton_j5.text() == '1' else self.pushButton_j5.setText('1')
            self.saveSeat()
            self.state = 'J5'

    def seat_button_j6(self):
        if self.state == 'J6':
            self.pushButton_j6.setText("0") if self.pushButton_j6.text() == '1' else self.pushButton_j6.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_j6.setText("0") if self.pushButton_j6.text() == '1' else self.pushButton_j6.setText('1')
            self.saveSeat()
            self.state = 'J6'

    def seat_button_j7(self):
        if self.state == 'J7':
            self.pushButton_j7.setText("0") if self.pushButton_j7.text() == '1' else self.pushButton_j7.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_j7.setText("0") if self.pushButton_j7.text() == '1' else self.pushButton_j7.setText('1')
            self.saveSeat()
            self.state = 'J7'

    def seat_button_j8(self):
        if self.state == 'J8':
            self.pushButton_j8.setText("0") if self.pushButton_j8.text() == '1' else self.pushButton_j8.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_j8.setText("0") if self.pushButton_j8.text() == '1' else self.pushButton_j8.setText('1')
            self.saveSeat()
            self.state = 'J8'

    def seat_button_j9(self):
        if self.state == 'J9':
            self.pushButton_j9.setText("0") if self.pushButton_j9.text() == '1' else self.pushButton_j9.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_j9.setText("0") if self.pushButton_j9.text() == '1' else self.pushButton_j9.setText('1')
            self.saveSeat()
            self.state = 'J9'

    def seat_button_j10(self):
        if self.state == 'J10':
            self.pushButton_j10.setText("0") if self.pushButton_j10.text() == '1' else self.pushButton_j10.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_j10.setText("0") if self.pushButton_j10.text() == '1' else self.pushButton_j10.setText('1')
            self.saveSeat()
            self.state = 'J10'

    def seat_button_j11(self):
        if self.state == 'J11':
            self.pushButton_j11.setText("0") if self.pushButton_j11.text() == '1' else self.pushButton_j11.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_j11.setText("0") if self.pushButton_j11.text() == '1' else self.pushButton_j11.setText('1')
            self.saveSeat()
            self.state = 'J11'

    def seat_button_k1(self):
        if self.state == 'K1':
            self.pushButton_k1.setText("0") if self.pushButton_k1.text() == '1' else self.pushButton_k1.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_k1.setText("0") if self.pushButton_k1.text() == '1' else self.pushButton_k1.setText('1')
            self.saveSeat()
            self.state = 'K1'

    def seat_button_k2(self):
        if self.state == 'K2':
            self.pushButton_k2.setText("0") if self.pushButton_k2.text() == '1' else self.pushButton_k2.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_k2.setText("0") if self.pushButton_k2.text() == '1' else self.pushButton_k2.setText('1')
            self.saveSeat()
            self.state = 'K2'

    def seat_button_k3(self):
        if self.state == 'K3':
            self.pushButton_k3.setText("0") if self.pushButton_k3.text() == '1' else self.pushButton_k3.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_k3.setText("0") if self.pushButton_k3.text() == '1' else self.pushButton_k3.setText('1')
            self.saveSeat()
            self.state = 'K3'

    def seat_button_k4(self):
        if self.state == 'K4':
            self.pushButton_k4.setText("0") if self.pushButton_k4.text() == '1' else self.pushButton_k4.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_k4.setText("0") if self.pushButton_k4.text() == '1' else self.pushButton_k4.setText('1')
            self.saveSeat()
            self.state = 'K4'

    def seat_button_k5(self):
        if self.state == 'K5':
            self.pushButton_k5.setText("0") if self.pushButton_k5.text() == '1' else self.pushButton_k5.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_k5.setText("0") if self.pushButton_k5.text() == '1' else self.pushButton_k5.setText('1')
            self.saveSeat()
            self.state = 'K5'

    def seat_button_k6(self):
        if self.state == 'K6':
            self.pushButton_k6.setText("0") if self.pushButton_k6.text() == '1' else self.pushButton_k6.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_k6.setText("0") if self.pushButton_k6.text() == '1' else self.pushButton_k6.setText('1')
            self.saveSeat()
            self.state = 'K6'

    def seat_button_k7(self):
        if self.state == 'K7':
            self.pushButton_k7.setText("0") if self.pushButton_k7.text() == '1' else self.pushButton_k7.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_k7.setText("0") if self.pushButton_k7.text() == '1' else self.pushButton_k7.setText('1')
            self.saveSeat()
            self.state = 'K7'

    def seat_button_k8(self):
        if self.state == 'K8':
            self.pushButton_k8.setText("0") if self.pushButton_k8.text() == '1' else self.pushButton_k8.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_k8.setText("0") if self.pushButton_k8.text() == '1' else self.pushButton_k8.setText('1')
            self.saveSeat()
            self.state = 'K8'

    def seat_button_k9(self):
        if self.state == 'K9':
            self.pushButton_k9.setText("0") if self.pushButton_k9.text() == '1' else self.pushButton_k9.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_k9.setText("0") if self.pushButton_k9.text() == '1' else self.pushButton_k9.setText('1')
            self.saveSeat()
            self.state = 'K9'

    def seat_button_k10(self):
        if self.state == 'K10':
            self.pushButton_k10.setText("0") if self.pushButton_k10.text() == '1' else self.pushButton_k10.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_k10.setText("0") if self.pushButton_k10.text() == '1' else self.pushButton_k10.setText('1')
            self.saveSeat()
            self.state = 'K10'

    def seat_button_k11(self):
        if self.state == 'K11':
            self.pushButton_k11.setText("0") if self.pushButton_k11.text() == '1' else self.pushButton_k11.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_k11.setText("0") if self.pushButton_k11.text() == '1' else self.pushButton_k11.setText('1')
            self.saveSeat()
            self.state = 'K11'

    def seat_button_l1(self):
        if self.state == 'L1':
            self.pushButton_l1.setText("0") if self.pushButton_l1.text() == '1' else self.pushButton_l1.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_l1.setText("0") if self.pushButton_l1.text() == '1' else self.pushButton_l1.setText('1')
            self.saveSeat()
            self.state = 'L1'

    def seat_button_l2(self):
        if self.state == 'L2':
            self.pushButton_l2.setText("0") if self.pushButton_l2.text() == '1' else self.pushButton_l2.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_l2.setText("0") if self.pushButton_l2.text() == '1' else self.pushButton_l2.setText('1')
            self.saveSeat()
            self.state = 'L2'

    def seat_button_l3(self):
        if self.state == 'L3':
            self.pushButton_l3.setText("0") if self.pushButton_l3.text() == '1' else self.pushButton_l3.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_l3.setText("0") if self.pushButton_l3.text() == '1' else self.pushButton_l3.setText('1')
            self.saveSeat()
            self.state = 'L3'

    def seat_button_l4(self):
        if self.state == 'L4':
            self.pushButton_l4.setText("0") if self.pushButton_l4.text() == '1' else self.pushButton_l4.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_l4.setText("0") if self.pushButton_l4.text() == '1' else self.pushButton_l4.setText('1')
            self.saveSeat()
            self.state = 'L4'

    def seat_button_l5(self):
        if self.state == 'L5':
            self.pushButton_l5.setText("0") if self.pushButton_l5.text() == '1' else self.pushButton_l5.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_l5.setText("0") if self.pushButton_l5.text() == '1' else self.pushButton_l5.setText('1')
            self.saveSeat()
            self.state = 'L5'

    def seat_button_l6(self):
        if self.state == 'L6':
            self.pushButton_l6.setText("0") if self.pushButton_l6.text() == '1' else self.pushButton_l6.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_l6.setText("0") if self.pushButton_l6.text() == '1' else self.pushButton_l6.setText('1')
            self.saveSeat()
            self.state = 'L6'

    def seat_button_l7(self):
        if self.state == 'L7':
            self.pushButton_l7.setText("0") if self.pushButton_l7.text() == '1' else self.pushButton_l7.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_l7.setText("0") if self.pushButton_l7.text() == '1' else self.pushButton_l7.setText('1')
            self.saveSeat()
            self.state = 'L7'

    def seat_button_l8(self):
        if self.state == 'L8':
            self.pushButton_l8.setText("0") if self.pushButton_l8.text() == '1' else self.pushButton_l8.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_l8.setText("0") if self.pushButton_l8.text() == '1' else self.pushButton_l8.setText('1')
            self.saveSeat()
            self.state = 'L8'

    def seat_button_l9(self):
        if self.state == 'L9':
            self.pushButton_l9.setText("0") if self.pushButton_l9.text() == '1' else self.pushButton_l9.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_l9.setText("0") if self.pushButton_l9.text() == '1' else self.pushButton_l9.setText('1')
            self.saveSeat()
            self.state = 'L9'

    def seat_button_l10(self):
        if self.state == 'L10':
            self.pushButton_l10.setText("0") if self.pushButton_l10.text() == '1' else self.pushButton_l10.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_l10.setText("0") if self.pushButton_l10.text() == '1' else self.pushButton_l10.setText('1')
            self.saveSeat()
            self.state = 'L10'

    def seat_button_l11(self):
        if self.state == 'L11':
            self.pushButton_l11.setText("0") if self.pushButton_l11.text() == '1' else self.pushButton_l11.setText('1')
            self.saveSeat()
            self.state = '0'
        elif self.state == '0':
            self.pushButton_l11.setText("0") if self.pushButton_l11.text() == '1' else self.pushButton_l11.setText('1')
            self.saveSeat()
            self.state = 'L11'

class link_user():
    def __init__(self):
        #if __name__ == "__main__":
            #import sys

            #app = QtWidgets.QApplication(sys.argv)

            user_win = user_window()

            ser_flight_win = ser_flight_window()

            user_win.show()

            user_win.in_flight_ser_win(ser_flight_win)

            #sys.exit(app.exec_())

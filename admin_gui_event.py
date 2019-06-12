from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

from admin import Ui_Form
import sql
import time
import datetime


class admin_window(QtWidgets.QWidget, Ui_Form):

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
        self.pushButton_a1
        self.pushButton_a2
        self.pushButton_a3
        self.pushButton_a4
        self.pushButton_b1
        self.pushButton_b2
        self.pushButton_b3
        self.pushButton_b4
        self.pushButton_c1
        self.pushButton_c2
        self.pushButton_c3
        self.pushButton_c4
        self.pushButton_e1
        self.pushButton_e2
        self.pushButton_e3
        self.pushButton_e4
        self.pushButton_f1
        self.pushButton_f2
        self.pushButton_f3
        self.pushButton_f4
        self.pushButton_g1
        self.pushButton_g2
        self.pushButton_g3
        self.pushButton_g4
        self.pushButton_h1
        self.pushButton_h2
        self.pushButton_h3
        self.pushButton_h4
        self.pushButton_j1
        self.pushButton_j2
        self.pushButton_j3
        self.pushButton_j4
        self.pushButton_k1
        self.pushButton_k2
        self.pushButton_k3
        self.pushButton_k4
        self.pushButton_l1
        self.pushButton_l2
        self.pushButton_l3
        self.pushButton_l4
        self.pushButton_a5
        self.pushButton_a6
        self.pushButton_a7
        self.pushButton_a8
        self.pushButton_a9
        self.pushButton_b5
        self.pushButton_b6
        self.pushButton_b7
        self.pushButton_b8
        self.pushButton_b9
        self.pushButton_c5
        self.pushButton_c6
        self.pushButton_c7
        self.pushButton_c8
        self.pushButton_c9
        self.pushButton_e5
        self.pushButton_e6
        self.pushButton_e7
        self.pushButton_e8
        self.pushButton_e9
        self.pushButton_f5
        self.pushButton_f6
        self.pushButton_f7
        self.pushButton_f8
        self.pushButton_f9
        self.pushButton_g5
        self.pushButton_g6
        self.pushButton_g7
        self.pushButton_g8
        self.pushButton_g9
        self.pushButton_h5
        self.pushButton_h6
        self.pushButton_h7
        self.pushButton_h8
        self.pushButton_h9
        self.pushButton_j5
        self.pushButton_j6
        self.pushButton_j7
        self.pushButton_j8
        self.pushButton_j9
        self.pushButton_k5
        self.pushButton_k6
        self.pushButton_k7
        self.pushButton_k8
        self.pushButton_k9
        self.pushButton_l5
        self.pushButton_l6
        self.pushButton_l7
        self.pushButton_l8
        self.pushButton_l9
        self.pushButton_l10
        self.pushButton_l11
        self.pushButton_k10
        self.pushButton_k11
        self.pushButton_j10
        self.pushButton_j11
        self.pushButton_h10
        self.pushButton_h11
        self.pushButton_g10
        self.pushButton_g11
        self.pushButton_f10
        self.pushButton_f11
        self.pushButton_e10
        self.pushButton_e11
        self.pushButton_c10
        self.pushButton_c11
        self.pushButton_b10
        self.pushButton_b11
        self.pushButton_a10
        self.pushButton_a11

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
        for row in results:
            fname = row[0]
            lname = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]
            adddd = row[5]
            # 打印结果
            print("fname=%s,lname=%s,age=%s,sex=%s,income=%s,addddd=%s" %
                  (fname, lname, age, sex, income, adddd))
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
        for row in results:
            fname = row[0]
            lname = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]
            # 打印结果
            print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" %
                  (fname, lname, age, sex, income))
            self.table_passenger.setItem(i, 0, QTableWidgetItem(row[0]))
            self.table_passenger.setItem(i, 1, QTableWidgetItem(row[1]))
            self.table_passenger.setItem(i, 2, QTableWidgetItem(row[2]))
            self.table_passenger.setItem(i, 3, QTableWidgetItem(row[3]))
            self.table_passenger.setItem(i, 4, QTableWidgetItem(row[4]))
            i = i + 1

    def add_table_bill(self):
        result_bill = self.S.bill_getAll()
        i = 0
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
        for row in results:
            self.list_flight.addItem(row[0])

    def add_seatMap(self, item):
        result = self.S.seat_get(item.text())
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
        self.saveSeat()

    def saveSeat(self):
        array_a = []
        array_b = []
        array_a.append(1)  # self.pushButton_a1.text()
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
        array_b.append(self.pushButton_c6.text())
        array_b.append(self.pushButton_c7.text())
        array_b.append(self.pushButton_c8.text())
        array_b.append(self.pushButton_c9.text())
        array_b.append(self.pushButton_c10.text())
        array_b.append(self.pushButton_c11.text())
        array_b.append(self.pushButton_e5.text())
        array_b.append(self.pushButton_e6.text())
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


        self.S.save_seat(self.list_flight.item(self.list_flight.itemAt()).text(), array_a, array_b)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    myshow = admin_window()

    myshow.show()

    sys.exit(app.exec_())

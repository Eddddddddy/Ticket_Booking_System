from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

from admin import Ui_Form
import sql
import time
import datetime

"""点击按钮，在控制台输出helloworld"""


class mywindow(QtWidgets.QWidget, Ui_Form):

    def __init__(self):
        super(mywindow, self).__init__()

        self.setupUi(self)

        self.table_flight.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_flight.setHorizontalHeaderLabels(['航班号', '到达城市', '出发城市', '机型', '出发时间', '到达时间', '满座率'])
        self.table_flight.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.button_flight.clicked.connect(self.stackedWidget_1)
        self.button_passenger.clicked.connect(self.stackedWidget_2)
        self.button_seat.clicked.connect(self.stackedWidget_3)
        self.button_bill.clicked.connect(self.stackedWidget_4)

        self.S = sql.SQL()
        self.add_table_flight()

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


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    myshow = mywindow()

    myshow.show()

    sys.exit(app.exec_())

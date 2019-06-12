from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

from user_gui_event import *
from admin_gui_event import *
from login import *
from ser_flight import Ui_Dialog_ser_flight
import sql
import time
import datetime



class Form_main(QtWidgets.QWidget, Ui_Form_main):

    def __init__(self):
        super(Form_main, self).__init__()

        self.setupUi(self)
        self.pushButton_user.clicked.connect(self.user)
        self.pushButton_admin.clicked.connect(self.admin)

    def user(self):
        self.u.show()
        self.hide()

    def admin(self):
        if self.lineEdit_password.text()=='123':
            self.a.show()
            self.hide()

    def in_user(self,u):
        self.u=u

    def in_admin(self,a):
        self.a=a

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    main_win = Form_main()

    main_win.show()

    #sys.exit(app.exec_())

    #app = QtWidgets.QApplication(sys.argv)

    user_win = user_window()

    ser_flight_win = ser_flight_window()

    #user_win.show()

    user_win.in_flight_ser_win(ser_flight_win)

    main_win.in_user(user_win)

    admin_win = admin_window()
    add_flight_win = add_flight_window()
    add_passenger_win = add_passenger_window()
    ser_flight_win = ser_flight_window()
    ser_passenger_win = ser_passenger_window()

    admin_win.in_flight_win(add_flight_win)
    admin_win.in_passenger_win(add_passenger_win)
    admin_win.in_flight_ser_win(ser_flight_win)
    admin_win.in_passenger_ser_win(ser_passenger_win)

    main_win.in_admin(admin_win)

    sys.exit(app.exec_())

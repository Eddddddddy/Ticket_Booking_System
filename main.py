import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

import admin_gui_event


class MyWindow(QMainWindow, admin_gui_event.admin_event):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())

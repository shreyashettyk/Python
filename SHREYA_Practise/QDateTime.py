import sys
from PyQt5.QtGui import  *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class DlgMain(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("window title")
        self.resize(500,500)
        self.btn = QPushButton("Date",self)
        self.btn.move(50,50)
        self.btn.clicked.connect(self.evt_btn_click)

    def evt_btn_click(self):
        print("button clicked")
        dt = QDate(2015,3,15)
        print("date ",dt)
        print("add months ",dt.addDays(23).toString())
        print("add months ",dt.addMonths(5).toString())
        print("add years ",dt.addYears(5).toString())

        tm = QTime.currentTime()
        print("time is ",tm)
        print("added seconds ..",tm.addSecs(10).toString())

        dtm = QDateTime.currentDateTime()
        print("current ",dtm.toString())
        print("added .. ",dtm.addDays(15).toString())

        # tz = QTimeZone(15)
        # print("timzone ",tz.standardTimeOffset())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = DlgMain()
    dlg.show()
    sys.exit(app.exec_())

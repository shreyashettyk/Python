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
        px = QPixmap(100,100)
        print(px.height())
        print(px.width())
        print(px.size())




if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = DlgMain()
    dlg.show()
    sys.exit(app.exec_())
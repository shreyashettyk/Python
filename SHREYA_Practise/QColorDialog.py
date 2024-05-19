import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class DlgMain(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window title")
        self.resize(500, 500)
        self.btn = QPushButton("Open font", self)
        self.btn.move(50, 50)
        # self.btn.clicked.connect(self.evt_btn_clikced_color)
        self.btn.clicked.connect(self.evt_btn_clikced_color)
    def evt_btn_clikced_color(self):

        color = QColorDialog.getColor(QColor("green"),self,"Color dialog")
        print("color value is ",color)

    def evt_btn_clicked_font(self):
        print("font slot....")
        font = QFontDialog.getFont(QFont("Lucida Sans",25,False),self,"font dialog")
        print("Font is ...",font)

if __name__=="__main__":
    print("start...")
    app = QApplication(sys.argv)
    dlg = DlgMain()
    dlg.show()
    sys.exit(app.exec())
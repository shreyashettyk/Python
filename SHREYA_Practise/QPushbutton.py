from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import sys

class DlgMain(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("my GUI")
        self.resize(500,500)
        self.btn = QPushButton("Disable Label",self)
        self.btn.move(50,50)
        self.btn.setIcon(QIcon(QPixmap("C:\\Users\\User\\PycharmProjects\\hello\\fotos\\search.png")))

        self.lbl = QLabel("Label Text",self)
        self.lbl.move(75,100)
        self.lbl.resize(200,200)

        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        print("starting slot... ")
        # self.btn.setText("Enable Label")
        if self.btn.text() == "Disable Label":
            self.btn.setText("Enable Label")
            self.lbl.setDisabled(True)
        else:
            self.btn.setText("Disable Label")
            self.lbl.setDisabled(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = DlgMain()
    dlg.show()
    sys.exit(app.exec_())


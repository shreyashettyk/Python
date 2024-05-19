import sys
from PyQt5.QtWidgets import *

class DlgMain(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window title")
        self.resize(500,500)
        self.btn = QPushButton("Open File",self)
        self.btn.move(50,50)
        self.btn.clicked.connect(self.evt_btn_clikced)
        # res = QFileDialog.getOpenFileName(self,"file title","C:\\Users\\User\\Desktop","JPG Files (*.jpg);;PNG Files (*.png)")
        # # res = QFileDialog.getSaveFileName(parent=self, directory = "C:\\Users\\User\\Desktop", filter="JPG Files (*.jpg);;PNG Files (*.png)")
        # print("Result is",res)

    def evt_btn_clikced(self):
        res = QFileDialog.getOpenFileName(self, "file title", "C:\\Users\\User\\Desktop","JPG Files (*.jpg);;PNG Files (*.png)")
        # res = QFileDialog.getSaveFileName(parent=self, directory = "C:\\Users\\User\\Desktop", filter="JPG Files (*.jpg);;PNG Files (*.png)")
        print("Result is", res)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = DlgMain()
    dlg.show()
    sys.exit(app.exec_())

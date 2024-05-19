import sys
from PyQt5.QtWidgets import *
print("import complete...")

##Method 1
# app = QApplication(sys.argv)
# dlg = QDialog()
# dlg.setWindowTitle("my GUI")
#
# dlg.show()
# sys.exit(app.exec_())


#Method 2

class DlgMain(QWidget):
    def __init__(self):
        print("constructor of DlgMain...")
        super().__init__()
        self.setWindowTitle("my GUI")
        self.resize(500,500)
        self.led = QLineEdit("Line edit component",self)
        self.led.move(50,50)
        print("Text from line edit",self.led.text())
        self.btn = QPushButton("Push button",self)
        self.btn.move(200,50)
        self.btn.clicked.connect(self.evt_onBtnPush)
        print(isinstance(self, DlgMain))



    def evt_onBtnPush(self):
        print("button pushed...",self.btn.text())
        self.setWindowTitle(self.led.text())

        res = QMessageBox.critical(self,"message box title","message for message box")

        print(res)

if __name__ == "__main__":
    print("start execution")
    app = QApplication(sys.argv)
    dlg = DlgMain()

    dlg.show()
    sys.exit(app.exec_())



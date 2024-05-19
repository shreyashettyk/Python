from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


class DlgMain(QWidget):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("my GUI")
        self.resize(500,500)

        self.two_state_btn = QCheckBox("Two state",self)
        self.two_state_btn.move(50,50)
        # self.two_state_btn.setChecked(True)

        self.three_state_btn = QCheckBox("Three state",self)
        self.three_state_btn.move(50,75)
        self.three_state_btn.setTristate(True)


        self.lbl = QLabel("Label",self)
        self.lbl.move(50,120)

        self.two_state_btn.toggled.connect(self.evt_two_state_btn)
        self.three_state_btn.stateChanged.connect(self.evt_three_state_btn)

    def evt_two_state_btn(self,ckhd):
        print(ckhd)
        # if self.two_state_btn.isChecked():
        #     self.lbl.setDisabled(True)
        if self.two_state_btn.isChecked():
            self.lbl.setDisabled(True)
        else:
            self.lbl.setDisabled(False)

    def evt_three_state_btn(self):
        state = {1: 'partial', 2: 'checked', 0: 'None'}
        check_state = self.three_state_btn.checkState()
        print(check_state)
        QMessageBox.information(self,"Three state check box","State is {}".format(state[check_state]))








if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = DlgMain()
    dlg.show()
    sys.exit(app.exec_())





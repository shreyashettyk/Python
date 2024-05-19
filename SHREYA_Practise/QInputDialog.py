import sys
from PyQt5.QtWidgets import *

class DlgMain(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window title")
        self.resize(500,500)
        self.btn = QPushButton("Push button",self)
        self.btn.move(50,50)
        self.btn.clicked.connect(self.evt_btn_click_inp_dialog)

    # def evt_btn_click_inp_dialog(self):    #input dialog using user input
    #     res_str,bOk = QInputDialog.getText(self,"Input dialog title","Enter your favorite food")
    #     if bOk:
    #         QMessageBox.information(self,"message box title","Food is {}".format(res_str))
    #     else:
    #         QMessageBox.information(self,"message box title","No food selected..")

    # def evt_btn_click_inp_dialog(self): #input dialog using drop down with diabling editing
    #     lst = ["Rice","Idli","Dosa"]
    #     res_str,bOk = QInputDialog.getItem(self,"Input dialog title","Select food item",lst,editable=False)
    #     if bOk:
    #         QMessageBox.information(self,"message box title","Food is {}".format(res_str))
    #     else:
    #         QMessageBox.information(self,"message box title","No food selected..")

    def evt_btn_click_inp_dialog(self):
        res_str,bOk = QInputDialog.getInt(self,"input dialog","enter Timer",min=10,max=20)
        print("type of input is ",type(res_str))
        if bOk:
            QMessageBox.information(self, "message box title", "Timer value is is {}".format(res_str))
        else:
            QMessageBox.crtitcal(self, "message box title", "No timer value selected")
if __name__ =="__main__":
    app = QApplication(sys.argv)
    dlg = DlgMain()
    dlg.show()
    sys.exit(app.exec_())
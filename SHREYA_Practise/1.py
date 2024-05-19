import sys
from PyQt5.QtWidgets import *

class DlgMain(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window title")
        self.resize(500,500)
        self.ledText = QLineEdit("line edit",self)
        self.ledText.move(50,50)


        self.btn = QPushButton("Push button",self)
        self.btn.move(200,50)
        self.btn.clicked.connect(self.evt_btnPush)



    def evt_ledText_changed(self):
        print("Line edit text is ",self.ledText.text())
        self.setWindowTitle(self.ledText.text())


    def evt_btnPush(self):
        print("button pushes")

        input_dialog_res = QInputDialog.getText(self, "Input Dialog title", "Prompt")
        print("result from input dialog ", input_dialog_res)

        self.setWindowTitle(self.ledText.text())
        res = QMessageBox.information(self, "title of message box", "text change to {}".format(self.ledText.text()),QMessageBox.Ok|QMessageBox.Cancel )
        print("Result .... ",res)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = DlgMain()
    dlg.show()
    sys.exit(app.exec_())

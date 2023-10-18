import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.Qt import QSize

form_class = uic.loadUiType("omok02.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flag_bw = True

        for i in range(10):
            for j in range(10):
                btn = QPushButton("", self)
                btn.setIcon(QtGui.QIcon("0.png"))
                btn.setIconSize(QSize(40, 40))
                btn.setGeometry(i * 40, j * 40, 40, 40)
                btn.clicked.connect(self.myclick)

        self.flag = True

    def myclick(self):
        if self.flag_bw:
            self.sender().setIcon(QtGui.QIcon("1.png"))
        else:
            self.sender().setIcon(QtGui.QIcon("2.png"))
        self.flag_bw = not self.flag_bw

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import secrets

form_class = uic.loadUiType("myqt03.ui")[0]

class WindowClass(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)

    def myclick(self):
        num = []
        for i in range(1, 46):
            num.append(i)
        rotto = []
        for i in range(0, 7):
            rotto.append(secrets.choice(num))
        rottoSet = list(set(rotto))

        # 정렬
        rottoSet.sort()
        self.lbl1.setText(str(rottoSet[0]))
        self.lbl2.setText(str(rottoSet[1]))
        self.lbl3.setText(str(rottoSet[2]))
        self.lbl4.setText(str(rottoSet[3]))
        self.lbl5.setText(str(rottoSet[4]))
        self.lbl6.setText(str(rottoSet[5]))

        num.clear()
        rotto.clear()
        rottoSet.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
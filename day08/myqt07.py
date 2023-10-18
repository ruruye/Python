import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("myqt07.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        
    def getstar(self,cnt):
        ret = ""
        for i in range(cnt):
            ret += "*"
        ret += "\n"
        return ret

    def myclick(self) :
        f = self.le_first.text()
        l = self.le_last.text()
        ff = int(f)
        ll = int(l)

        txt = ""
        for i in range(ff,ll+1):
            txt += self.getstar(i)

        self.te.setText(txt)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
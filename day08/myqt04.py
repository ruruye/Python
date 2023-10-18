import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


form_class = uic.loadUiType("myqt04.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self) :
        txt = self.le.text()
        num = int(txt)
        form = ""
        for i in range(1,10):
            form += "%d * %d  = %d\n" %(num, i, num*i)
            
        self.te.setText(form)
           
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
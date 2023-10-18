import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic
from random import random

form_class = uic.loadUiType("myqt08.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.com = "123"
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.le.returnPressed.connect(self.myclick)
        self.ranC()
        
    def getS(self,com,mine):
        ret = 0
        c1 = com[0:1]
        c2 = com[1:2]
        c3 = com[2:3]
        
        m1 = mine[0:1]
        m2 = mine[1:2]
        m3 = mine[2:3]
        
        if c1 == m1 : ret += 1
        if c2 == m2 : ret += 1
        if c3 == m3 : ret += 1
        
        return ret
    
    def getB(self,com,mine):
        ret = 0
        c1 = com[0:1]
        c2 = com[1:2]
        c3 = com[2:3]
        
        m1 = mine[0:1]
        m2 = mine[1:2]
        m3 = mine[2:3]
        
        if c1 == m2 or c1 == m3 : ret += 1
        if c2 == m1 or c2 == m3 : ret += 1
        if c3 == m1 or c3 == m2 : ret += 1
        
        return ret
        
    def ranC(self):
        
        arr = [1,2,3,4,5,6,7,8,9]
        
        for i in range(100) :
            rnd = int(random()*9)
            a = arr[0]
            arr[0] = arr[rnd]
            arr[rnd] = a

        self.com = "{}{}{}".format(arr[0],arr[1],arr[2])
        print("self.com",self.com)
        
    def myclick(self) :
        mine = self.le.text()
        s = self.getS(self.com,mine)
        b = self.getB(self.com,mine)
        str_new = mine + "\t" + str(s) + "S" + str(b) + "B" + "\n"
        str_old = self.te.toPlainText()
        
        self.te.setText(str_new+str_old)
        self.le.setText("")
        
        if s == 3:
            QMessageBox.about(self, '야구게임', mine+"맞췄습니다.")

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
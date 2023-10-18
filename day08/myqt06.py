import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import secrets
from random import random


form_class = uic.loadUiType("myqt06.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        
        
    def myclick(self) :
        mine = self.pte_mine.toPlainText()
        com = ""
        
        rnd = random()
        
        if rnd > 0.66:
            com = "가위"
        elif rnd > 0.33:
            com = "바위"
        else:
            com = "보"
        
        if mine == com:
            result = "비김"
        elif(mine=="가위" and com=="보") or (mine=="보" and com=="바위") or (mine=="바위" and com=="가위"): 
            result = "승리"
        else:
            result = "패배"    
        
        self.pte_com.setPlainText(com)
        self.pte_result.setPlainText(result)

               
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.Qt import QSize, QMessageBox

form_class = uic.loadUiType("omok03.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        self.flag_over = False
        super().__init__()
        self.setupUi(self)
        self.flag_bw = True
        self.arr2D = [
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0]        
        ]
        self.pb2D = []
        

        for i in range(10):
            line = []
            for j in range(10):
                btn = QPushButton("", self)
                btn.setIcon(QtGui.QIcon("0.png"))
                btn.setIconSize(QSize(40, 40))
                btn.setToolTip("{}, {}".format(i,j))
                btn.setGeometry(j * 40, i * 40, 40, 40)
                btn.clicked.connect(self.myclick)
                line.append(btn)
            self.pb2D.append(line)
        
        self.pb.clicked.connect(self.my_reset)
        self.myrender()
        
    def my_reset(self):   
        self.flag_over = False
        self.flag_bw = True
        for i in range(10):
            for j in range(10):
                self.arr2D[i][j]=0
        self.myrender()
        
    def checkLE(self, i, j, stone):
        cnt = 0 
        try:
            while True : 
                j -=1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
    
    def checkDL(self, i, j, stone):
        cnt = 0 
        try:
            while True : 
                i +=1
                j -=1
                if i < 0:
                    return cnt
                if i < 0:
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
    
    def checkDR(self, i, j, stone):
        cnt = 0 
        try:
            while True : 
                i +=1
                j +=1
                if i < 0:
                    return cnt
                if i < 0:
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
    
    def checkUL(self, i, j, stone):
        cnt = 0 
        try:
            while True : 
                i -=1
                j +=1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
    
    def checkUR(self, i, j, stone):
        cnt = 0 
        try:
            while True : 
                i -=1
                j +=1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
    
    def checkRI(self, i, j, stone):
        cnt = 0 
        try:
            while True : 
                j +=1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
    
    def checkDW(self, i, j, stone):
        cnt = 0 
        try:
            while True : 
                i +=1
                if i < 0:
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def checkUP(self, i, j, stone):
        cnt = 0 
        try:
            while True : 
                i -=1
                if i < 0:
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
            
   
    def myclick(self):
        if self.flag_over:
            return
        
        str_ij = self.sender().toolTip()
        print("str_ij", str_ij)
        arr_ij = str_ij.split(",")
        print("arr_ij", arr_ij)
        i = int(arr_ij[0])
        j = int(arr_ij[1])
        
        if self.arr2D[i][j] > 0: # 돌이 놓아져있으면
            return 
        
        
        stone = -1
        
        if self.flag_bw:
            self.arr2D[i][j]=1
            stone = 1
        else:
            self.arr2D[i] [j]=2
            stone = 2
            
        up = self.checkUP(i,j,stone)
        dw = self.checkDW(i,j,stone)
        le = self.checkLE(i,j,stone)
        ri = self.checkRI(i,j,stone)
        
        ul = self.checkUL(i,j,stone) 
        ur = self.checkUR(i,j,stone)
        dl = self.checkDL(i,j,stone)
        dr = self.checkDR(i,j,stone)
        print(dw, up, le, ri, ul, ur, dl, dr)
        
        d1 = le+ri+1
        d2 = ul+dr+1
        d3 = up+dw+1
        d4 = ur+dl+1
        
        self.myrender()
        
        if d1==5 or d2==5 or d3==5 or d4==5:
            if self.flag_bw:
                QMessageBox.about(self,'오목',"흑돌승리")
            else:
                QMessageBox.about(self,'오목',"백돌승리")
            self.flag_over = True
              
        
        self.flag_bw = not self.flag_bw
    
    def myrender(self):
        for i in range(10):
          for j in range(10):
            if self.arr2D[i][j]==0:
                self.pb2D[i][j].setIcon(QtGui.QIcon("0.png"))
            if self.arr2D[i][j]==1:
                self.pb2D[i][j].setIcon(QtGui.QIcon("1.png"))
            if self.arr2D[i][j]==2:
                self.pb2D[i][j].setIcon(QtGui.QIcon("2.png"))   
                
     
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
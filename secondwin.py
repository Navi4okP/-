from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from instr import *
from finalwin import *

class Experiment():
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
        
class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: black")
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()
        
    def next_click(self):
        self.tw = TestWin()
        self.hide()
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.btn_next = QPushButton(txt_sendresults, self)
        self.btn_next.setStyleSheet(
            "width: 180px;" 
            "height: 40px;" 
            "color: black;" 
            "font-size: 20px;" 
            "background-color: yellow;" 
            "border: 2px solid yellow;" 
            "border-radius: 20%")
        self.text_input = QLabel(txt_input)
        self.text_input.setStyleSheet(
            "color: yellow;" 
            "font-size: 25px;");
        self.line_height = QLineEdit(txt_hintheight)
        self.line_weight = QLineEdit(txt_hintweight)
        
        self.line_height.setStyleSheet(
            "color: yellow;"
            "font-size: 20px;");
        
        self.line_weight.setStyleSheet(
            "color: yellow;"
            "font-size: 20px;");
        
        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()
        self.h_line = QHBoxLayout()
        self.l_line.addWidget(self.text_input, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_height, alignment= Qt.AlignLeft)   
        self.l_line.addWidget(self.line_weight, alignment= Qt.AlignLeft)  
        self.l_line.addWidget(self.btn_next, alignment = Qt.AlignCenter) 
        self.h_line.addLayout(self.l_line)  
        self.h_line.addLayout(self.r_line)  
        self.setLayout(self.h_line)
    
    def next_click(self):
        self.hide()
        self.exp = Experiment(int(self.line_weight.text()), self.line_height.text())
        self.fw = FinalWin(self.exp)
        
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
        
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
        

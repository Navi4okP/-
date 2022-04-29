from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from instr import *
from secondwin import *
import sys

class MainWin(QWidget):
    def __init__(self):
        ''' окно, в котором располагается приветствие '''
        super().__init__()

        # создаём и настраиваем графические эелементы:
        self.initUI()

        #устанавливаем связи между элементами
        self.connects()

        #устанавливаем, как будет выглядеть окно (надпись, размер, место)
        self.set_appear()

        # старт:
        self.show()
        
    def initUI(self):
        self.btn_next = QPushButton(btn_next, self)
        self.hello_text = QLabel(txt_hello)
        self.label = QLabel(self)
        self.pixmap = QPixmap('bmi.png')
        self.label.setPixmap(self.pixmap)
        self.btn_next.setStyleSheet(
            "width: 180px;" 
            "height: 40px;" 
            "color: black;" 
            "font-size: 20px;" 
            "background-color: yellow;" 
            "border: 2px solid yellow;" 
            "border-radius: 20%");
        self.hello_text.setStyleSheet(
            "color: yellow;" 
            "font-size: 25px;");
        
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.label, alignment = Qt.AlignCenter) 
        self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.btn_next, alignment= Qt.AlignCenter)
        self.setLayout(self.layout_line)
        
    def next_click(self):
        self.tw = TestWin()
        self.hide()
    
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
        
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
        
app = QApplication([])
mw = MainWin()
mw.setStyleSheet('background-color: black')

app.exec_()
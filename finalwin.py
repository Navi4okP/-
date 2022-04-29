from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from instr import *

class FinalWin(QWidget):
    def __init__(self, exp):
        ''' окно, в котором проводится опрос '''
        super().__init__()

        self.setStyleSheet("background-color: black")

        self.exp = exp

        # создаём и настраиваем графические элелементы:
        self.initUI()

        #устанавливает, как будет выглядеть окно (надпись, размер, место)
        self.set_appear()
        
        # старт:
        self.show()
    def results(self):
        self.index = (float(self.exp.weight)) / ((float(self.exp.height)) ** 2)
        if self.index < 16:
            return txt_res1
        if self.index >= 16 and self.index < 18.5:
            return txt_res2
        if self.index >= 18.5 and self.index < 24.5:
            return txt_res3
        if self.index >= 24.5 and self.index < 30:
            return txt_res4
        if self.index >= 30 and self.index < 35:
            return txt_res5
        if self.index >= 35 and self.index < 40:
            return txt_res6
        if self.index >= 40:
            return txt_res7
        
    def initUI(self):
        self.index_text = QLabel(txt_index + self.results())
        self.index_text.setStyleSheet(
            "color: yellow;" 
            "font-size: 25px;");
        
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment= Qt.AlignCenter)
        self.setLayout(self.layout_line)
        
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
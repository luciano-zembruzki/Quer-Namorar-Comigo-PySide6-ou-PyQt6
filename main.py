import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import QObject, QEvent

import random

from main_ui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.coracao.setVisible(False)
        
        self.button_no.clicked.connect(self.moveButton)
        self.button_yes.clicked.connect(self.melhorOpcao)
        
        self.frame_no.installEventFilter(self)
        self.frame_yes.installEventFilter(self)
        
    def moveButton(self):
          self.frame_no.move(random.randint(0,300), random.randint(0,300))
          
          
    def melhorOpcao(self):
          self.label.setText("Escolheu a melhor opção!!!")
          self.label.setStyleSheet("QLabel{\n"
"	font-size: 30px;\n"
"	font-weight: bold;\n"
"	color: rgb(255, 255, 255);\n"
"}\n")    
          self.button_yes.setVisible(False)
          self.button_no.setVisible(False)
          self.coracao.setVisible(True)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Enter and obj == self.frame_no:
                self.moveButton()
                return True
        else:
            return False


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys
#from functools import partial
from PyQt5.QtCore import pyqtSlot
from loginForm import *
#from registerForm import *
#from clientForm import *

class App(QMainWindow):
    def loginForm(self):
        self.close()
        # Otvara se forma za login
        self.newApp = Login()
        #self.wasd = self.newApp.inputUn.text()
        #print(self.wasd)

    def __init__(self):
        super().__init__()
        self.title = 'Login and Register'
        self.top = 450 - 125
        self.left = 800 - 200
        self.width = 400
        self.height = 250
        self.initUI()
        # 1600 900
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        loginButton = QPushButton('Login', self)
        loginButton.setToolTip('Nemam pojma cijeli dan')
        loginButton.move(10, 10)
        loginButton.clicked.connect(self.loginForm)

        registerButton = QPushButton('Register', self)
        registerButton.setToolTip('Nemam pojma cijeli dan')
        registerButton.move(10, 50)


        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = App()
    sys.exit(app.exec_())
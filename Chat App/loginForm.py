from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import pyqtSlot
import mysql.connector
import sys
from functools import partial
from serverForm import *
from clientForm import *

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Login Form'
        self.top = 300
        self.left = 300
        self.width = 350
        self.height = 300
        self.mainDef()

        self.mydb = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = '',
            database = 'prvabaza'
        )

        self.myCursor = self.mydb.cursor()

        print(self.myCursor)

    def checkUser(self):
        try:
            self.myCursor.execute("SELECT password FROM pythonlogin WHERE username = '" + self.inputUn.text() + "'")
            self.myResult = self.myCursor.fetchone()

            if(self.myResult[0] == self.userUn.text()):
                return 1

            if(self.myResult[0] != self.userUn.text()):
                return 2

        except:
            return 3

    def nesto(self):
        print(self.inputUn.text() + ' : ' + self.userUn.text())
        if(self.checkUser() == 1):
            self.result.setText('Uspjesno si logovan')
            self.result.setStyleSheet("QLabel {color: green;}")

            self.close()
            self.openClientForm = ClientSocket()
            self.openClientForm.Connect(self.inputUn.text())
        
        if(self.checkUser() == 2):
            self.result.setText('Provjeri podatke ponovo')
            self.result.setStyleSheet('QLabel {color: yellow;}')

        if(self.checkUser() == 3):
            self.result.setText('Vas racun ne postoji')
            self.result.setStyleSheet('QLabel {color: red;}')

    def mainDef(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.welcome = QLabel(self)
        self.welcome.setText('Login')
        self.welcome.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome.move(20, 20)
        self.welcome.resize(310, 30)

        self.setStyleSheet('QMainWindow {border:2.3px solid green; background-color: #b0c2b5;} QLabel {color: green; font-family: Verdana; font-size: 24px} QLineEdit {border:1.3px solid green; border-radius: 8px;} QPushButton {border:1.3px solid green; border-radius: 8px; background-color: green; color:white;} QPushButton:hover {color: green;  background-color: white; border: 1.3px solid green;}')
        #self.setStyleSheet('QPushButton:hover {color: red;}')

        self.inputUn = QLineEdit(self)
        self.inputUn.move(20, 80)
        self.inputUn.setAlignment(QtCore.Qt.AlignCenter)
        self.inputUn.resize(310, 35)
        self.inputUn.setPlaceholderText('Username')

        self.userUn = QLineEdit(self)
        self.userUn.move(20, 132)
        self.userUn.setAlignment(QtCore.Qt.AlignCenter)
        self.userUn.resize(310, 35)
        self.userUn.setPlaceholderText('Password')

        self.printUn = QPushButton('Login', self)
        self.printUn.move(20, 200)
        self.printUn.resize(310, 35)
        self.printUn.clicked.connect(self.nesto)

        self.result = QLabel(self)
        self.result.setAlignment(QtCore.Qt.AlignCenter)
        self.result.move(20, 252)
        self.result.resize(310, 30)
        self.result.setText('')

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Login()
    sys.exit(app.exec_())

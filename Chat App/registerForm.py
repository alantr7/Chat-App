from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
import sys
from functools import partial
from PyQt5.QtCore import pyqtSlot
import mysql.connector

class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Register Form'
        self.top = 450
        self.left = 450
        self.width = 350
        self.height = 200

        self.mydb = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = '',
            database = 'prvabaza'
        )
        
        self.myCursor = self.mydb.cursor(buffered = True)

        self.newMain()

    def addAcc(self):
        print(self.inputUn.text())
        print(self.inputEm.text())
        print(self.inputPw.text())

        self.myCursor = self.mydb.cursor()
        self.myCursor.execute("SELECT * FROM pythonlogin WHERE username='" + self.inputUn.text() + "' AND email='" + self.inputEm.text() + "' AND password='" + self.inputPw.text() + "'")
        self.myResult = self.myCursor.fetchall()
        if((self.myResult) == 'NoneType' or len(self.myResult) == 0):
            self.myCursor = self.mydb.cursor()
            self.myCursor.execute("INSERT INTO pythonlogin (username, password, email) VALUES ('" + self.inputUn.text() + "', '" + self.inputEm.text() + "', '" + self.inputPw.text() + "')")
            self.mydb.commit()
            print('Dodano je.')
            return True
        else:
            print('Nije dodano')
            self.printUn.setText('ACCOUNT POSTOJI')
            self.printUn.setStyleSheet('QPushButton {background-color: red; color : black;}')
        
    def newMain(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.username = QLabel(self)
        self.username.setText('Username :')
        self.username.move(20, 20)

        self.email = QLabel(self)
        self.email.setText('E-mail :')
        self.email.move(20, 50)

        self.password = QLabel(self)
        self.password.setText('Password :')
        self.password.move(20, 80)

        self.inputUn = QLineEdit(self)
        self.inputUn.move(80, 25)
        self.inputUn.resize(200, 22)

        self.inputEm = QLineEdit(self)
        self.inputEm.move(80, 55)
        self.inputEm.resize(200, 22)

        self.inputPw = QLineEdit(self)
        self.inputPw.move(80, 85)
        self.inputPw.resize(200, 22)
        self.inputPw.setPlaceholderText('Password')

        self.printUn = QPushButton('Register', self)
        self.printUn.move(130, 130)
        self.printUn.clicked.connect(self.addAcc)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.show()

    def mousePressEvent(self, event):

        # Trenutna pozicija misa ako sam dobro shvatio?

        self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):
    
        # Ovo ne kontam ali je bitno da radi

        if event.buttons() == QtCore.Qt.RightButton or event.buttons() == QtCore.Qt.LeftButton:            
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Register()
    sys.exit(app.exec_())
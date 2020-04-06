import socket
import time
import sys
import threading
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import pyqtSlot
from loginForm import *
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, QGroupBox, QLabel, QPushButton

'''
name = input("Napisi ime >> ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
s.connect(("127.0.0.1", 5522))

s.send(bytes(name, "utf-8"))


def Listen():    
    try:                    
        while True:
            msg = s.recv(1024)
            print(msg)
            if (len(msg) <= 0):                                                     
                time.sleep(2)
                break
            print(f"Poruka: {msg}")                                       
        quit()
    except:
        quit()

nesto = threading.Thread(target = Listen, args = ())
nesto.start()

while True:
    try:
        s.send(bytes(input(">> "), "utf-8"))
    except:
        print('server je ugasen')
        quit()

'''

class ClientSocket(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'ClientSocket Form'
        self.top = 300
        self.left = 300
        self.width = 350
        self.height = 300

        self.ClientGui()

    def Connect(self, username):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        self.s.connect(("127.0.0.1", 5522))
        self.s.send(bytes(username, "utf-8"))

        self.ClientThread = threading.Thread(target = self.ClientListen, args = ())
        self.ClientThread.start()

    def ClientListen(self):
        try:                    
            while True:
                print('loop')
                self.msg = self.s.recv(1024).decode('utf-8')
                print(self.msg)
                self.chat.setText(self.chat.text() + self.msg + '\n')
                if (len(self.msg) <= 0):                                                     
                    time.sleep(2)
                    continue
                print(f"Poruka: {self.msg}")                                       
        except:
            print('Nesto se desilo na liniji 79 i iznad.')

    def SendMessage(self):
        self.s.send(bytes(self.inputMessage.text(), "utf-8"))
        self.inputMessage.setText('')

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:           
            self.SendMessage()
        else:
            pass

    def ClientGui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.chat = QLabel(self)
        self.chat.setText('')
        #self.chat.move(10, 10)
        self.chat.setAlignment(QtCore.Qt.AlignTop)

        self.chatScroll = QScrollArea(self)
        self.chatScroll.move(10, 10)
        self.chatScroll.setWidget(self.chat)
        self.chatScroll.setWidgetResizable(True)
        self.chatScroll.resize(330, 120)

        self.inputMessage = QLineEdit(self)
        self.inputMessage.move(10, 255)
        #self.inputMessage.setAlignment(QtCore.Qt.AlignCenter)
        self.inputMessage.resize(280, 35)
        self.inputMessage.setPlaceholderText('Message')

        self.submit = QPushButton('Submit', self)
        self.submit.move(292, 254)
        self.submit.resize(50, 37)
        self.submit.clicked.connect(self.SendMessage)

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ClientSocket()
    sys.exit(app.exec_())
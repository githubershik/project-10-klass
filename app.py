import sys
#import speech_recognition as sr
#import whisper
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QGridLayout, QPushButton)
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Speech Recognition App")
        self.setGeometry(400, 180, 800, 600)
        self.label = QLabel("helo",self)
        self.initUI()
        #label = QLabel("Welcome to the Speech Recognition App!", self)
        #label.setFont(QFont("Arial", 20))
        #label.setGeometry(160, 230, 600, 50)
        
        #label = QLabel(self)
        #label.setGeometry(0,0,250,250)
        #
        #pixmap = QPixmap("сабака.jpg")
        #label.setPixmap(pixmap)
        #
        #label.setScaledContents(True)
        #
        #label.setGeometry((self.width() - label.width())//2,(self.height() - label.height())//2, label.width(), label.height())

    #def initUI(self):
    #    central_widget = QWidget()
    #    self.setCentralWidget(central_widget)
    #    label1 = QLabel('#1',self)
    #    label2 = QLabel('#2',self)
    #    label3 = QLabel('#3',self)
    #    label4 = QLabel('#4',self)
    #    label5 = QLabel('#5',self)
    #    label1.setStyleSheet("background-color:red")
    #    label2.setStyleSheet("background-color:yellow")
    #    label3.setStyleSheet("background-color:green")
    #    label4.setStyleSheet("background-color:blue")
    #    label5.setStyleSheet("background-color:purple")
    #    vbox = QVBoxLayout()
    #    vbox.addWidget(label1)
    #    vbox.addWidget(label2)
    #    vbox.addWidget(label3)
    #    vbox.addWidget(label4)
    #    vbox.addWidget(label5)
    #    central_widget.setLayout(vbox)

    def initUI(self):
        self.button = QPushButton("click me",self)
        self.button.setGeometry(150,200,200,100)
        self.button.setStyleSheet("font-size:30px")
        self.button.clicked.connect(self.onclick)
        self.label.setGeometry(150,300,200,100)
        self.label.setStyleSheet("font-size:30px")
    
    def onclick(self):
        self.label.setText("goodbye")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys 
from pyautogui import *
import pyautogui
import time
from time import sleep
import win32api, win32con

############# Global Variables #############

x1 = 960
y1 = 540
x2 = 960
y2 = 540
x3 = 960
y3 = 540
x4 = 960
y4 = 540
x5 = 960
y5 = 540

adCounter = 0


class Window(QMainWindow): 
    def __init__(self): 
        super().__init__() 

############# Window #############

        title = "HTV Bot"
        self.setWindowTitle(title) 
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.setGeometry(810, 290, 300, 350) 
        self.setFixedSize(300, 350)
        self.UiComponents() 
        self.show()

    def UiComponents(self): 

        self.flag = False

############# Top Region #############

        # Top Label #

        self.label = QLabel(self)
        self.label.setText('HTV Bot') 
        self.label.setGeometry(-50, -25, 405, 100)
        self.label.setFont(QFont('Comic Sans MS', 20)) 
        self.label.setAlignment(Qt.AlignCenter)

        # Start Button #

        startButton = QPushButton("Start", self) 
        startButton.setGeometry(110, 50, 75, 25) 
        startButton.setFont(QFont('Comic Sans MS', 12)) 
        startButton.pressed.connect(self.startBot)
        startButton.pressed.connect(lambda: self.adBot(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5))

        # Stop Button #

        stop = QPushButton("Stop", self) 
        stop.setGeometry(110, 80, 75, 25) 
        stop.setFont(QFont('Comic Sans MS', 12)) 
        stop.pressed.connect(self.stopBot)

############# Center Region #############

        # Cursor position #

        self.label = QLabel(self)
        self.label.setText('Set Cursor Positions') 
        self.label.setGeometry(60, 110, 405, 100)
        self.label.setFont(QFont('Comic Sans MS', 14)) 
        self.label.setAlignment(Qt.AlignLeft)

        # Positions gif #

        self.label = QLabel(self)
        self.movie = QMovie("emilia.gif")
        self.label.setMovie(self.movie)
        self.label.setGeometry(10, 140, 170, 145)
        self.label.setAlignment(Qt.AlignLeft)
        self.movie.start()

        # Ad Pos Button #

        adButton = QPushButton("Ad Button", self) 
        adButton.setGeometry(190, 140, 100, 25) 
        adButton.setFont(QFont('Comic Sans MS', 12))
        adButton.pressed.connect(self.getPos1)

        # Ad Content #

        adContent = QPushButton("Ad Content", self) 
        adContent.setGeometry(190, 170, 100, 25) 
        adContent.setFont(QFont('Comic Sans MS', 12))
        adContent.pressed.connect(self.getPos2)

        # Close Playstore #

        playstore = QPushButton("Playstore", self) 
        playstore.setGeometry(190, 200, 100, 25) 
        playstore.setFont(QFont('Comic Sans MS', 12))
        playstore.pressed.connect(self.getPos3)

        # Close Ad #

        closeAd = QPushButton("Close Ad", self) 
        closeAd.setGeometry(190, 230, 100, 25) 
        closeAd.setFont(QFont('Comic Sans MS', 12))
        closeAd.pressed.connect(self.getPos4)

        # Collect Coins #

        coins = QPushButton("Coins", self) 
        coins.setGeometry(190, 260, 100, 25) 
        coins.setFont(QFont('Comic Sans MS', 12))
        coins.pressed.connect(self.getPos5)

############# Bottom Region #############

        # Ad Counter #

        self.label = QLabel(self)
        self.label.setText("Ads Found: " + str(adCounter)) 
        self.label.setGeometry(5, 325, 405, 100)
        self.label.setFont(QFont('Comic Sans MS', 12)) 
        self.label.setAlignment(Qt.AlignLeft)

############# Functions #############

    def click(x, y):
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.01)                                                        # Pause for click to register
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    def getPos1(self):

            global x1                                                           # Allows global variable editing
            global y1
                
            time.sleep(5)
            x1, y1 = pyautogui.position()
            print(x1,y1)
            time.sleep(0.5)
            QMessageBox.about(self, "HTV Bot", "Cursor Position Set")
            
    def getPos2(self):
            
            global x2
            global y2

            time.sleep(5)
            x2, y2 = pyautogui.position()
            print(x2,y2)
            time.sleep(0.5)
            QMessageBox.about(self, "HTV Bot", "Cursor Position Set")

    def getPos3(self):

            global x3
            global y3

            time.sleep(5)
            x3, y3 = pyautogui.position()
            print(x3,y3)
            time.sleep(0.5)
            QMessageBox.about(self, "HTV Bot", "Cursor Position Set")

    def getPos4(self):

            global x4
            global y4

            time.sleep(5)
            x4, y4 = pyautogui.position()
            print(x4,y4)
            time.sleep(0.5)
            QMessageBox.about(self, "HTV Bot", "Cursor Position Set")

    def getPos5(self):

            global x5
            global y5

            time.sleep(5)
            x5, y5 = pyautogui.position()
            print(x5,y5)
            time.sleep(0.5)
            QMessageBox.about(self, "HTV Bot", "Cursor Position Set")

    def startBot(self): 

        # Sets flag to True
        self.flag = True
        print(self.flag)

    def stopBot(self): 
  
        # Sets flag to False 
        self.flag = False
        print(self.flag)

    def adBot(self, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5):

        global adCounter

        while self.flag == True:
                QApplication.processEvents()                                    # Fake Multithreading
                time.sleep(0.1)
        
                if pyautogui.pixel(x1, y1)[0] == 243:                           # Checks if an ad is avaliable
                        click(x1, y1)                                           # Ad button
                        QApplication.processEvents()
                        time.sleep(2)
                        click(x2, y2)                                           # Ad content
                        QApplication.processEvents()
                        time.sleep(2)
                        click(x3, y3)                                           # Close Play Store
                        QApplication.processEvents()
                        time.sleep(2)
                        click(x4, y4)                                           # Close ad content
                        QApplication.processEvents()
                        time.sleep(2)
                        click(x5, y5)                                           # Collect coins
                        adCounter+= 1                                           # Adds 1 to variable adCounter
                        adText = str(adCounter)
                        self.label.setText("Ads Found: " + str(adText))         # Sets text to new adCounter value
                else:
                        print("Nothing Found")                                  # For debugging

############# Make Window #############

App = QApplication(sys.argv) 
window = Window()
sys.exit(App.exec())
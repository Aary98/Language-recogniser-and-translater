import sys
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import*


class WebClass(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()
        self.showMaximized()


WebApp = QApplication(sys.argv)
QApplication.setApplicationName("Web Browser - Devloped By Arun More")
obj = WebClass()
WebApp.exec_()

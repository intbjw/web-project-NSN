import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        cwd = os.getcwd()
        super(MainWindow, self).__init__()
        self.setWindowTitle('攻击来源')
        self.setGeometry(100,100,1250,630)
        self.browser=QWebEngineView()
        #加载外部的web界面
        self.browser.load(QUrl('file:///C:/Users/intbjwww/PycharmProjects/web-project-NSN/code/render.html'))
        self.setCentralWidget(self.browser)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=MainWindow()
    win.show()
    app.exit(app.exec_())
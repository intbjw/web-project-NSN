# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'web.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os

from PyQt5.QtWidgets import QFileDialog, QHeaderView


class Ui_MainWindow(object):
    cwd = os.getcwd()
    set = ()
    fileName_choose = ""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1117, 865)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/intbjwww/Downloads/bitbug_favicon (1).ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(2.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_top = QtWidgets.QFrame(self.centralwidget)
        self.frame_top.setGeometry(QtCore.QRect(30, 770, 321, 51))
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.pushButton_open = QtWidgets.QPushButton(self.frame_top)
        self.pushButton_open.setGeometry(QtCore.QRect(10, 10, 71, 31))
        self.pushButton_open.setObjectName("pushButton_open")
        self.pushButton = QtWidgets.QPushButton(self.frame_top)
        self.pushButton.setGeometry(QtCore.QRect(200, 10, 71, 31))
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 70, 1061, 691))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox)
        self.tabWidget.setGeometry(QtCore.QRect(10, 30, 1051, 651))
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.table = QtWidgets.QTableWidget(self.tab)
        self.table.setGeometry(QtCore.QRect(0, 0, 1031, 621))
        self.table.setMinimumSize(QtCore.QSize(299, 200))
        self.table.setStyleSheet("font: 9pt \"Microsoft YaHei UI\";")
        self.table.setObjectName("table")
        self.table.setColumnCount(6)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(16)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(16)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(16)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(16)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(16)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(16)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(5, item)
        self.table.horizontalHeader().setMinimumSectionSize(40)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 0, 1021, 611))
        self.groupBox_2.setObjectName("groupBox_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.groupBox_2)
        self.graphicsView.setGeometry(QtCore.QRect(10, 20, 1001, 581))
        self.graphicsView.setObjectName("graphicsView")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 0, 1021, 611))
        self.groupBox_3.setObjectName("groupBox_3")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.groupBox_3)
        self.graphicsView_2.setGeometry(QtCore.QRect(10, 20, 1001, 581))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 0, 1021, 611))
        self.groupBox_4.setObjectName("groupBox_4")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.groupBox_4)
        self.graphicsView_3.setGeometry(QtCore.QRect(10, 20, 1001, 581))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.tabWidget.addTab(self.tab_4, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(860, 780, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Handwriting")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(990, 770, 51, 61))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(400, 20, 301, 51))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1117, 23))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton_open.clicked.connect(Ui_MainWindow.slot_btn_chooseFile)
        self.pushButton.clicked.connect(MainWindow.slot_btn_start)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def slot_btn_chooseFile(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(None, "选取日志", Ui_MainWindow.cwd, "All Files (*);;logs Files (*.log)")
        # 选择完文件之后返回选择文件的路径
        Ui_MainWindow.fileName_choose = fileName_choose

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "web日志分析工具"))
        self.pushButton_open.setText(_translate("MainWindow", "日志导入"))
        self.pushButton.setText(_translate("MainWindow", "日志分析"))
        self.groupBox.setTitle(_translate("MainWindow", "分析结果"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "目标IP"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "时间"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "威胁等级"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "威胁类型"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "威胁描述"))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "连接器"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "表一"))
        self.groupBox_2.setTitle(_translate("MainWindow", "访问次数最高的前10个IP"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "表二"))
        self.groupBox_3.setTitle(_translate("MainWindow", "访问次数最高的前10个URL"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "表三"))
        self.groupBox_4.setTitle(_translate("MainWindow", "攻击次数"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "表四"))
        self.label.setText(_translate("MainWindow", "design by"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">NSN</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600;\">web日志分析工具</span></p></body></html>"))


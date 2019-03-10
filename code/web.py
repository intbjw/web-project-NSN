# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'web.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import os
import re

from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
from PyQt5.QtWidgets import QFileDialog, QHeaderView, QPushButton, QDialog, QTabWidget
import requests
from pyecharts import Geo
from PyQt5.QtGui import QColor

class Ui_MainWindow(object):
    cwd = os.getcwd()
    set = ()
    fileName_choose = ""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1419, 916)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../Downloads/bitbug_favicon (1).ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(2.0)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_top = QtWidgets.QFrame(self.centralwidget)
        self.frame_top.setGeometry(QtCore.QRect(50, 800, 551, 51))
        self.frame_top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_top.setLineWidth(0)
        self.frame_top.setObjectName("frame_top")
        self.pushButton_open = QtWidgets.QPushButton(self.frame_top)
        self.pushButton_open.setGeometry(QtCore.QRect(10, 10, 71, 31))
        self.pushButton_open.setStyleSheet("background:green;")
        self.pushButton_open.setObjectName("pushButton_open")
        self.pushButton = QtWidgets.QPushButton(self.frame_top)
        self.pushButton.setGeometry(QtCore.QRect(200, 10, 71, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_top)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 10, 71, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 90, 1321, 701))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox)
        self.tabWidget.setGeometry(QtCore.QRect(10, 30, 1301, 661))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(9)
        self.tabWidget.setFont(font)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setStyleSheet("/*\n"
"/**********子界面背景**********/\n"
"QWidget#customWidget {\n"
"        background: rgb(68, 69, 73);\n"
"}\n"
"\n"
"/**********子界面中央背景**********/\n"
"QWidget#centerWidget {\n"
"        background: rgb(50, 50, 50);\n"
"}\n"
"\n"
"/**********主界面样式**********/\n"
"QWidget#mainWindow {\n"
"        border: 1px solid rgb(50, 50, 50);\n"
"        background: rgb(50, 50, 50);\n"
"}\n"
"\n"
"QWidget#messageWidget {\n"
"        background: rgba(68, 69, 73, 50%);\n"
"}\n"
"\n"
"QWidget#loadingWidget {\n"
"        border: none;\n"
"        border-radius: 5px;\n"
"        background: rgb(50, 50, 50);\n"
"}\n"
"\n"
"QWidget#remoteWidget {\n"
"        border-top-right-radius: 10px;\n"
"        border-bottom-right-radius: 10px;\n"
"        border: 1px solid rgb(45, 45, 45);\n"
"        background: rgb(50, 50, 50);\n"
"}\n"
"\n"
"StyledWidget {\n"
"        qproperty-normalColor: white;\n"
"        qproperty-disableColor: gray;\n"
"        qproperty-highlightColor: rgb(0, 160, 230);\n"
"        qproperty-errorColor: red;\n"
"}\n"
"\n"
"QProgressIndicator {\n"
"        qproperty-color: rgb(175, 175, 175);\n"
"}\n"
"/**********菜单栏**********/\n"
"QMenuBar {\n"
"        background: rgb(57, 58, 60);\n"
"        border: none;\n"
"}\n"
"/**********分组框**********/\n"
"QGroupBox {\n"
"        font-size: 15px;\n"
"        border: 1px solid rgb(80, 80, 80);\n"
"        border-radius: 4px;\n"
"        margin-top: 10px;\n"
"}\n"
"QGroupBox::title {\n"
"        color: rgb(175, 175, 175);\n"
"        top: -12px;\n"
"        left: 10px;\n"
"}\n"
"\n"
"/**********页签项**********/\n"
"QTabWidget::pane {\n"
"        border: none;\n"
"        border-top: 3px solid rgb(0, 160, 230);\n"
"        background: rgb(57, 58, 60);\n"
"}\n"
"QTabWidget::tab-bar {\n"
"        border: none;\n"
"}\n"
"QTabBar::tab {\n"
"        border: none;\n"
"        border-top-left-radius: 4px;\n"
"        border-top-right-radius: 4px;\n"
"        color: rgb(175, 175, 175);\n"
"        background: rgb(255, 255, 255, 30);\n"
"        height: 28px;\n"
"        min-width: 85px;\n"
"        margin-right: 5px;\n"
"        padding-left: 5px;\n"
"        padding-right: 5px;\n"
"}\n"
"QTabBar::tab:hover {\n"
"        background: rgb(255, 255, 255, 40);\n"
"}\n"
"QTabBar::tab:selected {\n"
"        color: white;\n"
"        background: rgb(0, 160, 230);\n"
"}\n"
"\n"
"QTabWidget#tabWidget::pane {\n"
"        border: 1px solid rgb(45, 45, 45);\n"
"        background: rgb(57, 58, 60);\n"
"        margin-top: -1px;\n"
"}\n"
"\n"
"QTabBar#tabBar::tab {\n"
"        border: 1px solid rgb(45, 45, 45);\n"
"        border-bottom: none;\n"
"        background: transparent;\n"
"}\n"
"QTabBar#tabBar::tab:hover {\n"
"        color: white;\n"
"}\n"
"QTabBar#tabBar::tab:selected {\n"
"        color: white;\n"
"        background: rgb(57, 58, 60);\n"
"}\n"
"\n"
"/**********表头**********/\n"
"QHeaderView{\n"
"        border: none;\n"
"        border-bottom: 3px solid rgb(0, 160, 230);\n"
"        background: rgb(57, 58, 60);\n"
"        min-height: 30px;\n"
"}\n"
"QHeaderView::section:horizontal {\n"
"        border: none;\n"
"        color: white;\n"
"        background: transparent;\n"
"        padding-left: 5px;\n"
"}\n"
"QHeaderView::section:horizontal:hover {\n"
"        background: rgb(0, 160, 230);\n"
"}\n"
"QHeaderView::section:horizontal:pressed {\n"
"        background: rgb(0, 180, 255);\n"
"}\n"
"QHeaderView::up-arrow {\n"
"        width: 13px;\n"
"        height: 11px;\n"
"        padding-right: 5px;\n"
"        image: url(:/Black/topArrow);\n"
"        subcontrol-position: center right;\n"
"}\n"
"QHeaderView::up-arrow:hover, QHeaderView::up-arrow:pressed {\n"
"        image: url(:/Black/topArrowHover);\n"
"}\n"
"QHeaderView::down-arrow {\n"
"        width: 13px;\n"
"        height: 11px;\n"
"        padding-right: 5px;\n"
"        image: url(:/Black/bottomArrow);\n"
"        subcontrol-position: center right;\n"
"}\n"
"QHeaderView::down-arrow:hover, QHeaderView::down-arrow:pressed {\n"
"        image: url(:/Black/bottomArrowHover);\n"
"}\n"
"\n"
"/**********表格**********/\n"
"QTableView {\n"
"        border: 1px solid rgb(45, 45, 45);\n"
"        background: rgb(57, 58, 60);\n"
"        gridline-color: rgb(60, 60, 60);\n"
"}\n"
# "QTableView::item {\n"
# "        padding-left: 5px;\n"
# "        padding-right: 5px;\n"
# "        border: none;\n"
# "        background: rgb(72, 72, 74);\n"
# "        border-right: 1px solid rgb(45, 45, 45);\n"
# "        border-bottom: 1px solid rgb(45, 45, 45);\n"
# "}\n"
"QTableView::item:selected {\n"
"        background: rgba(255, 255, 255, 40);\n"
"}\n"
"QTableView::item:selected:!active {\n"
"        color: white;\n"
"}\n"
"QTableView::indicator {\n"
"        width: 20px;\n"
"        height: 20px;\n"
"}\n"
"QTableView::indicator:enabled:unchecked {\n"
"        image: url(:/Black/checkBox);\n"
"}\n"
"QTableView::indicator:enabled:unchecked:hover {\n"
"        image: url(:/Black/checkBoxHover);\n"
"}\n"
"QTableView::indicator:enabled:unchecked:pressed {\n"
"        image: url(:/Black/checkBoxPressed);\n"
"}\n"
"QTableView::indicator:enabled:checked {\n"
"        image: url(:/Black/checkBoxChecked);\n"
"}\n"
"QTableView::indicator:enabled:checked:hover {\n"
"        image: url(:/Black/checkBoxCheckedHover);\n"
"}\n"
"QTableView::indicator:enabled:checked:pressed {\n"
"        image: url(:/Black/checkBoxCheckedPressed);\n"
"}\n"
"QTableView::indicator:enabled:indeterminate {\n"
"        image: url(:/Black/checkBoxIndeterminate);\n"
"}\n"
"QTableView::indicator:enabled:indeterminate:hover {\n"
"        image: url(:/Black/checkBoxIndeterminateHover);\n"
"}\n"
"QTableView::indicator:enabled:indeterminate:pressed {\n"
"        image: url(:/Black/checkBoxIndeterminatePressed);\n"
"}\n"
"\n"
"/**********输入框**********/\n"
"QLineEdit {\n"
"        border-radius: 4px;\n"
"        height: 25px;\n"
"        border: 1px solid rgb(100, 100, 100);\n"
"        background: rgb(72, 72, 73);\n"
"}\n"
"QLineEdit:enabled {\n"
"        color: rgb(175, 175, 175);\n"
"}\n"
"QLineEdit:enabled:hover, QLineEdit:enabled:focus {\n"
"        color: rgb(230, 230, 230);\n"
"}\n"
"QLineEdit:!enabled {\n"
"        color: rgb(155, 155, 155);\n"
"}\n"
"\n"
"/**********文本编辑框**********/\n"
"QTextEdit {\n"
"        border: 1px solid rgb(45, 45, 45);\n"
"        color: rgb(175, 175, 175);\n"
"        background: rgb(57, 58, 60);\n"
"}\n"
"/**********微调器**********/\n"
"QSpinBox {\n"
"        border-radius: 4px;\n"
"        height: 24px;\n"
"        min-width: 40px;\n"
"        border: 1px solid rgb(100, 100, 100);\n"
"        background: rgb(68, 69, 73);\n"
"}\n"
"QSpinBox:enabled {\n"
"        color: rgb(220, 220, 220);\n"
"}\n"
"QSpinBox:enabled:hover, QLineEdit:enabled:focus {\n"
"        color: rgb(230, 230, 230);\n"
"}\n"
"QSpinBox:!enabled {\n"
"        color: rgb(65, 65, 65);\n"
"        background: transparent;\n"
"}\n"
"QSpinBox::up-button {\n"
"        width: 18px;\n"
"        height: 12px;\n"
"        border-top-right-radius: 4px;\n"
"        border-left: 1px solid rgb(100, 100, 100);\n"
"        image: url(:/Black/upButton);\n"
"        background: rgb(50, 50, 50);\n"
"}\n"
"QSpinBox::up-button:!enabled {\n"
"        border-left: 1px solid gray;\n"
"        background: transparent;\n"
"}\n"
"QSpinBox::up-button:enabled:hover {\n"
"        background: rgb(255, 255, 255, 30);\n"
"}\n"
"QSpinBox::down-button {\n"
"        width: 18px;\n"
"        height: 12px;\n"
"        border-bottom-right-radius: 4px;\n"
"        border-left: 1px solid rgb(100, 100, 100);\n"
"        image: url(:/Black/downButton);\n"
"        background: rgb(50, 50, 50);\n"
"}\n"
"QSpinBox::down-button:!enabled {\n"
"        border-left: 1px solid gray;\n"
"        background: transparent;\n"
"}\n"
"QSpinBox::down-button:enabled:hover {\n"
"        background: rgb(255, 255, 255, 30);\n"
"}\n"
"\n"
"/**********标签**********/\n"
"QLabel#grayLabel {\n"
"        color: rgb(175, 175, 175);\n"
"}\n"
"\n"
"QLabel#highlightLabel {\n"
"        color: rgb(175, 175, 175);\n"
"}\n"
"\n"
"QLabel#redLabel {\n"
"        color: red;\n"
"}\n"
"\n"
"QLabel#grayYaHeiLabel {\n"
"        color: rgb(175, 175, 175);\n"
"        font-size: 16px;\n"
"}\n"
"\n"
"QLabel#blueLabel {\n"
"        color: rgb(0, 160, 230);\n"
"}\n"
"\n"
"QLabel#listLabel {\n"
"        color: rgb(0, 160, 230);\n"
"}\n"
"\n"
"QLabel#lineBlueLabel {\n"
"        background: rgb(0, 160, 230);\n"
"}\n"
"\n"
"QLabel#graySeperateLabel {\n"
"        background: rgb(45, 45, 45);\n"
"}\n"
"\n"
"QLabel#seperateLabel {\n"
"        background: rgb(80, 80, 80);\n"
"}\n"
"\n"
"QLabel#radiusBlueLabel {\n"
"        border-radius: 15px;\n"
"        color: white;\n"
"        font-size: 16px;\n"
"        background: rgb(0, 160, 230);\n"
"}\n"
"\n"
"QLabel#skinLabel[colorProperty=\"normal\"] {\n"
"        color: rgb(175, 175, 175);\n"
"}\n"
"QLabel#skinLabel[colorProperty=\"highlight\"] {\n"
"        color: rgb(0, 160, 230);\n"
"}\n"
"\n"
"QLabel#informationLabel {\n"
"        qproperty-pixmap: url(:/Black/information);\n"
"}\n"
"\n"
"QLabel#errorLabel {\n"
"        qproperty-pixmap: url(:/Black/error);\n"
"}\n"
"\n"
"QLabel#successLabel {\n"
"        qproperty-pixmap: url(:/Black/success);\n"
"}\n"
"\n"
"QLabel#questionLabel {\n"
"        qproperty-pixmap: url(:/Black/question);\n"
"}\n"
"\n"
"QLabel#warningLabel {\n"
"        qproperty-pixmap: url(:/Black/warning);\n"
"}\n"
"\n"
"QLabel#groupLabel {\n"
"        color: rgb(0, 160, 230);\n"
"        border: 1px solid rgb(0, 160, 230);\n"
"        font-size: 15px;\n"
"        border-top-color: transparent;\n"
"        border-right-color: transparent;\n"
"        border-left-color: transparent;\n"
"}\n"
"\n"
"/**********按钮**********/\n"
"QToolButton#nsccButton{\n"
"        border: none;\n"
"        color: rgb(175, 175, 175);\n"
"        background: transparent;\n"
"        padding: 10px;\n"
"        qproperty-icon: url(:/Black/nscc);\n"
"        qproperty-iconSize: 32px 32px;\n"
"        qproperty-toolButtonStyle: ToolButtonTextUnderIcon;\n"
"}\n"
"QToolButton#nsccButton:hover{\n"
"        color: rgb(217, 218, 218);\n"
"        background: rgb(255, 255, 255, 20);\n"
"}\n"
"\n"
"QToolButton#transferButton{\n"
"        border: none;\n"
"        color: rgb(175, 175, 175);\n"
"        background: transparent;\n"
"        padding: 10px;\n"
"        qproperty-icon: url(:/Black/transfer);\n"
"        qproperty-iconSize: 32px 32px;\n"
"        qproperty-toolButtonStyle: ToolButtonTextUnderIcon;\n"
"}\n"
"QToolButton#transferButton:hover{\n"
"        color: rgb(217, 218, 218);\n"
"        background: rgb(255, 255, 255, 20);\n"
"}\n"
"\n"
"/**********按钮**********/\n"
"QPushButton{\n"
"        border-radius: 4px;\n"
"        border: none;\n"
"        width: 75px;\n"
"        height: 25px;\n"
"}\n"
"QPushButton:enabled {\n"
"        background: rgb(68, 69, 73);\n"
"        color: white;\n"
"}\n"
"QPushButton:!enabled {\n"
"        background: rgb(100, 100, 100);\n"
"        color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:enabled:hover{\n"
"        background: rgb(85, 85, 85);\n"
"}\n"
"QPushButton:enabled:pressed{\n"
"        background: rgb(80, 80, 80);\n"
"}\n"
"\n"
"QPushButton#blueButton {\n"
"        color: white;\n"
"}\n"
"QPushButton#blueButton:enabled {\n"
"        background: rgb(0, 165, 235);\n"
"        color: white;\n"
"}\n"
"QPushButton#blueButton:!enabled {\n"
"        background: gray;\n"
"        color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton#blueButton:enabled:hover {\n"
"        background: rgb(0, 180, 255);\n"
"}\n"
"QPushButton#blueButton:enabled:pressed {\n"
"        background: rgb(0, 140, 215);\n"
"}\n"
"\n"
"QPushButton#selectButton {\n"
"        border: none;\n"
"        border-radius: none;\n"
"        border-left: 1px solid rgb(100, 100, 100);\n"
"        image: url(:/Black/scan);\n"
"        background: transparent;\n"
"        color: white;\n"
"}\n"
"QPushButton#selectButton:enabled:hover{\n"
"        background: rgb(85, 85, 85);\n"
"}\n"
"QPushButton#selectButton:enabled:pressed{\n"
"        background: rgb(80, 80, 80);\n"
"}\n"
"\n"
"QPushButton#linkButton {\n"
"        background: transparent;\n"
"        color: rgb(0, 160, 230);\n"
"        text-align:left;\n"
"}\n"
"QPushButton#linkButton:hover {\n"
"        color: rgb(20, 185, 255);\n"
"        text-decoration: underline;\n"
"}\n"
"QPushButton#linkButton:pressed {\n"
"        color: rgb(0, 160, 230);\n"
"}\n"
"\n"
"QPushButton#transparentButton {\n"
"        background: transparent;\n"
"}\n"
"\n"
"/*****************标题栏按钮*******************/\n"
"QPushButton#minimizeButton {\n"
"        border-radius: none;\n"
"        border-bottom-left-radius: 4px;\n"
"        border-bottom-right-radius: 4px;\n"
"        background: rgb(50, 50, 50);\n"
"        image: url(:/Black/minimize);\n"
"}\n"
"QPushButton#minimizeButton:hover {\n"
"        background: rgb(60, 60, 60);\n"
"        image: url(:/Black/minimizeHover);\n"
"}\n"
"QPushButton#minimizeButton:pressed {\n"
"        background: rgb(55, 55, 55);\n"
"        image: url(:/Black/minimizePressed);\n"
"}\n"
"\n"
"QPushButton#maximizeButton[maximizeProperty=\"maximize\"] {\n"
"        border-radius: none;\n"
"        border-bottom-left-radius: 4px;\n"
"        border-bottom-right-radius: 4px;\n"
"        background: rgb(50, 50, 50);\n"
"        image: url(:/Black/maximize);\n"
"}\n"
"QPushButton#maximizeButton[maximizeProperty=\"maximize\"]:hover {\n"
"        background: rgb(60, 60, 60);\n"
"        image: url(:/Black/maximizeHover);\n"
"}\n"
"QPushButton#maximizeButton[maximizeProperty=\"maximize\"]:pressed {\n"
"        background: rgb(55, 55, 55);\n"
"        image: url(:/Black/maximizePressed);\n"
"}\n"
"\n"
"QPushButton#maximizeButton[maximizeProperty=\"restore\"] {\n"
"        border-radius: none;\n"
"        border-bottom-left-radius: 4px;\n"
"        border-bottom-right-radius: 4px;\n"
"        background: rgb(50, 50, 50);\n"
"        image: url(:/Black/restore);\n"
"}\n"
"QPushButton#maximizeButton[maximizeProperty=\"restore\"]:hover {\n"
"        background: rgb(60, 60, 60);\n"
"        image: url(:/Black/restoreHover);\n"
"}\n"
"QPushButton#maximizeButton[maximizeProperty=\"restore\"]:pressed {\n"
"        background: rgb(55, 55, 55);\n"
"        image: url(:/Black/restorePressed);\n"
"}\n"
"\n"
"QPushButton#closeButton {\n"
"        border-radius: none;\n"
"        border-bottom-left-radius: 4px;\n"
"        border-bottom-right-radius: 4px;\n"
"        background: rgb(50, 50, 50);\n"
"        image: url(:/Black/close);\n"
"}\n"
"QPushButton#closeButton:hover {\n"
"        background: rgb(60, 60, 60);\n"
"        image: url(:/Black/closeHover);\n"
"}\n"
"QPushButton#closeButton:pressed {\n"
"        background: rgb(55, 55, 55);\n"
"        image: url(:/Black/closePressed);\n"
"}\n"
"QPushButton#feedbackButton {\n"
"        border-radius: none;\n"
"        border-bottom-left-radius: 4px;\n"
"        border-bottom-right-radius: 4px;\n"
"        background: rgb(50, 50, 50);\n"
"        image: url(:/Black/feedback);\n"
"}\n"
"QPushButton#feedbackButton:hover {\n"
"        background: rgb(60, 60, 60);\n"
"        image: url(:/Black/feedbackHover);\n"
"}\n"
"QPushButton#feedbackButton:pressed {\n"
"        background: rgb(55, 55, 55);\n"
"        image: url(:/Black/feedbackPressed);\n"
"}\n"
"\n"
"QPushButton#closeTipButton {\n"
"        border-radius: none;\n"
"        border-image: url(:/Black/close);\n"
"        background: transparent;\n"
"}\n"
"QPushButton#closeTipButton:hover {\n"
"        border-image: url(:/Black/closeHover);\n"
"}\n"
"QPushButton#closeTipButton:pressed {\n"
"        border-image: url(:/Black/closePressed);\n"
"}\n"
"\n"
"QPushButton#changeSkinButton{\n"
"        border-radius: 4px;\n"
"        border: 2px solid rgb(41, 41, 41);\n"
"        background: rgb(51, 51, 51);\n"
"}\n"
"QPushButton#changeSkinButton:hover{\n"
"        border-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton#changeSkinButton:pressed, QPushButton#changeSkinButton:checked{\n"
"        border-color: rgb(0, 160, 230);\n"
"}\n"
"\n"
"QPushButton#transferButton {\n"
"        padding-left: 5px;\n"
"        padding-right: 5px;\n"
"        color: white;\n"
"        background: rgb(0, 165, 235);\n"
"}\n"
"QPushButton#transferButton:hover {\n"
"        background: rgb(0, 180, 255);\n"
"}\n"
"QPushButton#transferButton:pressed {\n"
"        background: rgb(0, 140, 215);\n"
"}\n"
"QPushButton#transferButton[iconProperty=\"left\"] {\n"
"        qproperty-icon: url(:/Black/left);\n"
"}\n"
"QPushButton#transferButton[iconProperty=\"right\"] {\n"
"        qproperty-icon: url(:/Black/right);\n"
"}\n"
"\n"
"QPushButton#openButton {\n"
"        border-radius: none;\n"
"        image: url(:/Black/open);\n"
"        background: transparent;\n"
"}\n"
"QPushButton#openButton:hover {\n"
"        image: url(:/Black/openHover);\n"
"}\n"
"QPushButton#openButton:pressed {\n"
"        image: url(:/Black/openPressed);\n"
"}\n"
"\n"
"QPushButton#deleteButton {\n"
"        border-radius: none;\n"
"        image: url(:/Black/delete);\n"
"        background: transparent;\n"
"}\n"
"QPushButton#deleteButton:hover {\n"
"        image: url(:/Black/deleteHover);\n"
"}\n"
"QPushButton#deleteButton:pressed {\n"
"        image: url(:/Black/deletePressed);\n"
"}\n"
"\n"
"QPushButton#menuButton {\n"
"        text-align: left center;\n"
"        padding-left: 3px;\n"
"        color: rgb(175, 175, 175);\n"
"        border: 1px solid rgb(100, 100, 100);\n"
"        background: rgb(72, 72, 73);\n"
"}\n"
"QPushButton#menuButton::menu-indicator{\n"
"        subcontrol-position: right center;\n"
"        subcontrol-origin: padding;\n"
"        image: url(:/Black/arrowBottom);\n"
"        padding-right: 3px;\n"
"}\n"
"")
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.table = QtWidgets.QTableWidget(self.tab)
        self.table.setGeometry(QtCore.QRect(0, 0, 1301, 651))
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
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_3.setGeometry(QtCore.QRect(0, -10, 1301, 641))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.groupBox_3)
        self.graphicsView_2.setGeometry(QtCore.QRect(0, 20, 1301, 621))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(0, -10, 1301, 651))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.groupBox_2)
        self.graphicsView.setGeometry(QtCore.QRect(0, 20, 1301, 621))
        self.graphicsView.setObjectName("graphicsView")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_4.setGeometry(QtCore.QRect(0, -10, 1301, 641))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.groupBox_4)
        self.graphicsView_3.setGeometry(QtCore.QRect(0, 20, 1301, 621))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.tabWidget.addTab(self.tab_4, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(910, 810, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Handwriting")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1090, 800, 81, 61))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(510, 20, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(26)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1419, 23))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        self.pushButton_open.clicked.connect(Ui_MainWindow.slot_btn_chooseFile)
        self.pushButton.clicked.connect(MainWindow.slot_btn_start)
        self.pushButton_2.clicked.connect(Ui_MainWindow.slot_btn_ip)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def slot_btn_chooseFile(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(None, "选取日志", Ui_MainWindow.cwd,
                                                                "All Files (*);;logs Files (*.log)")
        # 选择完文件之后返回选择文件的路径
        Ui_MainWindow.fileName_choose = fileName_choose
    def slot_btn_ip(self):
        getipaddress()
        cwd = os.path.abspath('render.html')
        Dialog = QDialog()
        Dialog.setObjectName("Dialog")
        Dialog.resize(1255, 640)
        Dialog.webEngineView = QtWebEngineWidgets.QWebEngineView(Dialog)
        Dialog.webEngineView.setGeometry(QtCore.QRect(19, 19, 1211, 630))
        Dialog.webEngineView.setUrl(QtCore.QUrl.fromLocalFile(cwd))
        Dialog.webEngineView.setObjectName("webEngineView")

        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setWindowTitle("IP溯源")
        Dialog.exec_()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "web日志分析工具"))
        self.pushButton_open.setText(_translate("MainWindow", "日志导入"))
        self.pushButton.setText(_translate("MainWindow", "日志分析"))
        self.pushButton_2.setText(_translate("MainWindow", "IP溯源"))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "攻击分析"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "访问次数最高的前10个URL"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "访问次数最高的前10个IP"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "攻击次数"))
        self.label.setText(_translate("MainWindow", "design by"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">NSN</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">web日志分析工具</span></p></body></html>"))

#采用百度的api
def ipGeo(data):
    geo = Geo(
        "攻击来源",
        "精确到市",
        title_color="#fff",
        title_pos="center",
        width=1200,
        height=600,
        background_color="#404a59",
        )
    attr, value = geo.cast(data)
    geo.add(
        "",
        attr,
        value,
        visual_range=[0, 2000],
        visual_text_color="#fff",
        symbol_size=15,
        is_visualmap=True,
    )
    geo.render()
def getipaddress():
    ipaddress = []
    with open('data.json') as f:
        data = f.read()
        data = eval(data)
        for i in data:
            ip = i['ip']
            r = requests.get('http://api.map.baidu.com/location/ip?ip=' + ip + '&ak=X7K1gs9RPEoakNnYOtcIgPeMaqGu7TVu&coor=bd09ll')
            #result1 = json.dumps(r.text)
            result1 = eval(r.text)
            if result1['status'] == 0:
                city = result1['content']['address_detail']['city']
                if city=='':
                    nr = requests.get('http://www.ip138.com/ips138.asp?ip='+ip+'&action=2')
                    nr.encoding = nr.apparent_encoding
                    try:
                        rlt = re.search(r'<li>本站数据：.*市',nr.text).group(0)

                    except:
                        print(ip)
                    pos = rlt.find('省')
                    rlt = rlt[pos + 1:].replace('市', '')
                    city = rlt
                    print(city)
                ipcount = i['ipcount']
                ipaddress = ipaddress + [(city,ipcount)]
    print(ipaddress)
    ipGeo(ipaddress)

class Ui_Dialog(object):
    cwd = os.path.abspath('render.html')
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1255, 697)
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(Dialog)
        self.webEngineView.setGeometry(QtCore.QRect(19, 19, 1211, 661))
        self.webEngineView.setUrl(QtCore.QUrl.fromLocalFile(self.cwd))
        self.webEngineView.setObjectName("webEngineView")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "IP溯源"))
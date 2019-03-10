import sys
import webbrowser

import requests
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from pyecharts import Geo
import sys
import analyse
from PyQt5 import QtWidgets
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem ,QMessageBox
from PyQt5 import QtCore, QtGui
from web import Ui_MainWindow
from figure import *
class Mainwindow(QMainWindow):
    def __init__(self,parent=None):
        super(Mainwindow,self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    def slot_btn_start(self):
        #分析程序开始,绘制相关的表格
        if Ui_MainWindow.fileName_choose == "":
            QMessageBox.critical(self, "错误", "请导入文件！！！")
        else:
            Ui_MainWindow.set = analyse.analyseLog(Ui_MainWindow.fileName_choose)
            #print(Ui_MainWindow.set)
            with open("data.json", "r") as f:
                datas = f.read()
                datas = eval(datas)
                #print(datas)
                self.ui.table.setRowCount(len(datas))
                i = 0
                for data in datas:
                    self.ui.table.setItem(i, 0, QTableWidgetItem(data['ip']))
                    self.ui.table.setItem(i, 1, QTableWidgetItem(data['date']))
                    self.ui.table.setItem(i, 2, QTableWidgetItem(str(data['level'])))
                    self.ui.table.setItem(i, 3, QTableWidgetItem(data['type']))
                    self.ui.table.setItem(i, 4, QTableWidgetItem(data['describe']))
                    self.ui.table.setItem(i, 5, QTableWidgetItem(data['user-agent']))
                    if i % 2 ==0 :
                        for j in range(6):
                            self.ui.table.item(i, j).setBackground(QBrush(QColor(176, 196, 222)))
                    if data['level'] == 1:
                        self.ui.table.item(i, 2).setBackground(QBrush(QColor(176, 196, 222)))
                    if data['level'] == 2:
                        self.ui.table.item(i, 2).setBackground(QBrush(QColor(255,255,0)))
                    if data['level'] == 3:
                        self.ui.table.item(i, 2).setBackground(QBrush(QColor(238,130,238)))
                    if data['level'] == 4:
                        self.ui.table.item(i, 2).setBackground(QBrush(QColor(128,0,0)))
                    i = i + 1

            #绘制访问次数最高的前10个IP
            dr = Figure_Canvas()
            dr.plot_1(Ui_MainWindow.set)
            graphicscene = QtWidgets.QGraphicsScene()
            graphicscene.addWidget(dr)
            self.ui.graphicsView.setScene(graphicscene)
            self.ui.graphicsView.show()
            #绘制访问次数最高的前10个URL
            dr = Figure_Canvas()
            dr.plot_2(Ui_MainWindow.set)
            graphicscene = QtWidgets.QGraphicsScene()
            graphicscene.addWidget(dr)
            self.ui.graphicsView_2.setScene(graphicscene)
            self.ui.graphicsView_2.show()
            #绘制攻击次数
            dr = Figure_Canvas()
            dr.plot_3(Ui_MainWindow.set)
            graphicscene = QtWidgets.QGraphicsScene()
            graphicscene.addWidget(dr)
            self.ui.graphicsView_3.setScene(graphicscene)
            self.ui.graphicsView_3.show()
    def slot_btn_ip(self):
        cwd = os.path.abspath('render.html')
        openUrl(cwd)

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
            result1 = r.json()
            #print(result1)
            city = result1['content']['address_detail']['city']
            ipcount = i['ipcount']
            ipaddress = ipaddress + [(city,ipcount)]
    #print(ipaddress)
    ipGeo(ipaddress)
def openUrl(url):
    try:
        webbrowser.get('chrome').open_new_tab(url)
    except Exception as e:
        webbrowser.open_new_tab(url)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = Mainwindow()
    MainWindow.show()
    sys.exit(app.exec_())

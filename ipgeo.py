import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    from pyecharts import Geo
    # 存放数据 攻击来源 攻击次数
    import requests
    # 采用百度的api
    import json
    def ip2address(ip):
        r = requests.get(
            'http://api.map.baidu.com/location/ip?ip=' + ip + '&ak=X7K1gs9RPEoakNnYOtcIgPeMaqGu7TVu&coor=bd09ll')
        result = r.json()
        city = result['content']['address_detail']['city']
        return city

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
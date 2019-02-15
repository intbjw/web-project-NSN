import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import pylab as pl
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
class Figure_Canvas(FigureCanvas):   # 通过继承FigureCanvas类，使得该类既是一个PyQt5的Qwidget，又是一个matplotlib的FigureCanvas，这是连接pyqt5与matplot                                          lib的关键

    def __init__(self, parent=None, width=11, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=100)  # 创建一个Figure，注意：该Figure为matplotlib下的figure，不是matplotlib.pyplot下面的figure
        FigureCanvas.__init__(self, fig) # 初始化父类
        self.setParent(parent)
        self.axes = fig.add_subplot(111) # 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法

    def plot_1(self,data):
        ip_data = data[1]
        ips = []
        for ip in ip_data:
            ips.append(ip[0])
        num = []
        for ip in ip_data:
            num.append(ip[1])
        y_pos = np.arange(len(ips))
        ax = self.axes
        # range 和 arange 的作用是类似的，只不过arange 可以接受非int 类型的数据
        ax.barh(y_pos, num, color='greenyellow', align="center")
        ax.set_yticks(y_pos)  # 设置标度的位置
        ax.set_yticklabels(ips)  # 设置纵坐标的每一个刻度的属性值
        ax.invert_yaxis()  # 反转标度值
        ax.set_xlabel("次数", fontproperties="SimHei")  # 设置横坐标的单位
        ax.set_title("访问次数最高的前10个IP", fontproperties="SimHei")  # 设定图片的标题

    def plot_2(self, data):
        url_data = data[0]
        urls = []
        for url in url_data:
            urls.append(url[0])
        num = []
        for url in url_data:
            num.append(url[1])
        y_pos = np.arange(len(urls))
        ax = self.axes
        # range 和 arange 的作用是类似的，只不过arange 可以接受非int 类型的数据
        ax.barh(y_pos, num, color='greenyellow', align="center")
        ax.set_yticks(y_pos)  # 设置标度的位置
        ax.set_yticklabels(urls)  # 设置纵坐标的每一个刻度的属性值
        ax.invert_yaxis()  # 反转标度值
        ax.set_xlabel("次数", fontproperties="SimHei")  # 设置横坐标的单位
        ax.set_title("访问次数最高的前10个IP", fontproperties="SimHei")  # 设定图片的标题

    def plot_3(self, data):
        attack_data = data[2]
        attacks = []
        for attack in attack_data:
            attacks.append(attack[0])
        num = []
        for url in attack_data:
            num.append(url[1])
        y_pos = np.arange(len(attacks))
        ax = self.axes
        # range 和 arange 的作用是类似的，只不过arange 可以接受非int 类型的数据
        ax.barh(y_pos, num, color='greenyellow', align="center")
        ax.set_yticks(y_pos)  # 设置标度的位置
        ax.set_yticklabels(attacks,fontproperties="SimHei")  # 设置纵坐标的每一个刻度的属性值
        ax.invert_yaxis()  # 反转标度值
        ax.set_xlabel("次数", fontproperties="SimHei")  # 设置横坐标的单位
        ax.set_title("攻击次数", fontproperties="SimHei")  # 设定图片的标题

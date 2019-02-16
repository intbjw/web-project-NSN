import sys
import analyse
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from web import Ui_MainWindow
from figure import *
class Mainwindow(QMainWindow):
    def __init__(self,parent=None):
        super(Mainwindow,self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    def slot_btn_start(self):
        #分析程序开始,绘制相关的表格
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
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = Mainwindow()
    MainWindow.show()
    sys.exit(app.exec_())

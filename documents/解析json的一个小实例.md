# 解析json的一个小实例

由于大多数据都以json的形式存储，所以我们也想把日志中的信息转化为json。

界面：

![](F:\web-project-NSN\pic\win.png)

其中用到的组件有QGroupbox，QComboBox(下拉菜单)，QTextEdit(文本编辑)，QPushButton(按钮)

给其中的两个按钮增加了信号

```python
self.pushButton.clicked.connect(Form.queryWeather)#括号中为接收信号的槽
self.pushButton_2.clicked.connect(Form.clearResult)
```

上传代码

WeatherWin.py

```python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WeatherWin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(405, 371)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 381, 281))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 22, 61, 20))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(90, 20, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(13, 60, 361, 211))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 320, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 320, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.queryWeather)
        self.pushButton_2.clicked.connect(Form.clearResult)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "查询城市天气"))
        self.label.setText(_translate("Form", "城市"))
        self.comboBox.setItemText(0, _translate("Form", "北京"))
        self.comboBox.setItemText(1, _translate("Form", "昌黎"))
        self.comboBox.setItemText(2, _translate("Form", "保定"))
        self.pushButton.setText(_translate("Form", "查询"))
        self.pushButton_2.setText(_translate("Form", "清空"))
```

CallWeatherWin.py

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from WeatherWin import Ui_Form

import requests

class Mainwindow(QMainWindow):
    def __init__(self,parent=None):
        super(Mainwindow,self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
	#查询按钮的事件响应
    def queryWeather(self):
        print("* queryWeather  ")
        cityName = self.ui.comboBox.currentText()
        cityCode = self.transCityName(cityName)
        rep = requests.get('http://www.weather.com.cn/data/sk/' + cityCode + '.html')
        rep.encoding = "utf-8"
        print(rep.json())
        msg1 = "城市：{}".format(rep.json()['weatherinfo']['city']) + '\n'
        msg2 = "风向：{}".format(rep.json()['weatherinfo']['WD']) + '\n'
        msg3 = "温度：{}".format(rep.json()['weatherinfo']['temp']) + '\n'
        msg4 = "风力：{}".format(rep.json()['weatherinfo']['WS']) + '\n'
        msg5 = "湿度：{}".format(rep.json()['weatherinfo']['SD']) + '\n'
        result = msg1 + msg2 + msg3 + msg4 + msg5
        self.ui.textEdit.setText(result)
    def transCityName(self,cityName):
        cityCode = ''
        if cityName == "北京":
            cityCode = '101010100'
        elif cityName == "昌黎":
            cityCode = '101091103'
        return cityCode
    #清空按钮的事件响应
    def clearResult(self):
        print("*  clearResult")
        self.ui.textEdit.clear()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Mainwindow()
    win.show()
    sys.exit(app.exec_())
```

运行结果：

![忽略数据](F:\web-project-NSN\pic\win2.png)
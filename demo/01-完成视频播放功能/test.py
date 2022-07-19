#下面这行代码是为了避免在所生成的pyqt中出现中文乱码的问题
# -*- coding:UTF-8 -*-
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        #初始化继承的父类（Qmainwindow）
        super(MainWindow, self).__init__(parent)
        #设置窗口的大小
        self.resize(400,200)
        #实例化创建状态栏
        self.status=self.statusBar()
        #将提示信息显示在状态栏中showMessage（‘提示信息’，显示时间（单位毫秒））
        self.status.showMessage('这是状态栏提示',4000)
        #创建窗口标题
        self.setWindowTitle('PyQt MainWindow例子')


if __name__ == '__main__':
    # 每一个pyqt程序中都需要有一个QApplication对象，sys.argv是一个命令行参数列表
    app=QApplication(sys.argv)
    #实例化窗口
    form=MainWindow()
    #窗口显示
    form.show()
    #进入程序的主循环，遇到退出情况，终止程序
    sys.exit(app.exec_())

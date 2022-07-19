from basic import Ui_MainWindow

import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

import cv2
import numpy as np
# 　　PyQt5 读取 opencv 的原始图像数据需要经过一些转换步骤.
#
# 　　由于历史原因，opencv 使用的像素格式为 BGR 格式，现在的图像和视频大都是 RGB 格式，所以使用 QImage 加载 opencv 原始数据前，需要使用 cv2.cvtColor 转换数据格式到 RGB 格式，参数为 cv2.COLOR_BGR2RGB.
# 　　使用 QImage 从 opencv mat 中读取图像原始数据，这里需要指定图像矩阵的数据格式和图像的宽度和高度，上面将像素格式转换为 RGB，图像深度为 8 位，所以格式为 RGB888.


class App(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sigal_slot()  # 信号和槽
        self.show_img()
        #self.save_img()



    def sigal_slot(self):
        self.pushButton.clicked.connect(self.save_img)

    def img_convert(self): # opencv格式数据转换为Qlabel可以加载的QPixmap格式
        #res = cv2.resize(self.img, (300, 400), interpolation=cv2.INTER_CUBIC)  # 用cv2.resize设置图片大小
        res = self.img
        img2 = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)  # opencv读取的bgr格式图片转换成rgb格式
        _image = QtGui.QImage(img2[:], img2.shape[1], img2.shape[0], img2.shape[1] * 3,
                              QtGui.QImage.Format_RGB888)  # pyqt5转换成自己能放的图片格式
        self.jpg_out = QtGui.QPixmap(_image).scaled(self.label.width(), self.label.height()) #适应label图片大小
        #self.jpg_out = QtGui.QPixmap(_image)  # 转换成QPixmap

    def show_img(self):
        img_path = 'E:\\images\\bus.jpg'
        self.img = cv2.imread(img_path)  # opencv读取图片
        self.img = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), -1)
        #print(type(self.img)) <class 'numpy.ndarray'>
        self.img_convert()

        self.label.setPixmap(self.jpg_out)  # 设置图片显示

    def save_img(self):
        cur_dir = os.path.dirname(__file__)
        save_dir = str(cur_dir) + '/results'
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)
        save_path = save_dir + '/1.jpg'
        #cv2.imwrite(str(save_path), self.img) # imwrite保存时不能含中文路径，可用imencode
        #cv2.imwrite('./1.jpg', self.img)
        cv2.imencode('.jpg', self.img)[1].tofile(save_path)
        #cv2.imshow('img', self.img)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = App()
    ui.show()
    # MainWindow = QtWidgets.QMainWindow()
    # ui = App()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    sys.exit(app.exec_())

from basic import Ui_MainWindow

import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
import cv2

class App(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sigal_slot()  # 信号和槽
        #self.show_img()
        self.timer_camera = QTimer()  # 定义定时器
        self.show_video()
        #self.save_img()

    def sigal_slot(self):
        self.pushButton_2.clicked.connect(self.slotStart)  # 按钮关联槽函数
        self.pushButton_3.clicked.connect(self.slotStop)

    def show_video(self):
        video = 'E:/video/Image1.wmv'  # 加载视频文件
        video = 'E:/video/2.avi'
        self.cap = cv2.VideoCapture(video)
        print(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))

    def slotStart(self):
        """ Slot function to start the progamme
        """
        self.timer_camera.start(10)
        print('start')
        self.timer_camera.timeout.connect(self.openFrame)

    def slotStop(self):
        self.cap.release()
        self.timer_camera.stop()  # 停止计时器

    def openFrame(self):
        ret, frame = self.cap.read()
        if (self.cap.isOpened()):
            ret, frame = self.cap.read()
            #print(type(frame)) <class 'numpy.ndarray'>
            if ret:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                gray = cv2.cvtColor(gray, cv2.COLOR_BGR2RGB)

                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                height, width, bytesPerComponent = frame.shape
                bytesPerLine = bytesPerComponent * width
                q_image = QtGui.QImage(frame.data, width, height, bytesPerLine,
                                 QtGui.QImage.Format_RGB888).scaled(self.label.width(), self.label.height())
                self.label.setPixmap(QtGui.QPixmap.fromImage(q_image))

                # q_image2 = QtGui.QImage(gray.data, width, height, width,
                #                   QtGui.QImage.Format_RGB888).scaled(self.label.width(),
                #                                                self.label.height())
                # self.label.setPixmap(QtGui.QPixmap.fromImage(q_image2))
            else:
                self.cap.release()
                self.timer_camera.stop()  # 停止计时器


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = App()
    ui.show()
    # MainWindow = QtWidgets.QMainWindow()
    # ui = App()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    sys.exit(app.exec_())

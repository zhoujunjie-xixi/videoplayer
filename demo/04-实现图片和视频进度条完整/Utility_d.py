# -*- coding: utf-8 -*-

import cv2
import time
from PyQt5 import QtCore, QtWidgets, QtGui

class Utility():
    def __init__(self, video_label):
        self.video_label = video_label

        self.framehandle_choice = False

    def Print(self):
        print("你成功的调用了我！")

    def Frame_Handle(self, cvframe):
        #print(self.framehandle_choice)
        if self.framehandle_choice is True:
            return cv2.flip(cvframe, -1)
        else:
            return cvframe

    # 将 opencv 格式的图片转换成 PyQt 可以呈现的图片格式并展现在 video_label 上
    def show_img(self, cvframe):
        self.cvframe = self.Frame_Handle(cvframe)

        frame = cv2.cvtColor(self.cvframe, cv2.COLOR_BGR2RGB)
        height, width, bytesPerComponent = frame.shape
        bytesPerLine = bytesPerComponent * width
        q_image = QtGui.QImage(frame.data, width, height, bytesPerLine,
                               QtGui.QImage.Format_RGB888).scaled(self.video_label.width(), self.video_label.height())
        self.video_label.setPixmap(QtGui.QPixmap.fromImage(q_image))

    def getframe(self):
        return self.cvframe
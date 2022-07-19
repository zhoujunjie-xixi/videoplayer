# -*- coding: utf-8 -*-

import cv2
import time
from PyQt5 import QtCore, QtWidgets, QtGui
from Utility_d import Utility

class VideoPlayer(QtCore.QThread):
    def __init__(self, slider, video_label, label_pos, label_total, utility):
        super().__init__()

        self.slider = slider
        self.video_label = video_label
        self.label_pos = label_pos
        self.label_total = label_total
        self.framehandle_choice = False
        #print(self.video_label)
        self.pos = -1
        self.Stop_Play = False  # 停止播放信号
        self.Is_Pause = False  # 暂停信号
        self.cvframe = None  # 用于保存图片

        self.utility = utility
        #self.utility = Utility(self.video_label)
        self.utility.Print()

    def Frame_Handle(self, cvframe):
        # print(self.framehandle_choice)
        if self.framehandle_choice is True:
            return cv2.flip(cvframe, -1)
        else:
            return cvframe


    # # 将 opencv 格式的图片转换成 PyQt 可以呈现的图片格式并展现在 video_label 上
    # def show_img(self, cvframe):
    #     #self.cvframe = self.Frame_Handle(cvframe)
    #     self.cvframe = self.utility.Frame_Handle(cvframe)
    #     #self.cvframe = cvframe
    #     frame = cv2.cvtColor(self.cvframe, cv2.COLOR_BGR2RGB)
    #     height, width, bytesPerComponent = frame.shape
    #     bytesPerLine = bytesPerComponent * width
    #     q_image = QtGui.QImage(frame.data, width, height, bytesPerLine,
    #                            QtGui.QImage.Format_RGB888).scaled(self.video_label.width(), self.video_label.height())
    #     self.video_label.setPixmap(QtGui.QPixmap.fromImage(q_image))


    def play(self, path):
        self.Stop_Play = False
        self.cap = cv2.VideoCapture(path)

        self.totalframe = self.cap.get(7) # 获取视频帧数
        self.framepersec = self.cap.get(5) #视频一秒有多少帧

        self.slider.setRange(0, int(self.cap.get(7)))
        self.label_total.setText(str(self.cap.get(7)))

    def run(self):
        while True:
            # 点击进度条响应   变化起始位置
            if self.pos != -1:
                #i = int(self.totalframe*(self.pos)/99)
                self.cap.set(1, self.pos)
                self.pos = -1
            if not self.Is_Pause:
                ret, frame = self.cap.read()
                i = self.cap.get(1)  # 当前读取到第几帧了
                #print(i)
                if self.Stop_Play:
                    break
                if not ret:
                    continue
                #self.show_img(frame)
                self.utility.show_img(frame)

                self.label_pos.setText(str(i))
                #self.slider.setValue(int(99*i/self.totalframe))
                self.slider.setValue(int(i))

                time.sleep(1/self.framepersec)


    def Stop(self):
        self.Stop_Play = True

    def Close(self):
        self.cap.release()

    def PauseOrStart(self):
        if self.Is_Pause:
            self.Is_Pause = False
        else:
            self.Is_Pause = True

    def Set_position(self, po):
        self.pos = po

    def getframe(self):
        return self.cvframe


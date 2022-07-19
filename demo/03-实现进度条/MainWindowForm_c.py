# -*- coding: utf-8 -*-

import os
import sys
import time
import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from videoform_c import Ui_Video_Form
from VideoPlayer_c import VideoPlayer

# cv2.VideoCapture().set/get的参数 https://blog.csdn.net/crazty/article/details/107365147

class MainWindowForm(QtWidgets.QMainWindow,  Ui_Video_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.player = None

        self.Signal_Slot()


    def Signal_Slot(self):
        self.open_btn.clicked.connect(self.Open_Video_Slot)
        self.start_btn.clicked.connect(self.Start_Btn_Slot)
        self.pushButton.clicked.connect(self.Prev_Frame_Slot)  # 前一帧
        self.pushButton_2.clicked.connect(self.Next_Frame_Slot)  # 后一帧
        self.save_btn.clicked.connect(self.Save_Slot)
        self.frame_handle_btn.clicked.connect(self.Frame_Handle_Slot)
        self.actionPicture.triggered.connect(self.Open_Picture_Slot)

        self.slider.sliderMoved.connect(self.SliderMove_Slot)  # 进度条

    def Open_Picture_Slot(self):
        print('open_picture')
        # self.player = None  # 单纯令 self.player=None是没法停止已经播放的视频的，视频仍会运行
        # print(self.player)
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Input File',
                                                         './',
                                                         "Picture(*.jpg *.png);;All Files(*))")
        #    4个参数分别是父控件、标题、起始路径、文件扩展名过滤。返回值是共两个元素的元组。元组第一个元素是文件名列表，第二个是文件类型名。
        file = QtCore.QFile(filename[0])
        if not file.open(QtCore.QIODevice.ReadOnly):
            return
        else:
            frame = cv2.imdecode(np.fromfile(filename[0], dtype=np.uint8), -1)
            #frame = cv2.imread(filename[0])
            cv2.imshow('img', frame)

    def Open_Video_Slot(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Input File',
                        './', "Video Files(*.avi *.mp4 *.flv *.mkv *.wmv)")#All Files (*);;
        #    4个参数分别是父控件、标题、起始路径、文件扩展名过滤。返回值是共两个元素的元组。元组第一个元素是文件名列表，第二个是文件类型名。
        file = QtCore.QFile(filename[0])
        if not file.open(QtCore.QIODevice.ReadOnly):
            return
        else:
            if self.player is None:
                self.player = VideoPlayer(self.slider, self.video_label, self.label_pos, self.label_total)
                self.player.play(filename[0])
                self.player.start()
            else:
                self.player.Stop()
                self.player.slider.setValue(0)
                self.player.Set_position(0)
                self.player.play(filename[0])

    def Start_Btn_Slot(self):
        self.player.PauseOrStart()

    def SliderMove_Slot(self):
        if self.player is not None:
            #  拖动进度条响应PaseOrStart在这里非常重要, 实现了拖动时的动态变化
            self.player.PauseOrStart()
            #self.player.Is_Pause = True
            self.player.Set_position(self.slider.value())

    def Prev_Frame_Slot(self):
        if self.player is not None:
            if self.slider.value() > 0:
                self.display_i_frame(self.slider.value() - 1)

    def Next_Frame_Slot(self):
        if self.player is not None:
            if self.slider.value() < self.player.totalframe:
                self.display_i_frame(self.slider.value() + 1)

    # 用于显示 VideoCapture 位于 pos 处的图像（显示前后帧图像的时候使用）
    def display_i_frame(self, pos):
        self.player.cap.set(1, pos - 1)
        ret, frame = self.player.cap.read()
        i = self.player.cap.get(1)
        self.player.show_img(frame)
        self.label_pos.setText(str(i))
        self.slider.setValue(int(i))

    def Frame_Handle_Slot(self):
        if self.player is None or self.player.cvframe is None:
            QtWidgets.QMessageBox.warning(self, "警告对话框", "当前没有可处理的图像", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
        else:
            self.player.framehandle_choice = True
            self.player.show_img(self.player.cvframe)
            self.player.framehandle_choice = False

    def Save_Slot(self):
        if self.player is None or self.player.cvframe is None:
            QtWidgets.QMessageBox.warning(self, "警告对话框", "当前没有可保存的图像", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
        else:
            self.save_frame(self.player.cvframe)

    def save_frame(self, cvframe):
        path = r'./results'

        if not os.path.exists(path):
            os.mkdir(path)
            fileprefix = '0'
        else:
            lastfile = os.listdir(path)[-1]
            fileprefix = str(int(lastfile.split('.')[0])+1)
        print(fileprefix)

        save_path = path + './' + fileprefix + '.jpg'
        cv2.imencode('.jpg', cvframe)[1].tofile(save_path)



#
# class VideoPlayer(QtCore.QThread):
#     def __init__(self, slider, video_label, label_pos, label_total):
#         super().__init__()
#
#         self.slider = slider
#         self.video_label = video_label
#         self.label_pos = label_pos
#         self.label_total = label_total
#         #print(self.video_label)
#         self.pos = -1
#         self.Stop_Play = False  # 停止播放信号
#         self.Is_Pause = False  # 暂停信号
#         self.cvframe = None  # 用于保存图片
#
#     # 将 opencv 格式的图片转换成 PyQt 可以呈现的图片格式并展现在 video_label 上
#     def show_img(self, cvframe):
#         self.cvframe = cvframe
#         frame = cv2.cvtColor(cvframe, cv2.COLOR_BGR2RGB)
#         height, width, bytesPerComponent = frame.shape
#         bytesPerLine = bytesPerComponent * width
#         q_image = QtGui.QImage(frame.data, width, height, bytesPerLine,
#                                QtGui.QImage.Format_RGB888).scaled(self.video_label.width(), self.video_label.height())
#         self.video_label.setPixmap(QtGui.QPixmap.fromImage(q_image))
#
#
#     def play(self, path):
#         self.Stop_Play = False
#         self.cap = cv2.VideoCapture(path)
#
#         self.totalframe = self.cap.get(7) # 获取视频帧数
#         self.framepersec = self.cap.get(5) #视频一秒有多少帧
#
#         self.slider.setRange(0, int(self.cap.get(7)))
#         self.label_total.setText(str(self.cap.get(7)))
#
#     def run(self):
#         while True:
#             # 点击进度条响应   变化起始位置
#             if self.pos != -1:
#                 #i = int(self.totalframe*(self.pos)/99)
#                 self.cap.set(1, self.pos)
#                 self.pos = -1
#             if not self.Is_Pause:
#                 ret, frame = self.cap.read()
#                 i = self.cap.get(1)  # 当前读取到第几帧了
#
#                 #print(i)
#                 if self.Stop_Play:
#                     break
#                 if not ret:
#                     continue
#                 self.show_img(frame)
#
#                 self.label_pos.setText(str(i))
#                 #self.slider.setValue(int(99*i/self.totalframe))
#                 self.slider.setValue(int(i))
#
#                 time.sleep(1/self.framepersec)
#
#
#     def Stop(self):
#         self.Stop_Play = True
#
#     def PauseOrStart(self):
#         if self.Is_Pause:
#             self.Is_Pause = False
#         else:
#             self.Is_Pause = True
#
#     def Set_position(self, po):
#         self.pos = po
#





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWindowForm()
    ui.show()
    sys.exit(app.exec_())

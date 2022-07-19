# -*- coding: utf-8 -*-

import os
import sys
import time
import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from videoform_d import Ui_Video_Form
from VideoPlayer_d import VideoPlayer
from PicturePlayer_d import PicturePlayer
from Utility_d import Utility
# cv2.VideoCapture().set/get的参数 https://blog.csdn.net/crazty/article/details/107365147

class MainWindowForm(QtWidgets.QMainWindow,  Ui_Video_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.cvframe = None
        self.player = None
        self.is_video = False  # is_video=0当前非视频, is_video=1为播放视频
        self.utility = Utility(self.video_label)

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
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Input File',
                                                         './',
                                                         "Picture(*.jpg *.png);;All Files(*))")
        # 4个参数分别是父控件、标题、起始路径、文件扩展名过滤。返回值是共两个元素的元组。元组第一个元素是文件名列表，第二个是文件类型名。
        file = QtCore.QFile(filename[0])
        if not file.open(QtCore.QIODevice.ReadOnly):
            return
        else:
            if self.is_video is True:
                self.player.Close()
            self.player = PicturePlayer(self.slider, self.video_label, self.label_pos, self.label_total, self.utility)
            self.player.play(filename[0])

        self.is_video = False

    def Open_Video_Slot(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Input File',
                        './', "Video Files(*.avi *.mp4 *.flv *.mkv *.wmv)")#All Files (*);;
        # 4个参数分别是父控件、标题、起始路径、文件扩展名过滤。返回值是共两个元素的元组。元组第一个元素是文件名列表，第二个是文件类型名。
        file = QtCore.QFile(filename[0])
        if not file.open(QtCore.QIODevice.ReadOnly):
            return
        else:
            if self.is_video is False:
                self.player = VideoPlayer(self.slider, self.video_label, self.label_pos, self.label_total, self.utility)
                self.player.play(filename[0])
                self.player.start()
            else:
                self.player.Stop()
                self.player.slider.setValue(0)
                self.player.Set_position(0)
                self.player.play(filename[0])
                self.display_i_frame(1)
        self.is_video = True

    def Start_Btn_Slot(self):
        print(self.is_video)
        if not self.is_video:
            QtWidgets.QMessageBox.warning(self, "警告对话框", "当前未加载视频",
                                          QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                          QtWidgets.QMessageBox.Yes)
        else:
            self.player.PauseOrStart()

    def SliderMove_Slot(self):
        if self.is_video is True:
            #  拖动进度条响应PaseOrStart在这里非常重要, 实现了拖动时的动态变化
            self.player.PauseOrStart()
            #self.player.Is_Pause = True
            self.player.Set_position(self.slider.value())

    def Prev_Frame_Slot(self):
        if not self.is_video:
            return
        else:
            if self.slider.value() > 0:
                self.player.Is_Pause = True
                self.display_i_frame(self.slider.value() - 1)

    def Next_Frame_Slot(self):
        if not self.is_video:
            return

        else:
            if self.slider.value() < self.player.totalframe:
                self.player.Is_Pause = True
                self.display_i_frame(self.slider.value() + 1)

    # 用于显示 VideoCapture 位于 pos 处的图像（显示前后帧图像的时候使用）
    def display_i_frame(self, pos):
        self.player.cap.set(1, pos - 1)
        ret, frame = self.player.cap.read()
        i = self.player.cap.get(1)
        self.utility.show_img(frame)
        #self.player.show_img(frame)
        self.label_pos.setText(str(i))
        self.slider.setValue(int(i))

    def Frame_Handle_Slot(self):
        if self.utility.cvframe is None:
            QtWidgets.QMessageBox.warning(self, "警告对话框", "当前没有可处理的图像", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
        else:
            self.cvframe = self.utility.getframe()
            self.utility.framehandle_choice = True
            self.utility.show_img(self.cvframe)
            self.utility.framehandle_choice = False

    def Save_Slot(self):
        if self.utility.cvframe is None:
            QtWidgets.QMessageBox.warning(self, "警告对话框", "当前没有可保存的图像", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
        else:
            self.save_frame(self.utility.cvframe)

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



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWindowForm()
    ui.show()
    sys.exit(app.exec_())

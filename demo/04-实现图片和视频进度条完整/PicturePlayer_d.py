# -*- coding: utf-8 -*-

import cv2
import time
import numpy as np
from PyQt5 import QtCore, QtWidgets, QtGui
from Utility_d import Utility

class PicturePlayer():
    def __init__(self, slider, video_label, label_pos, label_total, utility):
        super().__init__()

        self.slider = slider
        self.video_label = video_label
        self.label_pos = label_pos
        self.label_total = label_total
        self.framehandle_choice = False
        #print(self.video_label)

        self.cvframe = None  # 用于保存图片

        self.utility = utility
        self.utility.Print()

    def play(self, path):
        frame = cv2.imdecode(np.fromfile(path, dtype=np.uint8), -1)
        # frame = cv2.imread(filename[0])
        # cv2.imshow('img', frame)
        #self.show_img(frame)
        self.utility.show_img(frame)

        self.slider.setRange(0, 0)
        self.label_pos.setText('0')
        self.label_total.setText('0')

    def getframe(self):
        return self.cvframe


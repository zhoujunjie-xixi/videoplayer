import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
import MainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore, QtGui
import cv2


class MainCode(QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        MainWindow.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_video)
        self.open_flag = False
        self.video_stream = cv2.VideoCapture('E:\\video\\fire_1.mp4')
        self.painter = QPainter(self)

    def on_video(self):
        if self.open_flag:
            self.pushButton.setText('open')
        else:
            self.pushButton.setText('close')
        self.open_flag = bool(1 - self.open_flag)  #

    def paintEvent(self, a0: QtGui.QPaintEvent):
        if self.open_flag:
            ret, frame = self.video_stream.read()
            frame = cv2.resize(frame, (640, 480), interpolation=cv2.INTER_AREA)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # cv2.imshow('test',frame)
            # cv2.waitKey(10)
            self.Qframe = QImage(frame.data, frame.shape[1], frame.shape[0], frame.shape[1] * 3, QImage.Format_RGB888)
            # print(Qframe)
            # pix = QPixmap(Qframe).scaled(frame.shape[1], frame.shape[0])
            # self.setPixmap(pix)
            # QRect qq(20,50,self.img.width,self.img.height)
            self.img_label.setPixmap(QPixmap.fromImage(self.Qframe))
            # self.painter.drawImage(QPoint(20,50),Qframe)
            # print(Qframe)
            self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    md = MainCode()
    md.show()
    sys.exit(app.exec_())
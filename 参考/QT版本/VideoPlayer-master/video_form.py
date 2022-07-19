# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'video_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

class Ui_Video_Form(object):
    def setupUi(self, Video_Form):
        Video_Form.setObjectName("Video_Form")
        Video_Form.resize(837, 555)
        self.centralWidget = QtWidgets.QWidget(Video_Form)
        self.centralWidget.setEnabled(True)
        self.centralWidget.setObjectName("centralWidget")
        self.video_label = QtWidgets.QLabel(self.centralWidget)
        self.video_label.setGeometry(QtCore.QRect(61, 21, 731, 331))
        self.video_label.setStyleSheet("background:rgb(225, 225, 225);\n"
"font-size: 30px;\n"
"")
        self.video_label.setObjectName("video_label")
        self.slider = QtWidgets.QSlider(self.centralWidget)
        self.slider.setGeometry(QtCore.QRect(60, 380, 731, 16))
        self.slider.setStyleSheet("")
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.layoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 420, 741, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.open_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.open_btn.setObjectName("open_btn")
        self.horizontalLayout.addWidget(self.open_btn)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.start_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.start_btn.setObjectName("start_btn")
        self.horizontalLayout.addWidget(self.start_btn)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.label_mag = QtWidgets.QLabel(self.layoutWidget)
        self.label_mag.setObjectName("label_mag")
        self.horizontalLayout.addWidget(self.label_mag)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.choose_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.choose_btn.setObjectName("choose_btn")
        self.horizontalLayout.addWidget(self.choose_btn)
        self.frame_handle_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.frame_handle_btn.setObjectName("frame_handle_btn")
        self.horizontalLayout.addWidget(self.frame_handle_btn)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralWidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(660, 360, 131, 20))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_pos = QtWidgets.QLabel(self.layoutWidget1)
        self.label_pos.setObjectName("label_pos")
        self.horizontalLayout_2.addWidget(self.label_pos)
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_total = QtWidgets.QLabel(self.layoutWidget1)
        self.label_total.setObjectName("label_total")
        self.horizontalLayout_2.addWidget(self.label_total)
        Video_Form.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(Video_Form)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 837, 25))
        self.menuBar.setObjectName("menuBar")
        Video_Form.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(Video_Form)
        self.mainToolBar.setObjectName("mainToolBar")
        Video_Form.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(Video_Form)
        self.statusBar.setObjectName("statusBar")
        Video_Form.setStatusBar(self.statusBar)

        self.retranslateUi(Video_Form)
        QtCore.QMetaObject.connectSlotsByName(Video_Form)

    def retranslateUi(self, Video_Form):
        _translate = QtCore.QCoreApplication.translate
        Video_Form.setWindowTitle(_translate("Video_Form", "Video_Form"))
        self.video_label.setText(_translate("Video_Form", "NO VIDEO"))
        self.open_btn.setText(_translate("Video_Form", "打开视频"))
        self.pushButton.setText(_translate("Video_Form", "<<慢放"))
        self.start_btn.setText(_translate("Video_Form", "播放/暂停"))
        self.pushButton_2.setText(_translate("Video_Form", "快进>>"))
        self.label_mag.setText(_translate("Video_Form", " 0"))
        self.choose_btn.setText(_translate("Video_Form", "选择此处"))
        self.frame_handle_btn.setText(_translate("Video_Form", "帧处理"))
        self.label_2.setText(_translate("Video_Form", "帧:"))
        self.label_pos.setText(_translate("Video_Form", "0"))
        self.label.setText(_translate("Video_Form", "/"))
        self.label_total.setText(_translate("Video_Form", "0"))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Video_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
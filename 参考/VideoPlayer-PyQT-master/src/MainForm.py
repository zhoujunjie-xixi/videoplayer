# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from threading import Timer,Thread,Event
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog,QVBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(959, 834)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setEnabled(True)
        self.groupBox_5.setTitle("")
        self.groupBox_5.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_5.setCheckable(False)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 55))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 55))
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.timeComboBox = QtWidgets.QComboBox(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeComboBox.sizePolicy().hasHeightForWidth())
        self.timeComboBox.setSizePolicy(sizePolicy)
        self.timeComboBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.timeComboBox.setObjectName("timeComboBox")
        self.timeComboBox.addItem("")
        self.timeComboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.timeComboBox)
        self.fileButton = QtWidgets.QPushButton(self.frame_3)
        self.fileButton.setFocusPolicy(QtCore.Qt.NoFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("datafile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fileButton.setIcon(icon1)
        self.fileButton.setObjectName("fileButton")
        self.horizontalLayout_4.addWidget(self.fileButton)
        self.openButton = QtWidgets.QPushButton(self.frame_3)
        self.openButton.setEnabled(False)
        self.openButton.setFocusPolicy(QtCore.Qt.NoFocus)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons8-unsplash-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openButton.setIcon(icon2)
        self.openButton.setObjectName("openButton")
        self.horizontalLayout_4.addWidget(self.openButton)
        self.startButton = QtWidgets.QPushButton(self.frame_3)
        self.startButton.setEnabled(False)
        self.startButton.setFocusPolicy(QtCore.Qt.NoFocus)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons8-start-40.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startButton.setIcon(icon3)
        self.startButton.setObjectName("startButton")
        self.horizontalLayout_4.addWidget(self.startButton)
        self.pauseButton = QtWidgets.QPushButton(self.frame_3)
        self.pauseButton.setEnabled(True)
        self.pauseButton.setFocusPolicy(QtCore.Qt.NoFocus)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons8-pause-button-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pauseButton.setIcon(icon4)
        self.pauseButton.setObjectName("pauseButton")
        self.horizontalLayout_4.addWidget(self.pauseButton)
        self.verticalLayout.addWidget(self.frame_3)
        self.line = QtWidgets.QFrame(self.groupBox_5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.LeftImage = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LeftImage.sizePolicy().hasHeightForWidth())
        self.LeftImage.setSizePolicy(sizePolicy)
        self.LeftImage.setText("")
        self.LeftImage.setAlignment(QtCore.Qt.AlignCenter)
        self.LeftImage.setObjectName("LeftImage")
        self.verticalLayout.addWidget(self.LeftImage)
        self.line_2 = QtWidgets.QFrame(self.groupBox_5)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.bottomImage = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottomImage.sizePolicy().hasHeightForWidth())
        self.bottomImage.setSizePolicy(sizePolicy)
        self.bottomImage.setMinimumSize(QtCore.QSize(0, 200))
        self.bottomImage.setMaximumSize(QtCore.QSize(16777215, 300))
        self.bottomImage.setText("")
        self.bottomImage.setObjectName("bottomImage")
        self.verticalLayout.addWidget(self.bottomImage)
        self.frame = QtWidgets.QFrame(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalSlider = QtWidgets.QSlider(self.frame)
        self.horizontalSlider.setEnabled(False)
        self.horizontalSlider.setBaseSize(QtCore.QSize(10, 10))
        self.horizontalSlider.setMouseTracking(True)
        self.horizontalSlider.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.horizontalSlider.setStatusTip("")
        self.horizontalSlider.setTracking(True)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_2.addWidget(self.horizontalSlider)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout.addWidget(self.groupBox_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Video Player with Signal"))
        self.timeComboBox.setItemText(0, _translate("MainWindow", "Real-Time"))
        self.timeComboBox.setItemText(1, _translate("MainWindow", "Frame by Frame"))
        self.fileButton.setText(_translate("MainWindow", "Open Data File"))
        self.openButton.setText(_translate("MainWindow", "Open Video"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.pauseButton.setText(_translate("MainWindow", "Pause"))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
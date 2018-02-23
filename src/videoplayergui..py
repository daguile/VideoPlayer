# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'videoplayergui.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(578, 301)
        self.pushButtonPrevTrack = QtWidgets.QPushButton(Dialog)
        self.pushButtonPrevTrack.setGeometry(QtCore.QRect(10, 250, 75, 23))
        self.pushButtonPrevTrack.setObjectName("pushButtonPrevTrack")
        self.pushButtonSeekPrev = QtWidgets.QPushButton(Dialog)
        self.pushButtonSeekPrev.setGeometry(QtCore.QRect(90, 250, 75, 23))
        self.pushButtonSeekPrev.setObjectName("pushButtonSeekPrev")
        self.pushButtonPlay = QtWidgets.QPushButton(Dialog)
        self.pushButtonPlay.setGeometry(QtCore.QRect(170, 250, 75, 23))
        self.pushButtonPlay.setObjectName("pushButtonPlay")
        self.pushButtonPause = QtWidgets.QPushButton(Dialog)
        self.pushButtonPause.setGeometry(QtCore.QRect(250, 250, 75, 23))
        self.pushButtonPause.setObjectName("pushButtonPause")
        self.pushButtonStop = QtWidgets.QPushButton(Dialog)
        self.pushButtonStop.setGeometry(QtCore.QRect(330, 250, 75, 23))
        self.pushButtonStop.setObjectName("pushButtonStop")
        self.pushButtonSeekNext = QtWidgets.QPushButton(Dialog)
        self.pushButtonSeekNext.setGeometry(QtCore.QRect(410, 250, 75, 23))
        self.pushButtonSeekNext.setObjectName("pushButtonSeekNext")
        self.pushButtonNextTrack = QtWidgets.QPushButton(Dialog)
        self.pushButtonNextTrack.setGeometry(QtCore.QRect(490, 250, 75, 23))
        self.pushButtonNextTrack.setObjectName("pushButtonNextTrack")
        self.verticalSliderVolume = QtWidgets.QSlider(Dialog)
        self.verticalSliderVolume.setGeometry(QtCore.QRect(540, 40, 21, 201))
        self.verticalSliderVolume.setOrientation(QtCore.Qt.Vertical)
        self.verticalSliderVolume.setObjectName("verticalSliderVolume")
        self.pushButtonAddFile = QtWidgets.QPushButton(Dialog)
        self.pushButtonAddFile.setGeometry(QtCore.QRect(10, 210, 75, 23))
        self.pushButtonAddFile.setObjectName("pushButtonAddFile")
        self.listWidgetPlayList = QtWidgets.QListWidget(Dialog)
        self.listWidgetPlayList.setGeometry(QtCore.QRect(10, 31, 256, 171))
        self.listWidgetPlayList.setObjectName("listWidgetPlayList")
        self.pushButtonRemoveFile = QtWidgets.QPushButton(Dialog)
        self.pushButtonRemoveFile.setGeometry(QtCore.QRect(90, 210, 75, 23))
        self.pushButtonRemoveFile.setObjectName("pushButtonRemoveFile")
        self.pushButtonMoveUp = QtWidgets.QPushButton(Dialog)
        self.pushButtonMoveUp.setGeometry(QtCore.QRect(270, 50, 75, 23))
        self.pushButtonMoveUp.setObjectName("pushButtonMoveUp")
        self.pushButtonMoveDown = QtWidgets.QPushButton(Dialog)
        self.pushButtonMoveDown.setGeometry(QtCore.QRect(270, 160, 75, 23))
        self.pushButtonMoveDown.setObjectName("pushButtonMoveDown")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 0, 81, 31))
        self.label.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.checkBoxSecondScreen = QtWidgets.QCheckBox(Dialog)
        self.checkBoxSecondScreen.setGeometry(QtCore.QRect(180, 210, 111, 21))
        self.checkBoxSecondScreen.setObjectName("checkBoxSecondScreen")
        self.horizontalSliderVideoSize = QtWidgets.QSlider(Dialog)
        self.horizontalSliderVideoSize.setGeometry(QtCore.QRect(330, 210, 160, 16))
        self.horizontalSliderVideoSize.setMinimum(1)
        self.horizontalSliderVideoSize.setMaximum(2048)
        self.horizontalSliderVideoSize.setSingleStep(1)
        self.horizontalSliderVideoSize.setPageStep(1)
        self.horizontalSliderVideoSize.setProperty("value", 1024)
        self.horizontalSliderVideoSize.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderVideoSize.setObjectName("horizontalSliderVideoSize")
        self.labelVideoSize = QtWidgets.QLabel(Dialog)
        self.labelVideoSize.setGeometry(QtCore.QRect(340, 220, 46, 31))
        self.labelVideoSize.setObjectName("labelVideoSize")
        self.checkBoxLockVideoSize = QtWidgets.QCheckBox(Dialog)
        self.checkBoxLockVideoSize.setGeometry(QtCore.QRect(400, 190, 101, 21))
        self.checkBoxLockVideoSize.setObjectName("checkBoxLockVideoSize")
        self.labelVideoSize_width = QtWidgets.QLabel(Dialog)
        self.labelVideoSize_width.setGeometry(QtCore.QRect(410, 220, 61, 31))
        self.labelVideoSize_width.setObjectName("labelVideoSize_width")
        self.checkBoxScreenVisible = QtWidgets.QCheckBox(Dialog)
        self.checkBoxScreenVisible.setGeometry(QtCore.QRect(180, 230, 101, 18))
        self.checkBoxScreenVisible.setObjectName("checkBoxScreenVisible")
        self.checkBoxPlaySingleTrack = QtWidgets.QCheckBox(Dialog)
        self.checkBoxPlaySingleTrack.setGeometry(QtCore.QRect(270, 80, 101, 19))
        self.checkBoxPlaySingleTrack.setObjectName("checkBoxPlaySingleTrack")
        self.labelNowPlaying = QtWidgets.QLabel(Dialog)
        self.labelNowPlaying.setGeometry(QtCore.QRect(90, 0, 461, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.labelNowPlaying.setFont(font)
        self.labelNowPlaying.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNowPlaying.setObjectName("labelNowPlaying")
        self.lcdNumberTrackTime = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumberTrackTime.setGeometry(QtCore.QRect(280, 100, 64, 23))
        self.lcdNumberTrackTime.setObjectName("lcdNumberTrackTime")
        self.lcdNumberRemainingTime = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumberRemainingTime.setGeometry(QtCore.QRect(280, 130, 64, 23))
        self.lcdNumberRemainingTime.setObjectName("lcdNumberRemainingTime")
        self.horizontalSliderTrackPos = QtWidgets.QSlider(Dialog)
        self.horizontalSliderTrackPos.setGeometry(QtCore.QRect(10, 280, 551, 16))
        self.horizontalSliderTrackPos.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderTrackPos.setObjectName("horizontalSliderTrackPos")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Jogi\'s DualScreen VideoPlayer v0.01 "))
        self.pushButtonPrevTrack.setText(_translate("Dialog", "< prev. track"))
        self.pushButtonSeekPrev.setText(_translate("Dialog", "<< seek"))
        self.pushButtonPlay.setText(_translate("Dialog", "play >"))
        self.pushButtonPause.setText(_translate("Dialog", "pause ||"))
        self.pushButtonStop.setText(_translate("Dialog", "stop"))
        self.pushButtonSeekNext.setText(_translate("Dialog", "seek >>"))
        self.pushButtonNextTrack.setText(_translate("Dialog", "next track >>"))
        self.pushButtonAddFile.setText(_translate("Dialog", "add file"))
        self.pushButtonRemoveFile.setText(_translate("Dialog", "remove file"))
        self.pushButtonMoveUp.setText(_translate("Dialog", "move up"))
        self.pushButtonMoveDown.setText(_translate("Dialog", "move down"))
        self.label.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#aa0000;\">Playlist</span></p></body></html>"))
        self.checkBoxSecondScreen.setText(_translate("Dialog", "Second Screen"))
        self.labelVideoSize.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><span style=\" color:#000000;\">video size</span></p></body></html>"))
        self.checkBoxLockVideoSize.setText(_translate("Dialog", "lock video size"))
        self.labelVideoSize_width.setText(_translate("Dialog", "1024"))
        self.checkBoxScreenVisible.setText(_translate("Dialog", "Screen Visible"))
        self.checkBoxPlaySingleTrack.setText(_translate("Dialog", "play single track"))
        self.labelNowPlaying.setText(_translate("Dialog", "no track playing"))


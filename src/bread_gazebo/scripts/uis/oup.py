# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'STARTCONFIRMATION.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 1024)
        MainWindow.setMinimumSize(QtCore.QSize(800, 1024))
        MainWindow.setMaximumSize(QtCore.QSize(800, 1024))
        MainWindow.setTabletTracking(True)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(241, 244, 253);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 811, 1031))
        self.frame.setStyleSheet("background-color: rgb(137, 209, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(140, 230, 561, 201))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("\n"
"color: rgb(243, 243, 243);\n"
"")
        self.label_9.setTextFormat(QtCore.Qt.RichText)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(60, 430, 341, 121))
        self.frame_4.setStyleSheet("background-color: rgb(180, 228, 255);\n"
"\n"
"border-top-left-radius :35px;\n"
"border-top-right-radius :35px;\n"
"border-bottom-left-radius :35px;\n"
"border-bottom-right-radius :35px;\n"
"background-color: rgb(137, 209, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 291, 51))
        font = QtGui.QFont()
        font.setFamily("System-ui")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("\n"
"color: rgb(243, 243, 243);\n"
"")
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setGeometry(QtCore.QRect(420, 430, 341, 121))
        self.frame_5.setStyleSheet("background-color: rgb(137, 209, 255);\n"
"\n"
"border-top-left-radius :35px;\n"
"border-top-right-radius :35px;\n"
"border-bottom-left-radius :35px;\n"
"border-bottom-right-radius :35px;\n"
"\n"
"")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 291, 51))
        font = QtGui.QFont()
        font.setFamily("System-ui")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("\n"
"color: rgb(243, 243, 243);\n"
"")
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_9.setText(_translate("MainWindow", "START THE MACHINE (ENSURE BREAD IS LOADED IN CORRECTLY)"))
        self.label_2.setText(_translate("MainWindow", "START"))
        self.label_3.setText(_translate("MainWindow", "CANCEL"))
import Test_rc

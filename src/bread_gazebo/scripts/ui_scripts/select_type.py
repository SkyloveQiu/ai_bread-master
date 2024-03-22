from PyQt5 import QtCore, QtGui, QtWidgets


class SelectType(object):
    def __init__(self, callback = None):
        if not callback:
            callback = []
        self.callback_arr = callback
        
        super().__init__()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 900)
        MainWindow.setMinimumSize(QtCore.QSize(600, 900))
        MainWindow.setMaximumSize(QtCore.QSize(600, 900))
        MainWindow.setTabletTracking(True)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(241, 244, 253);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 801, 961))
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 799, 959))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setGeometry(QtCore.QRect(10, 170, 581, 141))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet("background-color: rgb(137, 209, 255);\n"
"border-top-left-radius :35px;\n"
"border-top-right-radius :35px;\n"
"border-bottom-left-radius :35px;\n"
"border-bottom-right-radius :35px;\n"
"\n"
"\n"
"box-shadow: 0px -2px 2px rgba(255,255,255,0.6);\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.bread_image_3 = QtWidgets.QGraphicsView(self.frame_2)
        self.bread_image_3.setGeometry(QtCore.QRect(40, 20, 111, 101))
        self.bread_image_3.setObjectName("bread_image_3")
        self.bread_type_3 = QtWidgets.QLabel(self.frame_2)
        self.bread_type_3.setGeometry(QtCore.QRect(40, 20, 481, 101))
        font = QtGui.QFont()
        font.setFamily("System-ui")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.bread_type_3.setFont(font)
        self.bread_type_3.setStyleSheet("color: rgb(243, 243, 243);\n"
"")
        self.bread_type_3.setTextFormat(QtCore.Qt.RichText)
        self.bread_type_3.setScaledContents(False)
        self.bread_type_3.setObjectName("bread_type_3")
        self.frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 611, 141))
        self.frame_3.setStyleSheet("background-color: rgb(137, 209, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setGeometry(QtCore.QRect(10, 70, 581, 51))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("\n"
"color: rgb(243, 243, 243);\n"
"")
        self.label_9.setTextFormat(QtCore.Qt.RichText)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(10, 20, 41, 41))
        self.label_10.setText("")
        self.label_10.setTextFormat(QtCore.Qt.RichText)
        self.label_10.setPixmap(QtGui.QPixmap(":/newPrefix/power.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.frame_6 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_6.setGeometry(QtCore.QRect(20, 710, 151, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setStyleSheet("background-color: rgb(137, 209, 255);\n"
"border-top-left-radius :35px;\n"
"border-top-right-radius :35px;\n"
"border-bottom-left-radius :35px;\n"
"border-bottom-right-radius :35px;\n"
"\n"
"\n"
"box-shadow: 0px -2px 2px rgba(255,255,255,0.6);\n"
"")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.bread_type_6 = QtWidgets.QLabel(self.frame_6)
        self.bread_type_6.setGeometry(QtCore.QRect(20, 10, 111, 71))
        font = QtGui.QFont()
        font.setFamily("System-ui")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bread_type_6.setFont(font)
        self.bread_type_6.setStyleSheet("color: rgb(243, 243, 243);\n"
"")
        self.bread_type_6.setTextFormat(QtCore.Qt.RichText)
        self.bread_type_6.setScaledContents(False)
        self.bread_type_6.setAlignment(QtCore.Qt.AlignCenter)
        self.bread_type_6.setObjectName("bread_type_6")
        self.frame_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setGeometry(QtCore.QRect(10, 340, 581, 141))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setStyleSheet("background-color: rgb(137, 209, 255);\n"
"border-top-left-radius :35px;\n"
"border-top-right-radius :35px;\n"
"border-bottom-left-radius :35px;\n"
"border-bottom-right-radius :35px;\n"
"\n"
"\n"
"box-shadow: 0px -2px 2px rgba(255,255,255,0.6);\n"
"")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.bread_image_4 = QtWidgets.QGraphicsView(self.frame_4)
        self.bread_image_4.setGeometry(QtCore.QRect(40, 20, 111, 101))
        self.bread_image_4.setObjectName("bread_image_4")
        self.bread_type_4 = QtWidgets.QLabel(self.frame_4)
        self.bread_type_4.setGeometry(QtCore.QRect(40, 20, 481, 101))
        font = QtGui.QFont()
        font.setFamily("System-ui")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.bread_type_4.setFont(font)
        self.bread_type_4.setStyleSheet("color: rgb(243, 243, 243);\n"
"")
        self.bread_type_4.setTextFormat(QtCore.Qt.RichText)
        self.bread_type_4.setScaledContents(False)
        self.bread_type_4.setObjectName("bread_type_4")
        self.frame_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setGeometry(QtCore.QRect(10, 510, 581, 141))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setStyleSheet("background-color: rgb(137, 209, 255);\n"
"border-top-left-radius :35px;\n"
"border-top-right-radius :35px;\n"
"border-bottom-left-radius :35px;\n"
"border-bottom-right-radius :35px;\n"
"\n"
"\n"
"box-shadow: 0px -2px 2px rgba(255,255,255,0.6);\n"
"")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.bread_image_5 = QtWidgets.QGraphicsView(self.frame_5)
        self.bread_image_5.setGeometry(QtCore.QRect(40, 20, 111, 101))
        self.bread_image_5.setObjectName("bread_image_5")
        self.bread_type_5 = QtWidgets.QLabel(self.frame_5)
        self.bread_type_5.setGeometry(QtCore.QRect(40, 20, 481, 101))
        font = QtGui.QFont()
        font.setFamily("System-ui")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.bread_type_5.setFont(font)
        self.bread_type_5.setStyleSheet("color: rgb(243, 243, 243);\n"
"")
        self.bread_type_5.setTextFormat(QtCore.Qt.RichText)
        self.bread_type_5.setScaledContents(False)
        self.bread_type_5.setObjectName("bread_type_5")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)

        self.frame_2.mouseReleaseEvent = self.callback_arr[0]
        self.bread_image_3.mouseReleaseEvent = self.callback_arr[0]
        self.bread_type_3.mouseReleaseEvent = self.callback_arr[0]

        self.frame_4.mouseReleaseEvent = self.callback_arr[1]
        self.bread_image_4.mouseReleaseEvent = self.callback_arr[1]
        self.bread_type_4.mouseReleaseEvent = self.callback_arr[1]

        self.frame_5.mouseReleaseEvent = self.callback_arr[2]
        self.bread_image_5.mouseReleaseEvent = self.callback_arr[2]
        self.bread_type_5.mouseReleaseEvent = self.callback_arr[2]
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bread_type_3.setText(_translate("MainWindow", "TYPE: BOULOGNE"))
        self.label_9.setText(_translate("MainWindow", "SELECT THE BREAD TYPE TO ADD"))
        self.label_10.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.bread_type_6.setText(_translate("MainWindow", "Cancel"))
        self.bread_type_4.setText(_translate("MainWindow", "TYPE: TIJGER WIT"))
        self.bread_type_5.setText(_translate("MainWindow", "TYPE: VOLKOREN MEERGRANEN"))


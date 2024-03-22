from PyQt5 import QtCore, QtGui, QtWidgets
class Bread_Select(object):
    def __init__(self, info = [], confidence = None, callback_arr= None):
        self.info = info
        self.confidence = confidence if confidence else []
        self.callback_arr = callback_arr if callback_arr else [self.callbackOption1, self.callbackOption2, self.callbackOption3, self.callbackOption4 ]
        self.output_text = ["S.L.I.C.E. Robot. Developed by: Nikolay Blagoev"]

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

        for x in range(len(self.info)):

            
            frame = QtWidgets.QFrame(self.centralwidget)
            frame.setGeometry(QtCore.QRect(20, 150+x*190, 561, 141))
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(frame.sizePolicy().hasHeightForWidth())
            frame.setSizePolicy(sizePolicy)
            frame.setStyleSheet("background-color: rgb(137, 209, 255);\n"
"border-top-left-radius :35px;\n"
"border-top-right-radius :35px;\n"
"border-bottom-left-radius :35px;\n"
"border-bottom-right-radius :35px;\n"
"\n"

"")
            frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            frame.setFrameShadow(QtWidgets.QFrame.Raised)
            frame.setObjectName("frame")
            
            bread_image = QtWidgets.QGraphicsView(frame)
            bread_image.setGeometry(QtCore.QRect(30, 10, 131, 121))
            bread_image.setObjectName("bread_image")
            bread_type = QtWidgets.QLabel(frame)
            bread_type.setGeometry(QtCore.QRect(210, 20, 331, 51))
            font = QtGui.QFont()
            font.setFamily("System-ui")
            font.setPointSize(15)
            font.setBold(True)
            font.setWeight(75)
            bread_type.setFont(font)
            bread_type.setStyleSheet("color: rgb(243, 243, 243);\n"
"")
            bread_type.setTextFormat(QtCore.Qt.RichText)
            bread_type.setScaledContents(False)
            bread_type.setObjectName("bread_type")

            bread_confidence = QtWidgets.QLabel(frame)
            bread_confidence.setGeometry(QtCore.QRect(210, 80, 331, 51))
            font = QtGui.QFont()
            font.setFamily("System-ui")
            font.setPointSize(15)
            font.setBold(True)
            font.setWeight(75)
            bread_confidence.setFont(font)

            bread_confidence.setStyleSheet("color: rgb(243, 243, 243);\n"
"")
            bread_confidence.setTextFormat(QtCore.Qt.RichText)
            bread_confidence.setScaledContents(False)
            bread_confidence.setObjectName("bread_confidence")
            _translate = QtCore.QCoreApplication.translate
            bread_type.setText(_translate("MainWindow", "TYPE: "+self.info[x]))
            bread_confidence.setText(_translate("MainWindow", "LIKELIHOOD: "+str(self.confidence[x])+"%"))
            frame.mouseReleaseEvent = self.callback_arr[x]
            bread_image.mouseReleaseEvent = self.callback_arr[x]
            bread_type.mouseReleaseEvent = self.callback_arr[x]
            bread_confidence.mouseReleaseEvent = self.callback_arr[x]

        


        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, -10, 621, 141))
        self.frame_2.setStyleSheet("background-color: rgb(137, 209, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(10, 70, 561, 51))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(25)
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
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(10, 20, 41, 41))
        self.label_10.setText("")
        self.label_10.setTextFormat(QtCore.Qt.RichText)
        self.label_10.setPixmap(QtGui.QPixmap(":/newPrefix/power.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label_9.setText(_translate("MainWindow", "SELECT THE CORRECT BREAD"))
        MainWindow.setWindowTitle(_translate("MainWindow", "Bread choice"))
        
    def callbackOption1(e, x):
        print("HAHA1")
        return
    def callbackOption2(e, x):
        print("HAHA2")
        return
    def callbackOption3(e, x):
        print("HAHA3")
        return
    def callbackOption4(e, x):
        print("HAHA4")
        return
import os
from PyQt5 import QtGui, QtCore, QtWidgets
dirpath = os.path.dirname(os.path.realpath(__file__))
class Queue_Overview(object):
    def __init__(self, return_to_main_menu, info = None):
        if info == None:
            info = []
        self.info = info
        self.return_to_main_menu = return_to_main_menu
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


        for x, bread in enumerate(self.info):
            frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)

            frame.setGeometry(QtCore.QRect(10, 170+x*180, 581, 141))
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
"\n"

"")
            frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            frame.setFrameShadow(QtWidgets.QFrame.Raised)
            frame.setObjectName("frame")
            bread_image = QtWidgets.QGraphicsView(frame)
            bread_image.setGeometry(QtCore.QRect(40, 20, 111, 101))
            bread_image.setObjectName("bread_image")
            bread_type = QtWidgets.QLabel(frame)
            bread_type.setGeometry(QtCore.QRect(190, 20, 371, 101))
            font = QtGui.QFont()
            font.setFamily("System-ui")
            font.setPointSize(14)
            font.setBold(True)
            font.setWeight(75)
            bread_type.setFont(font)
            bread_type.setStyleSheet("color: rgb(243, 243, 243);\n")
            bread_type.setTextFormat(QtCore.Qt.RichText)
            bread_type.setScaledContents(False)
            bread_type.setObjectName("bread_type")
            bread_type.setText( "TYPE: {}".format( bread))




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
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(10, 20, 41, 41))
        self.label_10.setText("")
        self.label_10.setTextFormat(QtCore.Qt.RichText)
        self.label_10.setPixmap(QtGui.QPixmap(dirpath+"/home.png"))
        self.label_10.mouseReleaseEvent = self.return_to_main_menu
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        
        self.label_9.setText(_translate("MainWindow", "QUEUE OVERVIEW"))


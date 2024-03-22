from PyQt5 import QtCore, QtWidgets, QtGui
import os
dirpath = os.path.dirname(os.path.realpath(__file__))

def defaultCallback():
    print("no callback")

class Main_Window(object):
    def __init__(self, start = defaultCallback, add_bread = defaultCallback, switch_to_queue= defaultCallback, switch_to_info = defaultCallback, shutdown = defaultCallback):
        self.start = start
        self.switch_to_info = switch_to_info
        self.add_bread = add_bread
        self.switch_to_queue = switch_to_queue
        self.shutdown = shutdown
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
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 811, 141))
        self.frame.setStyleSheet("background-color: rgb(137, 209, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(80, 70, 471, 51))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(40)
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
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.label_10.setText("")
        self.label_10.setTextFormat(QtCore.Qt.RichText)
        self.label_10.setPixmap(QtGui.QPixmap(dirpath+"/power.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(30, 170, 247, 284))
        self.frame_2.setStyleSheet("background-color: rgb(137, 209, 255);\n"
"\n"
"border-top-left-radius :35px;\n"
"border-top-right-radius :35px;\n"
"border-bottom-left-radius :35px;\n"
"border-bottom-right-radius :35px;\n"
"\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(30, 20, 191, 201))
        self.label_5.setText("")
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setPixmap(QtGui.QPixmap(dirpath+"/play.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(30, 220, 191, 51))
        font = QtGui.QFont()
        font.setFamily("System-ui")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("\n"
"color: rgb(243, 243, 243);\n"
"")
        self.label_6.setTextFormat(QtCore.Qt.RichText)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(320, 170, 247, 284))
        self.frame_3.setStyleSheet("background-color: rgb(137, 209, 255);\n"
"border-top-left-radius :35px;\n"
"border-top-right-radius :35px;\n"
"border-bottom-left-radius :35px;\n"
"border-bottom-right-radius :35px;\n"
"\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(30, 20, 201, 191))
        self.label_7.setText("")
        self.label_7.setTextFormat(QtCore.Qt.RichText)
        self.label_7.setPixmap(QtGui.QPixmap(dirpath+"/add.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(20, 230, 211, 31))
        font = QtGui.QFont()
        font.setFamily("System-ui")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("\n"
"color: rgb(243, 243, 243);\n"
"")
        self.label_8.setTextFormat(QtCore.Qt.RichText)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(30, 490, 247, 284))
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
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setGeometry(QtCore.QRect(40, 30, 171, 181))
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setPixmap(QtGui.QPixmap(dirpath+"/bread.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setGeometry(QtCore.QRect(20, 240, 211, 31))
        font = QtGui.QFont()
        font.setFamily("System-ui")
        font.setPointSize(15)
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
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(320, 490, 247, 284))
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
        self.label_3.setGeometry(QtCore.QRect(30, 220, 171, 51))
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
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setGeometry(QtCore.QRect(40, 10, 181, 191))
        self.label_4.setText("")
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setPixmap(QtGui.QPixmap(dirpath+"/info.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame_5.mouseReleaseEvent = self.switch_to_info
        self.label_3.mouseReleaseEvent = self.switch_to_info
        self.label_4.mouseReleaseEvent = self.switch_to_info


        self.frame_2.mouseReleaseEvent = self.start
        self.label_5.mouseReleaseEvent = self.start
        self.label_6.mouseReleaseEvent = self.start

        self.frame_4.mouseReleaseEvent = self.switch_to_queue
        self.label.mouseReleaseEvent = self.switch_to_queue
        self.label_2.mouseReleaseEvent = self.switch_to_queue

        self.frame_3.mouseReleaseEvent = self.add_bread
        self.label_7.mouseReleaseEvent = self.add_bread
        self.label_8.mouseReleaseEvent = self.add_bread
        self.label_10.mouseReleaseEvent = self.shutdown
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_9.setText(_translate("MainWindow", "BREAD CUTTER"))
        self.label_6.setText(_translate("MainWindow", "START"))
        self.label_8.setText(_translate("MainWindow", "ADD LOAVES"))
        self.label_2.setText(_translate("MainWindow", "QUEUE OVERVIEW"))
        self.label_3.setText(_translate("MainWindow", "INFO"))
       

from PyQt5 import QtCore, QtWidgets

# TODO: CLEAN UP THE CODE... A LOT.

app = QtWidgets.QApplication([])
MainWindow = QtWidgets.QMainWindow()
class Bread_Select(object):
    def setupUi(self, MainWindow):
        self.info = ["Tiger", "White", "Panini", "Whole grain"]
        self.confidence = [60, 21, 10, 4]
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 1000)
        MainWindow.setMinimumSize(QtCore.QSize(800, 1000))
        MainWindow.setMaximumSize(QtCore.QSize(800, 1000))
        MainWindow.setTabletTracking(True)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(241, 244, 253);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Programatically add N frames (at most 4)
        for x in range(4):

            
            frame = QtWidgets.QFrame(self.centralwidget)
            frame.setGeometry(QtCore.QRect(-30, 120+x*200, 881, 161))
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(frame.sizePolicy().hasHeightForWidth())
            frame.setSizePolicy(sizePolicy)
            frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
    "\n"
    "box-shadow: 0px -2px 2px rgba(255,255,255,0.6);\n"
    "")
            frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            frame.setFrameShadow(QtWidgets.QFrame.Raised)
            frame.setObjectName("frame")
            
            bread_image = QtWidgets.QGraphicsView(frame)
            bread_image.setGeometry(QtCore.QRect(60, 10, 151, 141))
            bread_image.setObjectName("bread_image")
            bread_type = QtWidgets.QLabel(frame)
            bread_type.setGeometry(QtCore.QRect(260, 20, 621, 51))
            bread_type.setStyleSheet("font: 75 24pt \"System-ui\";")
            bread_type.setTextFormat(QtCore.Qt.RichText)
            bread_type.setScaledContents(False)
            bread_type.setObjectName("bread_type")
            bread_confidence = QtWidgets.QLabel(frame)
            bread_confidence.setGeometry(QtCore.QRect(260, 90, 621, 51))
            bread_confidence.setStyleSheet("font: 75 24pt \"System-ui\";")
            bread_confidence.setTextFormat(QtCore.Qt.RichText)
            bread_confidence.setScaledContents(False)
            bread_confidence.setObjectName("bread_confidence")
            _translate = QtCore.QCoreApplication.translate
            bread_type.setText(_translate("MainWindow", "TYPE: "+self.info[x]))
            bread_confidence.setText(_translate("MainWindow", "CONFIDENCE: "+str(self.confidence[x])+"%"))
            if x == 0:
                frame.mouseReleaseEvent = self.callbackOption1
                bread_image.mouseReleaseEvent = self.callbackOption1
                bread_type.mouseReleaseEvent = self.callbackOption1
                bread_confidence.mouseReleaseEvent = self.callbackOption1
            elif x == 1:
                frame.mouseReleaseEvent = self.callbackOption2
                bread_image.mouseReleaseEvent = self.callbackOption2
                bread_type.mouseReleaseEvent = self.callbackOption2
                bread_confidence.mouseReleaseEvent = self.callbackOption2
            elif x == 2:
                frame.mouseReleaseEvent = self.callbackOption3
                bread_image.mouseReleaseEvent = self.callbackOption3
                bread_type.mouseReleaseEvent = self.callbackOption3
                bread_confidence.mouseReleaseEvent = self.callbackOption3
            else:
                frame.mouseReleaseEvent = self.callbackOption4
                bread_image.mouseReleaseEvent = self.callbackOption4
                bread_type.mouseReleaseEvent = self.callbackOption4
                bread_confidence.mouseReleaseEvent = self.callbackOption4

            

        
        self.prompt = QtWidgets.QLabel(self.centralwidget)
        self.prompt.setGeometry(QtCore.QRect(190, 20, 491, 71))
        self.prompt.setStyleSheet("font: 75 24pt \"System-ui\";")
        self.prompt.setObjectName("prompt")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.prompt.setText(_translate("MainWindow", "SELECT THE CORRECT BREAD"))
        MainWindow.setWindowTitle(_translate("MainWindow", "Bread choice"))
        
    def callbackOption1(e, x):
        ui = Error()
        ui.setupUi(MainWindow)
        MainWindow.show()
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

class Error(object):
    def setupUi(self, MainWindow):
        self.info = [66, "MACHINE HAS GAINED SENTIENCE"]
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 1000)
        MainWindow.setMinimumSize(QtCore.QSize(800, 1000))
        MainWindow.setMaximumSize(QtCore.QSize(800, 1000))
        MainWindow.setTabletTracking(True)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 56, 56);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.error = QtWidgets.QLabel(self.centralwidget)
        self.error.setGeometry(QtCore.QRect(0, 110, 801, 171))
        self.error.setStyleSheet("font: 75 60pt \"System-ui\";")
        self.error.setAlignment(QtCore.Qt.AlignCenter)
        self.error.setObjectName("error")
        self.error_message = QtWidgets.QLabel(self.centralwidget)
        self.error_message.setGeometry(QtCore.QRect(70, 300, 700, 491))
        self.error_message.setMaximumSize(QtCore.QSize(700, 1000))
        self.error_message.setStyleSheet("font: 75 60pt \"System-ui\";")
        self.error_message.setTextFormat(QtCore.Qt.RichText)
        self.error_message.setScaledContents(False)
        self.error_message.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.error_message.setWordWrap(True)
        self.error_message.setOpenExternalLinks(False)
        self.error_message.setObjectName("error_message")
        self.error_2 = QtWidgets.QLabel(self.centralwidget)
        self.error_2.setGeometry(QtCore.QRect(160, 820, 511, 121))
        self.error_2.setStyleSheet("font: 75 60pt \"System-ui\";\n"
"background-color: rgb(232, 140, 140);")
        self.error_2.setAlignment(QtCore.Qt.AlignCenter)
        self.error_2.setObjectName("error_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ERROR"))
        self.error.setText(_translate("MainWindow", "ERROR "+str(self.info[0]) + ":"))
        self.error_message.setText(_translate("MainWindow", self.info[1]))
        self.error_2.setText(_translate("MainWindow", "OK"))

if __name__ == "__main__":

    
    ui = Bread_Select()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()

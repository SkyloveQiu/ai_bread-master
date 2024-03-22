from PyQt5 import QtCore, QtGui, QtWidgets
class Error_View(object):
    def __init__(self, error_msg, error_code):
        self.error_msg = error_msg
        self.error_code = error_code
        super().__init__()
    def setupUi(self, MainWindow):
         
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 900)
        MainWindow.setMinimumSize(QtCore.QSize(600, 900))
        MainWindow.setMaximumSize(QtCore.QSize(600, 900))
        MainWindow.setTabletTracking(True)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 56, 56);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.error = QtWidgets.QLabel(self.centralwidget)
        self.error.setGeometry(QtCore.QRect(70, 60, 491, 171))
        font = QtGui.QFont()
        font.setFamily("System-ui")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.error.setFont(font)
        self.error.setStyleSheet("font: 75 40pt \"System-ui\";")
        self.error.setAlignment(QtCore.Qt.AlignCenter)
        self.error.setObjectName("error")
        self.error_message = QtWidgets.QLabel(self.centralwidget)
        self.error_message.setGeometry(QtCore.QRect(30, 270, 541, 401))
        self.error_message.setMaximumSize(QtCore.QSize(700, 1000))
        self.error_message.setStyleSheet("font: 75 40pt \"System-ui\";")
        self.error_message.setTextFormat(QtCore.Qt.RichText)
        self.error_message.setScaledContents(False)
        self.error_message.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.error_message.setWordWrap(True)
        self.error_message.setOpenExternalLinks(False)
        self.error_message.setObjectName("error_message")
        self.error_2 = QtWidgets.QLabel(self.centralwidget)
        self.error_2.setGeometry(QtCore.QRect(40, 760, 511, 91))
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
        self.error.setText(_translate("MainWindow", "ERROR "+str(self.error_code) + ":"))
        self.error_message.setText(_translate("MainWindow", self.error_msg))
        self.error_2.setText(_translate("MainWindow", "OK"))
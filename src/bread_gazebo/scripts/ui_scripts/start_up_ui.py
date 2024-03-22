from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Start_Up(object):
    def __init__(self):
        
        self.output_text = ["S.L.I.C.E. Robot. Developed by: Nikolay Blagoev"]

        super().__init__()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 800)
        MainWindow.setMinimumSize(QtCore.QSize(600, 800))
        MainWindow.setMaximumSize(QtCore.QSize(600, 800))
        MainWindow.setTabletTracking(True)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(137, 209, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 581, 211))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 680, 551, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 190, 551, 441))
        self.label_2.setStyleSheet("font: 20 20pt \"System-ui\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def append_output(self, new_message):
        _translate = QtCore.QCoreApplication.translate
        self.output_text.append(new_message)
        string_temp = ""
        for msg in self.output_text:
            string_temp += msg
            string_temp += "\n"
        
        self.label_2.setText(_translate("MainWindow", string_temp))
        self.output_text = self.output_text[-11:]
    
    def change_progress(self, new_progress):
        self.progressBar.setProperty("value", new_progress)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Starting the machine"))
        string_temp = ""
        for msg in self.output_text:
            string_temp += msg
            string_temp += "\n"
        
        self.label_2.setText(_translate("MainWindow", string_temp))






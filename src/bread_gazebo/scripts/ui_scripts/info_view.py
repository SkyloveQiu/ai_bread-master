# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'info.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Info_Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 800)
        MainWindow.setMinimumSize(QtCore.QSize(600, 800))
        MainWindow.setMaximumSize(QtCore.QSize(600, 800))
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
        self.label_9.setGeometry(QtCore.QRect(70, 90, 491, 51))
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
        self.label_10.setGeometry(QtCore.QRect(40, 20, 41, 41))
        self.label_10.setText("")
        self.label_10.setTextFormat(QtCore.Qt.RichText)
        self.label_10.setPixmap(QtGui.QPixmap(":/newPrefix/power.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setGeometry(QtCore.QRect(50, 200, 531, 401))
        self.scrollArea.setStyleSheet("QScrollBar:vertical {\n"
"            border: 0px solid #999999;\n"
"            background:white;\n"
"            width:10px;    \n"
"            margin: 0px 0px 0px 0px;\n"
"        }\n"
"        QScrollBar::handle:vertical {         \n"
"       \n"
"            min-height: 0px;\n"
"              border: 0px solid red;\n"
"            border-radius: 4px;\n"
"            background-color: gray;\n"
"        }\n"
"        QScrollBar::add-line:vertical {       \n"
"            height: 0px;\n"
"            subcontrol-position: bottom;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"        QScrollBar::sub-line:vertical {\n"
"            height: 0 px;\n"
"            subcontrol-position: top;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"\n"
"QScrollArea,  QAbstractScrollArea, QWidget{\n"
"    border-radius: 60px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 517, 851))
        self.scrollAreaWidgetContents.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 60px;")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.label.setStyleSheet("padding : 2px")
        self.verticalLayout.addWidget(self.label)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_9.setText(_translate("MainWindow", "INFO"))
        self.label_10.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label.setText(_translate("MainWindow", "A\n"
" A\n"
"AA\n"
" A\n"
"AA\n"
" A\n"
"AA\n"
" A\n"
"AA\n"
" A\n"
"AA\n"
" A\n"
"AA\n"
" A\n"
"AA\n"
" A\n"
"AA\n"
" A\n"
"AA\n"
" A\n"
"AA\n"
" A\n"
"AA\n"
" A\n"
"AA\n"
" A\n"
"AA\n"
" A\n"
"AA\n"
" A\n"
"AA\n"
" A\n"
"AA\n"
" A\n"
"AA\n"
" A\n"
"AA\n"
" A\n"
"AA\n"
" A\n"
"AA\n"
" A\n"
"AA\n"
" A\n"
"AA\n"
" A\n"
"AA\n"
" A\n"
"A"))

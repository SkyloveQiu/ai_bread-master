# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.error.setText(_translate("MainWindow", "ERROR [NNN]:"))
        self.error_message.setText(_translate("MainWindow", "EEEEEEEEE EEEEEEEEEEE  EEEEEE  EEERRRRR RRRRRRRRRRR"))
        self.error_2.setText(_translate("MainWindow", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

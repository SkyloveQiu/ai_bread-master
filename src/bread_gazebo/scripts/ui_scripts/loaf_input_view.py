import os
from PyQt5 import QtCore, QtGui, QtWidgets
from .select_type import SelectType
dirpath = os.path.dirname(os.path.realpath(__file__))

class Loaf_Input(object):
    def __init__(self, confirm_callback, home_return, loaves = None, loaf_count = None ):
        if loaves == None:
            loaves = []
        self.select_menu = None
        if loaf_count == None:
            loaf_count = []
        self.loaves = loaves
        self.loaf_count=loaf_count
        self.confirm_callback=confirm_callback
        self.home_return = home_return
        
        super().__init__()
    def setupUi(self, MainWindow):
        self.select_menu =  SelectType([self.add_bread(MainWindow, "Boulogne"),
        self.add_bread(MainWindow, "Tijger Wit"), self.add_bread(MainWindow, "Volkoren Meergranen")])
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

        count = 0
        for x, bread in enumerate(self.loaves):
            frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
            frame_2.setGeometry(QtCore.QRect(10, 150+x*180, 581, 141))
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(frame_2.sizePolicy().hasHeightForWidth())
            frame_2.setSizePolicy(sizePolicy)
            frame_2.setStyleSheet("background-color: rgb(137, 209, 255);\n"
    "border-top-left-radius :35px;\n"
    "border-top-right-radius :35px;\n"
    "border-bottom-left-radius :35px;\n"
    "border-bottom-right-radius :35px;\n"
    "\n"
    "\n"
    "")
            frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
            frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
            frame_2.setObjectName("frame_2")
            bread_image_3 = QtWidgets.QGraphicsView(frame_2)
            bread_image_3.setGeometry(QtCore.QRect(40, 20, 111, 101))
            bread_image_3.setObjectName("bread_image_3")
            bread_type_3 = QtWidgets.QLabel(frame_2)
            bread_type_3.setGeometry(QtCore.QRect(160, 20, 261, 101))
            font = QtGui.QFont()
            font.setFamily("System-ui")
            font.setPointSize(14)
            font.setBold(True)
            font.setWeight(75)
            bread_type_3.setFont(font)
            bread_type_3.setStyleSheet("color: rgb(243, 243, 243);\n"
    "")
            bread_type_3.setTextFormat(QtCore.Qt.RichText)
            bread_type_3.setScaledContents(False)
            bread_type_3.setObjectName("bread_type_3")
            frame = QtWidgets.QFrame(frame_2)
            frame.setGeometry(QtCore.QRect(430, 50, 41, 41))
            frame.setStyleSheet("background-color: rgb(255, 255, 255);")
            frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            frame.setFrameShadow(QtWidgets.QFrame.Raised)
            frame.setObjectName("frame")
            label = QtWidgets.QLabel(frame)
            label.setGeometry(QtCore.QRect(0, 6, 31, 31))
            label.setObjectName("label")
            label_2 = QtWidgets.QLabel(frame_2)
            label_2.setGeometry(QtCore.QRect(500, 10, 41, 41))
            font = QtGui.QFont()
            font.setFamily("System-ui")
            font.setPointSize(15)
            font.setBold(True)
            font.setWeight(75)
            label_2.setFont(font)
            label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
            label_2.setAlignment(QtCore.Qt.AlignCenter)
            label_2.setObjectName("label_2")
            label_3 = QtWidgets.QLabel(frame_2)
            label_3.setGeometry(QtCore.QRect(500, 70, 41, 41))
            font = QtGui.QFont()
            font.setFamily("System-ui")
            font.setPointSize(15)
            font.setBold(True)
            font.setWeight(75)
            label_3.setFont(font)
            label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
            label_3.setAlignment(QtCore.Qt.AlignCenter)
            label_3.setObjectName("label_3")
            _translate = QtCore.QCoreApplication.translate
            count= count+1
            bread_type_3.setText(_translate("MainWindow", self.loaves[x]))
            label.setText(_translate("MainWindow", str(self.loaf_count[x])))
            label_2.setText(_translate("MainWindow", "+"))
            label_3.setText(_translate("MainWindow", "-"))
            label_2.mouseReleaseEvent=self.increase_count(x,_translate,label,1,MainWindow)
            label_3.mouseReleaseEvent=self.increase_count(x,_translate,label,-1,MainWindow)

    
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
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.frame_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setGeometry(QtCore.QRect(410, count*180+150, 151, 91))
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

"")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.bread_type_5 = QtWidgets.QLabel(self.frame_4)
        self.bread_type_5.setGeometry(QtCore.QRect(20, 10, 111, 71))
        font = QtGui.QFont()
        font.setFamily("System-ui")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bread_type_5.setFont(font)
        self.bread_type_5.setStyleSheet("color: rgb(243, 243, 243);\n"
"")
        self.bread_type_5.setTextFormat(QtCore.Qt.RichText)
        self.bread_type_5.setScaledContents(False)
        self.bread_type_5.setAlignment(QtCore.Qt.AlignCenter)
        self.bread_type_5.setObjectName("bread_type_5")
        self.frame_6 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_6.setGeometry(QtCore.QRect(30, count*180+150, 151, 91))
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
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame_4.mouseReleaseEvent = self.switch_to_select(MainWindow)
        self.bread_type_5.mouseReleaseEvent=self.switch_to_select(MainWindow)
        self.frame_6.mouseReleaseEvent = self.confirm_callback
        self.label_10.mouseReleaseEvent = self.home_return
        self.bread_type_6.mouseReleaseEvent=self.confirm_callback
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def switch_to_select(self, MainWindow):
        return lambda e: self.select_menu.setupUi(MainWindow)
    def add_bread(self, MainWindow, type):
        
        return lambda e : (
            self.loaves.append(type),
            self.loaf_count.append(1),
            self.setupUi(MainWindow))
    def incr_helper(self,x,_translate, label,m,MainWindow):
        self.loaf_count[x]=self.loaf_count[x]+m
        if self.loaf_count[x] < 1:
            self.loaf_count.pop(x)
            self.loaves.pop(x)
            print("cleared")
            self.setupUi(MainWindow)
        else:
            label.setText(_translate("MainWindow", str(self.loaf_count[x])))
    
    def increase_count(self,x,_translate, label,m,MainWindow):
        return lambda e : self.incr_helper(x,_translate, label,m,MainWindow)
  

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.label_9.setText(_translate("MainWindow", "ADD LOAVES"))
        self.label_10.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.bread_type_5.setText(_translate("MainWindow", "ADD LOAF"))
        self.bread_type_6.setText(_translate("MainWindow", "CONFIRM"))

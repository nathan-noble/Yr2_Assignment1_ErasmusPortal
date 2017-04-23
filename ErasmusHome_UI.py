'''
Program Name:   SGM2 Assignment - Home Page UI of Erasmus Page
Author:         Jonathan Noble - C15487922 (DT282/2)
'''
from PyQt4 import QtCore, QtGui
import sys
import icons_rc

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class MainWindow(QtGui.QMainWindow):
    def __init__(self, image_files, parent=None):
        super(MainWindow, self).__init__()
        #QtGui.QWidget.__init__(self, parent)

        self.setupUi(self)
        self.styledata=' '
        file=open('blurange.css','r')
        self.styledata=file.read()
        file.close()
        self.slides_widget = Slides(image_files, self)
        self.setCentralWidget(self.slides_widget)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1278, 641)
        self.tabWidget = QtGui.QTabWidget(MainWindow)
        self.tabWidget.setGeometry(QtCore.QRect(690, 180, 531, 331))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.textBrowser_4 = QtGui.QTextBrowser(self.tab)
        self.textBrowser_4.setGeometry(QtCore.QRect(180, 80, 211, 41))
        self.textBrowser_4.setObjectName(_fromUtf8("textBrowser_4"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(40, 160, 81, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(50, 70, 81, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.toolButton = QtGui.QToolButton(self.tab)
        self.toolButton.setGeometry(QtCore.QRect(390, 20, 51, 51))
        self.toolButton.setStyleSheet(_fromUtf8("border-image:url(:/icons/info.png);\n"
    "background: none;\n"
    "background-color: transparent;\n"
    "border: none;"))
        self.toolButton.setText(_fromUtf8(""))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.textBrowser_2 = QtGui.QTextBrowser(self.tab)
        self.textBrowser_2.setGeometry(QtCore.QRect(180, 150, 211, 41))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.Submit = QtGui.QPushButton(self.tab)
        self.Submit.setGeometry(QtCore.QRect(240, 230, 75, 23))
        self.Submit.setObjectName(_fromUtf8("Submit"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(230, 20, 51, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.calendarWidget = QtGui.QCalendarWidget(self.tab_2)
        self.calendarWidget.setGeometry(QtCore.QRect(30, 60, 461, 231))
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.pushButton_3 = QtGui.QPushButton(MainWindow)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 450, 61, 61))
        self.pushButton_3.setStyleSheet(_fromUtf8("border-image:url(:/icons/contact_phone.png);\n"
    "background: none;\n"
    "background-color: transparent;\n"
    "border: none;\n"
    ""))
        self.pushButton_3.setText(_fromUtf8(""))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_5 = QtGui.QPushButton(MainWindow)
        self.pushButton_5.setGeometry(QtCore.QRect(490, 180, 71, 61))
        self.pushButton_5.setStyleSheet(_fromUtf8("border-image:url(:/icons/description.png);\n"
    "background: none;\n"
    "background-color: transparent;\n"
    "border: none;\n"
    ""))
        self.pushButton_5.setText(_fromUtf8(""))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.widget = QtGui.QWidget(MainWindow)
        self.widget.setGeometry(QtCore.QRect(690, 530, 531, 78))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(150, 30, 111, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton_2 = QtGui.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 30, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton = QtGui.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(490, 320, 71, 61))
        self.pushButton.setStyleSheet(_fromUtf8("border-image:url(:/icons/testimonials.png);\n"
    "background: none;\n"
    "background-color: transparent;\n"
    "border: none;\n"
    ""))
        self.pushButton.setText(_fromUtf8(""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayoutWidget = QtGui.QWidget(MainWindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(200, 210, 160, 80))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton_3.raise_()
        self.pushButton_5.raise_()
        self.widget.raise_()
        self.pushButton.raise_()
        self.tabWidget.raise_()
        self.verticalLayoutWidget.raise_()

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Erasmus", None))
        self.label_2.setText(_translate("MainWindow", "PASSWORD:", None))
        self.label.setText(_translate("MainWindow", "USERNAME:", None))
        self.Submit.setText(_translate("MainWindow", "SUBMIT", None))
        self.label_3.setText(_translate("MainWindow", "Register", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2", None))
        self.label_4.setText(_translate("MainWindow", "Have an account?", None))
        self.pushButton_2.setText(_translate("MainWindow", "Log-in here!", None))



class Slides(QtGui.QWidget):
    def __init__(self, image_files, parent=None):
        super(Slides, self).__init__(parent)
        #QWidget.__init__(self, parent)

        self.image_files = image_files
        self.label = QtGui.QLabel("", self)
        self.label.setGeometry(80, 170, 450, 350)

        #buttons to rewind and forward
        self.button = QtGui.QPushButton(". . .", self)
        self.button.setGeometry(200, 100, 140, 30)
        self.button.clicked.connect(self.timerEvent)

        self.timer = QtCore.QBasicTimer()
        self.step = 0
        self.delay = 3000 #ms
        sTitle = "DIT Erasmus Page : {} seconds"
        self.setWindowTitle(sTitle.format(self.delay/1000.0))


    def timerEvent(self, e=None):
        if self.step >= len(self.image_files):
            self.timer.start(self.delay, self)
            self.step = 0
            return
        self.timer.start(self.delay, self)
        file = self.image_files[self.step]
        image = QtGui.QPixmap(file)
        self.label.setPixmap(image)
        self.setWindowTitle("{} --> {}".format(str(self.step), file))
        self.step += 1




image_files = ["slide1.jpg", "slide2.jpg", "slide3.jpg", "slide4.jpg", "slide5.jpg"]


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Form = MainWindow(image_files)
    Form.show()
    sys.exit(app.exec_())

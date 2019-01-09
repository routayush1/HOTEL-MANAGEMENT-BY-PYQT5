# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'getinfo.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
import os
import pickle
import sys
import os
from subprocess import call
from PyQt5 import QtCore, QtGui, QtWidgets


def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)






class save:
    def __init__(self, NAME_PRO, ADDRESS_PRO, MOBILE_NO_PRO, ROOM_NO_PRO, PRICE_PRO):
        self.name=NAME_PRO
        self.address=ADDRESS_PRO
        self.mobile_no=MOBILE_NO_PRO
        self.room_no=ROOM_NO_PRO
        self.price=PRICE_PRO
        print(self.name,self.address,self.mobile_no,self.room_no,self.price)
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def check_room(self):
        self.rom = str(self.ENTERLIST.text())
        print(self.rom)
        print("\n")
        if self.rom.isdigit() == True and len(self.rom) != 0:
            self.b = "room no exist"
            self.listWidget.addItem(self.b)
            v = int(self.rom)
            f = open("hotel.dat", "rb")

            n = 0
            try:
                while True:
                    s = pickle.load(f)
                    if s.room_no == v:
                        n = 1
                        name1 = s.name
                        address=s.address
                        mobi=s.mobile_no
                        rooom=s.room_no
                        pappu=s.price

                        print(" ")
                    else:
                        continue

            except EOFError:
                if n == 0:
                    self.b = "no guest found"
                    self.listWidget.addItem(self.b)

                elif n == 1:

                    self.b = '''
                    NAME-%s
                    ADDRESS-%s
                    MOBILE NO.-%s
                    YOUR TOTAL BILL IS Rs.-%s
                    YOUR ROOM NUMBER IS %s    
                    '''%(name1,address,mobi,rooom,pappu)


                    self.listWidget.addItem(self.b)


                pass
            f.close()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(779, 627)
        MainWindow.setMinimumSize(QtCore.QSize(779, 627))
        MainWindow.setMaximumSize(QtCore.QSize(779, 627))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 791, 641))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setStyleSheet("QFrame{background-color: rgb(201, 76, 76);\n"
"\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.GETINFO = QtWidgets.QLabel(self.frame)
        self.GETINFO.setGeometry(QtCore.QRect(240, 20, 271, 71))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.GETINFO.setFont(font)
        self.GETINFO.setObjectName("GETINFO")
        self.ROOMNO = QtWidgets.QLabel(self.frame)
        self.ROOMNO.setGeometry(QtCore.QRect(110, 90, 321, 71))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.ROOMNO.setFont(font)
        self.ROOMNO.setObjectName("ROOMNO")
        self.ENTERLIST = QtWidgets.QLineEdit(self.frame)
        self.ENTERLIST.setGeometry(QtCore.QRect(460, 100, 113, 51))
        self.ENTERLIST.setStyleSheet("QLineEdit{\n"
" border: 2px solid red;\n"
"    padding: 10px;\n"
"    border-radius: 25px;\n"
"\n"
"\n"
"\n"
"}")
        self.ENTERLIST.setObjectName("ENTERLIST")
        self.OK = QtWidgets.QPushButton(self.frame)
        self.OK.setGeometry(QtCore.QRect(290, 170, 171, 81))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.OK.setFont(font)
        self.OK.setStyleSheet("QPushButton:active:after{\n"
"\n"
"    padding: 0;\n"
"    margin: 0;\n"
"    opacity: 1;\n"
"    transition: 1s;\n"
"-webkit-transition-duration: 0.4s; /* Safari */\n"
"    transition-duration: 0.4s;\n"
"\n"
"    background-color:#19707D;\n"
"    color: white;\n"
"\n"
"   }\n"
"")
        self.OK.setObjectName("OK")
        self.OK.clicked.connect(self.check_room)


        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(15, 280, 751, 331))
        self.listWidget.setStyleSheet("QListView{ background-color:white;\n"
"\n"
"border-radius:10px;\n"
"padding:10px;\n"
"\n"
"}")
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.GETINFO.setText(_translate("MainWindow", "GET INFO HERE !!!"))
        self.ROOMNO.setText(_translate("MainWindow", "ENTER THE ROOM NO. "))
        self.OK.setText(_translate("MainWindow", "✔"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RECIPTS.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from __main__ import *
import sys
import os
import pickle
import sys
import os
from subprocess import call
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def recipt(self):
        fo1 = open("recipt.txt", "r")

        list1 = fo1.readlines()
        print (list1)

        self.b = '''
        @@@@@@@@@@@  5 STAR HOTEL AND RESORT  @@@@@@@@@@
        @@@@@@@@@@@@ HAUS KHAZ,  NEW DELHI @@@@@@@@@@@
        @@@@@@@@@@ SERVING    GUEST   SINCE @@@@@@@@@@@@@
        @@@@@@@@@@@@@    ###1950###       @@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        YOUR ROOM NUMBER IS %s
        NAME-%s
        ADDRESS-%s
        MOBILE NO.-%s
        YOUR TOTAL BILL IS Rs.-%s
            



        ''' % ( list1[6],list1[0], list1[2], list1[4], list1[8])
        self.listView.addItem(self.b)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 597)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 811, 601))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setStyleSheet("QFrame{background-color: #3F9CED\n"
";\n"
"\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.listView = QtWidgets.QListWidget(self.frame)
        self.listView.setGeometry(QtCore.QRect(20, 120, 761, 451))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.listView.setFont(font)
        self.listView.setStyleSheet("QListView{\n"
"background-color: white;\n"
"\n"
"border-radius:10px;\n"
"padding:10px;\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"")
        self.listView.setObjectName("listView")
        self.LISTOFALLGUEST = QtWidgets.QLabel(self.frame)
        self.LISTOFALLGUEST.setGeometry(QtCore.QRect(350, 30, 91, 71))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.LISTOFALLGUEST.setFont(font)
        self.LISTOFALLGUEST.setStyleSheet("QWidget{\n"
" background-color:white;\n"
" padding: 10px;\n"
"    border-radius: 25px;\n"
"}")
        self.LISTOFALLGUEST.setObjectName("LISTOFALLGUEST")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.recipt()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LISTOFALLGUEST.setText(_translate("MainWindow", "RECIEPT"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


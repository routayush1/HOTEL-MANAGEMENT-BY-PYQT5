# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LISTOFALLGUEST.ui'
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

l2=[]
G=[]
from PyQt5 import QtCore, QtGui, QtWidgets
def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)


class save:
    def __init__(self,NAME_PRO,ADDRESS_PRO,MOBILE_NO_PRO,ROOM_NO_PRO,PRICE_PRO):
        self.name=NAME_PRO
        self.address=ADDRESS_PRO
        self.mobile_no=MOBILE_NO_PRO
        self.room_no=ROOM_NO_PRO
        self.price=PRICE_PRO


class Ui_MainWindow(object):


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(432, 813)
        MainWindow.setMinimumSize(QtCore.QSize(432, 813))
        MainWindow.setMaximumSize(QtCore.QSize(432, 813))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 781, 821))
        self.frame.setStyleSheet("QFrame{background-color: #3F9CED\n"
";\n"
"\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.LISTOFALLGUEST = QtWidgets.QLabel(self.frame)
        self.LISTOFALLGUEST.setGeometry(QtCore.QRect(10, 10, 391, 61))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.LISTOFALLGUEST.setFont(font)
        self.LISTOFALLGUEST.setStyleSheet("QWidget{\n"
" background-color:white;\n"
" padding: 10px;\n"
"    border-radius: 25px;\n"
"}")
        self.LISTOFALLGUEST.setObjectName("LISTOFALLGUEST")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(0, 80, 431, 731))
        self.tableWidget.setStyleSheet("QWidget{\n"
"\n"
"    border-radius: 50px;\n"
"}")
        self.tableWidget.setRowCount(100)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(185)
        self.tableWidget.verticalHeader().setMinimumSectionSize(40)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        print(l2,G)
        for i in range (0,len(G)):
            self.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(l2[i]))
            self.tableWidget.setItem(i,1,QtWidgets.QTableWidgetItem(str(G[i])))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LISTOFALLGUEST.setText(_translate("MainWindow", "LIST OF ALL GUEST"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "NAME"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ROOM NO."))


if __name__ == "__main__":
    f2 = open("hotel.dat", "rb")
    try:
        while True:
            s = pickle.load(f2)
            k = s.room_no
            o = s.name.upper()
            l2.append(o)

            G.append(k)
            continue
    except EOFError:
        pass
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


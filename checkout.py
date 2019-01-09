# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkout.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


import os
import pickle

details_list=[]
l2=[]
G = []
def file_save():
    NAME_PRO = details_list[0]
    ADDRESS_PRO = details_list[1]
    MOBILE_NO_PRO = details_list[2]
    ROOM_NO_PRO = details_list[3]
    PRICE_PRO = details_list[4]
    f = open("hotel.dat", "ab")
    a=save(NAME_PRO,ADDRESS_PRO,MOBILE_NO_PRO,ROOM_NO_PRO,PRICE_PRO)
    pickle.dump(a,f,protocol=2)
    f.close()
    restart_program()


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



class Ui_MainWindow(object):
    def check_room(self):
        self.rom = str(self.ENTER.text())
        print(self.rom)
        print("\n")
        if self.rom.isdigit() == True and len(self.rom) != 0:
            self.b = "room no exist"
            self.output.addItem(self.b)
            v = int(self.rom)
            f = open("hotel.dat", "rb")
            f1 = open("hote.dat", "ab")
            n = 0
            try:
                while True:
                    s = pickle.load(f)
                    if s.room_no == v:
                        n = 1
                        name1 = s.name

                        print(" ")
                    else:
                        pickle.dump(s, f1)
            except EOFError:
                if n == 0:
                    self.b = "no guest found"
                    self.output.addItem(self.b)

                elif n == 1:

                    self.b =  "THANK YOU  " + name1.upper() + " FOR VISTING US""\n"
                    self.output.addItem(self.b)


                pass
            f.close()
            f1.close()
            os.remove("hotel.dat")
            os.rename("hote.dat", "hotel.dat")

        else:
            self.Text1.insert(INSERT, "invalid input please input a valid ROOM NO.""\n")
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(770, 597)
        MainWindow.setMinimumSize(QtCore.QSize(770, 597))
        MainWindow.setMaximumSize(QtCore.QSize(770, 597))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 771, 601))
        self.frame.setMinimumSize(QtCore.QSize(771, 601))
        self.frame.setMaximumSize(QtCore.QSize(771, 601))
        self.frame.setStyleSheet("QFrame{background-color: #3F9CED\n"
";\n"
"\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.ENTERTHEROOMNO = QtWidgets.QLabel(self.frame)
        self.ENTERTHEROOMNO.setGeometry(QtCore.QRect(180, 30, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.ENTERTHEROOMNO.setFont(font)
        self.ENTERTHEROOMNO.setObjectName("ENTERTHEROOMNO")
        self.ENTER = QtWidgets.QLineEdit(self.frame)
        self.ENTER.setGeometry(QtCore.QRect(320, 80, 121, 51))
        self.ENTER.setStyleSheet("QLineEdit{\n"
" \n"
"    padding: 10px;\n"
"    border-radius: 25px;\n"
"\n"
"\n"
"\n"
"}")
        self.ENTER.setObjectName("ENTER")
        self.ok = QtWidgets.QPushButton(self.frame)
        self.ok.setGeometry(QtCore.QRect(340, 140, 81, 61))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.ok.setFont(font)
        self.ok.setStyleSheet("QPushButton:active:after{\n"
"\n"
"    padding: 0;\n"
"    margin: 0;\n"
"    opacity: 1;\n"
"    transition: 1s;\n"
"-webkit-transition-duration: 0.4s;\n"
"    transition-duration: 0.4s;\n"
"\n"
"    background-color:#19707D;\n"
"    color: white;\n"
"\n"
"   }\n"
"")
        self.ok.setObjectName("ok")
        self.ok.clicked.connect(self.check_room)
        self.output = QtWidgets.QListWidget(self.frame)
        self.output.setGeometry(QtCore.QRect(25, 221, 701, 331))
        self.output.setStyleSheet("QListView{ background-color:white;\n"
"\n"
"border-radius:10px;\n"
"padding:10px;\n"
"\n"
"}")
        self.output.setObjectName("output")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ENTERTHEROOMNO.setText(_translate("MainWindow", "ENTER THE ROOM NO."))
        self.ok.setText(_translate("MainWindow", "✔"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


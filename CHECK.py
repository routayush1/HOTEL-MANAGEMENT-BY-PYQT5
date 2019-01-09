# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CHECK.ui'
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

details_list=[]



u = list()
Delux = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
Semi_Delux = (11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25)
General = (26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45)
Joint_Room = (46, 47, 48, 49, 50, 46, 47, 48, 49, 50)
m = [9]
G = []

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

    def file_save(self):
        print("hello")
        NAME_PRO = details_list[0]
        ADDRESS_PRO = details_list[1]
        MOBILE_NO_PRO = details_list[2]
        ROOM_NO_PRO = details_list[3]
        PRICE_PRO = details_list[4]
        f = open("hotel.dat", "ab")
        a = save(NAME_PRO, ADDRESS_PRO, MOBILE_NO_PRO, ROOM_NO_PRO, PRICE_PRO)
        pickle.dump(a, f, protocol=2)
        f.close()
        listq = [str(NAME_PRO), str(ADDRESS_PRO), str(MOBILE_NO_PRO), str(ROOM_NO_PRO), str(PRICE_PRO)]
        myVars = {'A': NAME_PRO, "B": ADDRESS_PRO, "C": MOBILE_NO_PRO, "D": ROOM_NO_PRO, "E": PRICE_PRO}

        fo = open("recipt.txt", "w+")
        for h in range(0, 5):
            fo.write(listq[h] + "\r\n")
        fo.close()
        call(["python", "recipts.py"])
        restart_program()

    def chk_name(self):
        while True:

            self.k = str(self.nameedit.text())

            a = self.k.isdigit()
            if len(self.k) != 3 and a != True:
                self.NAME = self.k
                self.b="name has been inputed"
                self.listWidget.addItem(self.b)
                break
            else:
                self.b = "name has not been inputed"
                self.listWidget.addItem(self.b)

                break

    def chk_add(self):
        while True:
            self.g = str(self.addedit.text())

            ak = self.g.isdigit()
            if len(self.g) != 4 and ak != True:
                self.ADDERESS = self.g
                self.b = "address has been inputed"
                self.listWidget.addItem(self.b)
                break
            else:
                self.b = "address has been not inputed"
                self.listWidget.addItem(self.b)

                break

    def chk_mo(self):
        while True:

            self.h = str(self.cno_2.text())
            if self.h.isdigit() == True and len(self.h) != 0 and len(self.h) == 10:
                self.MOBILE = self.h
                self.b = "mobile no has been inputed"
                self.listWidget.addItem(self.b)
                break
            else:
                self.b = "mobile no has not been inputed"
                self.listWidget.addItem(self.b)
            break

    def chk_day(self):
        while True:

            self.l = str(self.daysedit.text())

            if self.l.isdigit() == True and len(self.l) != 0:
                self.DAYS = int(self.l)
                self.b = "no of days has been inputed"
                self.listWidget.addItem(self.b)
                break
            else:
                self.b = "no of days has not been inputed"
                self.listWidget.addItem(self.b)
                break

    def enter(self):
        print ("ch")
        self.name = self.NAME
        self.address = self.ADDERESS
        self.mobile_no = self.MOBILE
        self.no_of_days = int(self.DAYS)


        print("heloo")
        self.price=0

        if self.ch == 1:
            self.price = self.price + (2000 * self.no_of_days)
            m[0] = 1
        elif self.ch == 2:
            self.price = self.price + (1500 * self.no_of_days)
            m[0] = 2
        elif self.ch == 3:
            self.price = self.price + (1000 * self.no_of_days)
            m[0] = 3
        elif self.ch == 4:
            self.price = self.price + (1700 * self.no_of_days)
            m[0] = 4

    def payment_option(self):
        op = self.p
        if op == 1:
            self.b = "no discount"
            self.listWidget.addItem(self.b)
        elif op == 2:
            self.price = self.price - ((self.price * 10) / 100)
            self.b = "10% discount"
            self.listWidget.addItem(self.b)

    def bill(self):

        if m[0] == 1:
            a = Delux
        elif m[0] == 2:
            a = Semi_Delux
        elif m[0] == 3:
            a = General
        elif m[0] == 4:
            a = Joint_Room



        G = []
        print("A")
        f2 = open("hotel.dat", "rb")
        print("kya")
        try:
            while True:
                s = pickle.load(f2)
                print("G")

                k = s.room_no
                print (k)
                G.append(k)
                continue

        except EOFError:
            pass
        print("kya")
        x=0

        for r in a:
            x=x+1
            if r in G:
                continue

            elif x==len(a):
                break
            elif r not in G:
                self.room=r
                break

        f2.close()

        details_list.append(self.name)
        details_list.append(self.address)
        details_list.append(self.mobile_no)
        details_list.append(self.room)
        details_list.append(self.price)

        self.file_save()

    def submit_clicked(self):
        if self.DELUXE.isChecked() and (not self.general.isChecked()) and (not self.JOINT.isChecked()) and (
        not self.sdeluxe.isChecked()) and self.CASH.isChecked() and (not self.payonline.isChecked()):
            self.ch = 1
            self.p = 1
            self.enter()

            self.payment_option()
            self.bill()
            print("delux by cash")

        elif self.general.isChecked() and (not self.DELUXE.isChecked()) and (not self.JOINT.isChecked()) and (
        not self.sdeluxe.isChecked()) and self.CASH.isChecked() and (not self.payonline.isChecked()):
            self.ch = 3
            self.p = 1
            self.enter()

            self.payment_option()
            self.bill()
            print("general by cash")

        elif self.JOINT.isChecked() and (not self.DELUXE.isChecked()) and (not self.general.isChecked()) and (
        not self.sdeluxe.isChecked()) and self.CASH.isChecked() and (not self.payonline.isChecked()):
            self.ch = 4
            self.p = 1
            self.enter()

            self.payment_option()
            self.bill()
            print("joint by cash")
        elif self.sdeluxe.isChecked() and (not self.DELUXE.isChecked()) and (not self.JOINT.isChecked()) and (
        not self.general.isChecked()) and self.CASH.isChecked() and (not self.payonline.isChecked()):
            self.ch = 2
            self.p = 1
            self.enter()
            self.payment_option()
            self.bill()
            print("semi deluxe by cash")
        elif self.DELUXE.isChecked() and (not self.general.isChecked()) and (not self.JOINT.isChecked()) and (
        not self.sdeluxe.isChecked()) and self.payonline.isChecked() and (not self.CASH.isChecked()):
            self.ch = 1
            self.p = 2
            self.enter()
            self.payment_option()
            self.bill()
            print("delux by card")
        elif self.general.isChecked() and (not self.DELUXE.isChecked()) and (not self.JOINT.isChecked()) and (
        not self.sdeluxe.isChecked()) and self.payonline.isChecked() and (not self.CASH.isChecked()):
            self.ch = 3
            self.p = 2
            self.enter()
            self.payment_option()
            self.bill()
            print("genral by card")
        elif self.JOINT.isChecked() and (not self.general.isChecked()) and (not self.DELUXE.isChecked()) and (
        not self.sdeluxe.isChecked()) and self.payonline.isChecked() and (not self.CASH.isChecked()):
            self.ch = 4
            self.p = 2
            self.enter()
            self.payment_option()
            self.bill()
            print("joint by card")
        elif self.sdeluxe.isChecked() and (not self.general.isChecked()) and (not self.JOINT.isChecked()) and (
        not self.DELUXE.isChecked()) and self.payonline.isChecked() and (not self.CASH.isChecked()):
            self.ch = 2
            self.p = 2
            self.enter()
            self.payment_option()
            self.bill()
            print("semi deluxe by card")

        else:
            self.b = "pls select valid option"
            self.listWidget.addItem(self.b)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(892, 639)
        MainWindow.setMinimumSize(QtCore.QSize(892, 639))
        MainWindow.setMaximumSize(QtCore.QSize(892, 639))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 901, 641))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(16)
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
        self.INFO = QtWidgets.QLabel(self.frame)
        self.INFO.setGeometry(QtCore.QRect(120, 0, 611, 51))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.INFO.setFont(font)
        self.INFO.setObjectName("INFO")
        self.name = QtWidgets.QLabel(self.frame)
        self.name.setGeometry(QtCore.QRect(50, 40, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.cno = QtWidgets.QLabel(self.frame)
        self.cno.setGeometry(QtCore.QRect(50, 120, 371, 61))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.cno.setFont(font)
        self.cno.setObjectName("cno")
        self.address = QtWidgets.QLabel(self.frame)
        self.address.setGeometry(QtCore.QRect(50, 80, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.address.setFont(font)
        self.address.setObjectName("address")
        self.chooseroom = QtWidgets.QLabel(self.frame)
        self.chooseroom.setGeometry(QtCore.QRect(200, 210, 381, 61))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.chooseroom.setFont(font)
        self.chooseroom.setObjectName("chooseroom")
        self.days = QtWidgets.QLabel(self.frame)
        self.days.setGeometry(QtCore.QRect(50, 160, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.days.setFont(font)
        self.days.setObjectName("days")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(170, 340, 421, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.nameedit = QtWidgets.QLineEdit(self.frame)
        self.nameedit.setGeometry(QtCore.QRect(430, 60, 321, 20))
        self.nameedit.setStyleSheet("")

        self.nameedit.setObjectName("nameedit")
        self.ok1 = QtWidgets.QPushButton(self.frame)
        self.ok1.setGeometry(QtCore.QRect(770, 60, 75, 23))
        self.ok1.setStyleSheet("QPushButton:active:after{\n"
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
        self.ok1.setObjectName("ok1")
        self.ok1.clicked.connect(self.chk_name)







        self.addedit = QtWidgets.QLineEdit(self.frame)
        self.addedit.setGeometry(QtCore.QRect(430, 100, 321, 20))
        self.addedit.setStyleSheet("")
        self.addedit.setObjectName("addedit")
        self.ok2 = QtWidgets.QPushButton(self.frame)
        self.ok2.setGeometry(QtCore.QRect(770, 100, 75, 23))
        self.ok2.setStyleSheet("QPushButton:active:after{\n"
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

        self.ok2.clicked.connect(self.chk_add)
        self.ok2.setObjectName("ok2")

        self.cno_2 = QtWidgets.QLineEdit(self.frame)
        self.cno_2.setGeometry(QtCore.QRect(430, 140, 321, 20))
        self.cno_2.setStyleSheet("")
        self.cno_2.setObjectName("cno_2")
        self.ok3 = QtWidgets.QPushButton(self.frame)
        self.ok3.setGeometry(QtCore.QRect(770, 140, 75, 23))
        self.ok3.setStyleSheet("QPushButton:active:after{\n"
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
        self.ok3.clicked.connect(self.chk_mo)
        self.ok3.setObjectName("ok3")
        self.daysedit = QtWidgets.QLineEdit(self.frame)
        self.daysedit.setGeometry(QtCore.QRect(430, 180, 321, 20))
        self.daysedit.setStyleSheet("")
        self.daysedit.setObjectName("daysedit")
        self.ok4 = QtWidgets.QPushButton(self.frame)
        self.ok4.setGeometry(QtCore.QRect(770, 180, 75, 23))
        self.ok4.setStyleSheet("QPushButton:active:after{\n"
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
        self.ok4.clicked.connect(self.chk_day)
        self.ok4.setObjectName("ok4")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(690, 380, 91, 31))
        self.pushButton.setStyleSheet("QPushButton:active:after{\n"
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
        self.pushButton.clicked.connect(self.submit_clicked)
        self.pushButton.setObjectName("pushButton")


        self.listWidget = QtWidgets.QListWidget(self.frame)

        self.listWidget.setGeometry(QtCore.QRect(20, 420, 871, 211))
        self.listWidget.setStyleSheet("QListView{\n"
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
        self.listWidget.setObjectName("listWidget")
        self.general = QtWidgets.QCheckBox(self.frame)
        self.general.setGeometry(QtCore.QRect(500, 260, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.general.setFont(font)
        self.general.setObjectName("general")
        self.payonline = QtWidgets.QRadioButton(self.frame)
        self.payonline.setGeometry(QtCore.QRect(230, 380, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.payonline.setFont(font)
        self.payonline.setObjectName("payonline")
        self.JOINT = QtWidgets.QCheckBox(self.frame)
        self.JOINT.setGeometry(QtCore.QRect(500, 300, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.JOINT.setFont(font)
        self.JOINT.setObjectName("JOINT")
        self.DELUXE = QtWidgets.QCheckBox(self.frame)
        self.DELUXE.setGeometry(QtCore.QRect(110, 243, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.DELUXE.setFont(font)
        self.DELUXE.setObjectName("DELUXE")
        self.sdeluxe = QtWidgets.QCheckBox(self.frame)
        self.sdeluxe.setGeometry(QtCore.QRect(110, 300, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.sdeluxe.setFont(font)
        self.sdeluxe.setStyleSheet("")
        self.sdeluxe.setObjectName("sdeluxe")
        self.CASH = QtWidgets.QRadioButton(self.frame)
        self.CASH.setGeometry(QtCore.QRect(60, 380, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.CASH.setFont(font)
        self.CASH.setObjectName("CASH")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.INFO.setText(_translate("MainWindow", "YOU CLICKED ON  :   CHECK INN"))
        self.name.setText(_translate("MainWindow", "ENTER YOUR NAME"))
        self.cno.setText(_translate("MainWindow", "ENTER YOUR CONTACT NO."))
        self.address.setText(_translate("MainWindow", "ENTER YOUR ADDRESS"))
        self.chooseroom.setText(_translate("MainWindow", "CHOOSE YOUR ROOM"))
        self.days.setText(_translate("MainWindow", "NO. OF DAYS"))
        self.label_2.setText(_translate("MainWindow", "CHOOSE PAYMENT METHOD"))
        self.ok1.setText(_translate("MainWindow", "OK"))
        self.ok2.setText(_translate("MainWindow", "OK"))
        self.ok3.setText(_translate("MainWindow", "OK"))
        self.ok4.setText(_translate("MainWindow", "OK"))
        self.pushButton.setText(_translate("MainWindow", "✔"))
        self.general.setText(_translate("MainWindow", "GENERAL"))
        self.payonline.setText(_translate("MainWindow", "BY CREDIT/DEBIT CARD/PAYTM"))
        self.JOINT.setText(_translate("MainWindow", "JOINT"))
        self.DELUXE.setText(_translate("MainWindow", "DELUXE"))
        self.sdeluxe.setText(_translate("MainWindow", "SUPER DELUXE"))
        self.CASH.setText(_translate("MainWindow", "BY CASH"))


if __name__ == "__main__":
    import sys
    import atexit
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()







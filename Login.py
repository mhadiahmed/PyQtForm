# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sqlite3
from singup import Ui_SingUp
import hashlib
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

class Ui_Form(object):
    def SinForm(self):
        self.Form = QtGui.QWidget()
        self.ui = Ui_SingUp()
        self.ui.setupUi(self.Form)
        self.Form.show()
    def SingCall(self):
        self.SinForm()
    def connection(self):
        userName = self.lineEdit.text()
        passWord = self.lineEdit_2.text()
        Phash = hashlib.md5(passWord.encode()).hexdigest()
        
        
        db = sqlite3.connect('database')
        rb = db.execute('select * from user where users = ? and pass = ?', (userName,Phash))
        if len(rb.fetchall()) > 0:
            print('database connected')
        else:
            print('connected field')
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        ################lineEdit########################
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(190, 90, 113, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        ################lineEdit_2########################
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 120, 113, 21))
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        ################label########################
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 90, 61, 16))
        self.label.setStyleSheet(_fromUtf8("font-weight:bold"))
        self.label.setObjectName(_fromUtf8("label"))
        ################label_2########################
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(110, 120, 61, 16))
        self.label_2.setStyleSheet(_fromUtf8("font-weight:bold"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        ################pushButton########################
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(130, 180, 75, 23))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(_fromUtf8("border:none;background-color:#000;color:#fff"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.connection)
        ################pushButton_2########################
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 180, 75, 23))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(_fromUtf8("border:none;background-color:#000;color:#fff"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.SingCall)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        ################Global items########################
    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Login Form", None))
        self.lineEdit.setPlaceholderText(_translate("Form", "User Name", None))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Password", None))
        self.label.setText(_translate("Form", "User Name", None))
        self.label_2.setText(_translate("Form", "password", None))
        self.pushButton.setText(_translate("Form", "login", None))
        self.pushButton_2.setText(_translate("Form", "sing up", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


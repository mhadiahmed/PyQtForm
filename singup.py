#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'singup.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sqlite3
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

class Ui_SingUp(object):
    def insert(self):
        Name = self.lineEdit.text()
        Email = self.lineEdit_2.text()
        Pass = self.lineEdit_3.text()
        Phash = hashlib.md5(Pass.encode()).hexdigest()
        
        db = sqlite3.connect('database')
        db.execute('insert into user (users,email,pass)values(?,?,?)',(Name,Email,Phash))
        db.commit()
        print('Done.')
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(552, 358)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(130, 70, 61, 21))
        self.label.setStyleSheet(_fromUtf8("font-weight:bold;"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(130, 100, 61, 21))
        self.label_2.setStyleSheet(_fromUtf8("font-weight:bold;"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(130, 130, 61, 21))
        self.label_3.setStyleSheet(_fromUtf8("font-weight:bold;"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(190, 70, 131, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 100, 131, 21))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 130, 131, 21))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(190, 210, 75, 23))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(_fromUtf8("border:none;background-color:black;color:#fff"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.insert)
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 210, 75, 23))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(_fromUtf8("border:none;background-color:black;color:#fff"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Sing UP", None))
        self.label.setText(_translate("Form", "Name", None))
        self.label_2.setText(_translate("Form", "Email", None))
        self.label_3.setText(_translate("Form", "PassWord", None))
        self.lineEdit.setPlaceholderText(_translate("Form", "Enter Your Name", None))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Enter Your Email", None))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "Enter Your Pass", None))
        self.pushButton.setText(_translate("Form", "Save", None))
        self.pushButton_2.setText(_translate("Form", "Update", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_SingUp()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(431, 392)

        self.horizontalLayout = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.button_a = QtGui.QPushButton('Do something')
        self.button_b = QtGui.QPushButton('Hook should fail')

        self.horizontalLayout.addWidget(self.button_a)
        self.horizontalLayout.addWidget(self.button_b)

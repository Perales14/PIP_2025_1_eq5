# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\P2_Ejemplo.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txt_A = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_A.setGeometry(QtCore.QRect(330, 270, 113, 22))
        self.txt_A.setText("")
        self.txt_A.setObjectName("txt_A")
        self.txt_B = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_B.setGeometry(QtCore.QRect(330, 220, 113, 22))
        self.txt_B.setObjectName("txt_B")
        self.lbl_imagenGatos_2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_imagenGatos_2.setGeometry(QtCore.QRect(490, 390, 311, 171))
        self.lbl_imagenGatos_2.setStyleSheet("")
        self.lbl_imagenGatos_2.setText("")
        self.lbl_imagenGatos_2.setPixmap(QtGui.QPixmap(":/Logos/Archivos/export202502092301563482.png"))
        self.lbl_imagenGatos_2.setScaledContents(True)
        self.lbl_imagenGatos_2.setObjectName("lbl_imagenGatos_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 260, 121, 41))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 210, 121, 41))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.lbl_imagenUat = QtWidgets.QLabel(self.centralwidget)
        self.lbl_imagenUat.setGeometry(QtCore.QRect(0, 10, 331, 121))
        self.lbl_imagenUat.setStyleSheet("")
        self.lbl_imagenUat.setText("")
        self.lbl_imagenUat.setPixmap(QtGui.QPixmap(":/Logos/Archivos/log_uat_nuevo.png"))
        self.lbl_imagenUat.setScaledContents(True)
        self.lbl_imagenUat.setObjectName("lbl_imagenUat")
        self.btn_sumar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sumar.setGeometry(QtCore.QRect(290, 390, 161, 51))
        self.btn_sumar.setObjectName("btn_sumar")
        self.lbl_imagenFi = QtWidgets.QLabel(self.centralwidget)
        self.lbl_imagenFi.setGeometry(QtCore.QRect(590, 0, 211, 141))
        self.lbl_imagenFi.setStyleSheet("")
        self.lbl_imagenFi.setText("")
        self.lbl_imagenFi.setPixmap(QtGui.QPixmap(":/Logos/Archivos/FIT_logo_vertical.png"))
        self.lbl_imagenFi.setScaledContents(True)
        self.lbl_imagenFi.setObjectName("lbl_imagenFi")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 320, 121, 41))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.txt_C = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_C.setGeometry(QtCore.QRect(330, 330, 113, 22))
        self.txt_C.setText("")
        self.txt_C.setObjectName("txt_C")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Numero 2:  "))
        self.label.setText(_translate("MainWindow", "Numero 1: "))
        self.btn_sumar.setText(_translate("MainWindow", "Suma"))
        self.label_3.setText(_translate("MainWindow", "Numero 2:  "))
import Recursos_rc

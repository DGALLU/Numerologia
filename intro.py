# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'intro.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1232, 740)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"background-color:rgb(250, 220, 255);\n"
"color:rgb(250, 220, 255);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 100, 1231, 111))
        font = QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(4, 236, 1221, 141))
        font1 = QFont()
        font1.setPointSize(9)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.ingresar = QPushButton(self.centralwidget)
        self.ingresar.setObjectName(u"ingresar")
        self.ingresar.setGeometry(QRect(250, 470, 201, 41))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setWeight(50)
        self.ingresar.setFont(font2)
        self.salir = QPushButton(self.centralwidget)
        self.salir.setObjectName(u"salir")
        self.salir.setGeometry(QRect(790, 470, 211, 41))
        font3 = QFont()
        font3.setPointSize(10)
        self.salir.setFont(font3)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(780, 650, 441, 31))
        font4 = QFont()
        font4.setPointSize(6)
        self.label_3.setFont(font4)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(780, 680, 441, 31))
        self.label_4.setFont(font4)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1232, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Aplicaci\u00f3n de Numerolog\u00eda", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Detr\u00e1s de toda la existencia se esconden los n\u00fameros, esos c\u00f3digos detr\u00e1s de lo que vemos, de lo que \"percibimos\" \n"
"desde los sentidos como \"realidad\". Los n\u00fameros tienen, por lo tanto y si se los interpreta coherentemente,\n"
" muchos datos precisos del inconsciente. De ese gran socio del Creador..", None))
        self.ingresar.setText(QCoreApplication.translate("MainWindow", u"Ingresar", None))
        self.salir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Dise\u00f1o: Tom\u00e1s Videla - transgeneracional22@gmail.com", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Desarrollo: Daniel Gallucci - daniel.gallucci@gmail.com", None))
    # retranslateUi


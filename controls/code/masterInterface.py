# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reactor_master.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread
import time
import rpiTransm as rpi

def getData():
    energy = transm.getEnergy()
    ui.energyLcd.display(energy)
    time.sleep(0.3)
    for num in range(1, 17):
        val = transm.getSensor(num)
        eval("ui.t{}.display(val)".format(num))
        time.sleep(0.3)
    if exit == 1:
        getData()
    else:
        sys.exit(exit)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(1025, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 768))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Hurricane_in_glass/controls/design/img/nuke logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-image: url(:/img/img/bg_grey.jpg);")
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.menu2 = QtWidgets.QWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setItalic(False)
        self.menu2.setFont(font)
        self.menu2.setAutoFillBackground(False)
        self.menu2.setObjectName("menu2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.menu2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.reactor1Temp_2 = QtWidgets.QWidget(self.menu2)
        font = QtGui.QFont()
        font.setItalic(False)
        self.reactor1Temp_2.setFont(font)
        self.reactor1Temp_2.setStyleSheet("border: 2px solid white;")
        self.reactor1Temp_2.setObjectName("reactor1Temp_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.reactor1Temp_2)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.reactorLcd_2 = QtWidgets.QLCDNumber(self.reactor1Temp_2)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setItalic(False)
        self.reactorLcd_2.setFont(font)
        self.reactorLcd_2.setAutoFillBackground(False)
        self.reactorLcd_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.reactorLcd_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.reactorLcd_2.setObjectName("reactorLcd_2")
        self.verticalLayout_10.addWidget(self.reactorLcd_2)
        self.label_8 = QtWidgets.QLabel(self.reactor1Temp_2)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(24)
        font.setItalic(False)
        self.label_8.setFont(font)
        self.label_8.setAutoFillBackground(False)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255); border: 0;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_10.addWidget(self.label_8)
        self.verticalLayout.addWidget(self.reactor1Temp_2)
        self.reactor1Temp = QtWidgets.QWidget(self.menu2)
        font = QtGui.QFont()
        font.setItalic(False)
        self.reactor1Temp.setFont(font)
        self.reactor1Temp.setStyleSheet("border: 2px solid white;")
        self.reactor1Temp.setObjectName("reactor1Temp")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.reactor1Temp)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.reactorLcd = QtWidgets.QLCDNumber(self.reactor1Temp)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setItalic(False)
        self.reactorLcd.setFont(font)
        self.reactorLcd.setAutoFillBackground(False)
        self.reactorLcd.setStyleSheet("color: rgb(255, 255, 255);")
        self.reactorLcd.setFrameShadow(QtWidgets.QFrame.Plain)
        self.reactorLcd.setObjectName("reactorLcd")
        self.verticalLayout_9.addWidget(self.reactorLcd)
        self.label_7 = QtWidgets.QLabel(self.reactor1Temp)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(24)
        font.setItalic(False)
        self.label_7.setFont(font)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255); border: 0;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_9.addWidget(self.label_7)
        self.verticalLayout.addWidget(self.reactor1Temp)
        self.widget_4 = QtWidgets.QWidget(self.menu2)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setItalic(False)
        self.widget_4.setFont(font)
        self.widget_4.setAutoFillBackground(False)
        self.widget_4.setStyleSheet("border: 2px solid white;")
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.energyLcd = QtWidgets.QLCDNumber(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setItalic(False)
        self.energyLcd.setFont(font)
        self.energyLcd.setAutoFillBackground(False)
        self.energyLcd.setStyleSheet("color: rgb(255, 255, 255);")
        self.energyLcd.setFrameShadow(QtWidgets.QFrame.Plain)
        self.energyLcd.setObjectName("energyLcd")
        self.verticalLayout_8.addWidget(self.energyLcd)
        self.label_6 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(24)
        font.setItalic(False)
        self.label_6.setFont(font)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255); border: 0;")
        self.label_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_8.addWidget(self.label_6)
        self.verticalLayout.addWidget(self.widget_4)
        self.widget_3 = QtWidgets.QWidget(self.menu2)
        self.widget_3.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setItalic(False)
        self.widget_3.setFont(font)
        self.widget_3.setAutoFillBackground(False)
        self.widget_3.setStyleSheet("")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.turnOn = QtWidgets.QPushButton(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        font.setItalic(False)
        self.turnOn.setFont(font)
        self.turnOn.setStyleSheet("color:white;")
        self.turnOn.setObjectName("turnOn")
        self.verticalLayout_7.addWidget(self.turnOn)
        self.crash1 = QtWidgets.QPushButton(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        font.setItalic(False)
        self.crash1.setFont(font)
        self.crash1.setAutoFillBackground(False)
        self.crash1.setStyleSheet("color: rgb(255, 255, 255);")
        self.crash1.setObjectName("crash1")
        self.verticalLayout_7.addWidget(self.crash1)
        self.crash2 = QtWidgets.QPushButton(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        font.setItalic(False)
        self.crash2.setFont(font)
        self.crash2.setAutoFillBackground(False)
        self.crash2.setStyleSheet("color: rgb(255, 255, 255);")
        self.crash2.setObjectName("crash2")
        self.verticalLayout_7.addWidget(self.crash2)
        self.crash3 = QtWidgets.QPushButton(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        font.setItalic(False)
        self.crash3.setFont(font)
        self.crash3.setAutoFillBackground(False)
        self.crash3.setStyleSheet("color: rgb(255, 255, 255);")
        self.crash3.setObjectName("crash3")
        self.verticalLayout_7.addWidget(self.crash3)
        self.modelOff = QtWidgets.QPushButton(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        font.setItalic(False)
        self.modelOff.setFont(font)
        self.modelOff.setAutoFillBackground(False)
        self.modelOff.setStyleSheet("color: rgb(255, 255, 255);")
        self.modelOff.setObjectName("modelOff")
        self.verticalLayout_7.addWidget(self.modelOff)
        self.playersOff = QtWidgets.QPushButton(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        font.setItalic(False)
        self.playersOff.setFont(font)
        self.playersOff.setAutoFillBackground(False)
        self.playersOff.setStyleSheet("color: rgb(255, 255, 255);")
        self.playersOff.setObjectName("playersOff")
        self.verticalLayout_7.addWidget(self.playersOff)
        self.endGame = QtWidgets.QPushButton(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        font.setItalic(False)
        self.endGame.setFont(font)
        self.endGame.setAutoFillBackground(False)
        self.endGame.setStyleSheet("color: rgb(255, 255, 255);")
        self.endGame.setObjectName("endGame")
        self.verticalLayout_7.addWidget(self.endGame)
        self.modelOff.raise_()
        self.endGame.raise_()
        self.playersOff.raise_()
        self.crash1.raise_()
        self.crash2.raise_()
        self.crash3.raise_()
        self.turnOn.raise_()
        self.verticalLayout.addWidget(self.widget_3)
        self.horizontalLayout_4.addWidget(self.menu2)
        self.sensors = QtWidgets.QWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setItalic(False)
        self.sensors.setFont(font)
        self.sensors.setStyleSheet("border: 2px solid white;")
        self.sensors.setObjectName("sensors")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.sensors)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.w = QtWidgets.QWidget(self.sensors)
        font = QtGui.QFont()
        font.setItalic(False)
        self.w.setFont(font)
        self.w.setStyleSheet("border: 0;")
        self.w.setObjectName("w")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.w)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.label_5 = QtWidgets.QLabel(self.w)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: white;")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_28.addWidget(self.label_5)
        self.verticalLayout_27.addWidget(self.w)
        self.s1 = QtWidgets.QWidget(self.sensors)
        font = QtGui.QFont()
        font.setItalic(False)
        self.s1.setFont(font)
        self.s1.setStyleSheet("border: 0;")
        self.s1.setObjectName("s1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.s1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.t1 = QtWidgets.QLCDNumber(self.s1)
        self.t1.setStyleSheet("border: 2px solid white;")
        self.t1.setObjectName("t1")
        self.verticalLayout_6.addWidget(self.t1)
        self.verticalLayout_27.addWidget(self.s1)
        self.s1_10 = QtWidgets.QWidget(self.sensors)
        font = QtGui.QFont()
        font.setItalic(False)
        self.s1_10.setFont(font)
        self.s1_10.setStyleSheet("border: 0;")
        self.s1_10.setObjectName("s1_10")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.s1_10)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.t2 = QtWidgets.QLCDNumber(self.s1_10)
        self.t2.setStyleSheet("border: 2px solid white;")
        self.t2.setObjectName("t2")
        self.verticalLayout_20.addWidget(self.t2)
        self.verticalLayout_27.addWidget(self.s1_10)
        self.s1_9 = QtWidgets.QWidget(self.sensors)
        font = QtGui.QFont()
        font.setItalic(False)
        self.s1_9.setFont(font)
        self.s1_9.setStyleSheet("border: 0;")
        self.s1_9.setObjectName("s1_9")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.s1_9)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.t3 = QtWidgets.QLCDNumber(self.s1_9)
        self.t3.setStyleSheet("border: 2px solid white;")
        self.t3.setObjectName("t3")
        self.verticalLayout_19.addWidget(self.t3)
        self.verticalLayout_27.addWidget(self.s1_9)
        self.s1_2 = QtWidgets.QWidget(self.sensors)
        font = QtGui.QFont()
        font.setItalic(False)
        self.s1_2.setFont(font)
        self.s1_2.setStyleSheet("border: 0;")
        self.s1_2.setObjectName("s1_2")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.s1_2)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.t4 = QtWidgets.QLCDNumber(self.s1_2)
        self.t4.setStyleSheet("border: 2px solid white;")
        self.t4.setObjectName("t4")
        self.verticalLayout_12.addWidget(self.t4)
        self.verticalLayout_27.addWidget(self.s1_2)
        self.s1_3 = QtWidgets.QWidget(self.sensors)
        font = QtGui.QFont()
        font.setItalic(False)
        self.s1_3.setFont(font)
        self.s1_3.setStyleSheet("border: 0;")
        self.s1_3.setObjectName("s1_3")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.s1_3)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.t5 = QtWidgets.QLCDNumber(self.s1_3)
        self.t5.setStyleSheet("border: 2px solid white;")
        self.t5.setObjectName("t5")
        self.verticalLayout_13.addWidget(self.t5)
        self.verticalLayout_27.addWidget(self.s1_3)
        self.s1_8 = QtWidgets.QWidget(self.sensors)
        font = QtGui.QFont()
        font.setItalic(False)
        self.s1_8.setFont(font)
        self.s1_8.setStyleSheet("border: 0;")
        self.s1_8.setObjectName("s1_8")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.s1_8)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.t6 = QtWidgets.QLCDNumber(self.s1_8)
        self.t6.setStyleSheet("border: 2px solid white;")
        self.t6.setObjectName("t6")
        self.verticalLayout_18.addWidget(self.t6)
        self.verticalLayout_27.addWidget(self.s1_8)
        self.s1_7 = QtWidgets.QWidget(self.sensors)
        font = QtGui.QFont()
        font.setItalic(False)
        self.s1_7.setFont(font)
        self.s1_7.setStyleSheet("border: 0;")
        self.s1_7.setObjectName("s1_7")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.s1_7)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.t7 = QtWidgets.QLCDNumber(self.s1_7)
        self.t7.setStyleSheet("border: 2px solid white;")
        self.t7.setObjectName("t7")
        self.verticalLayout_17.addWidget(self.t7)
        self.verticalLayout_27.addWidget(self.s1_7)
        self.s1_6 = QtWidgets.QWidget(self.sensors)
        font = QtGui.QFont()
        font.setItalic(False)
        self.s1_6.setFont(font)
        self.s1_6.setStyleSheet("border: 0;")
        self.s1_6.setObjectName("s1_6")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.s1_6)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.t8 = QtWidgets.QLCDNumber(self.s1_6)
        self.t8.setStyleSheet("border: 2px solid white;")
        self.t8.setObjectName("t8")
        self.verticalLayout_16.addWidget(self.t8)
        self.verticalLayout_27.addWidget(self.s1_6)
        self.s1_5 = QtWidgets.QWidget(self.sensors)
        font = QtGui.QFont()
        font.setItalic(False)
        self.s1_5.setFont(font)
        self.s1_5.setStyleSheet("border: 0;")
        self.s1_5.setObjectName("s1_5")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.s1_5)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.t9 = QtWidgets.QLCDNumber(self.s1_5)
        self.t9.setStyleSheet("border: 2px solid white;")
        self.t9.setObjectName("t9")
        self.verticalLayout_15.addWidget(self.t9)
        self.verticalLayout_27.addWidget(self.s1_5)
        self.s1_4 = QtWidgets.QWidget(self.sensors)
        font = QtGui.QFont()
        font.setItalic(False)
        self.s1_4.setFont(font)
        self.s1_4.setStyleSheet("border: 0;")
        self.s1_4.setObjectName("s1_4")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.s1_4)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.t10 = QtWidgets.QLCDNumber(self.s1_4)
        self.t10.setStyleSheet("border: 2px solid white;")
        self.t10.setObjectName("t10")
        self.verticalLayout_14.addWidget(self.t10)
        self.verticalLayout_27.addWidget(self.s1_4)
        self.s1_13 = QtWidgets.QWidget(self.sensors)
        font = QtGui.QFont()
        font.setItalic(False)
        self.s1_13.setFont(font)
        self.s1_13.setStyleSheet("border: 0;")
        self.s1_13.setObjectName("s1_13")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.s1_13)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.t11 = QtWidgets.QLCDNumber(self.s1_13)
        self.t11.setStyleSheet("border: 2px solid white;")
        self.t11.setObjectName("t11")
        self.verticalLayout_23.addWidget(self.t11)
        self.verticalLayout_27.addWidget(self.s1_13)
        self.s1_12 = QtWidgets.QWidget(self.sensors)
        font = QtGui.QFont()
        font.setItalic(False)
        self.s1_12.setFont(font)
        self.s1_12.setStyleSheet("border: 0;")
        self.s1_12.setObjectName("s1_12")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.s1_12)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.t12 = QtWidgets.QLCDNumber(self.s1_12)
        self.t12.setStyleSheet("border: 2px solid white;")
        self.t12.setObjectName("t12")
        self.verticalLayout_22.addWidget(self.t12)
        self.verticalLayout_27.addWidget(self.s1_12)
        self.s1_11 = QtWidgets.QWidget(self.sensors)
        font = QtGui.QFont()
        font.setItalic(False)
        self.s1_11.setFont(font)
        self.s1_11.setStyleSheet("border: 0;")
        self.s1_11.setObjectName("s1_11")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.s1_11)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.t13 = QtWidgets.QLCDNumber(self.s1_11)
        self.t13.setStyleSheet("border: 2px solid white;")
        self.t13.setObjectName("t13")
        self.verticalLayout_21.addWidget(self.t13)
        self.verticalLayout_27.addWidget(self.s1_11)
        self.s1_14 = QtWidgets.QWidget(self.sensors)
        font = QtGui.QFont()
        font.setItalic(False)
        self.s1_14.setFont(font)
        self.s1_14.setStyleSheet("border: 0;")
        self.s1_14.setObjectName("s1_14")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.s1_14)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.t14 = QtWidgets.QLCDNumber(self.s1_14)
        self.t14.setStyleSheet("border: 2px solid white;")
        self.t14.setObjectName("t14")
        self.verticalLayout_24.addWidget(self.t14)
        self.verticalLayout_27.addWidget(self.s1_14)
        self.s1_16 = QtWidgets.QWidget(self.sensors)
        font = QtGui.QFont()
        font.setItalic(False)
        self.s1_16.setFont(font)
        self.s1_16.setStyleSheet("border: 0;")
        self.s1_16.setObjectName("s1_16")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.s1_16)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.t15 = QtWidgets.QLCDNumber(self.s1_16)
        self.t15.setStyleSheet("border: 2px solid white;")
        self.t15.setObjectName("t15")
        self.verticalLayout_26.addWidget(self.t15)
        self.verticalLayout_27.addWidget(self.s1_16)
        self.s1_15 = QtWidgets.QWidget(self.sensors)
        font = QtGui.QFont()
        font.setItalic(False)
        self.s1_15.setFont(font)
        self.s1_15.setStyleSheet("border: 0;")
        self.s1_15.setObjectName("s1_15")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.s1_15)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.t16 = QtWidgets.QLCDNumber(self.s1_15)
        self.t16.setStyleSheet("border: 2px solid white;")
        self.t16.setObjectName("t16")
        self.verticalLayout_25.addWidget(self.t16)
        self.verticalLayout_27.addWidget(self.s1_15)
        self.horizontalLayout_4.addWidget(self.sensors)
        self.waterpipes = QtWidgets.QWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setItalic(False)
        self.waterpipes.setFont(font)
        self.waterpipes.setAutoFillBackground(False)
        self.waterpipes.setStyleSheet("")
        self.waterpipes.setObjectName("waterpipes")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.waterpipes)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.Nasos4 = QtWidgets.QWidget(self.waterpipes)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setItalic(False)
        self.Nasos4.setFont(font)
        self.Nasos4.setAutoFillBackground(False)
        self.Nasos4.setStyleSheet("border: 2px solid white;")
        self.Nasos4.setObjectName("Nasos4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Nasos4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lcd4 = QtWidgets.QLCDNumber(self.Nasos4)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setItalic(False)
        self.lcd4.setFont(font)
        self.lcd4.setAutoFillBackground(False)
        self.lcd4.setStyleSheet("color: rgb(255, 255, 255);")
        self.lcd4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcd4.setObjectName("lcd4")
        self.verticalLayout_3.addWidget(self.lcd4)
        self.label_2 = QtWidgets.QLabel(self.Nasos4)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(24)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px;")
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.verticalLayout_11.addWidget(self.Nasos4)
        self.Nasos3 = QtWidgets.QWidget(self.waterpipes)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setItalic(False)
        self.Nasos3.setFont(font)
        self.Nasos3.setAutoFillBackground(False)
        self.Nasos3.setStyleSheet("border: 2px solid white;")
        self.Nasos3.setObjectName("Nasos3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Nasos3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lcd3 = QtWidgets.QLCDNumber(self.Nasos3)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setItalic(False)
        self.lcd3.setFont(font)
        self.lcd3.setAutoFillBackground(False)
        self.lcd3.setStyleSheet("color: rgb(255, 255, 255);")
        self.lcd3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcd3.setObjectName("lcd3")
        self.verticalLayout_4.addWidget(self.lcd3)
        self.label_3 = QtWidgets.QLabel(self.Nasos3)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(24)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px;")
        self.label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.verticalLayout_11.addWidget(self.Nasos3)
        self.Nasos2 = QtWidgets.QWidget(self.waterpipes)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setItalic(False)
        self.Nasos2.setFont(font)
        self.Nasos2.setAutoFillBackground(False)
        self.Nasos2.setStyleSheet("border: 2px solid white;")
        self.Nasos2.setObjectName("Nasos2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.Nasos2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lcd2 = QtWidgets.QLCDNumber(self.Nasos2)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setItalic(False)
        self.lcd2.setFont(font)
        self.lcd2.setAutoFillBackground(False)
        self.lcd2.setStyleSheet("color: rgb(255, 255, 255);")
        self.lcd2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcd2.setObjectName("lcd2")
        self.verticalLayout_5.addWidget(self.lcd2)
        self.label_4 = QtWidgets.QLabel(self.Nasos2)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(24)
        font.setItalic(False)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px;")
        self.label_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.verticalLayout_11.addWidget(self.Nasos2)
        self.Nasos1 = QtWidgets.QWidget(self.waterpipes)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setItalic(False)
        self.Nasos1.setFont(font)
        self.Nasos1.setAcceptDrops(False)
        self.Nasos1.setAutoFillBackground(False)
        self.Nasos1.setStyleSheet("border: 2px solid white;")
        self.Nasos1.setObjectName("Nasos1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Nasos1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lcd1 = QtWidgets.QLCDNumber(self.Nasos1)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setItalic(False)
        self.lcd1.setFont(font)
        self.lcd1.setAutoFillBackground(False)
        self.lcd1.setStyleSheet("color: rgb(255, 255, 255);")
        self.lcd1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcd1.setObjectName("lcd1")
        self.verticalLayout_2.addWidget(self.lcd1)
        self.label_1 = QtWidgets.QLabel(self.Nasos1)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.label_1.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_1.setFont(font)
        self.label_1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_1.setAutoFillBackground(False)
        self.label_1.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px;")
        self.label_1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_1.setObjectName("label_1")
        self.verticalLayout_2.addWidget(self.label_1)
        self.verticalLayout_11.addWidget(self.Nasos1)
        self.horizontalLayout_4.addWidget(self.waterpipes)
        MainWindow.setCentralWidget(self.centralwidget)

        def translucent(widget):
            widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        for i in range(1, 9):
            eval("translucent(self.label_{})".format(i))

        self.turnOn.clicked.connect(transm.turnOn)
        self.modelOff.clicked.connect(transm.turnOff)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Reactor"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Реактор 2, </span><span style=\" font-size:22pt; vertical-align:super;\">0</span><span style=\" font-size:22pt;\">С</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Реактор 1, </span><span style=\" font-size:22pt; vertical-align:super;\">0</span><span style=\" font-size:22pt;\">С</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Энергия</p></body></html>"))
        self.turnOn.setText(_translate("MainWindow", "Включить модель"))
        self.crash1.setText(_translate("MainWindow", "Поломка 1"))
        self.crash2.setText(_translate("MainWindow", "Поломка 2"))
        self.crash3.setText(_translate("MainWindow", "Поломка N"))
        self.modelOff.setText(_translate("MainWindow", "Выключить модель"))
        self.playersOff.setText(_translate("MainWindow", "Выключить пульт игроков"))
        self.endGame.setText(_translate("MainWindow", "Завершить игру"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Датчики температуры, <span style=\" vertical-align:super;\">0</span>C</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Насос 4, %</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Насос 3, %</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Насос 2, %</p></body></html>"))
        self.label_1.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Насос 1, %</p></body></html>"))

import reactor_res_rc

def runApp():
    global exit
    exit = app.exec_()

if __name__ == "__main__":
    import sys
    transm = rpi.Transmitter()
    exit = 1
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    dataThread = Thread(target=getData, args=())
    dataThread.start()
    runApp()

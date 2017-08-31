# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reactor_kid.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

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
        icon.addPixmap(QtGui.QPixmap("../../../../Desktop/Code/Hurricane_in_glass/controls/design/Hurricane_in_glass/controls/design/img/nuke logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.menu2)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.widget_2 = QtWidgets.QWidget(self.menu2)
        self.widget_2.setStyleSheet("border: 2px solid white;")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.r1power = QtWidgets.QLCDNumber(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setItalic(False)
        self.r1power.setFont(font)
        self.r1power.setAutoFillBackground(False)
        self.r1power.setStyleSheet("color: rgb(255, 255, 255);")
        self.r1power.setFrameShadow(QtWidgets.QFrame.Plain)
        self.r1power.setProperty("value", 0.0)
        self.r1power.setObjectName("r1power")
        self.verticalLayout_10.addWidget(self.r1power)
        self.r1slider = QtWidgets.QSlider(self.widget_2)
        self.r1slider.setOrientation(QtCore.Qt.Horizontal)
        self.r1slider.setObjectName("r1slider")
        self.verticalLayout_10.addWidget(self.r1slider)
        self.label_7 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(18)
        font.setItalic(False)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px;")
        self.label_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_10.addWidget(self.label_7)
        self.verticalLayout_21.addWidget(self.widget_2)
        self.widget = QtWidgets.QWidget(self.menu2)
        self.widget.setStyleSheet("border: 2px solid white;")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.r2power = QtWidgets.QLCDNumber(self.widget)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setItalic(False)
        self.r2power.setFont(font)
        self.r2power.setAutoFillBackground(False)
        self.r2power.setStyleSheet("color: rgb(255, 255, 255);")
        self.r2power.setFrameShadow(QtWidgets.QFrame.Plain)
        self.r2power.setObjectName("r2power")
        self.verticalLayout.addWidget(self.r2power)
        self.r2slider = QtWidgets.QSlider(self.widget)
        self.r2slider.setOrientation(QtCore.Qt.Horizontal)
        self.r2slider.setObjectName("r2slider")
        self.verticalLayout.addWidget(self.r2slider)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(18)
        font.setItalic(False)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px;")
        self.label_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.verticalLayout_21.addWidget(self.widget)
        self.widget_3 = QtWidgets.QWidget(self.menu2)
        self.widget_3.setStyleSheet("border: 2px solid white;")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.cpower = QtWidgets.QLCDNumber(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setItalic(False)
        self.cpower.setFont(font)
        self.cpower.setAutoFillBackground(False)
        self.cpower.setStyleSheet("color: rgb(255, 255, 255);")
        self.cpower.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cpower.setObjectName("cpower")
        self.verticalLayout_9.addWidget(self.cpower)
        self.cslider = QtWidgets.QSlider(self.widget_3)
        self.cslider.setMaximum(120)
        self.cslider.setOrientation(QtCore.Qt.Horizontal)
        self.cslider.setObjectName("cslider")
        self.verticalLayout_9.addWidget(self.cslider)
        self.label_10 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(18)
        font.setItalic(False)
        self.label_10.setFont(font)
        self.label_10.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_10.setAutoFillBackground(False)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px;")
        self.label_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_9.addWidget(self.label_10)
        self.verticalLayout_21.addWidget(self.widget_3)
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
        font.setFamily("Sans Serif")
        font.setPointSize(18)
        font.setItalic(False)
        self.label_6.setFont(font)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255); border: 0;")
        self.label_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_8.addWidget(self.label_6)
        self.verticalLayout_21.addWidget(self.widget_4)
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
        self.label = QtWidgets.QLabel(self.w)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(18)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;")
        self.label.setObjectName("label")
        self.verticalLayout_28.addWidget(self.label)
        self.verticalLayout_27.addWidget(self.w)
        self.s1 = QtWidgets.QWidget(self.sensors)
        font = QtGui.QFont()
        font.setItalic(False)
        self.s1.setFont(font)
        self.s1.setStyleSheet("border: 0;")
        self.s1.setObjectName("s1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.s1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.t1 = QtWidgets.QLCDNumber(self.s1)
        self.t1.setStyleSheet("border: 2px solid white; color: white;")
        self.t1.setDigitCount(10)
        self.t1.setObjectName("t1")
        self.horizontalLayout.addWidget(self.t1)
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
        self.t2.setStyleSheet("border: 2px solid white; color: white;")
        self.t2.setDigitCount(10)
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
        self.t3.setStyleSheet("border: 2px solid white; color: white;")
        self.t3.setDigitCount(10)
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
        self.t4.setStyleSheet("border: 2px solid white; color: white;")
        self.t4.setDigitCount(10)
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
        self.t5.setStyleSheet("border: 2px solid white; color: white;")
        self.t5.setDigitCount(10)
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
        self.t6.setStyleSheet("border: 2px solid white; color: white;")
        self.t6.setDigitCount(10)
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
        self.t7.setStyleSheet("border: 2px solid white; color: white;")
        self.t7.setDigitCount(10)
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
        self.t8.setStyleSheet("border: 2px solid white; color: white;")
        self.t8.setDigitCount(10)
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
        self.t9.setStyleSheet("border: 2px solid white; color: white;")
        self.t9.setDigitCount(10)
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
        self.t10.setStyleSheet("border: 2px solid white; color: white;")
        self.t10.setDigitCount(10)
        self.t10.setObjectName("t10")
        self.verticalLayout_14.addWidget(self.t10)
        self.verticalLayout_27.addWidget(self.s1_4)
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
        self.n1slider = QtWidgets.QSlider(self.Nasos1)
        self.n1slider.setOrientation(QtCore.Qt.Horizontal)
        self.n1slider.setObjectName("n1slider")
        self.verticalLayout_2.addWidget(self.n1slider)
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
        font.setFamily("Sans Serif")
        font.setPointSize(18)
        font.setItalic(False)
        self.label_1.setFont(font)
        self.label_1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_1.setAutoFillBackground(False)
        self.label_1.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px;")
        self.label_1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_1.setObjectName("label_1")
        self.verticalLayout_2.addWidget(self.label_1)
        self.verticalLayout_11.addWidget(self.Nasos1)
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
        self.n2slider = QtWidgets.QSlider(self.Nasos2)
        self.n2slider.setOrientation(QtCore.Qt.Horizontal)
        self.n2slider.setObjectName("n2slider")
        self.verticalLayout_5.addWidget(self.n2slider)
        self.label_4 = QtWidgets.QLabel(self.Nasos2)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(18)
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
        self.n3slider = QtWidgets.QSlider(self.Nasos3)
        self.n3slider.setOrientation(QtCore.Qt.Horizontal)
        self.n3slider.setObjectName("n3slider")
        self.verticalLayout_4.addWidget(self.n3slider)
        self.label_3 = QtWidgets.QLabel(self.Nasos3)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(18)
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
        self.n4slider = QtWidgets.QSlider(self.Nasos4)
        self.n4slider.setOrientation(QtCore.Qt.Horizontal)
        self.n4slider.setObjectName("n4slider")
        self.verticalLayout_3.addWidget(self.n4slider)
        self.label_2 = QtWidgets.QLabel(self.Nasos4)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(18)
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
        self.Nasos4_2 = QtWidgets.QWidget(self.waterpipes)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setItalic(False)
        self.Nasos4_2.setFont(font)
        self.Nasos4_2.setAutoFillBackground(False)
        self.Nasos4_2.setStyleSheet("border: 2px solid white;")
        self.Nasos4_2.setObjectName("Nasos4_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.Nasos4_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lcd5 = QtWidgets.QLCDNumber(self.Nasos4_2)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setItalic(False)
        self.lcd5.setFont(font)
        self.lcd5.setAutoFillBackground(False)
        self.lcd5.setStyleSheet("color: rgb(255, 255, 255);")
        self.lcd5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcd5.setObjectName("lcd5")
        self.verticalLayout_6.addWidget(self.lcd5)
        self.n5slider = QtWidgets.QSlider(self.Nasos4_2)
        self.n5slider.setOrientation(QtCore.Qt.Horizontal)
        self.n5slider.setObjectName("n5slider")
        self.verticalLayout_6.addWidget(self.n5slider)
        self.label_8 = QtWidgets.QLabel(self.Nasos4_2)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(18)
        font.setItalic(False)
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_8.setAutoFillBackground(False)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px;")
        self.label_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_6.addWidget(self.label_8)
        self.verticalLayout_11.addWidget(self.Nasos4_2)
        self.Nasos4_3 = QtWidgets.QWidget(self.waterpipes)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setItalic(False)
        self.Nasos4_3.setFont(font)
        self.Nasos4_3.setAutoFillBackground(False)
        self.Nasos4_3.setStyleSheet("border: 2px solid white;")
        self.Nasos4_3.setObjectName("Nasos4_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.Nasos4_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lcd6 = QtWidgets.QLCDNumber(self.Nasos4_3)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setItalic(False)
        self.lcd6.setFont(font)
        self.lcd6.setAutoFillBackground(False)
        self.lcd6.setStyleSheet("color: rgb(255, 255, 255);")
        self.lcd6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcd6.setObjectName("lcd6")
        self.verticalLayout_7.addWidget(self.lcd6)
        self.n6slider = QtWidgets.QSlider(self.Nasos4_3)
        self.n6slider.setOrientation(QtCore.Qt.Horizontal)
        self.n6slider.setObjectName("n6slider")
        self.verticalLayout_7.addWidget(self.n6slider)
        self.label_9 = QtWidgets.QLabel(self.Nasos4_3)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(18)
        font.setItalic(False)
        self.label_9.setFont(font)
        self.label_9.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_9.setAutoFillBackground(False)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px;")
        self.label_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_7.addWidget(self.label_9)
        self.verticalLayout_11.addWidget(self.Nasos4_3)
        self.horizontalLayout_4.addWidget(self.waterpipes)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Reactor"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Мощность</p><p align=\"center\">Реактор 1, %</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Мощность</p><p align=\"center\">Реактор 2, %</p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Температура тревоги, <span style=\" vertical-align:super;\">0</span>С</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Энергия</p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Датчики температуры, <span style=\" vertical-align:super;\">0</span>C</p></body></html>"))
        self.label_1.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Насос 1, %</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Насос 2, %</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Насос 3, %</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Насос 4, %</p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Насос 5, %</p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Насос 6, %</p></body></html>"))

import reactor_res_rc

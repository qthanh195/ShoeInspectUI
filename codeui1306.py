# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui1306.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1467, 820)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 0, 371, 641))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(u"QTabWidget::pane {\n"
"    border: 1px solid #3498db;\n"
"    border-radius:3px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: #ecf0f1;\n"
"    border: 1px solid #3498db;\n"
"    padding: 10px;\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    min-width: 60px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #3498db;\n"
"    color: white;\n"
"    margin-bottom: -1px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px;\n"
"}")
        self.tabWidget.setMovable(True)
        self.tabInspection = QWidget()
        self.tabInspection.setObjectName(u"tabInspection")
        self.widget_2 = QWidget(self.tabInspection)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 0, 351, 331))
        self.widget_2.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.cbb_NameSm = QComboBox(self.widget_2)
        self.cbb_NameSm.setObjectName(u"cbb_NameSm")
        font1 = QFont()
        font1.setBold(True)
        self.cbb_NameSm.setFont(font1)
        self.cbb_NameSm.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #3498db;\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"    font-size: 16px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border-left: 1px solid #3498db;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/down_arrow.png); /* Replace with your icon */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #3498db;\n"
"    selection-background-color: #3498db;\n"
"    selection-color: white;\n"
"}")

        self.verticalLayout.addWidget(self.cbb_NameSm)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #2980b9;\n"
"}")

        self.horizontalLayout.addWidget(self.label_4)

        self.lb_InWidthSample = QLabel(self.widget_2)
        self.lb_InWidthSample.setObjectName(u"lb_InWidthSample")
        self.lb_InWidthSample.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #2980b9;\n"
"}")

        self.horizontalLayout.addWidget(self.lb_InWidthSample)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #2980b9;\n"
"}")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.lb_IHeightSample = QLabel(self.widget_2)
        self.lb_IHeightSample.setObjectName(u"lb_IHeightSample")
        self.lb_IHeightSample.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #2980b9;\n"
"}")

        self.horizontalLayout_2.addWidget(self.lb_IHeightSample)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #2980b9;\n"
"}")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.lb_InWidthDeviation = QLabel(self.widget_2)
        self.lb_InWidthDeviation.setObjectName(u"lb_InWidthDeviation")
        self.lb_InWidthDeviation.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #2980b9;\n"
"}")

        self.horizontalLayout_3.addWidget(self.lb_InWidthDeviation)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #2980b9;\n"
"}")

        self.horizontalLayout_4.addWidget(self.label_7)

        self.lb_InHeightDeviation = QLabel(self.widget_2)
        self.lb_InHeightDeviation.setObjectName(u"lb_InHeightDeviation")
        self.lb_InHeightDeviation.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #2980b9;\n"
"}")

        self.horizontalLayout_4.addWidget(self.lb_InHeightDeviation)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_19 = QLabel(self.widget_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #2980b9;\n"
"}")

        self.horizontalLayout_5.addWidget(self.label_19)

        self.lb_InAccuracySample = QLabel(self.widget_2)
        self.lb_InAccuracySample.setObjectName(u"lb_InAccuracySample")
        self.lb_InAccuracySample.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #2980b9;\n"
"}")

        self.horizontalLayout_5.addWidget(self.lb_InAccuracySample)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.bt_Start = QPushButton(self.widget_2)
        self.bt_Start.setObjectName(u"bt_Start")
        self.bt_Start.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"    transition-duration: 0.4s;\n"
"    cursor: pointer;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"    transform: translateY(2px);\n"
"}")

        self.verticalLayout.addWidget(self.bt_Start)

        self.bt_InLog = QPushButton(self.widget_2)
        self.bt_InLog.setObjectName(u"bt_InLog")
        self.bt_InLog.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"    transition-duration: 0.4s;\n"
"    cursor: pointer;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"    transform: translateY(2px);\n"
"}")

        self.verticalLayout.addWidget(self.bt_InLog)

        self.widget_3 = QWidget(self.tabInspection)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(0, 340, 351, 181))
        self.widget_3.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_8 = QLabel(self.widget_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #2980b9;\n"
"}")

        self.horizontalLayout_6.addWidget(self.label_8)

        self.lb_InWidthcur = QLabel(self.widget_3)
        self.lb_InWidthcur.setObjectName(u"lb_InWidthcur")
        self.lb_InWidthcur.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #2980b9;\n"
"}")

        self.horizontalLayout_6.addWidget(self.lb_InWidthcur)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_9 = QLabel(self.widget_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #2980b9;\n"
"}")

        self.horizontalLayout_7.addWidget(self.label_9)

        self.lb_InHeightcur = QLabel(self.widget_3)
        self.lb_InHeightcur.setObjectName(u"lb_InHeightcur")
        self.lb_InHeightcur.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #2980b9;\n"
"}")

        self.horizontalLayout_7.addWidget(self.lb_InHeightcur)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_10 = QLabel(self.widget_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #2980b9;\n"
"}")

        self.horizontalLayout_8.addWidget(self.label_10)

        self.lb_Accuracy = QLabel(self.widget_3)
        self.lb_Accuracy.setObjectName(u"lb_Accuracy")
        self.lb_Accuracy.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #2980b9;\n"
"}")

        self.horizontalLayout_8.addWidget(self.lb_Accuracy)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.lb_okng = QLabel(self.widget_3)
        self.lb_okng.setObjectName(u"lb_okng")
        self.lb_okng.setFont(font1)
        self.lb_okng.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;\n"
"	color: rgb(50, 255, 35);\n"
"    font-size: 30px;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #2980b9;\n"
"}")

        self.verticalLayout_2.addWidget(self.lb_okng)

        self.tabWidget.addTab(self.tabInspection, "")
        self.tabAdd = QWidget()
        self.tabAdd.setObjectName(u"tabAdd")
        self.widget_6 = QWidget(self.tabAdd)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(0, 0, 351, 351))
        self.widget_6.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.widget_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.le_SampleName = QLineEdit(self.widget_6)
        self.le_SampleName.setObjectName(u"le_SampleName")
        self.le_SampleName.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #3498db;\n"
"    border-radius: 6px;\n"
"    padding: 8px;\n"
"    font-size: 16px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2980b9;\n"
"    background-color: #ffffff;\n"
"}")

        self.verticalLayout_3.addWidget(self.le_SampleName)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_14 = QLabel(self.widget_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #2980b9;\n"
"}")

        self.horizontalLayout_14.addWidget(self.label_14)

        self.le_AdWidth = QLineEdit(self.widget_6)
        self.le_AdWidth.setObjectName(u"le_AdWidth")
        self.le_AdWidth.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #3498db;\n"
"    border-radius: 6px;\n"
"    font-size: 16px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2980b9;\n"
"    background-color: #ffffff;\n"
"}")

        self.horizontalLayout_14.addWidget(self.le_AdWidth)


        self.verticalLayout_3.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_15 = QLabel(self.widget_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #2980b9;\n"
"}")

        self.horizontalLayout_13.addWidget(self.label_15)

        self.le_AdHeight = QLineEdit(self.widget_6)
        self.le_AdHeight.setObjectName(u"le_AdHeight")
        self.le_AdHeight.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #3498db;\n"
"    border-radius: 6px;\n"
"    font-size: 16px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2980b9;\n"
"    background-color: #ffffff;\n"
"}")

        self.horizontalLayout_13.addWidget(self.le_AdHeight)


        self.verticalLayout_3.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_16 = QLabel(self.widget_6)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #2980b9;\n"
"}")

        self.horizontalLayout_12.addWidget(self.label_16)

        self.le_AdWidthDeviation = QLineEdit(self.widget_6)
        self.le_AdWidthDeviation.setObjectName(u"le_AdWidthDeviation")
        self.le_AdWidthDeviation.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #3498db;\n"
"    border-radius: 6px;\n"
"    font-size: 16px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2980b9;\n"
"    background-color: #ffffff;\n"
"}")

        self.horizontalLayout_12.addWidget(self.le_AdWidthDeviation)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_17 = QLabel(self.widget_6)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #2980b9;\n"
"}")

        self.horizontalLayout_11.addWidget(self.label_17)

        self.le_AdHeightDeviation = QLineEdit(self.widget_6)
        self.le_AdHeightDeviation.setObjectName(u"le_AdHeightDeviation")
        self.le_AdHeightDeviation.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #3498db;\n"
"    border-radius: 6px;\n"
"    font-size: 16px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2980b9;\n"
"    background-color: #ffffff;\n"
"}")

        self.horizontalLayout_11.addWidget(self.le_AdHeightDeviation)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_18 = QLabel(self.widget_6)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #2980b9;\n"
"}")

        self.horizontalLayout_10.addWidget(self.label_18)

        self.le_AdAccuracySample = QLineEdit(self.widget_6)
        self.le_AdAccuracySample.setObjectName(u"le_AdAccuracySample")
        self.le_AdAccuracySample.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #3498db;\n"
"    border-radius: 6px;\n"
"    font-size: 16px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2980b9;\n"
"    background-color: #ffffff;\n"
"}")

        self.horizontalLayout_10.addWidget(self.le_AdAccuracySample)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.bt_Save = QPushButton(self.widget_6)
        self.bt_Save.setObjectName(u"bt_Save")
        self.bt_Save.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"    transition-duration: 0.4s;\n"
"    cursor: pointer;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"    transform: translateY(2px);\n"
"}")

        self.verticalLayout_3.addWidget(self.bt_Save)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.cbb_AdSampleName = QComboBox(self.widget_6)
        self.cbb_AdSampleName.setObjectName(u"cbb_AdSampleName")
        self.cbb_AdSampleName.setFont(font1)
        self.cbb_AdSampleName.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #3498db;\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"    font-size: 16px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border-left: 1px solid #3498db;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/down_arrow.png); /* Replace with your icon */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #3498db;\n"
"    selection-background-color: #3498db;\n"
"    selection-color: white;\n"
"}")

        self.horizontalLayout_9.addWidget(self.cbb_AdSampleName)

        self.bt_Delete = QPushButton(self.widget_6)
        self.bt_Delete.setObjectName(u"bt_Delete")
        self.bt_Delete.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"    transition-duration: 0.4s;\n"
"    cursor: pointer;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"    transform: translateY(2px);\n"
"}")

        self.horizontalLayout_9.addWidget(self.bt_Delete)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.tabWidget.addTab(self.tabAdd, "")
        self.tabRobot = QWidget()
        self.tabRobot.setObjectName(u"tabRobot")
        self.verticalLayout_6 = QVBoxLayout(self.tabRobot)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_4 = QWidget(self.tabRobot)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_4 = QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.le_ip = QLineEdit(self.widget_4)
        self.le_ip.setObjectName(u"le_ip")
        self.le_ip.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #3498db;\n"
"    border-radius:6px;\n"
"    padding: 8px;\n"
"    font-size: 16px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2980b9;\n"
"    background-color: #ffffff;\n"
"}")

        self.verticalLayout_4.addWidget(self.le_ip)

        self.bt_Connect = QPushButton(self.widget_4)
        self.bt_Connect.setObjectName(u"bt_Connect")
        self.bt_Connect.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"    transition-duration: 0.4s;\n"
"    cursor: pointer;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"    transform: translateY(2px);\n"
"}")

        self.verticalLayout_4.addWidget(self.bt_Connect)

        self.bt_Home = QPushButton(self.widget_4)
        self.bt_Home.setObjectName(u"bt_Home")
        self.bt_Home.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"    transition-duration: 0.4s;\n"
"    cursor: pointer;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"    transform: translateY(2px);\n"
"}")

        self.verticalLayout_4.addWidget(self.bt_Home)

        self.le_IO = QLineEdit(self.widget_4)
        self.le_IO.setObjectName(u"le_IO")
        self.le_IO.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #3498db;\n"
"    border-radius: 6px;\n"
"    padding: 8px;\n"
"    font-size: 16px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2980b9;\n"
"    background-color: #ffffff;\n"
"}")

        self.verticalLayout_4.addWidget(self.le_IO)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.bt_Setio = QPushButton(self.widget_4)
        self.bt_Setio.setObjectName(u"bt_Setio")
        self.bt_Setio.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"    transition-duration: 0.4s;\n"
"    cursor: pointer;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"    transform: translateY(2px);\n"
"}")

        self.horizontalLayout_15.addWidget(self.bt_Setio)

        self.bt_Resetio = QPushButton(self.widget_4)
        self.bt_Resetio.setObjectName(u"bt_Resetio")
        self.bt_Resetio.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"    transition-duration: 0.4s;\n"
"    cursor: pointer;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"    transform: translateY(2px);\n"
"}")

        self.horizontalLayout_15.addWidget(self.bt_Resetio)


        self.verticalLayout_4.addLayout(self.horizontalLayout_15)

        self.cbb_Dir = QComboBox(self.widget_4)
        self.cbb_Dir.addItem("")
        self.cbb_Dir.addItem("")
        self.cbb_Dir.setObjectName(u"cbb_Dir")
        self.cbb_Dir.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #3498db;\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"    font-size: 16px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border-left: 1px solid #3498db;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/down_arrow.png); /* Replace with your icon */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #3498db;\n"
"    selection-background-color: #3498db;\n"
"    selection-color: white;\n"
"}")

        self.verticalLayout_4.addWidget(self.cbb_Dir)

        self.bt_Run = QPushButton(self.widget_4)
        self.bt_Run.setObjectName(u"bt_Run")
        self.bt_Run.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"    transition-duration: 0.4s;\n"
"    cursor: pointer;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"    transform: translateY(2px);\n"
"}")

        self.verticalLayout_4.addWidget(self.bt_Run)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.bt_Pause = QPushButton(self.widget_4)
        self.bt_Pause.setObjectName(u"bt_Pause")
        self.bt_Pause.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"    transition-duration: 0.4s;\n"
"    cursor: pointer;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"    transform: translateY(2px);\n"
"}")

        self.horizontalLayout_16.addWidget(self.bt_Pause)

        self.bt_Stop = QPushButton(self.widget_4)
        self.bt_Stop.setObjectName(u"bt_Stop")
        self.bt_Stop.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"    transition-duration: 0.4s;\n"
"    cursor: pointer;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"    transform: translateY(2px);\n"
"}")

        self.horizontalLayout_16.addWidget(self.bt_Stop)


        self.verticalLayout_4.addLayout(self.horizontalLayout_16)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.verticalLayout_6.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.tabRobot)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_5 = QVBoxLayout(self.widget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_11 = QLabel(self.widget_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #2980b9;\n"
"}")

        self.horizontalLayout_17.addWidget(self.label_11)

        self.lb_RoWidth = QLabel(self.widget_5)
        self.lb_RoWidth.setObjectName(u"lb_RoWidth")
        self.lb_RoWidth.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #2980b9;\n"
"}")

        self.horizontalLayout_17.addWidget(self.lb_RoWidth)


        self.verticalLayout_5.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_12 = QLabel(self.widget_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #2980b9;\n"
"}")

        self.horizontalLayout_18.addWidget(self.label_12)

        self.lb_RoHeight = QLabel(self.widget_5)
        self.lb_RoHeight.setObjectName(u"lb_RoHeight")
        self.lb_RoHeight.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #2980b9;\n"
"}")

        self.horizontalLayout_18.addWidget(self.lb_RoHeight)


        self.verticalLayout_5.addLayout(self.horizontalLayout_18)


        self.verticalLayout_6.addWidget(self.widget_5)

        self.tabWidget.addTab(self.tabRobot, "")
        self.tabCalib = QWidget()
        self.tabCalib.setObjectName(u"tabCalib")
        self.widget_10 = QWidget(self.tabCalib)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setGeometry(QRect(0, 0, 351, 151))
        self.verticalLayout_8 = QVBoxLayout(self.widget_10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_30 = QLabel(self.widget_10)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"QLabel {\n"
"	border: none;\n"
"    color: #2c3e50;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #2980b9;\n"
"}")

        self.horizontalLayout_26.addWidget(self.label_30)

        self.sp_CalibCenterX = QSpinBox(self.widget_10)
        self.sp_CalibCenterX.setObjectName(u"sp_CalibCenterX")
        self.sp_CalibCenterX.setStyleSheet(u"QSpinBox {\n"
"    border: 1px solid #3498db;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"    font-size: 16px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QSpinBox::drop-down {\n"
"    border-left: 1px solid #3498db;\n"
"}")
        self.sp_CalibCenterX.setMaximum(3350)
        self.sp_CalibCenterX.setValue(1650)

        self.horizontalLayout_26.addWidget(self.sp_CalibCenterX)


        self.verticalLayout_8.addLayout(self.horizontalLayout_26)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_22 = QLabel(self.widget_10)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"QLabel {\n"
"	border: none;\n"
"    color: #2c3e50;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #2980b9;\n"
"}")

        self.horizontalLayout_27.addWidget(self.label_22)

        self.sp_CalibCenterY = QSpinBox(self.widget_10)
        self.sp_CalibCenterY.setObjectName(u"sp_CalibCenterY")
        self.sp_CalibCenterY.setStyleSheet(u"QSpinBox {\n"
"    border: 1px solid #3498db;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"    font-size: 16px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QSpinBox::drop-down {\n"
"    border-left: 1px solid #3498db;\n"
"}")
        self.sp_CalibCenterY.setMaximum(2310)
        self.sp_CalibCenterY.setValue(1032)

        self.horizontalLayout_27.addWidget(self.sp_CalibCenterY)


        self.verticalLayout_7.addLayout(self.horizontalLayout_27)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_29 = QLabel(self.widget_10)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #2980b9;\n"
"}")

        self.horizontalLayout_20.addWidget(self.label_29)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer)

        self.le_Anglerobot = QLineEdit(self.widget_10)
        self.le_Anglerobot.setObjectName(u"le_Anglerobot")
        self.le_Anglerobot.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #3498db;\n"
"    border-radius: 6px;\n"
"	padding:3px;\n"
"    font-size: 16px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2980b9;\n"
"    background-color: #ffffff;\n"
"}")

        self.horizontalLayout_20.addWidget(self.le_Anglerobot)


        self.verticalLayout_8.addLayout(self.horizontalLayout_20)

        self.checkBox_EnDrawLine = QCheckBox(self.widget_10)
        self.checkBox_EnDrawLine.setObjectName(u"checkBox_EnDrawLine")
        self.checkBox_EnDrawLine.setStyleSheet(u"QCheckBox {\n"
"    spacing: 5px;\n"
"    font-size: 16px;\n"
"    color: #2c3e50;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border: 1px solid #3498db;\n"
"    background-color: #ecf0f1;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 1px solid #2980b9;\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"    border: 1px solid #2980b9;\n"
"    background-color: #d0d0d0;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 1px solid #3498db;\n"
"    background-color: #3498db;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    border: 1px solid #2980b9;\n"
"    background-color: #2980b9;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:pressed {\n"
"    border: 1px solid #2980b9;\n"
"    background-color: #1c639e;\n"
"}\n"
"")

        self.verticalLayout_8.addWidget(self.checkBox_EnDrawLine)

        self.tabWidget_2 = QTabWidget(self.tabCalib)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(0, 160, 341, 261))
        self.tabWidget_2.setStyleSheet(u"QTabWidget::pane {\n"
"    border: 1px solid #3498db;\n"
"    border-radius:2px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: #ecf0f1;\n"
"    border: 1px solid #3498db;\n"
"    padding: 5px;\n"
"    border-top-left-radius: 2px;\n"
"    border-top-right-radius: 2px;\n"
"    min-width:20px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #3498db;\n"
"    color: white;\n"
"    margin-bottom: -1px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px;\n"
"}")
        self.tabWidget_2.setMovable(True)
        self.Frame = QWidget()
        self.Frame.setObjectName(u"Frame")
        self.widget_8 = QWidget(self.Frame)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(0, 0, 321, 161))
        self.verticalLayout_9 = QVBoxLayout(self.widget_8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_23 = QLabel(self.widget_8)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #2980b9;\n"
"}")

        self.horizontalLayout_21.addWidget(self.label_23)

        self.sp_widthframe = QSpinBox(self.widget_8)
        self.sp_widthframe.setObjectName(u"sp_widthframe")
        self.sp_widthframe.setStyleSheet(u"QSpinBox {\n"
"    border: 1px solid #3498db;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"    font-size: 16px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QSpinBox::drop-down {\n"
"    border-left: 1px solid #3498db;\n"
"}")
        self.sp_widthframe.setMaximum(490)
        self.sp_widthframe.setValue(300)

        self.horizontalLayout_21.addWidget(self.sp_widthframe)


        self.verticalLayout_9.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_24 = QLabel(self.widget_8)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #2980b9;\n"
"}")

        self.horizontalLayout_22.addWidget(self.label_24)

        self.sp_heightframe = QSpinBox(self.widget_8)
        self.sp_heightframe.setObjectName(u"sp_heightframe")
        self.sp_heightframe.setStyleSheet(u"QSpinBox {\n"
"    border: 1px solid #3498db;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"    font-size: 16px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QSpinBox::drop-down {\n"
"    border-left: 1px solid #3498db;\n"
"}")
        self.sp_heightframe.setMaximum(438)
        self.sp_heightframe.setValue(50)

        self.horizontalLayout_22.addWidget(self.sp_heightframe)


        self.verticalLayout_9.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_25 = QLabel(self.widget_8)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #2980b9;\n"
"}")

        self.horizontalLayout_23.addWidget(self.label_25)

        self.sp_rotate = QDoubleSpinBox(self.widget_8)
        self.sp_rotate.setObjectName(u"sp_rotate")
        self.sp_rotate.setStyleSheet(u"QDoubleSpinBox {\n"
"    border: 1px solid #3498db;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"    font-size: 16px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QDoubleSpinBox::drop-down {\n"
"    border-left: 1px solid #3498db;\n"
"}")
        self.sp_rotate.setMinimum(-180.000000000000000)
        self.sp_rotate.setMaximum(180.000000000000000)
        self.sp_rotate.setSingleStep(0.010000000000000)

        self.horizontalLayout_23.addWidget(self.sp_rotate)


        self.verticalLayout_9.addLayout(self.horizontalLayout_23)

        self.tabWidget_2.addTab(self.Frame, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.widget_13 = QWidget(self.tab_2)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setGeometry(QRect(0, 0, 321, 221))
        self.verticalLayout_12 = QVBoxLayout(self.widget_13)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.le_point1 = QLineEdit(self.widget_13)
        self.le_point1.setObjectName(u"le_point1")
        self.le_point1.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #3498db;\n"
"    border-radius: 6px;\n"
"	padding:3px;\n"
"    font-size: 16px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2980b9;\n"
"    background-color: #ffffff;\n"
"}")

        self.horizontalLayout_31.addWidget(self.le_point1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_2)

        self.bt_point1 = QPushButton(self.widget_13)
        self.bt_point1.setObjectName(u"bt_point1")
        self.bt_point1.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 7px 14px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"    transition-duration: 0.4s;\n"
"    cursor: pointer;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"    transform: translateY(2px);\n"
"}")

        self.horizontalLayout_31.addWidget(self.bt_point1)


        self.verticalLayout_12.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.le_point2 = QLineEdit(self.widget_13)
        self.le_point2.setObjectName(u"le_point2")
        self.le_point2.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #3498db;\n"
"    border-radius: 6px;\n"
"	padding:3px;\n"
"    font-size: 16px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2980b9;\n"
"    background-color: #ffffff;\n"
"}")

        self.horizontalLayout_30.addWidget(self.le_point2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_3)

        self.bt_point2 = QPushButton(self.widget_13)
        self.bt_point2.setObjectName(u"bt_point2")
        self.bt_point2.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 7px 14px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"    transition-duration: 0.4s;\n"
"    cursor: pointer;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"    transform: translateY(2px);\n"
"}")

        self.horizontalLayout_30.addWidget(self.bt_point2)


        self.verticalLayout_12.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_28 = QLabel(self.widget_13)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #2980b9;\n"
"}")

        self.horizontalLayout_19.addWidget(self.label_28)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_4)

        self.le_Zrobot = QLineEdit(self.widget_13)
        self.le_Zrobot.setObjectName(u"le_Zrobot")
        self.le_Zrobot.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #3498db;\n"
"    border-radius: 6px;\n"
"	padding:3px;\n"
"    font-size: 16px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2980b9;\n"
"    background-color: #ffffff;\n"
"}")

        self.horizontalLayout_19.addWidget(self.le_Zrobot)


        self.verticalLayout_12.addLayout(self.horizontalLayout_19)

        self.bt_confirmcenter = QPushButton(self.widget_13)
        self.bt_confirmcenter.setObjectName(u"bt_confirmcenter")
        self.bt_confirmcenter.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 7px 14px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"    transition-duration: 0.4s;\n"
"    cursor: pointer;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"    transform: translateY(2px);\n"
"}")

        self.verticalLayout_12.addWidget(self.bt_confirmcenter)

        self.tabWidget_2.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.widget_14 = QWidget(self.tab)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setGeometry(QRect(0, 0, 321, 221))
        self.verticalLayout_13 = QVBoxLayout(self.widget_14)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_26 = QLabel(self.widget_14)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #2980b9;\n"
"}")

        self.horizontalLayout_24.addWidget(self.label_26)

        self.sp_exposureTime = QSpinBox(self.widget_14)
        self.sp_exposureTime.setObjectName(u"sp_exposureTime")
        self.sp_exposureTime.setStyleSheet(u"QSpinBox {\n"
"    border: 1px solid #3498db;\n"
"    border-radius: 6px;\n"
"    padding: 3px;\n"
"    font-size: 16px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QSpinBox::drop-down {\n"
"    border-left: 1px solid #3498db;\n"
"}")
        self.sp_exposureTime.setMaximum(1600000)
        self.sp_exposureTime.setSingleStep(10)
        self.sp_exposureTime.setValue(35000)

        self.horizontalLayout_24.addWidget(self.sp_exposureTime)


        self.verticalLayout_13.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_27 = QLabel(self.widget_14)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #2980b9;\n"
"}")

        self.horizontalLayout_25.addWidget(self.label_27)

        self.sp_threshold = QSpinBox(self.widget_14)
        self.sp_threshold.setObjectName(u"sp_threshold")
        self.sp_threshold.setStyleSheet(u"QSpinBox {\n"
"    border: 1px solid #3498db;\n"
"    border-radius: 6px;\n"
"    padding: 3px;\n"
"    font-size: 16px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QSpinBox::drop-down {\n"
"    border-left: 1px solid #3498db;\n"
"}")
        self.sp_threshold.setMaximum(250)
        self.sp_threshold.setValue(220)

        self.horizontalLayout_25.addWidget(self.sp_threshold)


        self.verticalLayout_13.addLayout(self.horizontalLayout_25)

        self.label_31 = QLabel(self.widget_14)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;\n"
"    font-size: 16px;\n"
"	padding: 3px;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #2980b9;\n"
"}")

        self.verticalLayout_13.addWidget(self.label_31)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.cbb_bblur = QComboBox(self.widget_14)
        self.cbb_bblur.addItem("")
        self.cbb_bblur.addItem("")
        self.cbb_bblur.addItem("")
        self.cbb_bblur.setObjectName(u"cbb_bblur")
        self.cbb_bblur.setFont(font1)
        self.cbb_bblur.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #3498db;\n"
"    border-radius: 8px;\n"
"    padding: 3px;\n"
"    font-size: 16px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border-left: 1px solid #3498db;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/down_arrow.png); /* Replace with your icon */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #3498db;\n"
"    selection-background-color: #3498db;\n"
"    selection-color: white;\n"
"}")

        self.horizontalLayout_29.addWidget(self.cbb_bblur)

        self.cbb_ablur = QComboBox(self.widget_14)
        self.cbb_ablur.addItem("")
        self.cbb_ablur.addItem("")
        self.cbb_ablur.addItem("")
        self.cbb_ablur.setObjectName(u"cbb_ablur")
        self.cbb_ablur.setFont(font1)
        self.cbb_ablur.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #3498db;\n"
"    border-radius: 8px;\n"
"    padding: 3px;\n"
"    font-size: 16px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border-left: 1px solid #3498db;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/down_arrow.png); /* Replace with your icon */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #3498db;\n"
"    selection-background-color: #3498db;\n"
"    selection-color: white;\n"
"}")

        self.horizontalLayout_29.addWidget(self.cbb_ablur)


        self.verticalLayout_13.addLayout(self.horizontalLayout_29)

        self.bt_AutoAdjust = QPushButton(self.widget_14)
        self.bt_AutoAdjust.setObjectName(u"bt_AutoAdjust")
        self.bt_AutoAdjust.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 7px 14px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"    transition-duration: 0.4s;\n"
"    cursor: pointer;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"    transform: translateY(2px);\n"
"}")

        self.verticalLayout_13.addWidget(self.bt_AutoAdjust)

        self.tabWidget_2.addTab(self.tab, "")
        self.widget_11 = QWidget(self.tabCalib)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setGeometry(QRect(0, 430, 351, 101))
        self.verticalLayout_10 = QVBoxLayout(self.widget_11)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.cbb_ConfigName = QComboBox(self.widget_11)
        self.cbb_ConfigName.setObjectName(u"cbb_ConfigName")
        self.cbb_ConfigName.setFont(font1)
        self.cbb_ConfigName.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #3498db;\n"
"    border-radius: 8px;\n"
"    padding: 3px;\n"
"    font-size: 16px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border-left: 1px solid #3498db;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/down_arrow.png); /* Replace with your icon */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #3498db;\n"
"    selection-background-color: #3498db;\n"
"    selection-color: white;\n"
"}")

        self.verticalLayout_10.addWidget(self.cbb_ConfigName)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.bt_UseConfig = QPushButton(self.widget_11)
        self.bt_UseConfig.setObjectName(u"bt_UseConfig")
        self.bt_UseConfig.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 7px 14px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"    transition-duration: 0.4s;\n"
"    cursor: pointer;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"    transform: translateY(2px);\n"
"}")

        self.horizontalLayout_28.addWidget(self.bt_UseConfig)

        self.bt_DeleteConfig = QPushButton(self.widget_11)
        self.bt_DeleteConfig.setObjectName(u"bt_DeleteConfig")
        self.bt_DeleteConfig.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 7px 14px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"    transition-duration: 0.4s;\n"
"    cursor: pointer;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"    transform: translateY(2px);\n"
"}")

        self.horizontalLayout_28.addWidget(self.bt_DeleteConfig)


        self.verticalLayout_10.addLayout(self.horizontalLayout_28)

        self.widget_12 = QWidget(self.tabCalib)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setGeometry(QRect(0, 520, 351, 61))
        self.horizontalLayout_32 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.le_configName = QLineEdit(self.widget_12)
        self.le_configName.setObjectName(u"le_configName")
        self.le_configName.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #3498db;\n"
"    border-radius: 5px;\n"
"    padding: 4px;\n"
"    font-size: 16px;\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2980b9;\n"
"    background-color: #ffffff;\n"
"}")

        self.horizontalLayout_32.addWidget(self.le_configName)

        self.bt_saveConfig = QPushButton(self.widget_12)
        self.bt_saveConfig.setObjectName(u"bt_saveConfig")
        self.bt_saveConfig.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 7px 14px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"    transition-duration: 0.4s;\n"
"    cursor: pointer;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"    transform: translateY(2px);\n"
"}")

        self.horizontalLayout_32.addWidget(self.bt_saveConfig)

        self.tabWidget.addTab(self.tabCalib, "")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(390, 0, 1071, 791))
        self.widget.setStyleSheet(u"QWidget {\n"
"    border: 1px solid #3498db;\n"
"    border-radius: 6px;\n"
"    padding: 10px;\n"
"}")
        self.lb_showcam = QLabel(self.widget)
        self.lb_showcam.setObjectName(u"lb_showcam")
        self.lb_showcam.setGeometry(QRect(10, 70, 1051, 720))
        self.lb_showcam.setStyleSheet(u"QLabel {\n"
"	border: none;\n"
"    color: #2c3e50;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #2980b9;\n"
"}\n"
"")
        self.lb_thresh = QLabel(self.widget)
        self.lb_thresh.setObjectName(u"lb_thresh")
        self.lb_thresh.setGeometry(QRect(790, 600, 280, 190))
        self.lb_thresh.setStyleSheet(u"border: none;")
        self.widget_7 = QWidget(self.widget)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(0, 0, 1071, 71))
        self.bt_Camera = QPushButton(self.widget_7)
        self.bt_Camera.setObjectName(u"bt_Camera")
        self.bt_Camera.setGeometry(QRect(900, 10, 141, 51))
        self.bt_Camera.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"    transition-duration: 0.4s;\n"
"    cursor: pointer;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2980b9;\n"
"    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);\n"
"    transform: translateY(2px);\n"
"}")
        self.label_20 = QLabel(self.widget_7)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 10, 271, 51))
        self.label_20.setFont(font1)
        self.label_20.setStyleSheet(u"QLabel {\n"
"	\n"
"    color: #3498db;\n"
"    font-size: 26px;\n"
"	border: none;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #2980b9;\n"
"}\n"
"")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 650, 371, 141))
        self.label.setStyleSheet(u"QWidget {\n"
"    border: 1px solid #3498db;\n"
"    border-radius: 6px;\n"
"    padding: 10px;\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Width Sample (mm):", None))
        self.lb_InWidthSample.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Height Sample (mm):", None))
        self.lb_IHeightSample.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Width Deviation (mm):", None))
        self.lb_InWidthDeviation.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Height Deviation (mm):", None))
        self.lb_InHeightDeviation.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Accuracy Sample (%):", None))
        self.lb_InAccuracySample.setText("")
        self.bt_Start.setText(QCoreApplication.translate("MainWindow", u"Auto Inspection", None))
        self.bt_InLog.setText(QCoreApplication.translate("MainWindow", u"Log Dimension", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Width (mm):", None))
        self.lb_InWidthcur.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Height (mm):", None))
        self.lb_InHeightcur.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Accuracy (%):", None))
        self.lb_Accuracy.setText("")
        self.lb_okng.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabInspection), QCoreApplication.translate("MainWindow", u"Inspection", None))
        self.le_SampleName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Sample Name...", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Width Sample (mm):", None))
        self.le_AdWidth.setPlaceholderText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Height Sample (mm):", None))
        self.le_AdHeight.setPlaceholderText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Width Deviation (mm):", None))
        self.le_AdWidthDeviation.setPlaceholderText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Height Deviation (mm):", None))
        self.le_AdHeightDeviation.setPlaceholderText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Accuracy Sample (%):", None))
        self.le_AdAccuracySample.setPlaceholderText("")
        self.bt_Save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.bt_Delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAdd), QCoreApplication.translate("MainWindow", u"Sample", None))
        self.le_ip.setText(QCoreApplication.translate("MainWindow", u"192.168.1.10", None))
        self.le_ip.setPlaceholderText(QCoreApplication.translate("MainWindow", u"IP Address:", None))
        self.bt_Connect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.bt_Home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.le_IO.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Output Robot", None))
        self.bt_Setio.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.bt_Resetio.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.cbb_Dir.setItemText(0, QCoreApplication.translate("MainWindow", u"Right", None))
        self.cbb_Dir.setItemText(1, QCoreApplication.translate("MainWindow", u"Left", None))

        self.bt_Run.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.bt_Pause.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.bt_Stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Width (mm):", None))
        self.lb_RoWidth.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Height (mm):", None))
        self.lb_RoHeight.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabRobot), QCoreApplication.translate("MainWindow", u"Robot", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Origin X:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Origin Y:", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Angle Offset:", None))
        self.le_Anglerobot.setPlaceholderText("")
        self.checkBox_EnDrawLine.setText(QCoreApplication.translate("MainWindow", u"Draw Line Center", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Width Frame Offset:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Height Frame Offset:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Frame Rotation Angle:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Frame), QCoreApplication.translate("MainWindow", u"Frame Adjustment", None))
        self.le_point1.setPlaceholderText("")
        self.bt_point1.setText(QCoreApplication.translate("MainWindow", u"Point 1", None))
        self.le_point2.setPlaceholderText("")
        self.bt_point2.setText(QCoreApplication.translate("MainWindow", u"Point 2", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Robot Z Height:", None))
        self.le_Zrobot.setPlaceholderText("")
        self.bt_confirmcenter.setText(QCoreApplication.translate("MainWindow", u"Calib New Coordinates", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Center Calibration", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Exposure Time:", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Threshold:", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Blur:", None))
        self.cbb_bblur.setItemText(0, QCoreApplication.translate("MainWindow", u"3", None))
        self.cbb_bblur.setItemText(1, QCoreApplication.translate("MainWindow", u"5", None))
        self.cbb_bblur.setItemText(2, QCoreApplication.translate("MainWindow", u"7", None))

        self.cbb_ablur.setItemText(0, QCoreApplication.translate("MainWindow", u"3", None))
        self.cbb_ablur.setItemText(1, QCoreApplication.translate("MainWindow", u"5", None))
        self.cbb_ablur.setItemText(2, QCoreApplication.translate("MainWindow", u"7", None))

        self.bt_AutoAdjust.setText(QCoreApplication.translate("MainWindow", u"Auto Adjust", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Contour Adjustment", None))
        self.bt_UseConfig.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.bt_DeleteConfig.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.le_configName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Config Name...", None))
        self.bt_saveConfig.setText(QCoreApplication.translate("MainWindow", u"Save Config", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCalib), QCoreApplication.translate("MainWindow", u"Calibration", None))
        self.lb_showcam.setText("")
        self.lb_thresh.setText("")
        self.bt_Camera.setText(QCoreApplication.translate("MainWindow", u"Open Camera", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Shoe Inspection UI", None))
        self.label.setText("")
    # retranslateUi


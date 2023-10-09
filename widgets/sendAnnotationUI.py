# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sendAnnotation.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(772, 335)
        icon = QIcon()
        icon.addFile(u":/icons/icons8-order-64.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_Buttons = QFrame(self.frame)
        self.frame_Buttons.setObjectName(u"frame_Buttons")
        self.frame_Buttons.setMaximumSize(QSize(16777215, 35))
        self.frame_Buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_Buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_topMenu = QHBoxLayout(self.frame_Buttons)
        self.horizontalLayout_topMenu.setSpacing(2)
        self.horizontalLayout_topMenu.setObjectName(u"horizontalLayout_topMenu")
        self.horizontalLayout_topMenu.setContentsMargins(2, 2, 2, 2)
        self.pen = QPushButton(self.frame_Buttons)
        self.pen.setObjectName(u"pen")
        self.pen.setMinimumSize(QSize(30, 30))
        self.pen.setMaximumSize(QSize(30, 30))
        font = QFont()
        font.setPointSize(20)
        self.pen.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons8-pencil-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pen.setIcon(icon1)
        self.pen.setIconSize(QSize(23, 23))

        self.horizontalLayout_topMenu.addWidget(self.pen)

        self.eresar = QPushButton(self.frame_Buttons)
        self.eresar.setObjectName(u"eresar")
        self.eresar.setMinimumSize(QSize(30, 30))
        self.eresar.setMaximumSize(QSize(30, 30))
        self.eresar.setSizeIncrement(QSize(0, 0))
        self.eresar.setBaseSize(QSize(0, 0))
        self.eresar.setFont(font)
        self.eresar.setToolTipDuration(-1)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons8-pencil-eraser-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.eresar.setIcon(icon2)
        self.eresar.setIconSize(QSize(25, 25))
        self.eresar.setFlat(False)

        self.horizontalLayout_topMenu.addWidget(self.eresar)

        self.brush_size_slider = QSlider(self.frame_Buttons)
        self.brush_size_slider.setObjectName(u"brush_size_slider")
        self.brush_size_slider.setMinimumSize(QSize(0, 30))
        self.brush_size_slider.setMaximumSize(QSize(60, 16777215))
        self.brush_size_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    height: 5px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(97, 190, 252, 255), stop:1 rgba(213, 238, 254, 255));\n"
"    margin: 1px 0;\n"
"    border: 1px solid #4C525A;\n"
"    border-radius: 2px;\n"
"\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(205, 234, 255, 255), stop:1 rgba(148, 218, 255, 255));\n"
"    border: 1px solid #4C525A;\n"
"    width: 5px;\n"
"    margin: -9px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 2px;\n"
"}")
        self.brush_size_slider.setMinimum(3)
        self.brush_size_slider.setSingleStep(1)
        self.brush_size_slider.setPageStep(10)
        self.brush_size_slider.setValue(50)
        self.brush_size_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_topMenu.addWidget(self.brush_size_slider)

        self.text = QPushButton(self.frame_Buttons)
        self.text.setObjectName(u"text")
        self.text.setEnabled(True)
        self.text.setMinimumSize(QSize(30, 30))
        self.text.setMaximumSize(QSize(30, 30))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons8-text-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.text.setIcon(icon3)
        self.text.setIconSize(QSize(23, 23))

        self.horizontalLayout_topMenu.addWidget(self.text)

        self.color = QPushButton(self.frame_Buttons)
        self.color.setObjectName(u"color")
        self.color.setMaximumSize(QSize(30, 30))
        self.color.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid #565A6C;\n"
"    border-radius: 14px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")

        self.horizontalLayout_topMenu.addWidget(self.color)

        self.uname = QComboBox(self.frame_Buttons)
        self.uname.setObjectName(u"uname")
        self.uname.setMinimumSize(QSize(65, 30))
        self.uname.setMaximumSize(QSize(16777215, 30))
        self.uname.setEditable(True)

        self.horizontalLayout_topMenu.addWidget(self.uname)

        self.send = QPushButton(self.frame_Buttons)
        self.send.setObjectName(u"send")
        self.send.setMinimumSize(QSize(85, 30))
        self.send.setMaximumSize(QSize(85, 30))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons8-send-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.send.setIcon(icon4)
        self.send.setIconSize(QSize(30, 30))

        self.horizontalLayout_topMenu.addWidget(self.send)


        self.gridLayout_3.addWidget(self.frame_Buttons, 0, 0, 1, 1)

        self.frame_drawing = QFrame(self.frame)
        self.frame_drawing.setObjectName(u"frame_drawing")
        self.frame_drawing.setFrameShape(QFrame.StyledPanel)
        self.frame_drawing.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget = QWidget(self.frame_drawing)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 1481, 821))
        self.verticalLayout_drawing = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_drawing.setSpacing(0)
        self.verticalLayout_drawing.setObjectName(u"verticalLayout_drawing")
        self.verticalLayout_drawing.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_drawing)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 71, 18))
        self.label.raise_()
        self.verticalLayoutWidget.raise_()

        self.gridLayout_3.addWidget(self.frame_drawing, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"sendannotation", None))
        self.text.setText("")
        self.color.setText("")
        self.send.setText(QCoreApplication.translate("Form", u"Send", None))
        self.label.setText("")
    # retranslateUi


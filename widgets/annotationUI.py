# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'annotation.ui'
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
        Form.resize(666, 368)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_Buttons = QFrame(self.frame)
        self.frame_Buttons.setObjectName(u"frame_Buttons")
        self.frame_Buttons.setMaximumSize(QSize(16777215, 35))
        self.frame_Buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_Buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_Buttons)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.pen = QPushButton(self.frame_Buttons)
        self.pen.setObjectName(u"pen")
        self.pen.setMinimumSize(QSize(30, 30))
        self.pen.setMaximumSize(QSize(30, 30))
        font = QFont()
        font.setPointSize(20)
        self.pen.setFont(font)
        self.pen.setIconSize(QSize(23, 23))

        self.horizontalLayout_2.addWidget(self.pen)

        self.eresar = QPushButton(self.frame_Buttons)
        self.eresar.setObjectName(u"eresar")
        self.eresar.setMinimumSize(QSize(30, 30))
        self.eresar.setMaximumSize(QSize(30, 30))
        self.eresar.setSizeIncrement(QSize(0, 0))
        self.eresar.setBaseSize(QSize(0, 0))
        self.eresar.setFont(font)
        self.eresar.setToolTipDuration(-1)
        self.eresar.setText(u"\u25a9")

        self.horizontalLayout_2.addWidget(self.eresar)

        self.line = QPushButton(self.frame_Buttons)
        self.line.setObjectName(u"line")
        self.line.setEnabled(False)
        self.line.setMinimumSize(QSize(30, 30))
        self.line.setMaximumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(u"../icons/Line.png", QSize(), QIcon.Normal, QIcon.Off)
        self.line.setIcon(icon)
        self.line.setIconSize(QSize(23, 23))

        self.horizontalLayout_2.addWidget(self.line)

        self.circle = QPushButton(self.frame_Buttons)
        self.circle.setObjectName(u"circle")
        self.circle.setEnabled(False)
        self.circle.setMinimumSize(QSize(30, 30))
        self.circle.setMaximumSize(QSize(30, 30))
        icon1 = QIcon()
        icon1.addFile(u"../icons/Ellipse.png", QSize(), QIcon.Normal, QIcon.Off)
        self.circle.setIcon(icon1)
        self.circle.setIconSize(QSize(23, 23))

        self.horizontalLayout_2.addWidget(self.circle)

        self.arow = QPushButton(self.frame_Buttons)
        self.arow.setObjectName(u"arow")
        self.arow.setEnabled(False)
        self.arow.setMinimumSize(QSize(30, 30))
        self.arow.setMaximumSize(QSize(30, 30))
        icon2 = QIcon()
        icon2.addFile(u"../icons/Arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.arow.setIcon(icon2)
        self.arow.setIconSize(QSize(23, 23))

        self.horizontalLayout_2.addWidget(self.arow)

        self.rectangle = QPushButton(self.frame_Buttons)
        self.rectangle.setObjectName(u"rectangle")
        self.rectangle.setEnabled(False)
        self.rectangle.setMinimumSize(QSize(30, 30))
        self.rectangle.setMaximumSize(QSize(30, 30))
        icon3 = QIcon()
        icon3.addFile(u"../icons/Rectangle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.rectangle.setIcon(icon3)
        self.rectangle.setIconSize(QSize(23, 23))

        self.horizontalLayout_2.addWidget(self.rectangle)

        self.uname = QComboBox(self.frame_Buttons)
        self.uname.setObjectName(u"uname")
        self.uname.setMinimumSize(QSize(0, 30))
        self.uname.setMaximumSize(QSize(16777215, 30))
        self.uname.setEditable(True)

        self.horizontalLayout_2.addWidget(self.uname)

        self.send = QPushButton(self.frame_Buttons)
        self.send.setObjectName(u"send")
        self.send.setMinimumSize(QSize(85, 30))
        self.send.setMaximumSize(QSize(85, 30))

        self.horizontalLayout_2.addWidget(self.send)


        self.verticalLayout.addWidget(self.frame_Buttons)

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

        self.verticalLayout.addWidget(self.frame_drawing)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pen.setText(QCoreApplication.translate("Form", u"\u270e", None))
        self.line.setText("")
        self.circle.setText("")
        self.arow.setText("")
        self.rectangle.setText("")
        self.send.setText(QCoreApplication.translate("Form", u"\u2709 Send", None))
        self.label.setText("")
    # retranslateUi


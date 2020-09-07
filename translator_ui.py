# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'translatorXbcPuY.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(679, 490)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_4)

        self.comboBox_2 = QComboBox(Form)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout.addWidget(self.comboBox_2)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_5)

        self.comboBox_3 = QComboBox(Form)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout.addWidget(self.comboBox_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.plainTextEdit = QPlainTextEdit(Form)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout.addWidget(self.plainTextEdit)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.plainTextEdit_2 = QPlainTextEdit(Form)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")

        self.verticalLayout_2.addWidget(self.plainTextEdit_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_3.addWidget(self.label_6)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u4e09\u62f3\u53d4\u7ffb\u8bd1\u5668 v1.0", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u7ffb\u8bd1\u5f15\u64ce", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"\u8c37\u6b4c\u7ffb\u8bd1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"\u6709\u9053\u7ffb\u8bd1", None))

        self.label_4.setText(QCoreApplication.translate("Form", u"\u6e90\u8bed\u8a00", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Form", u"\u81ea\u52a8\u8bc6\u522b", None))

        self.label_5.setText(QCoreApplication.translate("Form", u"\u76ee\u6807\u8bed\u8a00", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("Form", u"\u4e2d\u6587", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("Form", u"\u82f1\u8bed", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("Form", u"\u65e5\u8bed", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("Form", u"\u97e9\u8bed", None))

        self.label_2.setText(QCoreApplication.translate("Form", u"\u7ffb\u8bd1\u524d", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u7ffb\u8bd1", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u7ffb\u8bd1\u540e", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u4f7f\u7528\u65b9\u6cd5\n"
"\u7b2c\u4e00\u79cd\uff1a(\u63a8\u8350\uff01\uff01\uff01\u5373\u65f6\u7ffb\u8bd1)\u590d\u5236\u4efb\u4f55\u60a8\u60f3\u8981\u7ffb\u8bd1\u7684\u6587\u5b57\u5373\u53ef\u81ea\u52a8\u7ffb\u8bd1 \u5feb\u6377\u952eCTRL+C\n"
"\u7b2c\u4e8c\u79cd\uff1a(\u624b\u52a8\u7ffb\u8bd1)\u5c06\u60a8\u9700\u8981\u7ffb\u8bd1\u7684\u6587\u5b57\u8f93\u5165\u5728\u5de6\u4fa7\u8f93\u5165\u6846\u4e2d\uff0c\u7ffb\u8bd1\u540e\u7684\u5185\u5bb9\u5c06\u5728\u53f3\u4fa7\u663e\u793a\n"
"(\u4f7f\u7528\u4e2d\u6709\u4efb\u4f55\u95ee\u9898\u6b22\u8fce\u8054\u7cfb\u6211 QQ1104751504)", None))
    # retranslateUi


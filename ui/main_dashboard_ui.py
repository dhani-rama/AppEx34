# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_dashboard.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)
import resources.resources as resources


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(245, 250, 254);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 20)
        self.horizontalSpacer_2 = QSpacerItem(
            148, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setPixmap(QPixmap(":/src/images/heti-50.png"))

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(
            5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setPixmap(QPixmap(":/src/images/Lambang ITS 50.png"))

        self.horizontalLayout.addWidget(self.label)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalSpacer_3 = QSpacerItem(
            148, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 15, -1, -1)
        self.horizontalSpacer_4 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        font = QFont()
        font.setFamilies(["Poppins"])
        font.setPointSize(22)
        self.label_3.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer_5 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 15)
        self.horizontalSpacer_6 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.btn_sign_up = QPushButton(self.centralwidget)
        self.btn_sign_up.setObjectName("btn_sign_up")
        self.btn_sign_up.setMinimumSize(QSize(180, 60))
        self.btn_sign_up.setMaximumSize(QSize(180, 60))
        font1 = QFont()
        font1.setFamilies(["Poppins"])
        font1.setPointSize(15)
        font1.setBold(True)
        self.btn_sign_up.setFont(font1)
        self.btn_sign_up.setStyleSheet(
            "background-color: rgb(31, 149, 239);\n"
            "color: rgb(255, 255, 255);\n"
            "border-style:outset;\n"
            "border-radius:20px"
        )
        self.btn_sign_up.setCheckable(False)

        self.horizontalLayout_4.addWidget(self.btn_sign_up)

        self.horizontalSpacer_7 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalSpacer_8 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)

        self.btn_list_patient = QPushButton(self.centralwidget)
        self.btn_list_patient.setObjectName("btn_list_patient")
        self.btn_list_patient.setMinimumSize(QSize(180, 60))
        self.btn_list_patient.setMaximumSize(QSize(180, 60))
        self.btn_list_patient.setFont(font1)
        self.btn_list_patient.setStyleSheet(
            "background-color: rgb(31, 149, 239);\n"
            "color: rgb(255, 255, 255);\n"
            "border-style:outset;\n"
            "border-radius:20px"
        )

        self.horizontalLayout_5.addWidget(self.btn_list_patient)

        self.horizontalSpacer_9 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_5.addItem(self.horizontalSpacer_9)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_3 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.label_2.setText("")
        self.label.setText("")
        self.label_3.setText(
            QCoreApplication.translate("MainWindow", "Selamat Datang", None)
        )
        self.btn_sign_up.setText(
            QCoreApplication.translate("MainWindow", "Daftar", None)
        )
        self.btn_list_patient.setText(
            QCoreApplication.translate("MainWindow", "List Pasien", None)
        )

    # retranslateUi

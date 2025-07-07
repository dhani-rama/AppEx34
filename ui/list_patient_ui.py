# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'list_patient.ui'
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
    QLineEdit,
    QListWidget,
    QListWidgetItem,
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
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(245, 250, 254);\n" "\n" "")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.img_dikbud = QLabel(self.centralwidget)
        self.img_dikbud.setObjectName("img_dikbud")
        self.img_dikbud.setPixmap(QPixmap(":/src/images/heti-50.png"))

        self.horizontalLayout_2.addWidget(self.img_dikbud)

        self.horizontalSpacer_4 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.et_search = QLineEdit(self.centralwidget)
        self.et_search.setObjectName("et_search")
        self.et_search.setMinimumSize(QSize(250, 30))
        self.et_search.setMaximumSize(QSize(250, 30))
        self.et_search.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            "border: 1px outset rgb(135, 134, 134);\n"
            "border-radius: 15px;"
        )

        self.horizontalLayout.addWidget(self.et_search)

        self.horizontalSpacer_3 = QSpacerItem(
            10, 15, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.btn_search = QPushButton(self.centralwidget)
        self.btn_search.setObjectName("btn_search")
        self.btn_search.setMinimumSize(QSize(30, 30))
        self.btn_search.setMaximumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(
            ":/src/images/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        self.btn_search.setIcon(icon)

        self.horizontalLayout.addWidget(self.btn_search)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalSpacer_5 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.img_its = QLabel(self.centralwidget)
        self.img_its.setObjectName("img_its")
        self.img_its.setPixmap(QPixmap(":/src/images/Lambang ITS 50.png"))

        self.horizontalLayout_2.addWidget(self.img_its)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 10, -1, 15)
        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.txt_header_list_patient = QLabel(self.centralwidget)
        self.txt_header_list_patient.setObjectName("txt_header_list_patient")
        font = QFont()
        font.setFamilies(["Poppins"])
        font.setPointSize(18)
        self.txt_header_list_patient.setFont(font)

        self.horizontalLayout_3.addWidget(self.txt_header_list_patient)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.rv_list = QListWidget(self.centralwidget)
        self.rv_list.setObjectName("rv_list")
        self.rv_list.setStyleSheet("border: none;")

        self.verticalLayout.addWidget(self.rv_list)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.img_dikbud.setText("")
        self.btn_search.setText("")
        self.img_its.setText("")
        self.txt_header_list_patient.setText(
            QCoreApplication.translate("MainWindow", "Daftar Pasien", None)
        )

    # retranslateUi

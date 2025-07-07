# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sign_up_patient.ui'
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
    QComboBox,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
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
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.widget.setStyleSheet("background-color: rgb(31, 149, 239);")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName("label")
        self.label.setPixmap(QPixmap(":/src/images/img_daftar_3.png"))

        self.verticalLayout_2.addWidget(self.label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        font = QFont()
        font.setFamilies(["Poppins"])
        font.setPointSize(13)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        font1 = QFont()
        font1.setFamilies(["Poppins"])
        font1.setPointSize(9)
        font1.setBold(True)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_3)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_11 = QVBoxLayout(self.widget_2)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.img_dikbud = QLabel(self.widget_2)
        self.img_dikbud.setObjectName("img_dikbud")
        self.img_dikbud.setPixmap(QPixmap(":/src/images/heti-50.png"))

        self.horizontalLayout.addWidget(self.img_dikbud)

        self.img_its = QLabel(self.widget_2)
        self.img_its.setObjectName("img_its")
        self.img_its.setPixmap(QPixmap(":/src/images/Lambang ITS 50.png"))

        self.horizontalLayout.addWidget(self.img_its)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.verticalLayout_10.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.tv_header_sign_up = QLabel(self.widget_2)
        self.tv_header_sign_up.setObjectName("tv_header_sign_up")
        font2 = QFont()
        font2.setFamilies(["Poppins"])
        font2.setPointSize(18)
        font2.setBold(True)
        self.tv_header_sign_up.setFont(font2)
        self.tv_header_sign_up.setStyleSheet("color: rgb(135, 134, 134);")

        self.horizontalLayout_3.addWidget(self.tv_header_sign_up)

        self.horizontalSpacer_5 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.verticalLayout_10.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalSpacer_6 = QSpacerItem(
            18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, -1, -1, 15)
        self.tv_name = QLabel(self.widget_2)
        self.tv_name.setObjectName("tv_name")
        font3 = QFont()
        font3.setFamilies(["Poppins"])
        font3.setPointSize(12)
        font3.setKerning(True)
        self.tv_name.setFont(font3)
        self.tv_name.setStyleSheet("color: rgb(135, 134, 134);")

        self.verticalLayout_5.addWidget(self.tv_name)

        self.et_username = QLineEdit(self.widget_2)
        self.et_username.setObjectName("et_username")
        self.et_username.setMinimumSize(QSize(490, 40))
        self.et_username.setMaximumSize(QSize(480, 40))
        self.et_username.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            "border: 1px outset rgb(135, 134, 134);\n"
            "border-radius: 15px;"
        )

        self.verticalLayout_5.addWidget(self.et_username)

        self.verticalLayout_9.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, -1, 15)
        self.tv_nik = QLabel(self.widget_2)
        self.tv_nik.setObjectName("tv_nik")
        self.tv_nik.setFont(font3)
        self.tv_nik.setStyleSheet("color: rgb(135, 134, 134);")

        self.verticalLayout_6.addWidget(self.tv_nik)

        self.et_nik = QLineEdit(self.widget_2)
        self.et_nik.setObjectName("et_nik")
        self.et_nik.setMinimumSize(QSize(490, 40))
        self.et_nik.setMaximumSize(QSize(490, 40))
        self.et_nik.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            "border: 1px outset rgb(135, 134, 134);\n"
            "border-radius: 15px;"
        )

        self.verticalLayout_6.addWidget(self.et_nik)

        self.verticalLayout_9.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, -1, -1, 15)
        self.tv_sex = QLabel(self.widget_2)
        self.tv_sex.setObjectName("tv_sex")
        self.tv_sex.setFont(font3)
        self.tv_sex.setStyleSheet("color: rgb(135, 134, 134);")

        self.verticalLayout_7.addWidget(self.tv_sex)

        self.et_sex = QComboBox(self.widget_2)
        self.et_sex.addItem("")
        self.et_sex.addItem("")
        self.et_sex.setObjectName("et_sex")
        self.et_sex.setMinimumSize(QSize(490, 40))
        self.et_sex.setMaximumSize(QSize(490, 37))
        font4 = QFont()
        font4.setFamilies(["Poppins"])
        font4.setPointSize(12)
        self.et_sex.setFont(font4)
        self.et_sex.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            "border: 1px outset rgb(135, 134, 134);\n"
            "border-radius: 15px;\n"
            "color: rgb(135, 134, 134);"
        )

        self.verticalLayout_7.addWidget(self.et_sex)

        self.verticalLayout_9.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, -1, -1, 15)
        self.tv_address = QLabel(self.widget_2)
        self.tv_address.setObjectName("tv_address")
        self.tv_address.setFont(font3)
        self.tv_address.setStyleSheet("color: rgb(135, 134, 134);")

        self.verticalLayout_8.addWidget(self.tv_address)

        self.et_address = QLineEdit(self.widget_2)
        self.et_address.setObjectName("et_address")
        self.et_address.setMinimumSize(QSize(490, 40))
        self.et_address.setMaximumSize(QSize(490, 40))
        self.et_address.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            "border: 1px outset rgb(135, 134, 134);\n"
            "border-radius: 15px;"
        )

        self.verticalLayout_8.addWidget(self.et_address)

        self.verticalLayout_9.addLayout(self.verticalLayout_8)

        self.horizontalLayout_4.addLayout(self.verticalLayout_9)

        self.horizontalSpacer_7 = QSpacerItem(
            17, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.verticalLayout_10.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalSpacer_8 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)

        self.btn_sign_up = QPushButton(self.widget_2)
        self.btn_sign_up.setObjectName("btn_sign_up")
        self.btn_sign_up.setMinimumSize(QSize(120, 40))
        self.btn_sign_up.setMaximumSize(QSize(120, 40))
        self.btn_sign_up.setFont(font)
        self.btn_sign_up.setStyleSheet(
            "background-color: rgb(31, 149, 239);\n"
            "color: rgb(255, 255, 255);\n"
            "border-style:outset;\n"
            "border-radius:15px"
        )

        self.horizontalLayout_5.addWidget(self.btn_sign_up)

        self.horizontalSpacer_9 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_5.addItem(self.horizontalSpacer_9)

        self.verticalLayout_10.addLayout(self.horizontalLayout_5)

        self.verticalLayout_11.addLayout(self.verticalLayout_10)

        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.label.setText("")
        self.label_2.setText(
            QCoreApplication.translate("MainWindow", "Yuk, isi biodatamu dulu!", None)
        )
        self.label_3.setText(
            QCoreApplication.translate(
                "MainWindow",
                "Biar kami bisa bantu cek kondisi tubuhmu dengan lebih akurat",
                None,
            )
        )
        self.img_dikbud.setText("")
        self.img_its.setText("")
        self.tv_header_sign_up.setText(
            QCoreApplication.translate("MainWindow", "Pendaftaran Pasien", None)
        )
        self.tv_name.setText(
            QCoreApplication.translate("MainWindow", "Nama Pasien", None)
        )
        self.tv_nik.setText(QCoreApplication.translate("MainWindow", "NIK", None))
        self.tv_sex.setText(
            QCoreApplication.translate("MainWindow", "Jenis Kelamin", None)
        )
        self.et_sex.setItemText(
            0, QCoreApplication.translate("MainWindow", "LAKI - LAKI", None)
        )
        self.et_sex.setItemText(
            1, QCoreApplication.translate("MainWindow", "PEREMPUAN", None)
        )

        self.tv_address.setText(
            QCoreApplication.translate("MainWindow", "Alamat", None)
        )
        self.btn_sign_up.setText(
            QCoreApplication.translate("MainWindow", "Daftar", None)
        )

    # retranslateUi

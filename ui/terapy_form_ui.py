# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'terapy_form.ui'
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
        MainWindow.resize(800, 603)
        MainWindow.setStyleSheet("background-color: rgb(245, 250, 254);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.widget.setStyleSheet("background-color: rgb(31, 149, 239);")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName("label")
        self.label.setPixmap(QPixmap(":/src/images/animasi_form_terapi_200.png"))

        self.verticalLayout.addWidget(self.label)

        self.tv_caution_1 = QLabel(self.widget)
        self.tv_caution_1.setObjectName("tv_caution_1")
        font = QFont()
        font.setFamilies(["Poppins"])
        font.setPointSize(12)
        font.setBold(True)
        self.tv_caution_1.setFont(font)
        self.tv_caution_1.setStyleSheet("color: rgb(255, 255, 255);")
        self.tv_caution_1.setWordWrap(True)

        self.verticalLayout.addWidget(self.tv_caution_1)

        self.tv_caution_2 = QLabel(self.widget)
        self.tv_caution_2.setObjectName("tv_caution_2")
        font1 = QFont()
        font1.setFamilies(["Poppins"])
        font1.setPointSize(9)
        font1.setBold(False)
        self.tv_caution_2.setFont(font1)
        self.tv_caution_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.tv_caution_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tv_caution_2.setWordWrap(True)

        self.verticalLayout.addWidget(self.tv_caution_2)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalLayout_9.addWidget(self.widget)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.img_dikbud = QLabel(self.centralwidget)
        self.img_dikbud.setObjectName("img_dikbud")
        self.img_dikbud.setPixmap(QPixmap(":/src/images/heti-50.png"))

        self.horizontalLayout.addWidget(self.img_dikbud)

        self.img_its = QLabel(self.centralwidget)
        self.img_its.setObjectName("img_its")
        self.img_its.setPixmap(QPixmap(":/src/images/Lambang ITS 50.png"))

        self.horizontalLayout.addWidget(self.img_its)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.tv_header_1 = QLabel(self.centralwidget)
        self.tv_header_1.setObjectName("tv_header_1")
        font2 = QFont()
        font2.setFamilies(["Poppins"])
        font2.setPointSize(18)
        font2.setBold(True)
        self.tv_header_1.setFont(font2)
        self.tv_header_1.setStyleSheet("color: rgb(135, 134, 134);")
        self.tv_header_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.tv_header_1)

        self.verticalLayout_11.addLayout(self.verticalLayout_4)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalSpacer_5 = QSpacerItem(
            18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 10, 0, 10)
        self.tv_name = QLabel(self.centralwidget)
        self.tv_name.setObjectName("tv_name")
        font3 = QFont()
        font3.setFamilies(["Poppins"])
        font3.setPointSize(12)
        self.tv_name.setFont(font3)
        self.tv_name.setStyleSheet("color: rgb(135, 134, 134);")

        self.verticalLayout_5.addWidget(self.tv_name)

        self.et_name = QLineEdit(self.centralwidget)
        self.et_name.setObjectName("et_name")
        self.et_name.setMinimumSize(QSize(490, 40))
        self.et_name.setMaximumSize(QSize(490, 40))
        self.et_name.setFont(font3)
        self.et_name.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            "border: 1px outset rgb(135, 134, 134);\n"
            "border-radius: 15px;\n"
            "color: rgb(135, 134, 134);"
        )

        self.verticalLayout_5.addWidget(self.et_name)

        self.horizontalLayout_4.addLayout(self.verticalLayout_5)

        self.horizontalSpacer_6 = QSpacerItem(
            18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.verticalLayout_10.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalSpacer_7 = QSpacerItem(
            18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, -1, 10)
        self.tv_weight = QLabel(self.centralwidget)
        self.tv_weight.setObjectName("tv_weight")
        self.tv_weight.setFont(font3)
        self.tv_weight.setStyleSheet("color: rgb(135, 134, 134);")

        self.verticalLayout_6.addWidget(self.tv_weight)

        self.et_weight = QLineEdit(self.centralwidget)
        self.et_weight.setObjectName("et_weight")
        self.et_weight.setMinimumSize(QSize(490, 40))
        self.et_weight.setMaximumSize(QSize(490, 40))
        self.et_weight.setFont(font3)
        self.et_weight.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            "border: 1px outset rgb(135, 134, 134);\n"
            "border-radius: 15px;\n"
            "color: rgb(135, 134, 134);"
        )

        self.verticalLayout_6.addWidget(self.et_weight)

        self.horizontalLayout_5.addLayout(self.verticalLayout_6)

        self.horizontalSpacer_8 = QSpacerItem(
            18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)

        self.verticalLayout_10.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalSpacer_9 = QSpacerItem(
            13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_6.addItem(self.horizontalSpacer_9)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, -1, -1, 15)
        self.tv_type_terapy = QLabel(self.centralwidget)
        self.tv_type_terapy.setObjectName("tv_type_terapy")
        self.tv_type_terapy.setFont(font3)
        self.tv_type_terapy.setStyleSheet("color: rgb(135, 134, 134);")

        self.verticalLayout_7.addWidget(self.tv_type_terapy)

        self.et_type_terapy = QComboBox(self.centralwidget)
        self.et_type_terapy.addItem("")
        self.et_type_terapy.addItem("")
        self.et_type_terapy.setObjectName("et_type_terapy")
        self.et_type_terapy.setMinimumSize(QSize(490, 40))
        self.et_type_terapy.setMaximumSize(QSize(490, 40))
        font4 = QFont()
        font4.setFamilies(["Poppins"])
        font4.setPointSize(12)
        font4.setBold(False)
        self.et_type_terapy.setFont(font4)
        self.et_type_terapy.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            "border: 1px outset rgb(135, 134, 134);\n"
            "border-radius: 15px;\n"
            "color: rgb(135, 134, 134);"
        )

        self.verticalLayout_7.addWidget(self.et_type_terapy)

        self.horizontalLayout_6.addLayout(self.verticalLayout_7)

        self.horizontalSpacer_10 = QSpacerItem(
            18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_6.addItem(self.horizontalSpacer_10)

        self.verticalLayout_10.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalSpacer_11 = QSpacerItem(
            13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_7.addItem(self.horizontalSpacer_11)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, -1, -1, 10)
        self.tv_method_terapy = QLabel(self.centralwidget)
        self.tv_method_terapy.setObjectName("tv_method_terapy")
        self.tv_method_terapy.setFont(font3)
        self.tv_method_terapy.setStyleSheet("color: rgb(135, 134, 134);")

        self.verticalLayout_8.addWidget(self.tv_method_terapy)

        self.et_method_terapy = QComboBox(self.centralwidget)
        self.et_method_terapy.addItem("")
        self.et_method_terapy.setObjectName("et_method_terapy")
        self.et_method_terapy.setMinimumSize(QSize(490, 40))
        self.et_method_terapy.setMaximumSize(QSize(490, 40))
        self.et_method_terapy.setFont(font3)
        self.et_method_terapy.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            "border: 1px outset rgb(135, 134, 134);\n"
            "border-radius: 15px;\n"
            "color: rgb(135, 134, 134);"
        )

        self.verticalLayout_8.addWidget(self.et_method_terapy)

        self.horizontalLayout_7.addLayout(self.verticalLayout_8)

        self.horizontalSpacer_12 = QSpacerItem(
            18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_7.addItem(self.horizontalSpacer_12)

        self.verticalLayout_10.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalSpacer_13 = QSpacerItem(
            13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_8.addItem(self.horizontalSpacer_13)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, -1, -1, 10)
        self.tv_time = QLabel(self.centralwidget)
        self.tv_time.setObjectName("tv_time")
        self.tv_time.setFont(font3)
        self.tv_time.setStyleSheet("color: rgb(135, 134, 134);")

        self.verticalLayout_9.addWidget(self.tv_time)

        self.et_time = QLineEdit(self.centralwidget)
        self.et_time.setObjectName("et_time")
        self.et_time.setMinimumSize(QSize(490, 40))
        self.et_time.setMaximumSize(QSize(490, 40))
        self.et_time.setFont(font3)
        self.et_time.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            "border: 1px outset rgb(135, 134, 134);\n"
            "border-radius: 15px;\n"
            "color: rgb(135, 134, 134);"
        )

        self.verticalLayout_9.addWidget(self.et_time)

        self.horizontalLayout_8.addLayout(self.verticalLayout_9)

        self.horizontalSpacer_14 = QSpacerItem(
            18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_8.addItem(self.horizontalSpacer_14)

        self.verticalLayout_10.addLayout(self.horizontalLayout_8)

        self.verticalLayout_11.addLayout(self.verticalLayout_10)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.btn_save = QPushButton(self.centralwidget)
        self.btn_save.setObjectName("btn_save")
        self.btn_save.setMinimumSize(QSize(120, 40))
        self.btn_save.setMaximumSize(QSize(120, 40))
        font5 = QFont()
        font5.setFamilies(["Poppins"])
        font5.setPointSize(13)
        font5.setBold(True)
        self.btn_save.setFont(font5)
        self.btn_save.setStyleSheet(
            "background-color: rgb(31, 149, 239);\n"
            "color: rgb(255, 255, 255);\n"
            "border-style:outset;\n"
            "border-radius:15px"
        )

        self.horizontalLayout_3.addWidget(self.btn_save)

        self.horizontalSpacer_4 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.verticalLayout_11.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_9.addLayout(self.verticalLayout_11)

        self.gridLayout.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.label.setText("")
        self.tv_caution_1.setText(
            QCoreApplication.translate(
                "MainWindow", "Lengkapi form ini dulu, ya!", None
            )
        )
        self.tv_caution_2.setText(
            QCoreApplication.translate(
                "MainWindow",
                "Supaya terapis tahu metode dan durasi yang paling cocok buatmu",
                None,
            )
        )
        self.img_dikbud.setText("")
        self.img_its.setText("")
        self.tv_header_1.setText(
            QCoreApplication.translate("MainWindow", "Pendaftaran Terapi", None)
        )
        self.tv_name.setText(
            QCoreApplication.translate("MainWindow", "Nama Pasien", None)
        )
        self.tv_weight.setText(
            QCoreApplication.translate("MainWindow", "Berat Pasien (KG)", None)
        )
        self.tv_type_terapy.setText(
            QCoreApplication.translate("MainWindow", "Jenis Terapi", None)
        )
        self.et_type_terapy.setItemText(
            0, QCoreApplication.translate("MainWindow", "Kepala", None)
        )
        self.et_type_terapy.setItemText(
            1, QCoreApplication.translate("MainWindow", "Pinggang", None)
        )

        self.tv_method_terapy.setText(
            QCoreApplication.translate("MainWindow", "Metode Terapi", None)
        )
        self.et_method_terapy.setItemText(
            0, QCoreApplication.translate("MainWindow", "Langsung", None)
        )

        self.tv_time.setText(
            QCoreApplication.translate("MainWindow", "Waktu Terapi (Menit)", None)
        )
        self.et_time.setText("")
        self.btn_save.setText(QCoreApplication.translate("MainWindow", "Simpan", None))

    # retranslateUi

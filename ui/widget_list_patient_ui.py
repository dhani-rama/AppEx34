# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_list_patient.ui'
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
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)
import resources.resources as resources


class Ui_containerPasien(object):
    def setupUi(self, containerPasien):
        if not containerPasien.objectName():
            containerPasien.setObjectName("containerPasien")
        containerPasien.resize(588, 98)
        containerPasien.setStyleSheet(
            "QWidget#containerPasien {\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QPushButton{\n"
            "\n"
            "	background-color: #ffffff;\n"
            "    border: 1px solid #878686;\n"
            "    border-radius: 10px;\n"
            "\n"
            "}"
        )
        self.gridLayout = QGridLayout(containerPasien)
        self.gridLayout.setObjectName("gridLayout")
        self.containerPasien1 = QWidget(containerPasien)
        self.containerPasien1.setObjectName("containerPasien1")
        self.containerPasien1.setStyleSheet(
            "background-color: #ffffff;\n"
            "border: 1px solid #878686;\n"
            "border-radius: 15px;"
        )
        self.verticalLayout_2 = QVBoxLayout(self.containerPasien1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.username_patient = QLabel(self.containerPasien1)
        self.username_patient.setObjectName("username_patient")
        font = QFont()
        font.setFamilies(["Poppins"])
        font.setPointSize(13)
        font.setBold(False)
        self.username_patient.setFont(font)
        self.username_patient.setStyleSheet("border: none;")

        self.verticalLayout.addWidget(self.username_patient)

        self.nik_patient = QLabel(self.containerPasien1)
        self.nik_patient.setObjectName("nik_patient")
        self.nik_patient.setFont(font)
        self.nik_patient.setStyleSheet("border: none;")

        self.verticalLayout.addWidget(self.nik_patient)

        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(
            188, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_edit = QPushButton(self.containerPasien1)
        self.btn_edit.setObjectName("btn_edit")
        self.btn_edit.setMinimumSize(QSize(40, 40))
        self.btn_edit.setMaximumSize(QSize(40, 40))
        icon = QIcon()
        icon.addFile(
            ":/src/images/icon edit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        self.btn_edit.setIcon(icon)

        self.horizontalLayout.addWidget(self.btn_edit)

        self.btn_delete = QPushButton(self.containerPasien1)
        self.btn_delete.setObjectName("btn_delete")
        self.btn_delete.setMinimumSize(QSize(40, 40))
        self.btn_delete.setMaximumSize(QSize(40, 40))
        icon1 = QIcon()
        icon1.addFile(
            ":/src/images/icon delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        self.btn_delete.setIcon(icon1)

        self.horizontalLayout.addWidget(self.btn_delete)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.gridLayout.addWidget(self.containerPasien1, 0, 0, 1, 1)

        self.retranslateUi(containerPasien)

        QMetaObject.connectSlotsByName(containerPasien)

    # setupUi

    def retranslateUi(self, containerPasien):
        containerPasien.setWindowTitle(
            QCoreApplication.translate("containerPasien", "Form", None)
        )
        self.username_patient.setText(
            QCoreApplication.translate("containerPasien", "Nama Pasien", None)
        )
        self.nik_patient.setText(
            QCoreApplication.translate("containerPasien", "199828282929292299292", None)
        )
        self.btn_edit.setText("")
        self.btn_delete.setText("")

    # retranslateUi

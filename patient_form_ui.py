# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'patient_form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(245, 250, 254);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_7 = QVBoxLayout(self.widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)

        self.horizontalLayout_3.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_6 = QVBoxLayout(self.widget_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(16)
        self.label_2.setFont(font1)

        self.verticalLayout.addWidget(self.label_2)

        self.verticalSpacer = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout.addWidget(self.label_3)

        self.verticalSpacer_2 = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout.addWidget(self.label_4)

        self.verticalSpacer_3 = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label_6 = QLabel(self.widget_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.verticalLayout.addWidget(self.label_6)

        self.verticalSpacer_4 = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout.addWidget(self.label_5)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.horizontalLayout_4.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_4 = QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.et_name_patient = QLineEdit(self.widget_4)
        self.et_name_patient.setObjectName(u"et_name_patient")
        font2 = QFont()
        font2.setPointSize(14)
        self.et_name_patient.setFont(font2)

        self.verticalLayout_2.addWidget(self.et_name_patient)

        self.verticalSpacer_5 = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.et_weight_patient = QLineEdit(self.widget_4)
        self.et_weight_patient.setObjectName(u"et_weight_patient")
        self.et_weight_patient.setFont(font2)

        self.horizontalLayout.addWidget(self.et_weight_patient)

        self.label_7 = QLabel(self.widget_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.horizontalLayout.addWidget(self.label_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer_6 = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)

        self.et_sort_patient = QComboBox(self.widget_4)
        self.et_sort_patient.addItem("")
        self.et_sort_patient.addItem("")
        self.et_sort_patient.setObjectName(u"et_sort_patient")
        self.et_sort_patient.setFont(font2)

        self.verticalLayout_2.addWidget(self.et_sort_patient)

        self.verticalSpacer_7 = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_7)

        self.et_mode_patient = QComboBox(self.widget_4)
        self.et_mode_patient.addItem("")
        self.et_mode_patient.addItem("")
        self.et_mode_patient.setObjectName(u"et_mode_patient")
        self.et_mode_patient.setFont(font2)

        self.verticalLayout_2.addWidget(self.et_mode_patient)

        self.verticalSpacer_8 = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_8)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.et_time_patient = QLineEdit(self.widget_4)
        self.et_time_patient.setObjectName(u"et_time_patient")
        self.et_time_patient.setFont(font2)

        self.horizontalLayout_2.addWidget(self.et_time_patient)

        self.label_8 = QLabel(self.widget_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_8)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.horizontalLayout_4.addWidget(self.widget_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_9 = QSpacerItem(20, 28, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_9)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.btn_save_patient = QPushButton(self.widget_2)
        self.btn_save_patient.setObjectName(u"btn_save_patient")
        self.btn_save_patient.setFont(font1)
        self.btn_save_patient.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.btn_save_patient)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_10 = QSpacerItem(20, 28, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_10)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.gridLayout.addWidget(self.widget_2, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Form Pasien", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nama Pasien", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Berat Pasien", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Jenis Terapi", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Metode Terapi", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Waktu Terapi", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"KG", None))
        self.et_sort_patient.setItemText(0, QCoreApplication.translate("MainWindow", u"Kepala", None))
        self.et_sort_patient.setItemText(1, QCoreApplication.translate("MainWindow", u"Pinggang", None))

        self.et_mode_patient.setItemText(0, QCoreApplication.translate("MainWindow", u"Langsung", None))
        self.et_mode_patient.setItemText(1, QCoreApplication.translate("MainWindow", u"Per Step", None))

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Menit", None))
        self.btn_save_patient.setText(QCoreApplication.translate("MainWindow", u"Simpan", None))
    # retranslateUi


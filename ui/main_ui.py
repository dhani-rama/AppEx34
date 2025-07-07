# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'diagram_form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
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
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)
import resources


class Ui_mainmenu(object):
    def setupUi(self, mainmenu):
        if not mainmenu.objectName():
            mainmenu.setObjectName("mainmenu")
        mainmenu.resize(800, 600)
        mainmenu.setStyleSheet("background-color: rgb(245, 250, 254);")
        self.centralwidget = QWidget(mainmenu)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName("icon_only_widget")
        self.icon_only_widget.setStyleSheet(
            "QWidget{\n"
            "	background-color: rgb(31, 149, 239);\n"
            "}\n"
            "\n"
            "QPushButton{\n"
            "	color: white;\n"
            "	height:30px;\n"
            "	border: none;\n"
            "	border-radius:10px;\n"
            "}\n"
            "\n"
            "QPushButton:checked{\n"
            "	background-color: #F5FAFE;\n"
            "	color: #1F95EF;\n"
            "	font-weight: bold;\n"
            "}\n"
            "\n"
            ""
        )
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName("label")
        self.label.setMinimumSize(QSize(40, 40))
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setPixmap(QPixmap(":/src/images/profile_pic.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.btn_dashboard_1 = QPushButton(self.icon_only_widget)
        self.btn_dashboard_1.setObjectName("btn_dashboard_1")
        icon = QIcon()
        icon.addFile(
            ":/src/images/dashboard_white.png",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        icon.addFile(
            ":/src/images/dashboard.png", QSize(), QIcon.Mode.Normal, QIcon.State.On
        )
        self.btn_dashboard_1.setIcon(icon)
        self.btn_dashboard_1.setCheckable(True)
        self.btn_dashboard_1.setChecked(True)
        self.btn_dashboard_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_dashboard_1)

        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(
            20, 263, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.btn_logout_1 = QPushButton(self.icon_only_widget)
        self.btn_logout_1.setObjectName("btn_logout_1")
        icon1 = QIcon()
        icon1.addFile(
            ":/src/images/log_out_white.png",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.btn_logout_1.setIcon(icon1)
        self.btn_logout_1.setCheckable(True)

        self.verticalLayout_3.addWidget(self.btn_logout_1)

        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName("icon_name_widget")
        self.icon_name_widget.setStyleSheet(
            "QWidget{\n"
            "	background-color: rgb(31, 149, 239);\n"
            "	color:white;\n"
            "}\n"
            "\n"
            "QPushButton{\n"
            "	color: white;\n"
            "	text-align:left;\n"
            "	height:30px;\n"
            "	border: none;\n"
            "	padding-left: 10px;\n"
            "	border-top-left-radius:10px;\n"
            "	border-bottom-left-radius:10px;\n"
            "}\n"
            "\n"
            "QPushButton:checked{\n"
            "	background-color: #F5FAFE;\n"
            "	color: #1F95EF;\n"
            "	font-weight: bold;\n"
            "}\n"
            "\n"
            "\n"
            ""
        )
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 20, -1)
        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName("label_2")
        self.label_2.setMinimumSize(QSize(40, 40))
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(":/src/images/profile_pic.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.tv_name_patient = QLabel(self.icon_name_widget)
        self.tv_name_patient.setObjectName("tv_name_patient")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.tv_name_patient.setFont(font)

        self.horizontalLayout_2.addWidget(self.tv_name_patient)

        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.btn_dashboard_2 = QPushButton(self.icon_name_widget)
        self.btn_dashboard_2.setObjectName("btn_dashboard_2")
        self.btn_dashboard_2.setStyleSheet("")
        self.btn_dashboard_2.setIcon(icon)
        self.btn_dashboard_2.setCheckable(True)
        self.btn_dashboard_2.setChecked(True)
        self.btn_dashboard_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_dashboard_2)

        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(
            20, 263, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.btn_logout_2 = QPushButton(self.icon_name_widget)
        self.btn_logout_2.setObjectName("btn_logout_2")
        self.btn_logout_2.setIcon(icon1)
        self.btn_logout_2.setCheckable(True)

        self.verticalLayout_4.addWidget(self.btn_logout_2)

        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName("main_menu")
        self.verticalLayout_5 = QVBoxLayout(self.main_menu)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.header_widget = QWidget(self.main_menu)
        self.header_widget.setObjectName("header_widget")
        self.horizontalLayout_4 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_menu = QPushButton(self.header_widget)
        self.btn_menu.setObjectName("btn_menu")
        self.btn_menu.setStyleSheet("border:none;")
        icon2 = QIcon()
        icon2.addFile(
            ":/src/images/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        self.btn_menu.setIcon(icon2)
        self.btn_menu.setIconSize(QSize(20, 20))
        self.btn_menu.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.btn_menu)

        self.horizontalSpacer_2 = QSpacerItem(
            161, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QLineEdit(self.header_widget)
        self.lineEdit.setObjectName("lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton_14 = QPushButton(self.header_widget)
        self.pushButton_14.setObjectName("pushButton_14")
        icon3 = QIcon()
        icon3.addFile(
            ":/src/images/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        self.pushButton_14.setIcon(icon3)

        self.horizontalLayout.addWidget(self.pushButton_14)

        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalSpacer = QSpacerItem(
            161, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.pushButton_15 = QPushButton(self.header_widget)
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_15.setStyleSheet("border:none;")
        icon4 = QIcon()
        icon4.addFile(
            ":/src/images/image.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        self.pushButton_15.setIcon(icon4)

        self.horizontalLayout_4.addWidget(self.pushButton_15)

        self.verticalLayout_5.addWidget(self.header_widget)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidget.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "\n" "\n" "\n" "\n" ""
        )
        self.dashboard_page = QWidget()
        self.dashboard_page.setObjectName("dashboard_page")
        self.verticalLayout_7 = QVBoxLayout(self.dashboard_page)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(30, 40, 30, -1)
        self.line_graph_view = QChartView(self.dashboard_page)
        self.line_graph_view.setObjectName("line_graph_view")

        self.verticalLayout_6.addWidget(self.line_graph_view)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 40, -1, -1)
        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.btn_start = QPushButton(self.dashboard_page)
        self.btn_start.setObjectName("btn_start")
        self.btn_start.setMinimumSize(QSize(120, 40))
        self.btn_start.setMaximumSize(QSize(120, 40))
        self.btn_start.setFont(font)
        self.btn_start.setStyleSheet(
            "background-color: rgb(31, 149, 239);\n"
            "color: rgb(255, 255, 255);\n"
            "border-style:outset;\n"
            "border-radius:15px\n"
            "\n"
            ""
        )
        self.btn_start.setCheckable(True)
        self.btn_start.setAutoExclusive(False)

        self.horizontalLayout_6.addWidget(self.btn_start)

        self.horizontalSpacer_4 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.stackedWidget.addWidget(self.dashboard_page)
        self.messages_page = QWidget()
        self.messages_page.setObjectName("messages_page")
        self.stackedWidget.addWidget(self.messages_page)
        self.notifications_page = QWidget()
        self.notifications_page.setObjectName("notifications_page")
        self.stackedWidget.addWidget(self.notifications_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName("settings_page")
        self.stackedWidget.addWidget(self.settings_page)
        self.profile_page = QWidget()
        self.profile_page.setObjectName("profile_page")
        self.stackedWidget.addWidget(self.profile_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)

        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        mainmenu.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainmenu)
        self.btn_menu.toggled.connect(self.icon_only_widget.setHidden)
        self.btn_menu.toggled.connect(self.icon_name_widget.setVisible)
        self.btn_dashboard_1.toggled.connect(self.btn_dashboard_2.setChecked)
        self.btn_dashboard_2.toggled.connect(self.btn_dashboard_1.setChecked)
        self.btn_logout_1.toggled.connect(mainmenu.close)
        self.btn_logout_2.toggled.connect(mainmenu.close)

        QMetaObject.connectSlotsByName(mainmenu)

    # setupUi

    def retranslateUi(self, mainmenu):
        mainmenu.setWindowTitle(
            QCoreApplication.translate("mainmenu", "mainmenu", None)
        )
        self.label.setText("")
        self.btn_dashboard_1.setText("")
        self.btn_logout_1.setText("")
        self.label_2.setText("")
        self.tv_name_patient.setText(
            QCoreApplication.translate("mainmenu", "Admin", None)
        )
        self.btn_dashboard_2.setText(
            QCoreApplication.translate("mainmenu", "Dashboard", None)
        )
        self.btn_logout_2.setText(
            QCoreApplication.translate("mainmenu", "Logout", None)
        )
        self.btn_menu.setText("")
        self.pushButton_14.setText("")
        self.pushButton_15.setText("")
        self.btn_start.setText(QCoreApplication.translate("mainmenu", "Mulai", None))

    # retranslateUi

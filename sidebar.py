# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 15:36:48 2024

@author: ramad
"""

from main_ui import Ui_mainmenu
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtGui import Qt, QIcon
from PySide6 import QtCharts
from PySide6.QtCore import QTimer
import random
import serial

# import RPi.GPIO as GPIO
import time


class MySideBar(QMainWindow, Ui_mainmenu):
    def __init__(self, name, weight, sort, mode, time, serial_port, baud_rate):
        super().__init__()
        self.setupUi(self)

        # Konfigurasi serial
        self.serial_connection = serial.Serial(serial_port, baud_rate, timeout=1)
        self.serial_connection.flush()

        self.icon_name_widget.setHidden(True)

        self.tv_name_patient.setText(name)

        # Cetak data ke terminal

        if sort == "Kepala":
            sort1 = 1
        elif sort == "Pinggang":
            sort1 = 2

        if mode == "Langsung":
            mode1 = 1
        elif mode == "Per Step":
            mode1 = 2

        print("Data Pasien dari Halaman Pertama:")
        print(f"Nama Pasien: {name}")
        print(f"Berat Pasien: {weight} kg")
        print(f"Jenis Terapi: {sort} == {sort1}")
        print(f"Metode Terapi: {mode} == {mode1}")
        print(f"Waktu Terapi: {time} menit")
        print(f"serial_port: {serial_port}")
        print(f"baud_rate: {baud_rate}")

        print("Berpindah ke halaman kedua...")

        self.btn_dashboard_1.clicked.connect(self.switch_to_dashboardPage)
        self.btn_dashboard_2.clicked.connect(self.switch_to_dashboardPage)

        # self.btn_start.clicked.connect(self.)
        """
        # Inisialisasi timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_real_time_data)
        self.data_list = []  # List untuk menyimpan data
        """

    """
    def start_real_time_data(self):
        # Mulai timer dengan interval 100 ms (0.1 detik)
        self.timer.start(100)
    """

    def switch_to_dashboardPage(self):
        self.stackedWidget.setCurrentIndex(0)

    def send_data_to_esp(self, weight, sort1, mode1, time):
        """
        Mengirim data ke ESP melalui serial
        """
        try:
            # Format data dalam JSON-like string
            data_to_send = f"{{'weight': {weight}, 'sort': {sort1}, 'mode': {mode1}, 'time': {time}}}"
            print(f"Mengirim data ke ESP: {data_to_send}")

            # Kirim data ke ESP
            self.serial_connection.write(data_to_send.encode("utf-8"))
        except Exception as e:
            print(f"Error saat mengirim data ke ESP: {e}")
        finally:
            # Tutup koneksi setelah pengiriman
            self.serial_connection.close()

    """
    def update_real_time_data(self):

        # Inisialisasi grafik dan timer
        self.chart = QtCharts.QChart()
        self.chart.legend().hide()

        self.number_series = QtCharts.QLineSeries()
        self.chart.addSeries(self.number_series)

        # Sumbu X dan Y
        self.axis_x = QtCharts.QValueAxis()
        self.axis_x.setRange(0, 500)  # Rentang sumbu X untuk 500 titik
        self.chart.addAxis(self.axis_x, Qt.AlignBottom)

        self.axis_y = QtCharts.QValueAxis()
        self.axis_y.setRange(0, 100)  # Set nilai Y sesuai dengan rentang data Anda
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)

        self.number_series.attachAxis(self.axis_x)
        self.number_series.attachAxis(self.axis_y)

        # Tampilkan grafik di view
        self.line_graph_view.setChart(self.chart)

        # Tambahkan data baru ke list
        new_data = random.randint(0, 100)  # Gantilah ini dengan data aktual Anda
        self.data_list.append(new_data)

        # Pastikan hanya menyimpan 500 data terakhir
        if len(self.data_list) > 500:
            self.data_list.pop(0)

        # Perbarui seri data di grafik
        self.number_series.clear()
        for i, value in enumerate(self.data_list):
            self.number_series.append(i, value)
    """

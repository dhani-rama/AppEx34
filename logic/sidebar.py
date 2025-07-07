# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 15:36:48 2024

@author: ramad
"""

from ui.main_ui import Ui_mainmenu
import threading
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtGui import Qt, QIcon
from PySide6 import QtCharts
from PySide6.QtCore import QTimer
import random
import serial
import math

# import RPi.GPIO as GPIO
import time


class MySideBar(QMainWindow, Ui_mainmenu):
    def __init__(
        self,
        pasien_id,
        name,
        nik,
        sex,
        address,
        weight,
        sort,
        mode,
        time_val,
        serial_port,
        baud_rate,
    ):
        super().__init__()
        self.setupUi(self)

        self.pasien_id = pasien_id
        self.name = name
        self.nik = nik
        self.sex = sex
        self.address = address
        self.serial_port = serial_port
        self.baud_rate = baud_rate
        self.sort = sort
        self.weight = weight
        self.mode = mode
        self.time = time_val

        self.icon_name_widget.setHidden(True)

        self.tv_name_patient.setText(name)

        # Inisialisasi komunikasi serial
        try:
            self.ser = serial.Serial(self.serial_port, self.baud_rate, timeout=1)
            print(f"Terhubung ke {self.serial_port} dengan baud rate {self.baud_rate}")
        except serial.SerialException as e:
            print(f"Kesalahan serial: {e}")
            self.ser = None  # Pastikan port serial tidak digunakan jika gagal

        print("\nData Pasien dari Halaman Pertama:")
        print(f"id Pasien: {pasien_id}")
        print(f"Nama Pasien: {name}")
        print(f"NIK Pasien: {nik}")
        print(f"Jenis Kelamin: {sex}")
        print(f"address: {address}")
        print(f"Berat Pasien: {weight} kg")
        print(f"Jenis Terapi: {sort}")
        print(f"Metode Terapi: {mode}")
        print(f"Waktu Terapi: {time_val} menit")
        print(f"serial_port: {serial_port}")
        print(f"baud_rate: {baud_rate}")

        print("Berpindah ke halaman kedua... \n\n")

        self.btn_dashboard_1.clicked.connect(self.switch_to_dashboardPage)
        self.btn_dashboard_2.clicked.connect(self.switch_to_dashboardPage)

        self.btn_start.clicked.connect(self.send_data_to_esp)

        # Grafik: inisialisasi data dan timer
        self.data_list = []
        self.time_list = []
        self.start_time = time.time()
        self.init_chart()

        self.chart_timer = QTimer()
        self.chart_timer.timeout.connect(self.update_chart)
        self.chart_timer.start(200)

        # Mulai thread untuk membaca data serial secara kontinu
        self.serial_thread = threading.Thread(target=self.serial_read_loop, daemon=True)
        self.serial_thread.start()

       

    def switch_to_dashboardPage(self):
        self.stackedWidget.setCurrentIndex(0)

    def send_data_to_esp(self):
        if not self.ser or not self.ser.is_open:
            print("Port serial belum terbuka.")
            return

        try:
            # Kirim jenis terapi (A untuk Kepala, B untuk Pinggang)
            if self.sort == "Kepala":
                self.ser.write(b"A")
                print("Kirim 'A' untuk KEPALA")
            elif self.sort == "Pinggang":
                self.ser.write(b"B")
                print("Kirim 'B' untuk PINGGANG")
            time.sleep(0.1)

            # Kirim metode terapi (C untuk Langsung, D untuk Per Step)
            if self.mode == "Langsung":
                self.ser.write(b"C")
                print("Kirim 'C' untuk METODE LANGSUNG")
            elif self.mode == "Per Step":
                self.ser.write(b"D")
                print("Kirim 'D' untuk METODE PER STEP")
            time.sleep(0.1)

            # Kirim berat pasien, format: "W{berat}\n" misalnya "W75\n"
            weight_command = f"W{self.weight}\n".encode("utf-8")
            self.ser.write(weight_command)
            print(f"Kirim berat: {self.weight}")
            time.sleep(0.1)

            # Kirim waktu terapi, format: "T{waktu}\n" misalnya "T30\n"
            time_command = f"T{self.time}\n".encode("utf-8")
            self.ser.write(time_command)
            print(f"Kirim waktu: {self.time} menit")
            time.sleep(0.1)

        except Exception as e:
            print("Kesalahan saat mengirim data:", e)

    def serial_read_loop(self):
        """Loop untuk membaca data yang dikirim dari ESP32 secara kontinu."""
        while True:
            try:
                if self.ser and self.ser.in_waiting:
                    # Baca satu baris data dari ESP32
                    line = self.ser.readline().decode("utf-8", errors="replace").strip()
                    if line:
                        if line.startswith("DATA,"):
                            # Cetak data sensor beserta sisa waktu
                            print("Data sensor dari ESP32:", line)
                            self.process_data_line(line)
                        else:
                            print("Pesan dari ESP32:", line)
                else:
                    time.sleep(0.1)
            except Exception as e:
                print("Kesalahan membaca data:", e)
                time.sleep(0.5)

    def process_data_line(self, line):
        try:
            # Hapus "DATA," dari awal
            line = line.replace("DATA,", "").strip()

            # Pisahkan berdasarkan koma
            parts = line.split(",")

            # Bersihkan setiap bagian agar hanya berisi angka
            def extract_value(part):
                return float(part.split("=")[-1].strip())

            if len(parts) >= 6:
                weight_pinggang = extract_value(parts[2])
                weight_kepala = extract_value(parts[3])

                # Hitung gaya sesuai rumus
                gaya_pinggang = weight_pinggang * (1.0 / 3.0)
                gaya_kepala = weight_kepala * (1.0 / 7.0)

                # Hitung waktu berlalu
                elapsed_time = time.time() - self.start_time

                # Pilih gaya berdasarkan mode
                gaya = gaya_kepala if self.sort == "Kepala" else gaya_pinggang

                if gaya >= 0.5:
                    # Simpan data untuk grafik
                    self.time_list.append(elapsed_time)
                    self.data_list.append(gaya)

                    # Batasi jumlah data untuk menjaga performa
                    if len(self.time_list) > 300:
                        self.time_list.pop(0)
                        self.data_list.pop(0)

        except Exception as e:
            print(f"Gagal parsing data sensor: {e}, Line: {line}")

    def init_chart(self):
        self.chart = QtCharts.QChart()
        self.chart.legend().hide()

        self.series = QtCharts.QLineSeries()
        self.chart.addSeries(self.series)

        self.axis_x = QtCharts.QValueAxis()
        self.axis_x.setLabelFormat("%ds")
        self.axis_x.setTitleText("Waktu (s)")
        self.axis_x.setRange(0, 60)
        self.chart.addAxis(self.axis_x, Qt.AlignBottom)
        self.series.attachAxis(self.axis_x)

        self.axis_y = QtCharts.QValueAxis()
        self.axis_y.setTitleText("Gaya (N)")
        self.axis_y.setRange(0, 10)
        self.axis_y.setTickInterval(5)  # Interval 5
        self.axis_y.setTickCount(
            13
        )  # Agar labelnya muncul dari 0 sampai 60 dengan interval 5
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)
        self.series.attachAxis(self.axis_y)

        self.line_graph_view.setChart(self.chart)

    def update_chart(self):
        self.series.clear()
        for t, g in zip(self.time_list, self.data_list):
            self.series.append(t, g)

        if self.time_list:
            # Update sumbu X agar menampilkan 60 detik terakhir
            self.axis_x.setRange(max(0, self.time_list[-1] - 60), self.time_list[-1])

            # Dapatkan nilai gaya maksimum dari data
            max_gaya = max(self.data_list)

            # Tentukan batas maksimum sumbu Y secara dinamis
            y_max = 10 if max_gaya <= 10 else math.ceil(max_gaya + 1)
            self.axis_y.setRange(0, y_max)

            # Buat label sumbu Y tetap rapi (interval 5)
            interval = 5
            tick_count = (y_max // interval) + 1
            self.axis_y.setTickInterval(interval)
            self.axis_y.setTickCount(tick_count)

    

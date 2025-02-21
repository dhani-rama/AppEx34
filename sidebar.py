# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 15:36:48 2024

@author: ramad
"""

from main_ui import Ui_mainmenu
import threading
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtGui import Qt, QIcon
from PySide6 import QtCharts
from PySide6.QtCore import QTimer
import random
import serial

# import RPi.GPIO as GPIO
import time


class MySideBar(QMainWindow, Ui_mainmenu):
    def __init__(self, name, weight, sort, mode, time_val, serial_port, baud_rate):
        super().__init__()
        self.setupUi(self)

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

        print("Data Pasien dari Halaman Pertama:")
        print(f"Nama Pasien: {name}")
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

        # Mulai thread untuk membaca data serial secara kontinu
        self.serial_thread = threading.Thread(target=self.serial_read_loop, daemon=True)
        self.serial_thread.start()

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
                        else:
                            print("Pesan dari ESP32:", line)
                else:
                    time.sleep(0.1)
            except Exception as e:
                print("Kesalahan membaca data:", e)
                time.sleep(0.5)


'''
    def send_data_to_esp(self):
        if not self.ser or not self.ser.is_open:
            print("Port serial belum terbuka atau tidak tersedia.")
            return

        command = self.sort
        mode1 = self.mode
        weight1 = str(self.weight)  # Konversi weight ke string
        time1 = str(self.time)  # Konversi time ke string

        try:
            # Kirim command
            if command == "Kepala":
                self.ser.write(b"A")
                print("Perintah 'A' telah dikirim")
                self.read_response()

            elif command == "Pinggang":
                self.ser.write(b"B")
                print("Perintah 'B' telah dikirim")
                self.read_response()

            # Kirim mode
            if mode1 == "Langsung":
                self.ser.write(b"C")
                print("Perintah 'C' telah dikirim")
                self.read_response()

            elif mode1 == "Per Step":
                self.ser.write(b"D")
                print("Perintah 'D' telah dikirim")
                self.read_response()

            # Kirim berat
            weight_command = f"W{weight1}\n".encode("utf-8")  # Format dengan prefix 'W'
            self.ser.write(weight_command)
            print(f"Berat {weight1} kg telah dikirim")
            self.read_response()

            # Kirim waktu
            time_command = f"T{time1}\n".encode("utf-8")  # Format dengan prefix 'T'
            self.ser.write(time_command)
            print(f"Waktu {time1} menit telah dikirim")
            self.read_response()

        except Exception as e:
            print(f"Kesalahan: {e}")
            
    def read_response(self):
        """Baca respons dari ESP32."""
        try:
            response = self.ser.readline()
            decoded_response = response.decode("utf-8").strip()
            if decoded_response:
                print(f"Respons dari ESP32: {decoded_response}")
        except UnicodeDecodeError:
            print("Respons tidak dapat didekode, mungkin bukan teks.")

    def close_serial(self):
        """Menutup komunikasi serial jika diperlukan."""
        if self.ser and self.ser.is_open:
            self.ser.close()
            print("Komunikasi serial ditutup.")
'''
# def send_data_to_esp(self):

#     port = self.serial_port
#     baud_rate = self.baud_rate
#     command = self.sort
#     mode1 = self.mode
#     weight1 = self.weight
#     time1 = self.time

#     try:
#         ser = serial.Serial(port, baud_rate, timeout=1)
#         print(f"Terhubung ke {port} dengan baud rate {baud_rate}")

#         # while True:
#         if command == "Kepala":
#             ser.write(b"A")
#             print("Perintah 'A' telah dikirim")

#             response = ser.readline()

#             try:
#                 decoded_response = response.decode("utf-8").strip()
#                 if decoded_response:
#                     print(f"Respons dari ESP32: {decoded_response}")
#                     print(f"Led ON \n")

#             except UnicodeDecodeError:
#                 print(
#                     "Respons Jenis Terapi Kepala tidak dapat didekode, mungkin bukan teks."
#                 )

#         elif command == "Pinggang":
#             ser.write(b"B")
#             print("Perintah 'B' telah dikirim")

#             response = ser.readline()

#             try:
#                 decoded_response = response.decode("utf-8").strip()
#                 if decoded_response:
#                     print(f"Respons dari ESP32: {decoded_response}")
#                     print(f"Led ON \n")

#             except UnicodeDecodeError:
#                 print(
#                     "Respons Jenis Terapi Pinggang tidak dapat didekode, mungkin bukan teks."
#                 )

#         elif mode1 == "Langsung":
#             ser.write(b"C")
#             print("Perintah 'C' telah dikirim")

#             response = ser.readline()

#             try:
#                 decoded_response = response.decode("utf-8").strip()
#                 if decoded_response:
#                     print(f"Respons dari ESP32: {decoded_response}")
#                     print(f"Led ON \n")

#             except UnicodeDecodeError:
#                 print(
#                     "Respons Mode Terapi Langsung tidak dapat didekode, mungkin bukan teks."
#                 )

#         elif mode1 == "Per Step":
#             ser.write(b"D")
#             print("Perintah 'D' telah dikirim")

#             response = ser.readline()

#             try:
#                 decoded_response = response.decode("utf-8").strip()
#                 if decoded_response:
#                     print(f"Respons dari ESP32: {decoded_response}")
#                     print(f"Led ON \n")

#             except UnicodeDecodeError:
#                 print(
#                     "Respons Mode Per Step Langsung tidak dapat didekode, mungkin bukan teks."
#                 )

#         else:
#             print("Perintah tidak dikenali.")

#     except serial.SerialException as e:
#         print(f"Kesalahan serial: {e}")

#     except Exception as e:
#         print(f"Kesalahan: {e}")

#     finally:
#         # Menutup komunikasi serial
#         if "ser" in locals() and ser.is_open:
#             ser.close()
#             print("Komunikasi serial ditutup.")

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

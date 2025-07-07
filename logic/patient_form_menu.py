from ui.patient_form_ui import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow
from logic.sidebar import MySideBar


class MyPatientForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Hubungkan tombol dengan fungsi handle_save_button
        self.btn_save_patient.clicked.connect(self.handle_save_button)

    def handle_save_button(self):
        # Ambil data dari inputan pengguna
        name = self.et_name_patient.text()
        weight = self.et_weight_patient.text()
        sort = self.et_sort_patient.currentText()
        mode = self.et_mode_patient.currentText()
        time = self.et_time_patient.text()
        serial_port = "COM3"
        baud_rate = 115200

        # Pindah ke halaman kedua dan parsing data
        self.second_window = MySideBar(
            name, weight, sort, mode, time, serial_port, baud_rate
        )
        self.second_window.show()

        # (Opsional) Tutup jendela utama
        self.close()

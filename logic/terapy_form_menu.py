from PySide6.QtWidgets import QApplication, QMainWindow
from logic.sidebar import MySideBar
from ui.terapy_form_ui import Ui_MainWindow
from db.firebase_config import get_db_root


class TerapyFormMenu(QMainWindow, Ui_MainWindow):
    def __init__(self, pasien_id, name, nik, sex, address):
        super().__init__()
        self.setupUi(self)

        self.root_ref = get_db_root()

        # Data pasien yang diteruskan ke halaman ini
        self.pasien_id = pasien_id
        self.name = name
        self.nik = nik
        self.sex = sex
        self.address = address

        print("\nHasil parsing data dari halaman sebelah")
        print("ID Pasien : ", pasien_id)
        print("Nama Pasien : ", name)
        print("NIK: ", nik)
        print("Sex: ", sex)
        print("Address: ", address)

        self.et_name.setText(self.name)

        self.btn_save.clicked.connect(self.handle_save_button)

    #event button simpan data
    def handle_save_button(self):

        weight = self.et_weight.text()
        sort = self.et_type_terapy.currentText()
        mode = self.et_method_terapy.currentText()
        time = self.et_time.text()
        serial_port = "COM3"
        baud_rate = 115200

        # Pindah ke halaman kedua dan parsing data
        self.second_window = MySideBar(
            self.pasien_id,
            self.name,
            self.nik,
            self.sex,
            self.address,
            weight,
            sort,
            mode,
            time,
            serial_port,
            baud_rate,
        )
        self.second_window.show()

        # (Opsional) Tutup jendela utama
        self.close()

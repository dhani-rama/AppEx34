from ui.sign_up_patient_ui import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from logic.sidebar import MySideBar
from firebase_admin import db
from db.firebase_config import get_db_root
from datetime import datetime
from logic.main_list_patient import ListPatientMenu


class SignUpPatientMenu(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.root_ref = get_db_root()

        self.btn_sign_up.clicked.connect(self.create_user)

    def validate_id_user(self, nik: str) -> bool:

        data_user = self.root_ref.child("Data User").get()

        if data_user:
            for key, value in data_user.items():
                if str(value.get("nik")) == nik:
                    return True

        return False

    #Buat pasien baru
    def create_user(self):
        username = self.et_username.text().strip()
        nik = self.et_nik.text().strip()
        sex = self.et_sex.currentText().strip()
        address = self.et_address.text().strip()

        if self.validate_id_user(nik):
            QMessageBox.warning(
                self,
                "Pendaftaran Gagal",
                "NIK sudah terdaftar. Silakan gunakan NIK lain atau periksa kembali.",
            )
            return  # Kembali tanpa hapus input, user bisa ubah NIK saja

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        user_id = f"{timestamp}_{nik}"

        # Referensi ke node "Data User"
        user_ref = db.reference(f"Data User/{user_id}")

        # Simpan ke Firebase
        user_ref.set(
            {"nama": username, "nik": nik, "jenis_kelamin": sex, "alamat": address}
        )

        self.move_list = ListPatientMenu()

        self.move_list.show()

        # (Opsional) Tutup jendela utama
        self.close()

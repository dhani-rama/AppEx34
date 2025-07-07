from ui.main_dashboard_ui import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from logic.sign_up_patient_menu import SignUpPatientMenu
from logic.main_list_patient import ListPatientMenu
from firebase_admin import db
from db.firebase_config import get_db_root


class MainDashboard(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_sign_up.clicked.connect(self.move_to_sign_up)
        self.btn_list_patient.clicked.connect(self.move_to_list)

    #Pindah ke halaman list patient menu
    def move_to_list(self):
        self.move_list = ListPatientMenu()

        self.move_list.show()

        # (Opsional) Tutup jendela utama
        self.close()

    #Pindah ke halaman sign up patient menu
    def move_to_sign_up(self):
        self.signup = SignUpPatientMenu()

        self.signup.show()

        # (Opsional) Tutup jendela utama
        self.close()

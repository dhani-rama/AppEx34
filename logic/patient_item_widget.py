from PySide6.QtWidgets import QWidget
from ui.widget_list_patient_ui import Ui_containerPasien


class PatientItemWidget(QWidget):
    def __init__(self, nama: str, nik: str):
        super().__init__()
        self.ui = Ui_containerPasien()
        self.ui.setupUi(self)

        self.ui.username_patient.setText(nama)
        self.ui.nik_patient.setText(nik)

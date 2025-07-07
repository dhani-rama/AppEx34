# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QApplication
import sys
from logic.patient_form_menu import MyPatientForm
from logic.main_dashboard import MainDashboard

app = QApplication.instance()

if app is None:  # Jika belum ada, buat instance baru
    app = QApplication(sys.argv)

# window = MyPatientForm()
window = MainDashboard()

window.show()
app.exec()

from PySide6.QtWidgets import QMainWindow, QListWidget, QListWidgetItem, QMessageBox
from ui.list_patient_ui import Ui_MainWindow
from logic.patient_item_widget import PatientItemWidget
from db.firebase_config import get_db_root
from logic.terapy_form_menu import TerapyFormMenu


class ListPatientMenu(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Pastikan menggunakan QListWidget, bukan QListView
        self.listPasienWidget = QListWidget(self.centralwidget)
        self.listPasienWidget.setGeometry(10, 130, 781, 441)

        self.root_ref = get_db_root()
        self.load_data_pasien()

        self.listPasienWidget.itemClicked.connect(self.on_item_click)

    #Menampilkan data pasien
    def load_data_pasien(self):
        data = self.root_ref.child("Data User").get()

        #Kondisi jika tidak ada di database
        if not data:
            return

        for key, value in data.items():
            nama = value.get("nama", "Tidak ada nama")
            nik = value.get("nik", "-")
            pasien_id = key

            widget = PatientItemWidget(nama, nik)
            list_item = QListWidgetItem()
            list_item.setSizeHint(widget.sizeHint())

            self.listPasienWidget.addItem(list_item)
            self.listPasienWidget.setItemWidget(list_item, widget)

            # Simpan id pasien untuk keperluan detail
            list_item.setData(1, pasien_id)

    def on_item_click(self, item: QListWidgetItem):
        pasien_id = item.data(1)  # Ambil pasien_id yang sudah disimpan
        self.open_detail_patient(pasien_id)

    def open_detail_patient(self, pasien_id):
        # Ambil data pasien berdasarkan ID
        data = self.root_ref.child("Data User").child(pasien_id).get()

        if not data:
            QMessageBox.warning(self, "Error", "Data pasien tidak ditemukan!")
            return

        # Ambil data pasien
        nama = data.get("nama", "Tidak ada nama")
        nik = data.get("nik", "-")
        sex = data.get("jenis_kelamin", "-")
        address = data.get("alamat", "-")

        print("nama : ", nama)
        print("nik : ", nik)
        print("sex : ", sex)
        print("address : ", address)

        # Buka halaman detail
        self.detail_window = TerapyFormMenu(pasien_id, nama, nik, sex, address)
        self.detail_window.show()
        self.close()

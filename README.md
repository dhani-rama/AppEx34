# Monitoring Alat Traksi

Sistem alat traksi berbasis dekstop yang digunakan untuk monitoring pasien yang sedang terapi menggunakan alat traksi. 

## Struktur Proyek

```
.
├── db/        # konfigurasi firebase
├── esp32/     # micro controller
├── logic/     # program logic desktop (python)
├── ui/        # program ui desktop (python)
├── ui_qt/     # program ui dari qt
├── resources/ # asset dalam bentuk python dari hasil convert qrc 
└── main_window.py # main program
```

## Prasyarat

- Python 3.9.13 (Atau Versi Lebih Tinggi)
- Qt Creator
- Database (Firebase)
- Esp32

## Instalasi

1. Clone repository:
   ```bash
   git clone https://github.com/dhani-rama/AppEx34.git
   ```

2. Install Dependencies:
   ```bash
   pip install requirements.txt
   ```

3. Jalankan program:
   ```bash
   python mainwindow.py
   ```




 

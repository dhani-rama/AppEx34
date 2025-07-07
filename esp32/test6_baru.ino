#include <AccelStepper.h>
#include "ACS712.h"
#include <HX711.h>

// --- Konfigurasi pin dan variabel global ---
const int dirPin = 27;
const int stepPin = 26;
const int enablePin = 14;
const int dirSpPin = 33;     // Pin Direction Stepper (SP)
const int stepSpPin = 32;    // Pin Step Pulse Stepper (SP)
const int enableSpPin = 25;  // Pin Enable Stepper (SP)

int bobot = 0;       // Berat pasien yang diterima dari Python
int metode = 0;      // Metode terapi (1: Langsung, 2: Per Step)
int STEP = 0;
int waktu = 0;       // Waktu terapi dalam milidetik
unsigned long startTime = 0;  // Waktu mulai terapi

#define DT 18
#define SCK 19
#define DT2 22
#define SCK2 23
#define LS_K 15
#define LS_P 13
bool State_K = 0;
bool State_P = 0;

HX711 scale;
HX711 scale2;
float calibration_factor = -44.58;
float calibration_factor2 = -44.96;
float weight = 0.00;    // Berat dari load cell 1 (Pinggang)
float weight2 = 0.00;   // Berat dari load cell 2 (Kepala)
int speed = 0;
int mode = 0;      // 1: Kepala, 2: Pinggang

#define motorInterfaceType 1
unsigned long previousTime_1 = 0;  // Untuk interval pengiriman data sensor

// Inisialisasi motor
AccelStepper myStepper(motorInterfaceType, stepPin, dirPin);
AccelStepper myStepperSp(motorInterfaceType, stepSpPin, dirSpPin);

// Konfigurasi sensor arus
const int pinACS712 = 35;
const int pinACS712_2 = 34;
const float VCC = 3.3;
const float ACS712_MV_PER_AMPERE = 100;
const float ZERO_POINT = 2.39;

void setup() {
  Serial.begin(115200);
  
  // Set pin input/output
  pinMode(LS_K, INPUT);
  pinMode(LS_P, INPUT);
  pinMode(enablePin, OUTPUT);
  digitalWrite(enablePin, LOW);
  pinMode(enableSpPin, OUTPUT);
  digitalWrite(enableSpPin, LOW);
  
  myStepper.setMaxSpeed(1000);
  myStepper.setAcceleration(500);
  myStepper.setCurrentPosition(0);
  
  myStepperSp.setMaxSpeed(1000);
  myStepperSp.setAcceleration(500);
  
  initLoadCell();
  initLoadCell2();
}

void loop() {
  // --- Pembacaan sensor ---
  int nilaiAdc1 = analogRead(pinACS712);
  float tegangan1 = (nilaiAdc1 * VCC) / 4095.0;
  float arus1 = (tegangan1 - ZERO_POINT) / (ACS712_MV_PER_AMPERE / 1000);

  int nilaiAdc2 = analogRead(pinACS712_2);
  float tegangan2 = (nilaiAdc2 * VCC) / 4095.0;
  float arus2 = (tegangan2 - ZERO_POINT) / (ACS712_MV_PER_AMPERE / 1000);

  long rawWeight = scale.get_units(1);
  weight = rawWeight < 0 ? 0 : rawWeight;
  weight = weight / 1000;

  long rawWeight2 = scale2.get_units(1);
  weight2 = rawWeight2 < 0 ? 0 : rawWeight2;
  weight2 = weight2 / 1000;

  // --- Mesin state untuk pengaturan terapi ---
  switch (STEP) {
    case 0:
      Serial.println("HOMING....");
      if (digitalRead(LS_P) == 0 && State_P == 0) {
        myStepperSp.setSpeed(-500);
      } else {
        myStepperSp.setSpeed(0);
        State_P = 1;
      }
      if (digitalRead(LS_K) == 0 && State_K == 0) {
        myStepper.setSpeed(500);
      } else {
        myStepper.setSpeed(0);
        State_K = 1;
      }
      if (digitalRead(LS_P) == 1 && State_K == 1) {
        initLoadCell();
        initLoadCell2();
        STEP = 1;
        State_K = 0;
        State_P = 0;
        myStepper.setCurrentPosition(0);
        myStepperSp.setCurrentPosition(0);
      }
      break;
      
    case 1:
      // Terima perintah jenis terapi dari Python: 'A' (Kepala) atau 'B' (Pinggang)
      if (Serial.available() > 0) {
        char cmd = Serial.read();
        if (cmd == 'A') {
          Serial.println("KEPALA");
          mode = 1;
          STEP = 11;  // Lanjut ke penerimaan metode terapi
        } else if (cmd == 'B') {
          Serial.println("PINGGANG");
          mode = 2;
          STEP = 11;  // Lanjut ke penerimaan metode terapi
        } else {
          Serial.println("Perintah terapi tidak valid.");
        }
      }
      break;
      
    case 11:
      // Terima perintah metode terapi dari Python: 'C' (Langsung) atau 'D' (Per Step)
      if (Serial.available() > 0) {
        char cmd = Serial.read();
        if (cmd == 'C') {
          Serial.println("METODE LANGSUNG");
          metode = 1;  // 1 untuk Langsung
          STEP = 2;    // Lanjut ke penerimaan berat pasien
        } else if (cmd == 'D') {
          Serial.println("METODE PER STEP");
          metode = 2;  // 2 untuk Per Step
          STEP = 2;    // Lanjut ke penerimaan berat pasien
        } else {
          Serial.println("Perintah metode tidak valid.");
        }
      }
      break;
      
    case 2:
      // Terima input berat pasien dari Python dengan format: "W{nilai}\n"
      if (Serial.available() > 0) {
        String input = Serial.readStringUntil('\n');
        input.trim();
        if (input.charAt(0) == 'W') {
          String valueStr = input.substring(1); // Ambil angka setelah 'W'
          bobot = valueStr.toInt();
          Serial.print("Berat pasien diterima: ");
          Serial.println(bobot);
          STEP = 5;  // Lanjut ke penerimaan waktu terapi
        } else {
          Serial.println("Format berat tidak valid.");
        }
      }
      break;
      
    case 5:
      // Terima input waktu terapi dari Python dengan format: "T{nilai}\n"
      if (Serial.available() > 0) {
        String input = Serial.readStringUntil('\n');
        input.trim();
        if (input.charAt(0) == 'T') {
          String timeStr = input.substring(1); // Ambil angka setelah 'T'
          int waktuMenit = timeStr.toInt();
          waktu = waktuMenit * 60 * 1000;  // Konversi menit ke milidetik
          Serial.print("Waktu terapi diterima: ");
          Serial.print(waktuMenit);
          Serial.println(" menit");
          // Lanjut ke proses terapi berdasarkan mode
          if (mode == 1) {
            STEP = 3;  // Untuk terapi KEPALA
          } else {
            STEP = 4;  // Untuk terapi PINGGANG
          }
        } else {
          Serial.println("Format waktu tidak valid.");
        }
      }
      break;
      
    case 3:  // Proses terapi untuk KEPALA
      speed = (bobot - weight2) * 20;
      if (speed > 50) speed = 50;
      if (speed < -50) speed = -50;
      myStepperSp.setSpeed(speed);
      if (abs(bobot - weight2) <= 0.05) {
        STEP = 6;
        startTime = millis();
      }
      break;
      
    case 4:  // Proses terapi untuk PINGGANG
      speed = (bobot - weight) * -20;
      if (speed > 50) speed = 50;
      if (speed < -50) speed = -50;
      myStepper.setSpeed(speed);
      if (abs(bobot - weight) <= 0.05) {
        STEP = 6;
        startTime = millis();
      }
      break;
      
    case 6:
      // Hentikan motor dan hitung sisa waktu terapi
      myStepper.setSpeed(0);
      myStepperSp.setSpeed(0);
      unsigned long elapsedTime = millis() - startTime;
      // Jika terapi belum selesai, hitung sisa waktu
      unsigned long remainingTime = (waktu > elapsedTime) ? (waktu - elapsedTime) : 0;
      
      // Tampilkan sisa waktu di monitor serial (bisa juga dipakai untuk log internal)
      int remMinutes = remainingTime / 60000;
      int remSeconds = (remainingTime % 60000) / 1000;
      Serial.print("Sisa Waktu: ");
      Serial.print(remMinutes);
      Serial.print(" menit ");
      Serial.print(remSeconds);
      Serial.println(" detik");
      
      // Jika waktu habis, reset atau tanyakan kelanjutan terapi
      if (remMinutes == 0 && remSeconds == 0) {
        Serial.println("WAKTU HABIS");
        if (metode == 1) {
          STEP = 0;
        }
        if (metode == 2) {
          Serial.println("LANJUTKAN ?");
          Serial.println("1. YA");
          Serial.println("2. TIDAK");
          if (Serial.available() > 0) {
            String input = Serial.readStringUntil('\n');
            input.trim();
            int pilihan = input.toInt();
            if (pilihan == 1) {
              STEP = 2;
            } else {
              STEP = 0;
            }
          }
        }
      }
      break;
  }
  
  myStepper.runSpeed();
  myStepperSp.runSpeed();

  // --- Optional: Kirim data sensor secara periodik ke Python ---
  unsigned long currentTime = millis();
  if (currentTime - previousTime_1 >= 5000) {
    // Mulai cetak data dalam satu baris CSV
    // Format: DATA,<arus1>,<arus2>,<weight_pinggang>,<weight_kepala>,<jarak_pinggang>,<jarak_kepala>,<sisa_menit>,<sisa_detik>
    Serial.print("DATA,");
    Serial.print(arus1);
    Serial.print(",");
    Serial.print(arus2);
    Serial.print(",");
    Serial.print(weight, 2);
    Serial.print(",");
    Serial.print(weight2, 2);
    Serial.print(",");
    Serial.print(static_cast<float>(myStepper.currentPosition()) / 80.0, 2);
    Serial.print(",");
    Serial.print(static_cast<float>(myStepperSp.currentPosition()) / 80.0, 2);
    
    // Jika terapi sedang berjalan (STEP 6), kirim sisa waktu; jika tidak, kirim 0,0
    if (STEP == 6) {
      unsigned long elapsedTime = millis() - startTime;
      unsigned long remainingTime = (waktu > elapsedTime) ? (waktu - elapsedTime) : 0;
      int remMinutes = remainingTime / 60000;
      int remSeconds = (remainingTime % 60000) / 1000;
      Serial.print(",");
      Serial.print(remMinutes);
      Serial.print(",");
      Serial.println(remSeconds);
    } else {
      Serial.println(",0,0");
    }
    
    previousTime_1 = currentTime;
  }
}

void initLoadCell() {
  scale.begin(DT, SCK);
  if (scale.wait_ready_timeout(1000)) {
    Serial.println("HX711 (Load Cell 1) ready.");
  } else {
    Serial.println("HX711 (Load Cell 1) not detected.");
    while (1);
  }
  scale.set_scale(calibration_factor);
  scale.tare();
  Serial.println("Tare for Load Cell 1 completed.");
  delay(2000);
}

void initLoadCell2() {
  scale2.begin(DT2, SCK2);
  if (scale2.wait_ready_timeout(1000)) {
    Serial.println("HX711 (Load Cell 2) ready.");
  } else {
    Serial.println("HX711 (Load Cell 2) not detected.");
    while (1);
  }
  scale2.set_scale(calibration_factor2);
  scale2.tare();
  Serial.println("Tare for Load Cell 2 completed.");
  delay(2000);
}

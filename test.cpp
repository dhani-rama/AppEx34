// Include the AccelStepper Library
#include <AccelStepper.h>
#include "ACS712.h"
#include <HX711.h>

// Define pin connections
const int dirPin = 27;
const int stepPin = 26;
const int enablePin = 14;
const int dirSpPin = 33;     // Pin Direction Stepper (SP)
const int stepSpPin = 32;    // Pin Step Pulse Stepper (SP)
const int enableSpPin = 25;  // Pin Enable Stepper (SP)
float distance_mm = 0;
int bobot = 0;
int metode = 0;
int STEP = 0;
int waktu = 0;
unsigned long startTime = 0;

#define DT 18    // Pin data HX711 (Load cell 1)
#define SCK 19   // Pin clock HX711 (Load cell 1)
#define DT2 22   // Pin data HX711 (Load cell 2)
#define SCK2 23  // Pin clock HX711 (Load cell 2)
#define LS_K 15
#define LS_P 13
bool State_K = 0;
bool State_P = 0;

HX711 scale;
HX711 scale2;
float calibration_factor = -44.58;   // Faktor kalibrasi load cell
float calibration_factor2 = -44.96;  // Faktor kalibrasi load cell
float weight = 0.00;
float weight2 = 0.00;
int selector = 0;
int speed = 0;
int mode = 0;


// Define motor interface type
#define motorInterfaceType 1
unsigned long previousTime_1 = 0;
unsigned long prev_terapi = 0;

// Create instances for motors
AccelStepper myStepper(motorInterfaceType, stepPin, dirPin);
AccelStepper myStepperSp(motorInterfaceType, stepSpPin, dirSpPin);  // Stepper SP

const int pinACS712 = 35;                // Pin analog ESP32 untuk ACS712 (Arus utama)
const int pinACS712_2 = 34;              // Pin analog ESP32 untuk ACS712 (Arus tambahan)
const float VCC = 3.3;                   // Tegangan VCC ESP32
const float ACS712_MV_PER_AMPERE = 100;  // Sensitivitas ACS712 (100 mV/A)
const float ZERO_POINT = 2.39;           // Titik nol tegangan ACS712 (2.5 V)

void setup() {
  // Initialize serial communication
  Serial.begin(115200);

  // Set pin modes
  pinMode(LS_K, INPUT);
  pinMode(LS_P, INPUT);
  pinMode(enablePin, OUTPUT);
  digitalWrite(enablePin, LOW);  // Enable the driver for main stepper

  pinMode(enableSpPin, OUTPUT);
  digitalWrite(enableSpPin, LOW);  // Enable the driver for SP stepper

  // Set the maximum speed and acceleration factor for both steppers
  myStepper.setMaxSpeed(1000);
  myStepper.setAcceleration(500);
  myStepper.setCurrentPosition(0);

  myStepperSp.setMaxSpeed(1000);     // Speed for SP stepper
  myStepperSp.setAcceleration(500);  // Acceleration for SP stepper
  initLoadCell();
  initLoadCell2();
}

void loop() {
  // Read current sensor data from ACS712 (pin 34)
  int nilaiAdc1 = analogRead(pinACS712);
  float tegangan1 = (nilaiAdc1 * VCC) / 4095.0;
  float arus1 = (tegangan1 - ZERO_POINT) / (ACS712_MV_PER_AMPERE / 1000);

  // Read current sensor data from ACS712 (pin 35)
  int nilaiAdc2 = analogRead(pinACS712_2);
  float tegangan2 = (nilaiAdc2 * VCC) / 4095.0;
  float arus2 = (tegangan2 - ZERO_POINT) / (ACS712_MV_PER_AMPERE / 1000);

  // Pembacaan data Load Cell 1
  long rawWeight = scale.get_units(1);     // Membaca rata-rata 10 pengukuran
  weight = rawWeight < 0 ? 0 : rawWeight;  // Pastikan nilai tidak negatif
  weight = weight / 1000;

  // Pembacaan data Load Cell 2
  long rawWeight2 = scale2.get_units(1);
  weight2 = rawWeight2 < 0 ? 0 : rawWeight2;
  weight2 = weight2 / 1000;
  // // Check for serial input
  switch (STEP) {
    case 0:
      Serial.println("HOMING....");
      metode = 0;
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
      Serial.println("PILIH TERAPI");
      Serial.println("1. KEPALA");
      Serial.println("2. PINGGANG");
      if (Serial.available() > 0) {
        String input = Serial.readStringUntil('\n');
        input.trim();  // Remove whitespace
        // Convert input to integer for speed
        selector = input.toInt();
        if (selector == 1) {
          Serial.println("KEPALA");
          mode = 1;
          STEP = 11;
        }
        if (selector == 2) {
          Serial.println("PINGGANG");
          mode = 2;
          STEP = 11;
        } else {
          Serial.println("TIDAK VALID silahkan pilih 1 atau 2");
        }
      }
      break;
    case 11:
      Serial.println("PILIH METODE :");
      Serial.println("1. LANGSUNG");
      Serial.println("2. PER STEP");
      if (Serial.available() > 0) {
        String input = Serial.readStringUntil('\n');
        input.trim();  // Remove whitespace
        // Convert input to integer for speed
        metode = input.toInt();
        STEP = 2;
      }
      break;
    case 2:
      Serial.println("MASUKAN BOBOT :.....KG");
      if (Serial.available() > 0) {
        String input = Serial.readStringUntil('\n');
        input.trim();  // Remove whitespace
        // Convert input to integer for speed
        bobot = input.toInt();
        STEP = 5;
      }
      break;
    case 5:
      Serial.println("MASUKAN WAKTU :..... M");
      if (Serial.available() > 0) {
        String input = Serial.readStringUntil('\n');
        input.trim();  // Remove whitespace
        // Convert input to integer for speed
        waktu = input.toInt() * 60 * 1000;
        if (mode == 1) {
          STEP = 3;
        } else {
          STEP = 4;
        }
      }
      break;
    case 3:  //KEPALA
      speed = (bobot - weight2) * 20;
      if (speed > 50) {
        speed = 50;
      }
      if (speed < -50) {
        speed = -50;
      }
      myStepperSp.setSpeed(speed);
      if (abs(bobot - weight2) <= 0.05) {
        STEP = 6;
        startTime = millis();
      }
      break;

    case 4:  //PINGGANG
      speed = (bobot - weight) * -20;
      if (speed > 50) {
        speed = 50;
      }
      if (speed < -50) {
        speed = -50;
      }
      myStepper.setSpeed(speed);
      if (abs(bobot - weight) <= 0.05) {
        STEP = 6;
        startTime = millis();
      }
      break;
    case 6:
      myStepper.setSpeed(0);
      myStepperSp.setSpeed(0);
      unsigned long elapsedTime = millis() - startTime;
      unsigned long remainingTime = (waktu > elapsedTime) ? (waktu - elapsedTime) : 0;

      int minutes = remainingTime / 60000;
      int seconds = (remainingTime % 60000) / 1000;

      Serial.print("Sisa Waktu: ");
      Serial.print(minutes);
      Serial.print(" menit ");
      Serial.print(seconds);
      Serial.println(" detik");

      if (minutes == 0 && seconds == 0) {
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
            input.trim();  // Remove whitespace
            // Convert input to integer for speed
            selector = input.toInt();
            if (selector == 1) {
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

  // Periodically print current sensor data
  unsigned long currentTime = millis();
  if (currentTime - previousTime_1 >= 5000) {
    Serial.print("Current (MTR_KEPALA): ");
    Serial.print(arus1);
    Serial.println(" A");

    Serial.print("Current (MTR_PINGGANG): ");
    Serial.print(arus2);
    Serial.println(" A");

    Serial.print("Weight Pinggang: ");
    Serial.print(weight, 2);  // Berat dengan 2 angka desimal
    Serial.println(" KG");

    Serial.print("Weight Kepala: ");
    Serial.print(weight2, 2);  // Berat load cell 2 dengan 2 angka desimal
    Serial.println(" KG");
    Serial.print("Jarak Motor Pinggang: ");
    Serial.println(static_cast<float>(myStepper.currentPosition()) / 80.0, 2);
    Serial.print("Jarak Motor Kepala: ");
    Serial.println(static_cast<float>(myStepperSp.currentPosition()) / 80.0, 2);

    previousTime_1 = currentTime;
  }
}

void initLoadCell() {
  scale.begin(DT, SCK);  // Memulai komunikasi dengan HX711
  if (scale.wait_ready_timeout(1000)) {
    Serial.println("HX711 (Load Cell 1) ready.");
  } else {
    Serial.println("HX711 (Load Cell 1) not detected.");
    while (1)
      ;  // Program berhenti jika tidak ada koneksi dengan HX711
  }

  scale.set_scale(calibration_factor);  // Menetapkan faktor kalibrasi
  scale.tare();                         // Lakukan tare awal (set nilai awal ke 0)
  Serial.println("Tare for Load Cell 1 completed.");
  delay(2000);  // Memberi waktu untuk stabilisasi tare
}

void initLoadCell2() {
  scale2.begin(DT2, SCK2);  // Memulai komunikasi dengan HX711
  if (scale2.wait_ready_timeout(1000)) {
    Serial.println("HX711 (Load Cell 2) ready.");
  } else {
    Serial.println("HX711 (Load Cell 2) not detected.");
    while (1)
      ;  // Program berhenti jika tidak ada koneksi dengan HX711
  }

  scale2.set_scale(calibration_factor2);  // Menetapkan faktor kalibrasi
  scale2.tare();                          // Lakukan tare awal (set nilai awal ke 0)
  Serial.println("Tare for Load Cell 2 completed.");
  delay(2000);  // Memberi waktu untuk stabilisasi tare
}
// First proof of concept for a programmer for my 8-bit breadboard computer.
// Instead of manually flipping dip switches, this would allow to input the raw machine code via a keypad.

#include <LiquidCrystal.h>
#include <Keypad.h>

int pin = 22;

const byte ROWS = 4;
const byte COLS = 4;

char hexaKeys[ROWS][COLS] = {
  {'1', '2', '3', 'A'},
  {'4', '5', '6', 'B'},
  {'7', '8', '9', 'C'},
  {'*', '0', '#', 'D'}
};

byte rowPins[ROWS] = {53, 52, 51, 50};
byte colPins[COLS] = {49, 48, 47, 46};

Keypad customKeypad = Keypad( makeKeymap(hexaKeys), rowPins, colPins, ROWS, COLS);

LiquidCrystal lcd(7, 8, 9, 10, 11, 12);

void setup() {
  for (int pin = 22; pin <= 29; pin++) {
    pinMode(pin, OUTPUT);
  }
  lcd.begin(16, 2);
}

void loop() {
  char customKey = customKeypad.getKey();
  while (pin >= 22 && pin <= 29) {

    char customKey = customKeypad.getKey();
    if (customKey) {
      switch (customKey) {
        case '0':
          digitalWrite(pin, 0);
          lcd.print(customKey);
          pin++;
          break;
        case '1':
          digitalWrite(pin, 1);
          lcd.print(customKey);
          pin++;
          break;
        default:
          break;
      }
    }
  }
  lcd.setCursor(0, 1);
  if (pin > 29) {
    pin = 32;
  }
  while (pin >= 32 && pin <= 35) {
    char customKey = customKeypad.getKey();
    if (customKey) {
      switch (customKey) {
        case '0':
          digitalWrite(pin, 0);
          lcd.print(customKey);
          pin++;
          break;
        case '1':
          digitalWrite(pin, 1);
          lcd.print(customKey);
          pin++;
          break;
        default:
          break;
      }
      if (customKey == '*') {
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Programming.");
        delay(2500);
        lcd.clear();
        lcd.setCursor(0, 0);
        pin = 22;
      }
    }
  }
}

// Using the Bluetooth features of the ESP32, and an Android app built with MIT App Inventor, this code allows for programming my 8-bit computer wirelessly.


#include "BluetoothSerial.h"

//opcode values
#define NOP 0b00000000
#define LDA 0b00001000
#define ADD 0b00010000
#define SUB 0b00011000
#define STA 0b00100000
#define LDI 0b00101000
#define JMP 0b00110000
#define JC  0b00111000
#define JZ  0b01000000
#define CMP 0b01001000
#define INC 0b01010000
#define DEC 0b01011000
#define IN  0b01100000
#define RO  0b01101000
#define OUT 0b01110000
#define HLT 0b01111000
#define JNZ 0b10000000
#define JNC 0b10001000

#define set 0b11111111100000000 - 1

BluetoothSerial ESP_BT;

//linear output for the pins on the esp32
int pinOut[] = {1, 2, 3, 4, 5, 12, 13, 15, 16, 17, 19, 21, 22, 23, 25, 26, 27};

//***************************************************************//
//                        autoPrograms
//             If INC, DEC or set, add a value
//
int pre1[] = {LDI, 1, STA, 254, LDI, 0, STA, 255, OUT, LDA, 254, ADD, 255, 
              STA, 254, OUT, LDA, 255, ADD, 254, JC, 0, JMP, 6};
              
int pre2[] = {OUT, INC + 1, JC, 6, JMP, 0, DEC + 1, OUT, JZ, 0, JMP, 6};

int pre3[] = {LDI, 0, STA, 253, STA, 254, STA, 255, IN, CMP, 252, JZ, 35,
              CMP, 251, JZ , 43, CMP, 250, JZ, 51, CMP, 249, JZ, 57, CMP,
              248, JZ, 63, CMP, 247, JZ, 95, JMP, 8, LDA, 255, INC + 1, OUT, STA,
              255, JMP, 8, LDA, 255, DEC + 1, OUT, STA, 255, JMP, 8, LDA, 255,
              STA, 254, JMP, 8, LDA, 255, STA, 253, JMP, 8, LDI, 0, STA, 246,
              LDA, 254, STA, 245, LDA, 253, STA, 244, LDA, 244, DEC + 1, JC,
              85, LDA, 246, OUT, JMP, 8, STA, 244, LDA, 246, ADD, 245, STA,
              246, JMP, 75, HLT, set + 244, 0, 0, 0, 15, 10, 2, 8, 1, 4};
              
int pre4[] = {IN, CMP, 254, JZ, 11, CMP, 255, JZ, 19, JMP, 0, LDA, 253, 
              INC + 1, OUT, STA, 253, JMP, 0, LDA, 253, DEC + 1, OUT, STA, 
              253, JMP, 0, set + 253, 0, 4, 1};

int pre5[] = {0};
//
//
//
//***************************************************************//

String incoming = "";
int opCode;
int value;
int inc = 0;
int address = 0;

void setup() {
  //start the bluetooth
  ESP_BT.begin("8 Bit Computer Programmer");

  //setup the pins to output and their default state
  for (int i = 0; i <= 16; i++) {
    pinMode(pinOut[i], OUTPUT);
    digitalWrite(pinOut[i], LOW);
  }
  digitalWrite(pinOut[16], HIGH);
}

//output the data to the pins on the esp32 and write it to memory
void write(int num) {
  if (num > set) {
    address = num - set;
  } else {
    for (int pin = 0; pin <= 7; pin++) {
      digitalWrite(pinOut[pin], (address  >> pin) & 0b00000001);
      digitalWrite(pinOut[pin + 8], (num  >> pin) & 0b00000001);
    }
    delay(100);
    digitalWrite(pinOut[16], LOW);
    delay(10);
    digitalWrite(pinOut[16], HIGH);
    delay(100);
  }
}

//program the preprogrammed values into memory
void preProgrammed(int value) {
  address = 0;

  switch (value) {
    case 1:
      for (int i = 0; i < (sizeof(pre1) / sizeof(pre1[0])); i++) {
        write(pre1[i]);
        address++;
      }
      break;
    case 2:
      for (int i = 0; i < (sizeof(pre2) / sizeof(pre2[0])); i++) {
        write(pre2[i]);
        address++;
      }
      break;
    case 3:
      for (int i = 0; i < (sizeof(pre3) / sizeof(pre3[0])); i++) {
        write(pre3[i]);
        address++;
      }
      break;
    case 4:
      for (int i = 0; i < (sizeof(pre4) / sizeof(pre4[0])); i++) {
        write(pre4[i]);
        address++;
      }
      break;
    case 5:
      for (int i = 0; i < (sizeof(pre5) / sizeof(pre5[0])); i++) {
        write(pre5[i]);
        address++;
      }
      break;
  }

}

//decode the incoming data from the bluetooth app
void program(int opCode, int value) {
  if (opCode == 0b00000000 || opCode == 0b01110000 || opCode == 0b01111000) {
    write(opCode);
    address++;
  } else if (opCode == 0b11111111) {
    address = value;
  } else if (opCode == 0b11111110 && value == 0b11111111) {
    address = 0;
  } else if (opCode == 0b11111100) {
    write(value);
  } else if (opCode == 0b01010000 || opCode == 0b01011000) {
    opCode += value;
    write(opCode);
    address++;
  } else if (opCode == 0b11111101) {
    preProgrammed(value);
  } else {
    write(opCode);
    address++;
    write(value);
    address++;
  }
}

//parse the incoming 2 bytes of data
void split(int i) {
  incoming = String(i) + " " + incoming;
  inc++;
  if ((inc % 2) == 0) {
    opCode = (incoming.substring(incoming.indexOf(" ") + 1, incoming.length())).toInt();
    value = (incoming.substring(0, incoming.indexOf(" "))).toInt();
    program(opCode, value);
    incoming = "";
    inc = 0;
  }

}

//read the incoming data
void loop() {
  if (ESP_BT.available())
  {
    split(ESP_BT.read());
  }
}

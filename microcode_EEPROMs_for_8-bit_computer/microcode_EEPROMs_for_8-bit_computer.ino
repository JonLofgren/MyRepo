#define SHIFT_DATA 2
#define SHIFT_CLK 3
#define SHIFT_LATCH 4
#define EEPROM_D0 5
#define EEPROM_D7 12
#define WRITE_EN 13

int which = 1;  //  Which EEPROM do you want to program?: 1, 2, 3.

#define HLT 0b10000000000000000000000000000000  // Halt clock
#define MI  0b01000000000000000000000000000000  // Memory address register in
#define RI  0b00100000000000000000000000000000  // RAM data in
#define RO  0b00010000000000000000000000000000  // RAM data out
#define SR  0b00001000000000000000000000000000  // Step reset
#define II  0b00000100000000000000000000000000  // Instruction register in
#define AI  0b00000010000000000000000000000000  // A register in
#define AO  0b00000001000000000000000000000000  // A register out
#define EO  0b00000000100000000000000000000000  // ALU out
#define SU  0b00000000010000000000000000000000  // ALU subtract
#define BI  0b00000000001000000000000000000000  // B register in
#define OI  0b00000000000100000000000000000000  // Output register in
#define CE  0b00000000000010000000000000000000  // Program counter enable
#define CO  0b00000000000001000000000000000000  // Program counter out
#define J   0b00000000000000100000000000000000  // Jump (program counter in)
#define FI  0b00000000000000010000000000000000  // Flags in
#define IO  0b00000000000000001000000000000000  // Input out
#define IU  0b00000000000000000100000000000000  // Input Update
#define IRO 0b00000000000000000010000000000000  // Instruction register out

#define FLAGS_Z0C0 0
#define FLAGS_Z0C1 1
#define FLAGS_Z1C0 2
#define FLAGS_Z1C1 3

#define JC  0b00111
#define JZ  0b01000
#define JNZ 0b10000
#define JNC 0b10001

uint32_t UCODE_TEMPLATE[32][8] = { 
  { MI|CO,  RO|II|CE,  0,      0,           0,                     0,  0 },   // 00000 - NOP
  { MI|CO,  RO|II|CE,  MI|CO,  RO|MI|CE,    RO|AI,                 SR, 0 },   // 00001 - LDA
  { MI|CO,  RO|II|CE,  MI|CO,  RO|MI|CE,    RO|BI,  EO|AI|FI,      SR, 0 },   // 00010 - ADD
  { MI|CO,  RO|II|CE,  MI|CO,  RO|MI|CE,    RO|BI,  EO|AI|SU|FI,   SR, 0 },   // 00011 - SUB
  { MI|CO,  RO|II|CE,  MI|CO,  RO|MI|CE,    AO|RI,  SR,            0,  0 },   // 00100 - STA
  { MI|CO,  RO|II|CE,  MI|CO,  RO|AI|CE,    SR,     0,             0,  0 },   // 00101 - LDI
  { MI|CO,  RO|II|CE,  MI|CO,  RO|J,        SR,     0,             0,  0 },   // 00110 - JMP
  { MI|CO,  RO|II|CE,  CE,     SR,          SR,     0,             0,  0 },   // 00111 - JC
  { MI|CO,  RO|II|CE,  CE,     SR,          SR,     0,             0,  0 },   // 01000 - JZ
  { MI|CO,  RO|II|CE,  MI|CO,  RO|MI|CE,    RO|BI,  SU|FI,         SR, 0 },   // 01001 - CMP
  { MI|CO,  RO|II|CE,  IRO|BI, EO|AI|FI,    SR,     0,             0,  0 },   // 01010 - INC
  { MI|CO,  RO|II|CE,  IRO|BI, EO|AI|SU|FI, SR,     0,             0,  0 },   // 01011 - DEC
  { MI|CO,  RO|II|CE,  IO|AI,  IU,          SR,     0,             0,  0 },   // 01100 - IN
  { MI|CO,  RO|II|CE,  MI|CO,  RO|MI,       RO|OI,  SR,            0,  0 },   // 01101 - RO
  { MI|CO,  RO|II|CE,  AO|OI,  SR,          0,      0,             0,  0 },   // 01110 - OUT
  { MI|CO,  RO|II|CE,  HLT,    0,           0,      0,             0,  0 },   // 01111 - HLT
  { MI|CO,  RO|II|CE,  MI|CO,  RO|J,        SR,     0,             0,  0 },   // 10000 - JNZ
  { MI|CO,  RO|II|CE,  MI|CO,  RO|J,        SR,     0,             0,  0 },   // 10001 - JNC
  { MI|CO,  RO|II|CE,  MI|CO,  RO|MI|CE,    IRO|RI, SR,            0,  0 },   // 10010 - STI
  { MI|CO,  RO|II|CE,  IU,     SR,          0,      0,             0,  0 },   // 10011 - CLR (Input Reg.)
  { MI|CO,  RO|II|CE,  SR,     0,           0,      0,             0,  0 },   // 10100
  { MI|CO,  RO|II|CE,  SR,     0,           0,      0,             0,  0 },   // 10101
  { MI|CO,  RO|II|CE,  SR,     0,           0,      0,             0,  0 },   // 10110
  { MI|CO,  RO|II|CE,  SR,     0,           0,      0,             0,  0 },   // 10111
  { MI|CO,  RO|II|CE,  SR,     0,           0,      0,             0,  0 },   // 11000
  { MI|CO,  RO|II|CE,  SR,     0,           0,      0,             0,  0 },   // 11001
  { MI|CO,  RO|II|CE,  SR,     0,           0,      0,             0,  0 },   // 11010
  { MI|CO,  RO|II|CE,  SR,     0,           0,      0,             0,  0 },   // 11011
  { MI|CO,  RO|II|CE,  SR,     0,           0,      0,             0,  0 },   // 11100
  { MI|CO,  RO|II|CE,  SR,     0,           0,      0,             0,  0 },   // 11101
  { MI|CO,  RO|II|CE,  SR,     0,           0,      0,             0,  0 },   // 11110
  { MI|CO,  RO|II|CE,  SR,     0,           0,      0,             0,  0 },   // 11111 
};

uint32_t ucode[4][32][8];

void initUCode() {
  // ZF = 0, CF = 0
  memcpy(ucode[FLAGS_Z0C0], UCODE_TEMPLATE, sizeof(UCODE_TEMPLATE));

  // ZF = 0, CF = 1
  memcpy(ucode[FLAGS_Z0C1], UCODE_TEMPLATE, sizeof(UCODE_TEMPLATE));
  ucode[FLAGS_Z0C1][JC][2]  = CO|MI;
  ucode[FLAGS_Z0C1][JC][3]  = RO|J;
  ucode[FLAGS_Z0C1][JNC][2] = CO|MI;
  ucode[FLAGS_Z0C1][JNC][3] = RO|J;

  // ZF = 1, CF = 0
  memcpy(ucode[FLAGS_Z1C0], UCODE_TEMPLATE, sizeof(UCODE_TEMPLATE));
  ucode[FLAGS_Z1C0][JZ][2]  = CO|MI;
  ucode[FLAGS_Z1C0][JZ][3]  = RO|J;
  ucode[FLAGS_Z1C0][JNZ][2] = CO|MI;
  ucode[FLAGS_Z1C0][JNZ][3] = RO|J;

  // ZF = 1, CF = 1
  memcpy(ucode[FLAGS_Z1C1], UCODE_TEMPLATE, sizeof(UCODE_TEMPLATE));
  ucode[FLAGS_Z1C1][JC][2] = CO|MI;
  ucode[FLAGS_Z1C1][JZ][2] = CO|MI;
  ucode[FLAGS_Z1C1][JC][3] = RO|J;
  ucode[FLAGS_Z1C1][JZ][3] = RO|J;
}

/*
 * Output the address bits and outputEnable signal using shift registers.
 */
void setAddress(int address, bool outputEnable) {
  shiftOut(SHIFT_DATA, SHIFT_CLK, MSBFIRST, (address >> 8) | (outputEnable ? 0x00 : 0x80));
  shiftOut(SHIFT_DATA, SHIFT_CLK, MSBFIRST, address);

  digitalWrite(SHIFT_LATCH, LOW);
  digitalWrite(SHIFT_LATCH, HIGH);
  digitalWrite(SHIFT_LATCH, LOW);
}


/*
 * Read a byte from the EEPROM at the specified address.
 */
byte readEEPROM(int address) {
  for (int pin = EEPROM_D0; pin <= EEPROM_D7; pin += 1) {
    pinMode(pin, INPUT);
  }
  setAddress(address, /*outputEnable*/ true);

  byte data = 0;
  for (int pin = EEPROM_D7; pin >= EEPROM_D0; pin -= 1) {
    data = (data << 1) + digitalRead(pin);
  }
  return data;
}


/*
 * Write a byte to the EEPROM at the specified address.
 */
void writeEEPROM(int address, byte data) {
  setAddress(address, /*outputEnable*/ false);
  for (int pin = EEPROM_D0; pin <= EEPROM_D7; pin += 1) {
    pinMode(pin, OUTPUT);
  }

  for (int pin = EEPROM_D0; pin <= EEPROM_D7; pin += 1) {
    digitalWrite(pin, data & 1);
    data = data >> 1;
  }
  digitalWrite(WRITE_EN, LOW);
  delayMicroseconds(1);
  digitalWrite(WRITE_EN, HIGH);
  delay(10);
}


/*
 * Read the contents of the EEPROM and print them to the serial monitor.
 */
void printContents(int start, int length) {
  for (int base = start; base < length; base += 16) {
    byte data[16];
    for (int offset = 0; offset <= 15; offset += 1) {
      data[offset] = readEEPROM(base + offset);
    }

    char buf[80];
    sprintf(buf, "%03x:  %02x %02x %02x %02x %02x %02x %02x %02x   %02x %02x %02x %02x %02x %02x %02x %02x",
            base, data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7],
            data[8], data[9], data[10], data[11], data[12], data[13], data[14], data[15]);

    Serial.println(buf);
  }
}


void setup() {
  // put your setup code here, to run once:
  initUCode();

  pinMode(SHIFT_DATA, OUTPUT);
  pinMode(SHIFT_CLK, OUTPUT);
  pinMode(SHIFT_LATCH, OUTPUT);
  digitalWrite(WRITE_EN, HIGH);
  pinMode(WRITE_EN, OUTPUT);
  Serial.begin(57600);

  // Program data bytes
  Serial.print("Programming EEPROM ");
  Serial.print(which);

  for (int address = 0; address < 1024; address += 1) {
    int flags       = (address & 0b1100000000) >> 8;
    int instruction = (address & 0b0011111000) >> 3;
    int step        = (address & 0b0000000111);

    if (which == 1) {
      writeEEPROM(address, ucode[flags][instruction][step] >> 24);
    }
    
    if(which == 2){
      writeEEPROM(address, ucode[flags][instruction][step] >> 16);
    }
    
    if(which == 3){
      writeEEPROM(address, ucode[flags][instruction][step] >> 8);
    }

    if (address % 64 == 0) {
      Serial.print(".");
    }
  }

  Serial.println(" done");


  // Read and print out the contents of the EERPROM
  Serial.println("Reading EEPROM");
  printContents(0, 1024);
}


void loop() {
  // put your main code here, to run repeatedly:

}

// Commissioned code for a communication system at a restaurant to let the front know when food is ready.
// Has two 3d printed boxes with LEDs and buttons connected together with an ethernet cable.

#include <Metro.h>
#include "pitches.h"

int drive = 3;
int sit = 2;
int buzz = 4;

int driveLED = 12;
int sitLED = 13;

int buzzer = 8;

int state0 = LOW;
int state1 = LOW;

int driveFlip = 0;
int sitFlip = 0;

Metro metro0 = Metro(500);
Metro metro1 = Metro(500);

void setup() {
  pinMode(driveLED, OUTPUT);
  digitalWrite(driveLED, state0);
  pinMode(sitLED, OUTPUT);
  digitalWrite(sitLED, state1);
  pinMode(drive, INPUT_PULLUP);
  pinMode(sit, INPUT_PULLUP);
  pinMode(buzz, INPUT_PULLUP);
}

void loop() {
  if (digitalRead(drive) == LOW)
  {
    if (driveFlip == 1)
    {
      driveFlip = 0;
      delay(400);
    } else
    {
      driveFlip = 1;
      tone(8, NOTE_G5, 150);
      delay(150);
      tone(8, NOTE_E5, 150);
      delay(150);
      tone(8, NOTE_C5, 150);
      delay(150);
    }
  }


  if (digitalRead(sit) == LOW)
  {
    if (sitFlip == 1)
    {
      sitFlip = 0;
      delay(400);
    } else
    {
      sitFlip = 1;
      tone(8, NOTE_C5, 150);
      delay(150);
      tone(8, NOTE_E5, 150);
      delay(150);
      tone(8, NOTE_G5, 150);
      delay(150);
    }
  }

  if (driveFlip == 1)
  {
    if (metro0.check() == 1) {
      if (state0 == HIGH)  {
        state0 = LOW;
      } else {
        state0 = HIGH;
      }
      digitalWrite(driveLED, state0);
    }
  } else
  {
    digitalWrite(driveLED, LOW);
  }

  if (sitFlip == 1)
  {
    if (metro1.check() == 1) { 
      if (state1 == HIGH)  {
        state1 = LOW;
      } else {
        state1 = HIGH;
      }
      digitalWrite(sitLED, state1);
    }
  } else
  {
    digitalWrite(sitLED, LOW);
  }

  if (digitalRead(buzz) == LOW)
  {
    tone(8, NOTE_D5, 1);
  }
}

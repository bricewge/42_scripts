#include "Arduino.h"
#include "HID-Project.h"


void setup() {
  Keyboard.begin();
  Consumer.begin();
}


void loop() {
  // Wait for the OS to ready
  delay(1000);
  // Set brightness to the minimum
  for (int i = 0; i <= 16; i++)
  	  Keyboard.write(KEY_F1);
  // Lock the session
  Keyboard.press(KEY_RIGHT_CTRL);
  Keyboard.press(KEY_RIGHT_SHIFT);
  Consumer.write(HID_CONSUMER_EJECT);
  Keyboard.releaseAll();
  // Wake up the computer regulary
  while (42) {
	delay(1000 * 60 * 30); // 30min
    Keyboard.write(KEY_ESC);
    delay(500);
    Keyboard.write(KEY_ENTER);
    delay(500);
    Keyboard.write(KEY_ESC);
  }
}

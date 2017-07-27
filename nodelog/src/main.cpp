/*
  Copyright (c) 2014-2015 NicoHood
  See the readme for credit to other people.

  BootKeyboard example

  Shows that keyboard works even in bios.
  Led indicats if we are in bios.

  See HID Project documentation for more information.
  https://github.com/NicoHood/HID/wiki/Keyboard-API#boot-keyboard
*/

#include <HID-Project.h>


void setup() {
  // Sends a clean report to the host. This is important on any Arduino type.
  BootKeyboard.begin();
}


void loop() {
  // Wait for the OS to ready
  delay(1000);
  // TODO Min screen backlight and lock session
  // Trigger caps lock manually via button
  while (42) {
    BootKeyboard.write(KEY_ENTER);
    delay(100);
    BootKeyboard.write(KEY_ENTER);
    delay(100);
    BootKeyboard.write(KEY_ESC);
    delay(1000 * 60 * 30);
    // delay(1000 * 7);
  }
}

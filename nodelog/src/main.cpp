#include "Arduino.h"
#include "HID-Project.h"

unsigned long second = 1000L;
unsigned long minute = second * 60;

void setup()
{
	Keyboard.begin();
	Consumer.begin();
}

void lock_session()
{
	Keyboard.press(KEY_RIGHT_CTRL);
	Keyboard.press(KEY_RIGHT_SHIFT);
	Consumer.write(HID_CONSUMER_EJECT);
	Keyboard.releaseAll();
}

void hide_login()
{
	Keyboard.press(KEY_RIGHT_ALT);
	Keyboard.write(KEY_ENTER);
	Keyboard.releaseAll();
}

void bright_min()
{
	for (int i = 0; i <= 16; i++)
		Keyboard.write(KEY_F1);
}

void loop()
{
	// Wait for the OS to ready
	delay(second);
	lock_session();

	delay(second * 2);
	Keyboard.write(KEY_ESC); // Show lockscreen
	delay(second / 2);
	bright_min();
	hide_login();
	Keyboard.write(KEY_ESC); // Hide lockscreen

	// Wake up the computer regulary
	while (42) {
		delay(minute * 30);
		Keyboard.write(KEY_ESC);
		delay(second / 2);
		Keyboard.press(KEY_TAB);
		Keyboard.write(KEY_ENTER);
		Keyboard.releaseAll();
		delay(second / 2);
		Keyboard.write(KEY_ESC);
	}
}

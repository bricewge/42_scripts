#include "Arduino.h"
#include "HID-Project.h"

unsigned long second = 1000L;
unsigned long minute = second * 60;

char username[] = "username";
char password[] = "pASSw0rd";

// Put the mouse on the top right corner no matter where it was before
void mouse_init()
{
	for (int i = 0; i <= 100; i++)
		Mouse.move(-100, -100, 0);
}

void mouse_select_username()
{
	Mouse.move(100, 55, 0);
	Mouse.click(MOUSE_LEFT);
}

void enter_creds()
{
	Keyboard.press(KEY_LEFT_WINDOWS);
	Keyboard.write(KEY_A);
	Keyboard.releaseAll();

	Keyboard.print(username);
	Keyboard.press(KEY_TAB);
	Keyboard.println(password);
}

void setup()
{
	Keyboard.begin();
	Mouse.begin();

	delay(second); 				// Wait for the OS to ready
	Keyboard.press(KEY_ESC);	// Turn-on the screen
	mouse_init();
	mouse_select_username();
	enter_creds();

	Mouse.end();
	Keyboard.end();
}

void loop()
{
}

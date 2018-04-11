#!/usr/bin/python

from Adafruit_CharLCD import Adafruit_CharLCD
import time

lcd = Adafruit_CharLCD()

lcd.begin(16, 2)

lcd.clear()
lcd.message("Hello\nNITTTR")

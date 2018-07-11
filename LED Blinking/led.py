import RPi.GPIO as GPIO						# Import libraries
import time
GPIO.setmode(GPIO.BCM)						# Set GPIOs of Raspberry pi for BCM2836 architecture 
GPIO.setup(27, GPIO.OUT)						# set GPIO 25 as output

while True:
	GPIO.output(27, GPIO.HIGH)				# set GPIO 25 High
	time.sleep(2)					# set time delay of 2 sec for LED toggling
	GPIO.output(27, GPIO.LOW)				# set GPIO 25 Low
	time.sleep(2)					# set time delay of 2 sec for LED toggling

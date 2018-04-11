import RPi.GPIO as GPIO						# Import GPIO library
import time							# Import time library
GPIO.setmode(GPIO.BCM)						# Set GPIOs of Raspberry pi for BCM2836 architecture 
GPIO.setup(27, GPIO.OUT)						# Configure GPIO 25 as an output pin

while True:							# Continuous loop for togging
	GPIO.output(27, GPIO.HIGH)				# set GPIO 25 High(LED On)
	time.sleep(2)					# set time delay of 2 sec for LED toggling
	GPIO.output(27, GPIO.LOW)				# set GPIO 25 Low(LED Off)	
	time.sleep(2)					# set time delay of 2 sec for LED toggling

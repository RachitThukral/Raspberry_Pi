import RPi.GPIO as GPIO			#import libraries
import dht11
import time
import datetime

# initialize GPIO
GPIO.setmode(GPIO.BCM)

dht11_object = dht11.DHT11(pin = 4)		#object of class DHT11

while True:
	result = dht11_object.read()		#read data using pin 4
	if result.is_valid():
		print("Temperature: %d C" % result.temperature)	#print temperature and humidity
		print("Humidity: %d %%" % result.humidity)
	time.sleep(1)

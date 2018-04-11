# ADXL345 Python example 
#
# author:  Jonathan Williamson
# license: BSD, see LICENSE.txt included in this package
# 
# This is an example to show you how to use our ADXL345 Python library
# http://shop.pimoroni.com/products/adafruit-triple-axis-accelerometer
import time
from sht21 import SHT21
  

while True:
	sht21 = SHT21(1)
	print "temp   ",sht21.read_temperature()
	print "hum   ",sht21.read_humidity()
	print ".................................................................................................."
	
	time.sleep(2)

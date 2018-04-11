# ADXL345 Python example 
#
# author:  Jonathan Williamson
# license: BSD, see LICENSE.txt included in this package
# 
# This is an example to show you how to use our ADXL345 Python library
# http://shop.pimoroni.com/products/adafruit-triple-axis-accelerometer
import time
from adxl345 import ADXL345
  
adxl345 = ADXL345()
while True:
    
	axes = adxl345.getAxes(True)
	#print "ADXL345 on address 0x%x:" % (adxl345.address)
	#print "   x = %.3fG" % ( axes['x'] )
	#print "   y = %.3fG" % ( axes['y'] )
	#print "   z = %.3fG" % ( axes['z'] )
	if (axes['z']>0.9 and axes['z']<1.1):
		print "XY plane parallel to ground and Z axis upwards"
	if (axes['z']>-1.1 and axes['z']<-0.9):
		print "XY plane parallel to ground and Z axis downwards"

	if (axes['x']>0.9 and axes['x']<1.1):
		print "YZ plane parallel to ground and X axis upwards"
	if (axes['x']>-1.1 and axes['x']<-0.9):
		print "YZ plane parallel to ground and X axis downwards"

	if (axes['y']>0.9 and axes['y']<1.1):
		print "XZ plane parallel to ground and Y axis upwards"
	if (axes['y']>-1.1 and axes['y']<-0.9):
		print "XZ plane parallel to ground and Y axis downwards"

	time.sleep(2)


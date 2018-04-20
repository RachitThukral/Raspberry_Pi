from TSL2561 import Luxmeter
import time
TSL2561_sensor = Luxmeter(0x39)
While True:
	print "Light intensity = ",  TSL2561_sensor.getLux(1), "Lux"
	time.sleep(1)
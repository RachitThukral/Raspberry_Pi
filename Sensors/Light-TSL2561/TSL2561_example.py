import TSL2561
import time
TSL2561_object = Luxmeter.Luxmeter(0x39)
While True:
	print "Light intensity = ",  TSL2561_object.getLux(1), "Lux"
	time.sleep(1)
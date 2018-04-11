import RPi.GPIO as GPIO
import spidev
import time
import serial

port=serial.Serial("/dev/ttyAMA0",9600,timeout=3.0)
# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
 
# Function to read SPI data from MCP3008 chip, Channel must be an integer 0-7
def ReadChannel(channel):
	adc = spi.xfer2([1,(8+channel)<<4,0])
	data = ((adc[1]&3) << 8) + adc[2]
	return data
 
# Function to convert data to voltage level, rounded to specified number of decimal places.
def ConvertVolts(data,places):
	volts = (data * 3.3) / float(1023)
	volts = round(volts,places)
	return volts

dust_channel = 0 #Define sensor channels
delay = 2 #Define delay between readings
dust_led=4
samplingTime = .000000280
deltaTime = .00000040
sleepTime = .000009680
 
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(dust_led, GPIO.OUT) # LED pin set as output
 
while True:
	GPIO.output(dust_led, GPIO.LOW) #power on the LED
	time.sleep(samplingTime)

	# Read the light sensor data
	dust_level = ReadChannel(dust_channel)
	time.sleep(deltaTime)
	GPIO.output(dust_led, GPIO.HIGH) #turn the LED off
	time.sleep(sleepTime)

	dust_volts = ConvertVolts(dust_level,2)
	dust_volts = dust_volts*1.515
	if dust_volts<0.583:
		dust_Density = 0
	else:
		dust_Density = 0.17 * dust_volts - 0.1
		port.write(" dust_density=")
		port.write(str(round(dust_Density,2)))
		port.write("mg/mc\n")
	 
	# Print out results
	print("Dust : {} ({}V) {} mg/metre cube".format(dust_level,dust_volts,dust_Density))
	 
	# Wait before repeating loop
	time.sleep(delay)	

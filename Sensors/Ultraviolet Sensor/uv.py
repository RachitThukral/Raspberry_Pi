import spidev
import time
import os
 
# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
 
# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data
 
# Function to convert data to voltage level,
# rounded to specified number of decimal places.
def ConvertVolts(data,places):
  volts = (data * 3.3) / float(1023)
  volts = round(volts,places)
  return volts
 
 
# Define sensor channels
uv_channel = 0

# Define delay between readings
delay = 2
 
while True:
 
  # Read the temperature sensor data
  uv_level = ReadChannel(uv_channel)
  uv_volts = ConvertVolts(uv_level,2)
  uv_index = round(uv_volts/0.1)

  # Print out results
  print "___________________________________________________________________"
  print("Count={} Voltage={}V uv_index={}".format(uv_level,uv_volts,uv_index))


  # Wait before repeating loop
  time.sleep(delay)
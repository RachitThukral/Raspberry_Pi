import RPi.GPIO as GPIO                    #Import libraries
import time
GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering 

TRIG = 23                                  #Associate pin 23,24 to TRIG and ECHO
ECHO = 24

GPIO.setup(TRIG,GPIO.OUT)                  #Set TRIG,ECHO as out,in
GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIG, False)                 #initially TRIG LOW

while True:
	GPIO.output(TRIG, True)                  # 10uS pulse on TRIG
	time.sleep(0.00001)
	GPIO.output(TRIG, False)

	while GPIO.input(ECHO)==0:               #calculate ECHO pulse duration
		pulse_start = time.time()
	while GPIO.input(ECHO)==1:
		pulse_end = time.time()
	pulse_duration = pulse_end - pulse_start

	distance = pulse_duration * 17150      #calculate distance
	distance = round(distance, 2)            #Round to two decimal points
	print "Distance:",distance,"cm"  		#Print distance
	time.sleep(2)                            #Delay of 2 seconds
	
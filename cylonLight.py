from numpy import *

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import time

pins = [4,17,18,27]
pinback = [18,17]

try:
	while True:
		for i,pin in enumerate(pins):
			GPIO.setup(pin,GPIO.OUT)
			GPIO.output(pin,1)
			time.sleep(.25)
			GPIO.output(pin,0)
		for i,pin2 in enumerate(pinback):
			GPIO.setup(pin2,GPIO.OUT)
			GPIO.output(pin2,1)
			time.sleep(.25)
			GPIO.output(pin2,0)

finally:
	GPIO.cleanup()

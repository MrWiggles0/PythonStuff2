from numpy import *
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

RATE = 34300
trigPin = 18
echoPin = 17
ledPin = 27

GPIO.setup(trigPin,GPIO.OUT)
GPIO.setup(echoPin,GPIO.IN)
GPIO.setup(ledPin,GPIO.OUT)

try:
	while True:
		GPIO.output(trigPin,0)
		time.sleep(0.000002)
		GPIO.output(trigPin, 1)
		time.sleep(0.00001)
		GPIO.output(trigPin,0)
		t = GPIO.input(echoPin)
		d = t*RATE/2
		if d <= 20:
			GPIO.output(ledPin,1)
		else:
			GPIO.output(ledPin,0)

finally:
	GPIO.cleanup()

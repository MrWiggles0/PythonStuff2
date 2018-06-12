#Jonathan Doucette
#ME492
#Week 4 Day 1 Discussion

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

ledpin = 18
uppin = 27
downpin = 4

GPIO.setup(ledpin,GPIO.OUT)
GPIO.setup(uppin,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(downpin,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

pwmlevel = 50
pwmled = GPIO.PWM(ledpin,500)
pwmled.start(pwmlevel)
print pwmlevel

try:
	while True:
		if GPIO.input(uppin):
			if pwmlevel < 100:
				pwmlevel = pwmlevel+5
				print pwmlevel
				pwmled.ChangeDutyCycle(pwmlevel)
				time.sleep(.25)
		if GPIO.input(downpin):
			if pwmlevel > 0:
				pwmlevel = pwmlevel-5
				print pwmlevel
				pwmled.ChangeDutyCycle(pwmlevel)
				time.sleep(.25)

finally:
	GPIO.cleanup()

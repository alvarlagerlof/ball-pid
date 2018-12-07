import RPi.GPIO as GPIO
from time import sleep

# conf
time = 0.5

# setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)

p = GPIO.PWM(2, 50)

p.start(7.5)

try:
	while True:
		p.ChangeDutyCycle(10)  # turn towards 90 degree
		sleep(time)
		
		p.ChangeDutyCycle(7.5) # turn towards 0 degree
		sleep(time)
		
		p.ChangeDutyCycle(2.5) # turn towards 0 degree
		sleep(time) 
		
except KeyboardInterrupt:
	p.stop()
        GPIO.cleanup()

import RPi.GPIO as GPIO
import pigpio
from gpiozero import AngularServo
import time
from threading import Thread

from config import *




class Servo:
    
    def __init__(self, servo):
        self.servo = servo
        
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(self.servo, GPIO.OUT)

	self.pwm = GPIO.PWM(self.servo, 50)
	self.pwm.start(0)
	
	time.sleep(conf.servo_startup)
		
	print("Servo init completed")
	
	
    def setAngle(self, angle):
        self.duty = angle / 18 + 2
        
        def work():
            
            print("do work")
            
            GPIO.output(self.servo, True)
            self.pwm.ChangeDutyCycle(self.duty)            
           
            time.sleep(conf.servo_sleep)

            GPIO.output(self.servo, False)
            self.pwm.ChangeDutyCycle(0)
            
        background_thread = Thread(target=work)
        background_thread.start()

	
    """def moveTo(self, servo, pos):
        if servo == "x":
            self.p1.ChangeDutyCycle(pos)
            print("x moved", pos)
            
        elif servo == "y":
            self.p2.ChangeDutyCycle(pos)
            print("y moved", pos)
        
	sleep(conf.servo_sleep)
		
	#print("move to", pos)"""
	
	
    def stop(self):
        self.p1.stop()
        self.p2.stop()
        GPIO.cleanup()
        
        print("Servos stopped")




"""class Servo:
    
    def __init__(self):
        
        self.pi = pigpio.pi()
        #pigpio.setMode(2, pigpio.OUT)
        
        
        
	GPIO.setmode(GPIO.BCM)
	
	GPIO.setup(2, GPIO.OUT)
	GPIO.setup(3, GPIO.OUT)

	#self.p1 = GPIO.PWM(2, 50)
	#self.p2 = GPIO.PWM(3, 50)
	#self.p1.start(7.5)
	#self.p2.start(7.5)
	
	sleep(conf.servo_start_wakeup)
		
	print("Servo init completed")
	
	
    def moveTo(self, servo, pos):
        
        if servo == "x":
            self.pi.set_servo_pulsewidth(2, pos)
            print("x moved", pos)
            
        elif servo == "y":
            self.pi.set_servo_pulsewidth(3, pos)
            print("y moved", pos)
        
        
	sleep(conf.servo_sleep)
		
	self.stop()
		
	#print("move to", pos)
	
	
    def stop(self):
        self.pi.set_servo_pulsewidth(2, 0)
        self.pi.set_servo_pulsewidth(3, 0)
        self.pi.stop()
        GPIO.cleanup()
        
        print("Servos stopped")
"""


"""class Servo:
    
    def __init__(self):
        
        self.s1 = AngularServo(2, min_angle=-180, max_angle=180)
        self.s2 = AngularServo(3, min_angle=-180, max_angle=180)

	
	sleep(conf.servo_start_wakeup)
		
	print("Servo init completed")
	
	
    def moveTo(self, servo, pos):
        
        if servo == "x":
            self.s1.angle = pos
            print("x moved", pos)
            
        elif servo == "y":
            self.s2.angle = pos
            print("y moved", pos)
        
        #self.s.angle = -45
        
	sleep(conf.servo_sleep)
		
		
	#print("move to", pos)
	
	
    def stop(self):
        GPIO.cleanup()
        
        print("Servos stopped")
"""
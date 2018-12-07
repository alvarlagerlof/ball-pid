import math
import time

from config import *



class PID:
    
    def __init__(self):
        self.error_x_prev = 0.0
        self.error_y_prev = 0.0
        self.prev_time = time.time()
        
        self.integral_x = 0.0
        self.integral_y = 0.0
        
        self.derivative_x = 0.0
        self.derivative_y = 0.0
        
        
    def calculate(self, error_x, error_y):
        
        
        # x
	self.integral_x = self.integral_x + (error_x*conf.PID_iteration_time)
	self.derivative_x = error_x - self.error_x_prev
 
	output_x = (conf.P * error_x)
	+ (conf.I * self.integral_x)
	+ (conf.D * self.derivative_x)

	# y
	self.integral_y = self.integral_y + (error_y*conf.PID_iteration_time)
	self.derivative_y = error_y - self.error_y_prev
 
	output_y = (conf.P * error_y)
	+ (conf.I * self.integral_y)
	+ (conf.D * self.derivative_y)


	# Set previous values 
	# for next time
	self.time_diff = time.time() - self.prev_time
	self.prev_time = time.time()
	
	self.error_x_prev = error_x
	self.error_y_prev = error_y
        
        return (output_x, output_y, self.time_diff)
    
#from __future__ import print_function
from camera import Camera
from tracking import Tracking
from process import Process
from windows import Window, WindowStack

import imutils
import cv2
import time
import numpy as np
import copy



# Init
cam = Camera(src=0)
process = Process()
tracking = Tracking()
stack = WindowStack()

running = True

 


# Main loop
while running:

	# Get frame
	raw = cam.read()
	processed = process.run(copy.deepcopy(raw))


	# Get ball
	(tracked_frame, x, y) = tracking.findBall(copy.deepcopy(raw))
	print(x, y)



	# Create window
	stack.add(Window("Raw", raw))
	stack.add(Window("Processed", processed))
	stack.add(Window("Tracked", tracked_frame))


	
	cv2.imshow("Result", stack.compute())
	key = cv2.waitKey(1) & 0xFF

	# Stop if 'q' is pressed
	if key == ord("q"):
		cam.stop()
		cv2.destroyAllWindows()

		running = False

 

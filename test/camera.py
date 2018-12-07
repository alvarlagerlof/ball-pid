from threading import Thread
import numpy as np
import cv2
import imutils
import time

 
class Camera:
    def __init__(self, src=0):
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False

        time.sleep(1)

        Thread(target=self.update, args=()).start()
        
        print("[init] Camera")
        
    def update(self):
        while True:
            if self.stopped:
                return
                
            (self.grabbed, self.frame) = self.stream.read()
            
    def read(self):
        return self.frame

    def stop(self):
		self.stopped = True
			

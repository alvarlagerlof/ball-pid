from collections import deque
import numpy as np
import argparse
import imutils
import cv2
import math
import time
import sys

from config import *



class Camera:
    
    def __init__(self):
                
        # Specify color to look for TODO: Change to black or white
        #self.greenLower = (29, 86, 6)
        #self.greenUpper = (64, 255, 255)
        
        self.greenLower = (75, 65, 75)
        self.greenUpper = (235, 245, 230)
        
        #self.greenLower = (100, 100, 100)
        #self.greenUpper = (255, 255, 255)
        
        self.pts = deque(maxlen=conf.cam_buffer)
        
        # Choose webcam
        self.camera = cv2.VideoCapture(0)
        
        #time.sleep(1)
    
    def skeletonize(self, image, size, structuring=cv2.MORPH_RECT):
        # determine the area (i.e. total number of pixels in the image),
        # initialize the output skeletonized image, and construct the
        # morphological structuring element
        self.area = image.shape[0] * image.shape[1]
        self.skeleton = np.zeros(image.shape, dtype="uint8")
        self.elem = cv2.getStructuringElement(structuring, size)

        # keep looping until the erosions remove all pixels from the
        # image
        while True:
            # erode and dilate the image using the structuring element
            #self.eroded = cv2.erode(image, self.elem, iterations=0)
            #self.temp = cv2.dilate(self.eroded, self.elem, iterations=0)

            self.kernel = np.ones((5,5), np.uint8)

            self.eroded = cv2.erode(image, self.kernel, iterations=1)
            
            
            self.temp = cv2.dilate(self.eroded, self.kernel, iterations=2)

          

            #print(self.eroded)

            # subtract the temporary image from the original, eroded
            # image, then take the bitwise 'or' between the skeleton
            # and the temporary image
            self.temp = cv2.subtract(image, self.temp)
            
            
            self.skeleton = cv2.bitwise_or(self.skeleton, self.temp)

	    cv2.imshow("d", self.skeleton)
            cv2.waitKey(0)

            image = self.eroded.copy()
            
            # if there are no more 'white' pixels in the image, then
            # break from the loop
            if self.area == self.area - cv2.countNonZero(image):
                break

        # return the skeletonized image
        return self.skeleton
                
                
    def getBallPos(self):
        (self.grabbed, self.frame) = self.camera.read()
                
        # Resize the frame
        self.frame = imutils.resize(self.frame, width=conf.cam_width)
        
        #self.frame = imutils.translate(self.frame, 25, -75)
        
        # Skeletonize 
        #gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        #skele = self.skeletonize(gray, size=(3, 3))
        
        #cv2.imshow("skel", skele)
        #cv2.waitKey(1)
        
        # Blur
        #blurred = cv2.GaussianBlur(frame, (11, 11), 0)
        
        # Convert to HSV
        self.hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
        
        # construct a mask for the color "green", then perform
        # a series of dilations and erosions to remove any small
        # blobs left in the mask
        self.mask = cv2.inRange(self.hsv, self.greenLower, self.greenUpper)
        self.mask = cv2.erode(self.mask, None, iterations=2)
        self.mask = cv2.dilate(self.mask, None, iterations=2)
        
        
        # find contours in the mask and initialize the current
        # (x, y) center of the ball
        self.cnts = cv2.findContours(self.mask.copy(),
                    cv2.RETR_EXTERNAL,
                    cv2.CHAIN_APPROX_SIMPLE)[-2]
        self.center = None
            
                
                
        # only proceed if at least one contour was found
        if len(self.cnts) > 0:
            # find the largest contour in the mask, then use
            # it to compute the minimum enclosing circle and
            # centroid
            self.c = max(self.cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(self.c)
            M = cv2.moments(self.c)
            self.center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

            # only proceed if the radius meets a minimum size
            if radius > conf.cam_ball_min:
                # draw the circle and centroid on the frame,
                # then update the list of tracked points
                cv2.circle(self.frame, (int(x), int(y)), int(radius),
                        (0, 255, 255), 2)
                cv2.circle(self.frame, self.center, 5, (0, 0, 255), -1)


                # Calculate error
                #error_x = ((conf.cam_width/2)-x)*600/conf.cam_width
                #error_y = ((conf.cam_height/2)-y)*450/conf.cam_height

                error_x = ((conf.cam_width/2)-x)*600/conf.cam_width
                error_y = ((conf.cam_height/2)-y)*450/conf.cam_height

                                
                # Send result back
                return (error_x, error_y, self.frame)
        
        return (None, None, self.frame)
                
    def stop(self):
        self.camera.release()
        cv2.destroyAllWindows()
        
        print("Camera stopped")
                
                
         

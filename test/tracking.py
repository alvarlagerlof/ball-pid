import numpy as np
import cv2
import imutils
import copy


class Tracking:
    def __init__(self):
        print("[init] Tracking")
        

    def findBall(self, frame):

        ORANGE_MIN = np.array([100, 5, 220],np.uint8)
        ORANGE_MAX = np.array([160, 80, 255],np.uint8)

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # construct a mask for the color "green", then perform
        # a series of dilations and erosions to remove any small
        # blobs left in the mask
        mask = cv2.inRange(hsv, ORANGE_MIN, ORANGE_MAX)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
                
        
        # find contours in the mask and initialize the current
        # (x, y) center of the ball
        cnts = cv2.findContours(mask.copy(),
                    cv2.RETR_EXTERNAL,
                    cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None
            
                
                
        # only proceed if at least one contour was found
        if len(cnts) > 0:
            # find the largest contour in the mask, then use
            # it to compute the minimum enclosing circle and
            # centroid
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

            # only proceed if the radius meets a minimum size
            if radius > 5:
                # draw the circle and centroid on the frame,
                # then update the list of tracked points
                cv2.circle(frame, (int(x), int(y)), int(radius),
                        (0, 255, 255), 2)
                cv2.circle(frame, center, 5, (0, 0, 255), -1)


                # Calculate error
                #error_x = ((conf.cam_width/2)-x)*600/conf.cam_width
                #error_y = ((conf.cam_height/2)-y)*450/conf.cam_height

                error_x = x
                error_y = y

                                
                # Send result back
                return (frame, error_x, error_y)
        

        return (frame, None, None)
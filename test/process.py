import numpy as np
import cv2
import imutils
import copy


class Process:
    def __init__(self):
        print("[init] Post process")
        
    def run(self, frame):
        #frame = self.resize(frame, 600)
        #frame = self.cropSquare(frame)

        return frame


    def resize(self, frame, size):
        return imutils.resize(frame, width=size)


    def cropSquare(self, frame):
        size = frame.shape[:2]
        r = [(size[1]-size[0])/2, 0, size[0], size[0]]

        return frame[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]


    def bw(self, frame):
        l = 0
        u = 100

        lower_black = np.array([l,l,l], dtype = "uint16")
        upper_black = np.array([u,u,u], dtype = "uint16")

        return cv2.inRange(frame, lower_black, upper_black)
        

    def greyScale(self, frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

       
import numpy as np
import cv2

class Window:
    def __init__(self, title, frame):
        self.title = title
        self.frame = frame


class WindowStack:

    def __init__(self):
        self.stack = []

        print("[init] Window stack")


    def add(self, window):
        self.stack.append(window)
        

    def compute(self):
        window_list = []

        for w in self.stack:

            # Title
            size = w.frame.shape[:2]
            #print("w", size[1])
            title = np.zeros((size[1],100,3), np.uint8)

            final = np.stack((w.frame, w.frame), 0)

            # Append combined title
            # and frame
            window_list.append(final)

        self.stack = []

        return np.concatenate(window_list, axis=1)
import cv2
import numpy as np

class Vision:
    # properties
    needle_img = None
    needle_w = 0
    needle_h = 0
    method = None
# constructor
    def __init__(self, needle_img_path, method=cv.TM_CCORR_NORMED):
        # cargar la imagen
        # https://docs.opencv.org/4.2.0/d4/da8/group__imgcodecs.html
        self.needle_img = cv.imread(needle_img_path, 0)
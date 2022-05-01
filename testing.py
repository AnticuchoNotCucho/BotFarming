from windowcapture import WindowCapture
from time import *
from visionfilter import Vision
import cv2
from hsvfilter import HsvFilter

hsv_filter = HsvFilter(0, 136, 0, 179, 66, 255, 0, 24, 255, 0)


# capturar la pantalla
capture = WindowCapture('Musa-Chan - Dofus 2.63.7.8')
loop_time = time()
vision = Vision("Img/FresnoResaltadoNegativo3.png")
vision.init_control_gui()


# loop de captura
while True:
    img = cv2.imread("Img/screenshot.png")
    output = vision.apply_hsv_filter(img, hsv_filter)
    trees = vision.find(img, 0.8)
    output_image = vision.draw_rectangles(img, trees)
    cv2.imshow('output', output_image)
    print('FPS {}'.format(1 / (time() - loop_time)))
    if cv2.waitKey(4) == ord('q'):
        break
cv2.destroyAllWindows()



from windowcapture import WindowCapture
from time import *
from visionfilter import Vision
import cv2

# capturar la pantalla
capture = WindowCapture('Musa-Chan - Dofus 2.63.7.8')
loop_time = time()
vision = Vision("Img/FresnoResaltado2.png")
vision.init_control_gui()


# loop de captura
while True:
    img = capture.get_screenshot()
    output = vision.apply_hsv_filter(img)
    cv2.imshow("output", output)
    #trees = vision.find(img, 0.31)
    #output_image = vision.draw_rectangles(img, trees)
    #cv2.imshow('output', output_image)
    print('FPS {}'.format(1 / (time() - loop_time)))
    if cv2.waitKey(4) == ord('q'):
        break
cv2.destroyAllWindows()

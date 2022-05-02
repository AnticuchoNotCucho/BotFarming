from windowcapture import WindowCapture
from time import *
from visionfilter import Vision
import cv2
from hsvfilter import HsvFilter
hsv_filter = HsvFilter(0, 0, 192, 179, 66, 255, 0, 25, 255, 0)
hsv_filter1 = HsvFilter(0, 0, 215, 117, 33, 255, 0, 54, 255, 0)
hsv_filter3 = HsvFilter(0, 0, 0, 55, 255, 255, 0, 0, 0, 0)

# capturar la pantalla
capture = WindowCapture('Musa-Chan - Dofus 2.63.7.8')
loop_time = time()
vision = Vision("Img/TreeResalted.png")
vision.init_control_gui()


# loop de captura
while True:
    img = capture.get_screenshot()
    #img = cv2.imread("Img/Screenshot.png")
    output = vision.apply_hsv_filter(img)
    trees = vision.find(output, 0.95)
    print(len(trees))
    output_image = vision.draw_rectangles(img, trees)
    cv2.imshow('output', output_image)
    print('FPS {}'.format(1 / (time() - loop_time)))
    if cv2.waitKey(4) == ord('q'):
        break
cv2.destroyAllWindows()



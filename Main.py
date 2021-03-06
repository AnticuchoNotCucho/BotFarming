from windowcapture import WindowCapture
from time import *
from visionfilter import Vision
import cv2

# capturar la pantalla
capture = WindowCapture('Musa-Chan - Dofus 2.63.7.8')
loop_time = time()
vision = Vision("Img/TreeResalted.png")


# loop de captura
while True:
    img = capture.get_screenshot()
    trees = vision.find(img, 0.95)
    print(len(trees))
    output_image = vision.draw_rectangles(img, trees)
    cv2.imshow('output', output_image)
    print('FPS {}'.format(1 / (time() - loop_time)))
    if cv2.waitKey(4) == ord('q'):
        break
cv2.destroyAllWindows()

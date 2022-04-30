# -*- coding: utf-8 -*-
import win32gui
import win32ui
import win32con
import numpy as np
import cv2



class WindowCapture:
    # properties
    w = 0
    h = 0
    hwnd = None
    cropped_x = 0
    cropped_y = 0
    offset_x = 0
    offset_y = 0

    # constructor
    def __init__(self, window_name=None):

        # obtener la ventana, si no la encuentra, captura toda la pantalla
        if window_name is None:
            self.hwnd = win32gui.GetDesktopWindow()
        else:
            self.hwnd = win32gui.FindWindow(None, window_name)
            if not self.hwnd:
                raise Exception('Pantalla no encontrada: {}'.format(window_name))

        # obtener el tamaño de la ventana
        window_rectangle = win32gui.GetWindowRect(self.hwnd)
        self.w = window_rectangle[2] - window_rectangle[0]
        self.h = window_rectangle[3] - window_rectangle[1]

        if not window_name is None:
            # remover el título de la ventana y el borde

            border_pixels = 8
            titlebar_pixels = 30
            self.w = self.w - (border_pixels * 2)
            self.h = self.h - titlebar_pixels - border_pixels
            self.cropped_x = border_pixels
            self.cropped_y = titlebar_pixels
            self.offset_x = window_rectangle[0] + self.cropped_x
            self.offset_y = window_rectangle[1] + self.cropped_y

    # obtener la captura de pantalla
    def get_screenshot(self):

        # obtener la data de la imagen
        wdc = win32gui.GetWindowDC(self.hwnd)
        dcObj = win32ui.CreateDCFromHandle(wdc)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (self.w, self.h), dcObj, (self.cropped_x, self.cropped_y), win32con.SRCCOPY)

        # crear una imagen de la data en un formato para el opencv
        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.frombuffer(signedIntsArray, dtype='uint8')
        img.shape = (self.h, self.w, 4)

        # liberar los recursos
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wdc)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        # drop the alpha channel, or cv.matchTemplate() will throw an error like:
        #   error: (-215:Assertion failed) (depth == CV_8U || depth == CV_32F) && type == _templ.type()
        #   && _img.dims() <= 2 in function 'cv::matchTemplate'
        img = img[..., :3]

        # retornar la imagen
        img = np.ascontiguousarray(img)
        return img

    @staticmethod
    def list_window_names():
        # obtener la lista de ventanas
        windows = []

        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd), win32gui.GetWindowText(hwnd))

        win32gui.EnumWindows(winEnumHandler, None)

    def get_screen_position(self, pos):
        return pos[0] + self.offset_x, pos[1] + self.offset_y


if __name__ == '__main__':
    windlist = WindowCapture('Musa-Chan - Dofus 2.63.7.8')
    img = windlist.get_screenshot()
    print(img.shape)
    cv2.imshow('img', img)
    cv2.waitKey(200000)
    cv2.destroyAllWindows()
    # cv2.imwrite('test.png', img)
    

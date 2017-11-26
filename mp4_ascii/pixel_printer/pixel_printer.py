#! /usr/bin/env python
# -*- coding: utf-8 -*-
########################################
# Author: CirQ
# Created Time: 2017-04-08 22:49:09
########################################

from mp4_ascii.AsciiDrawer import AsciiImg
from mp4_ascii.AsciiDrawer import ImgDrawer
from PIL import Image
import numpy
import cv2


class pixel_printer(object):
    def __init__(self, path, **kw):
        """
        A encapsulation class for print an ascii image lines by lines.
        :param path: the path of an image that what to be printed.
        :param kw: the same keyword parameters as ImgDrawer.ImgDrawer() constructor.
        """
        self.image = Image.open(path)
        self.ai = AsciiImg.AsciiImg()
        self.id = ImgDrawer.ImgDrawer(**kw)

    def PRINT(self, windowsize, **kw):
        """
        To print a image lines by lines. Press "q" key can interrupt printing.
         After the image is shown, the window will wait for 5s for press any key to return.
        :param windowsize: the size of the displaying window.
        :param kw: the same keyword parameters as AsciiImg.AsciiImg.color_iter() method.
        """
        self.ai.to_image(self.image)
        cv2.namedWindow("name", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("name", windowsize[0], windowsize[1])
        for img, col in self.ai.color_iter(**kw):
            col_img = self.id.get_color_ascii(img, col)
            mat = numpy.array(col_img)
            cv2.imshow("name", mat)
            if cv2.waitKey(50) & 0xFF == ord("q"):
                break
        cv2.waitKey(5000)
        cv2.destroyAllWindows()
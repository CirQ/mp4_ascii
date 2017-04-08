#! /usr/bin/env python
# -*- coding: utf-8 -*-
########################################
# Author: CirQ
# Created Time: 2017-04-07 09:52:27
########################################
from PIL import Image


class AsciiImg(object):
    GRAYSCALE = "KWXDFPQASUZbdehx*8Gm&04LOVYkpq5Tagns69owz$CIu23Jcfry%1v7l+it[]{}?j|()=~!-/\\<>\"^_';,:`. "
    DEFAULTCHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\" ^ `'. "

    def __init__(self, scale=0.5):
        """
        Constructor, this class is for image to ascii art conversion.
        :param scale: change the resolution of the image
        """
        self.scale = float(scale)
        self.image, self.width, self.height = None, 0, 0

    def switch_to(self, path):
        """
        Switch to an image in path.
        :param path: the path of the image with prefix
        """
        self.image = Image.open(path)
        self.width = int(self.image.size[0] * self.scale)
        self.height = int(self.image.size[1] * 0.53 * self.scale)

    def draw_grey_ascii(self, charset=DEFAULTCHARS):
        """
        Draw an ascii image of the current image in grey level.
        :param charset: specify a character set as pigment.
        :return: a drawn grey ascii image.
        """
        img = self.image.resize((self.width, self.height), Image.BILINEAR)
        ascii_img = ["" for k in range(self.height)]
        for j in range(self.height):
            for i in range(self.width):
                r, g, b = img.getpixel((i,j))
                intensity = 0.299*r + 0.587*g + 0.114*b
                grey_index = int(intensity * len(charset) / 255.0)
                ascii_img[j] += charset[grey_index if grey_index<len(charset) else grey_index-1]
        return ascii_img

    def draw_color_ascii(self, charset=DEFAULTCHARS):
        """
        Draw an ascii image of the current image with color level in rgb.
        :param charset: specify a character set as pigment.
        :return: a drawn ascii image with rgb value at each pixel.
        """
        img = self.image.resize((self.width, self.height), Image.BILINEAR)
        ascii_img = ["" for k in range(self.height)]
        color_map = [[] for k in range(self.height)]
        for j in range(self.height):
            for i in range(self.width):
                r, g, b = img.getpixel((i,j))
                intensity = 0.299*r + 0.587*g + 0.114*b
                grey_index = int(intensity * len(charset) / 255.0)
                ascii_img[j] += charset[grey_index if grey_index<len(charset) else grey_index-1]
                color_map[j].append((r, g, b))
        return ascii_img, color_map

    @staticmethod
    def sort(charset):
        """
        Sort a given character set so that the elements are in pixel-sparsity order.
        :param charset: any user given character set.
        :return: the sorted character set
        """
        dic = [(AsciiImg.GRAYSCALE.index(c), c) for c in charset]
        ret = [c for (ci, c) in sorted(dic, key=lambda d: d[0])]
        return "".join(ret)

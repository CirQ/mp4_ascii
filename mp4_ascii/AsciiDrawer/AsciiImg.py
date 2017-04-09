#! /usr/bin/env python
# -*- coding: utf-8 -*-
########################################
# Author: CirQ
# Created Time: 2017-04-07 09:52:27
########################################
from PIL import Image


class AsciiImg(object):
    GRAYSCALE = "KWXDFPQASUZbdehx*8Gm&04LOVYkpq5Tagns69owz$CIu23Jcfry%1v7l+it[]{}?j|()=~!-/\\<>\"^_';,:`. "
    __DEFAULTCHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\" ^ `'. "

    def __init__(self):
        """
        Constructor, this class is for image to ascii art conversion.
        """
        self.image, self.width, self.height = None, 0, 0

    def switch_to(self, path):
        """
        Switch to an image in path.
        :param path: the path of the image with prefix
        """
        self.image = Image.open(path)
        self.width = int(self.image.size[0])
        self.height = int(self.image.size[1] * 0.53)

    def to_image(self, image):
        """
        Input a image in Pillow.Image class
        :param image: a Pillow.Image image
        """
        self.image = image
        self.width = int(self.image.size[0])
        self.height = int(self.image.size[1] * 0.53)

    def draw_grey_ascii(self, charset=__DEFAULTCHARS):
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

    def draw_color_ascii(self, charset=__DEFAULTCHARS):
        """
        Draw an ascii image of the current image with color level in rgb.
        :param charset: specify a character set as pigment.
        :return: a drawn ascii image and a corresponding rgb value mapping.
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

    def color_iter(self, charset=__DEFAULTCHARS, line=10):
        """
        Return the color image every specific lines. This method is only for 
         pixel_printer class which invokes OpenCV as a screen.
        :param charset: specify a character set as pigment.
        :param line: due to performance reason, the iterator is designed to return a frame at this specific lines. 
        """
        img = self.image.resize((self.width, self.height), Image.BILINEAR)
        ascii_img = ["" for k in range(self.height)]
        color_map = [[] for k in range(self.height)]
        count = 0
        for j in range(self.height):
            for i in range(self.width):
                r, g, b = img.getpixel((i,j))
                intensity = 0.299*r + 0.587*g + 0.114*b
                grey_index = int(intensity * len(charset) / 255.0)
                ascii_img[j] += charset[grey_index if grey_index<len(charset) else grey_index-1]
                ###############################################################
                # The color map is rearanged  in B, G, R order, it is because #
                # OpenCV reads the RGB image in such ways. (Damn design)      #
                ###############################################################
                color_map[j].append((b, g, r))
            if count > line:
                yield ascii_img, color_map
                count = 0
            count += 1

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

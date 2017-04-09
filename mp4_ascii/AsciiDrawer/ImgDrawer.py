#! /usr/bin/env python
# -*- coding: utf-8 -*-
########################################
# Author: CirQ
# Created Time: 2017-04-07 17:33:15
########################################
from PIL import Image, ImageDraw


class ImgDrawer(object):
    def __init__(self, font=None, spacing=0):
        """
        Construtor, this class is for saving an ascii-form image as jpg file,
         or return this image as a Pillow.Image instance.
        :param font: font used in this class, should be a Pillow.Image instance.
        :param spacing: spacing between lines in pixels.
        """
        self.draw = ImageDraw.Draw(Image.new("RGB", (0,0)))
        self.font = font
        self.spacing = spacing
        self.awidth, self.aheight = self.draw.textsize("@", font=self.font, spacing=self.spacing)

    def __getbase(self, ascii_img):
        """
        Get a base (or canvas) of the ascii image, which is necessary for
         image size definition since the backgroud image is previously unknown.
        :param ascii_img: an ascii image as a 2-d array.
        :return: the background (canvas) of the new image, and its spacial resolution.
        """
        txt = "\n".join(ascii_img)
        width, height = self.draw.textsize(txt, font=self.font, spacing=self.spacing)
        return Image.new("RGB", (width, height), color=(255,255,255)), (width, height)

    def save_grey_ascii(self, save_name, ascii_img, ratio=0.5):
        """
        Save the ascii image as save_name in general file format.
        :param save_name: the name of new image.
        :param ascii_img: an ascii image as a 2-d array.
        :param ratio: to shrink or expand the image since a single pixel 
            is now became a character-size element.
        """
        img, size = self.__getbase(ascii_img)
        self.draw = ImageDraw.Draw(img)
        for i in range(len(ascii_img)):
            self.draw.text((0, self.aheight*i), ascii_img[i],
                    fill=(0,0,0), font=self.font, spacing=self.spacing)
        img = img.resize((int(size[0]*ratio), int(size[1]*ratio)), Image.BILINEAR)
        img.save(save_name)

    def save_color_ascii(self, save_name, ascii_img, color_map, ratio=0.5):
        """
        Save the ascii image in rgb color scheme as file.
        :param save_name: the name pf the new image.
        :param ascii_img: an ascii image as a 2-d array.
        :param color_map: the color mapping respect to each pixel.
        :param ratio: the same as previous method.
        """
        img, size = self.__getbase(ascii_img)
        self.draw = ImageDraw.Draw(img)
        for i in range(len(ascii_img)):
            for j in range(len(ascii_img[i])):
                self.draw.text((self.awidth*j, self.aheight*i), ascii_img[i][j],
                        fill=color_map[i][j], font=self.font, spacing=self.spacing)
        img = img.resize((int(size[0]*ratio), int(size[1]*ratio)), Image.BILINEAR)
        img.save(save_name)

    def get_grey_ascii(self, ascii_img):
        """
        To obtain a grey ascii image in Pillow.Image format.
        :param ascii_img: the ascii image.
        :return: a Pillow.Image instance.
        """
        img, size = self.__getbase(ascii_img)
        self.draw = ImageDraw.Draw(img)
        for i in range(len(ascii_img)):
            self.draw.text((0, self.aheight*i), ascii_img[i],
                    fill=(0,0,0), font=self.font, spacing=self.spacing)
        return img

    def get_color_ascii(self, ascii_img, color_map):
        """
        To obtain a color ascii image in Pillow.Image format.
        :param ascii_img: the ascii image.
        :param color_map: the color mapping at each pixel.
        :return: a Pillow.Image instance.
        """
        img, size = self.__getbase(ascii_img)
        self.draw = ImageDraw.Draw(img)
        for i in range(len(ascii_img)):
            for j in range(len(ascii_img[i])):
                self.draw.text((self.awidth*j, self.aheight*i), ascii_img[i][j],
                        fill=color_map[i][j], font=self.font, spacing=self.spacing)
        return img

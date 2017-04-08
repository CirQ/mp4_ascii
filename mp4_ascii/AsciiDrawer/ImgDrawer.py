#! /usr/bin/env python
# -*- coding: utf-8 -*-
########################################
# Author: CirQ
# Created Time: 2017-04-07 17:33:15
########################################
from PIL import Image, ImageDraw

class ImgDrawer(object):
    def __init__(self, font=None, spacing=0):
        self.draw = ImageDraw.Draw(Image.new("RGB", (0,0)))
        self.font = font
        self.spacing = spacing
        self.awidth, self.aheight = self.draw.textsize("@", font=self.font, spacing=self.spacing)

    def __getbase(self, ascii_img):
        txt = "\n".join(ascii_img)
        width, height = self.draw.textsize(txt, font=self.font, spacing=self.spacing)
        return Image.new("RGB", (width, height), color=(255,255,255)), (width, height)


    def save_grey_ascii(self, save_name, ascii_img, ratio=0.5):
        img, size = self.__getbase(ascii_img)
        self.draw = ImageDraw.Draw(img)
        for i in range(len(ascii_img)):
            self.draw.text((0,self.aheight*i), ascii_img[i],
                           fill=(0,0,0), font=self.font, spacing=self.spacing)
        img = img.resize((int(size[0]*ratio), int(size[1]*ratio)), Image.BILINEAR)
        img.save(save_name)


    def save_color_ascii(self, save_name, ascii_img, color_map, ratio=0.5):
        img, size = self.__getbase(ascii_img)
        self.draw = ImageDraw.Draw(img)
        for i in range(len(ascii_img)):
            for j in range(len(ascii_img[i])):
                self.draw.text((self.awidth*j,self.aheight*i), ascii_img[i][j],
                               fill=color_map[i][j], font=self.font, spacing=self.spacing)
        img = img.resize((int(size[0]*ratio), int(size[1]*ratio)), Image.BILINEAR)
        img.save(save_name)



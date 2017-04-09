#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: CirQ
# Created Time: 17-4-7 下午1:21

from mp4_ascii.AsciiDrawer.AsciiImg import AsciiImg
from mp4_ascii.AsciiDrawer.ImgDrawer import ImgDrawer

"""
    Test for the functions of AsciiDrawer package.
    Testing including read an image then convert it into ascii form,
    and save this ascii image as a new jpg file.
"""

ai = AsciiImg()
ai.switch_to("cat.jpg")
idr = ImgDrawer()

gimg = ai.draw_grey_ascii()
idr.save_grey_ascii("grey_ascii_cat.jpg", gimg, ratio=0.7)

cimg, col = ai.draw_color_ascii(charset=AsciiImg.sort("miao~"))
idr.save_color_ascii("color_ascii_cat.jpg", cimg, col, ratio=0.7)
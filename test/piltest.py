#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: CirQ
# Created Time: 17-4-7 下午1:21

from mp4_ascii.AsciiDrawer.AsciiImg import AsciiImg
from mp4_ascii.AsciiDrawer.ImgDrawer import ImgDrawer

ai = AsciiImg()
ai.switch_to("cat.jpg")
img, col = ai.draw_color_ascii()
id = ImgDrawer()
id.save_color_ascii("hahaha.jpg", img, col, ratio=0.5)

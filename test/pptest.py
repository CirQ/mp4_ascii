#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: CirQ
# Created Time: 2017-04-08 17:30:04

from mp4_ascii.pixel_printer.pixel_printer import pixel_printer

"""
    Test for the function of pixel_printer.
"""

pp = pixel_printer("no.jpg")
pp.PRINT((1280, 1280), charset="wang", line=8)
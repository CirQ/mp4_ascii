#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: CirQ
# Created Time: 2017-04-09 11:09:02

from mp4_ascii.Mp4Processor.Mp4Reader import Mp4Reader
import time
import numpy
from PIL import Image

reader = Mp4Reader("gensou.mp4")
count = 0
for f in reader.frames():
    # cv2.imshow("BAKA", f)
    img = Image.fromarray(numpy.uint8(f))
    count += 1
    if count == 50:
        img.show()
        time.sleep(2)
        count = 0
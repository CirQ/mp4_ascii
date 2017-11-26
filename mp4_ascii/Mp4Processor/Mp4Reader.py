#! /usr/bin/env python
# -*- coding: utf-8 -*-
########################################
# Author: CirQ
# Created Time: 2017-04-08 17:09:59
########################################
import os
import cv2


class Mp4Reader(object):
    __VALID_FPS = [1, 2, 3, 4, 6, 8, 12, 24]

    def __init__(self, filename):
        self.__videocpture = None
        self.filename = filename

    def frames(self, fps=24):
        if fps not in self.__VALID_FPS:
            raise ValueError("FPS value can only be in %s." % self.__VALID_FPS)
        self.__videocpture = cv2.VideoCapture(self.filename)
        count, interval = 0, 24/fps
        while True: #self.__videocpture.isOpened(): #This is for better performance
            ret, frame = self.__videocpture.read()
            if ret:
                count += 1
                if count == interval:
                    count = 0
                    yield frame
            else:
                self.__videocpture.release()
                raise StopIteration

    def save_frames(self, **kw):
        fileprefix, i = self.filename.split(".")[0], 0
        dirname = "frames_" + fileprefix
        os.mkdir(dirname)
        for frame in self.frames(**kw):
            i += 1
            cv2.imwrite("%s/%s_%d.jpg"%(dirname, fileprefix, i), frame)

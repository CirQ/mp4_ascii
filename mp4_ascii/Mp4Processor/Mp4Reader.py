#! /usr/bin/env python
# -*- coding: utf-8 -*-
########################################
# Author: CirQ
# Created Time: 2017-04-08 17:09:59
########################################
import cv2


class Mp4Reader(object):
    def __init__(self, filename):
        self.__videocpture = None
        self.__filename = filename

    def frames(self):
        self.__videocpture = cv2.VideoCapture(self.__filename)
        while self.__videocpture.isOpened():
            ret, frame = self.__videocpture.read()
            yield frame
            if cv2.waitKey(1) & 0xFF == ord("q"):
                raise StopIteration
        self.__videocpture.release()
        cv2.destroyAllWindows()

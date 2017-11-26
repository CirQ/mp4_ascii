#! /usr/bin/env python
# -*- coding: utf-8 -*-
########################################
# Author: CirQ
# Created Time: 2017-04-09 20:34:17
########################################
from mp4_ascii.AsciiDrawer import AsciiImg
from mp4_ascii.AsciiDrawer import ImgDrawer
from mp4_ascii.Mp4Processor import Mp4Reader
from PIL import Image
import os
import cv2
import numpy


class ascii_player(object):
    def __init__(self, videoname, **kw):
        """
        This is the final class used to directly 
         generate ascii video and display it.
        :param videoname: the file name of the video
        :param kw: The same as ImgDrawer() constructor.
        """
        self.fileprefix = videoname.split(".")[0]
        self.dirname = "ascii_frames_" + self.fileprefix
        self.reader = Mp4Reader.Mp4Reader(videoname)
        self.ai = AsciiImg.AsciiImg()
        self.id = ImgDrawer.ImgDrawer(**kw)

    def save_ascii_frames(self, charset=None, **kw):
        """
        After an ascii_player instance is created,
         this method should be invoked to save all
         intermediate frames in a directory.
        :param charset: the charactor set of the ascii image.
        :param kw: the same as Mp4Reader.frames() iterator.
        """
        i = 0
        os.mkdir(self.dirname)
        for frame in self.reader.frames(**kw):
            i += 1
            img = Image.fromarray(numpy.uint8(frame))
            self.ai.to_image(img)
            ascii_img = self.ai.draw_grey_ascii(charset) if charset else self.ai.draw_grey_ascii()
            self.id.save_grey_ascii("%s/ascii_%s_%d.jpg"%(self.dirname, self.fileprefix, i), ascii_img)

    def delete_ascii_frames(self):
        """
        Delete all cached files (images), which will be hundreds of megabytes.
        """
        for fle in os.listdir(self.dirname):
            filepath = os.path.join(self.dirname, fle)
            os.remove(filepath)
        os.rmdir(self.dirname)

    def display_ascii(self, windowsize):
        """
        Display the ascii image like a video.
        :param windowsize: the size of displaying window.
        """
        frames = len(os.listdir(self.dirname))
        cv2.namedWindow(self.fileprefix, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(self.fileprefix, windowsize[0], windowsize[1])
        for i in range(1, frames+1):
            filepath = "%s/ascii_%s_%d.jpg" % (self.dirname, self.fileprefix, i)
            frame = cv2.imread(filepath)
            cv2.imshow(self.fileprefix, frame)
            cv2.waitKey(50)
        cv2.destroyAllWindows()

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: CirQ
# Created Time: 2017-04-09 11:09:02

from mp4_ascii.ascii_player import ascii_player

"""
    Test for generating and displaying a video in ascii form
    and then delete all intermediate cached frames.
"""

ap = ascii_player.ascii_player("gensou.mp4")
ap.save_ascii_frames(charset="MNHQ$OC?7>!:-;. ", fps=4)
ap.display_ascii((1280, 698))
ap.delete_ascii_frames()
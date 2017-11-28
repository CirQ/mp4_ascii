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
# ap.save_ascii_frames(ratio=0.16, charset="@#&Os*o~\"'`,. ", fps=6)
# ap.display_ascii()
ap.save_video(fps=6, size=(1428, 720)) # an ugly solution
# ap.delete_ascii_frames()
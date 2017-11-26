# mp4_ascii

This is a mp4 format video to ascii converter. Created in Apr. 7th, 2017, and seems far away from complete project.

And finally it is ended on Apr. 9th, but not complete yet.

---

### Purpose
The personal project is inspired by [this](http://www.bilibili.com/video/av8833366/) video, and what is learned is the usage of [python.Pillow](http://pillow.readthedocs.io) package and [python.OpenCV](http://opencv-python-tutroals.readthedocs.io) library.

---

### Source File
The sorce file is categorized into 4 parts, each part carries out an individual task.

+ **AsciiDrawer**: serves as an RGB-image to ascii-image convertor, the output can be saved as either grey or color image. The test case is shown in `imgtest.py`.
+ **pixel_printer**: to display an image lines-by-lines just like printing it, a by-product of this works that is unexpected before project planning. Test case in `pptest.py`.
+ **Mp4Processor**: the only job is to extract frames from a video in specific frame rate.
+ **ascii_player**: the final goal of this project, to display a video in ascii form, but it need a long time pre-processing and will generate hundreds of megabytes of image files. The package provide method to remove these intermediate files. Example shown as `vdotest.py`.

---

### Further improvement
Here I list some possible improvements for better performance.
+ Gathering all source file in a single directory, to obtain a more friendly file structure.
+ Improving the ways of parameter passing between classes.
+ Considering a block of pixels to compute a corresponding character, rather than read a single pixel. This will make the resulting image more ascii-style.
+ Applying digital-image-processing algorithms to gain nicer images.
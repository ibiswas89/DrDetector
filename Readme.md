#Drowsiness Detection OpenCV

This code can detect your eyes and alert when the user is drowsy

#Code Requirements

The example code is in Python (version 2.7 or higher will work).

#Dependencies

import cv2
import immutils
import dlib
import scipy
Description


#Algorithm

Each eye is represented by 6 (x, y)-coordinates, starting at the left-corner of the eye (as if you were looking at the person), and then working clockwise around the eye:


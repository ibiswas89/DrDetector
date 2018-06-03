# Drowsiness Detection OpenCV
This is a implementation of Drowsiness_Detection
Original repo can be found at 
https://github.com/akshaybahadur21/Drowsiness_Detection

This code can detect your eyes and alert when the user is drowsy

# Code Requirements

The example code is in Python (version 2.7 or higher will work).

# Dependencies

1. import cv2
2. import immutils
3. import dlib
4. import scipy


# Algorithm

Each eye is represented by 6 (x, y)-coordinates, starting at the left-corner of the eye (as if you were looking at the person), and then working clockwise around the eye:


# Drowsiness Detection OpenCV
This is a implementation of Drowsiness_Detection.
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

You would also need the pre-trained facial landmark detector file which can be downloaded from this link:
http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
Unzip this file and place it in the project directory before running the code
# Algorithm

Each eye is represented by 6 (x, y)-coordinates, starting at the left-corner of the eye (as if you were looking at the person), and then working clockwise around the eye.
We calculate the eye aspect ratio for each eye and average it out for both eyes.
If average eye aspect ratio is less than threshold then user is alerted

# Extras
A tutorial on the general working of dlib and facial landmark detection can be found at 
https://www.pyimagesearch.com/2017/04/03/facial-landmarks-dlib-opencv-python/

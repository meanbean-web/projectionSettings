# import necessary libraries and when you have the tar file import the projector files

import argparse
import imutils
import cv2
import time
from functions import ShapeDetector

#import piCamera

# 1: TURN PROJECTOR OFF BY DEFAULT
# use some Python GUI deal, that you can set to full screen

# 2: LOAD LIVE IMAGE DATA
# test image for now - we'll want it to be video stream later on

original = cv2.imread('test.jpg')
image = cv2.resize(original, (0,0), fx=0.5, fy=0.5)

# 3: EXTRACT CONTOURS
# load the image, convert it to grayscale, blur it slightly and threshold it

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

# find contours in the thresholded images
contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, contours, -1, (240, 0, 159), 3)

# display image + contours
cv2.imshow('win', image)

#logic?:
# find square contour, find center of square contour.


# CHECK IF SQUARE
# if the contours has 4 sides and 4 intersections, it is a square.



# IF SQUARE, FIND CENTER POINT


# AVERAGE SQUARE CONTOURS
# return one clean contour

# COMPUTE SQUARE CENTER


# TURN PROJECTOR ON

# DISPLAY PNG IMAGE AT SQUARE CENTER
# you'll always want the size of your png image to be x% of the total area of the detected square.

cv2.waitKey(1)

time.sleep(60)

cv2.destroyAllWindows()

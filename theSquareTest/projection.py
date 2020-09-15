# import necessary libraries and when you have the tar file import the projector files

import argparse
import imutils
import cv2
import time

#import piCamera

# 1: TURN PROJECTOR OFF BY DEFAULT

# 2: LOAD LIVE IMAGE DATA
# test image for now - we'll want it to be video stream later on

image = cv2.imread('test1.jpg')

# 3: EXTRACT CONTOURS
# load the image, convert it to grayscale, blur it slightly and threshold it

gray = cv2.cvtColor(cv2.UMat(image), cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

# find contours in the thresholded images
contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(thresh, contours, -1, cv2.UMat(0, 255, 0), 3)

# cv2.imshow('win', cnts)


# CHECK IF SQUARE
# if the contours has 4 sides and 4 intersections, it is a square.

# AVERAGE SQUARE CONTOURS
# return one clean contour

# COMPUTE SQUARE CENTER


# TURN PROJECTOR ON

# DISPLAY PNG IMAGE AT SQUARE CENTER
# you'll always want the size of your png image to be x% of the total area of the detected square.

cv2.waitKey(1)

time.sleep(60)

cv2.destroyAllWindows()

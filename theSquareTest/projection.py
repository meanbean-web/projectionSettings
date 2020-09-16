# import necessary libraries and when you have the tar file import the projector files

import argparse
import imutils
import cv2
import time

# from functions import ShapeDetector

# import piCamera

# 1: TURN PROJECTOR OFF BY DEFAULT
# use some Python GUI deal, that you can set to full screen

# 2: LOAD LIVE IMAGE DATA
# test image for now - we'll want it to be video stream later on

original = cv2.imread('test.jpg')
image = cv2.resize(original, (0, 0), fx=0.5, fy=0.5)

# 3: EXTRACT CONTOURS
# load the image, convert it to grayscale, blur it slightly and threshold it

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

# find contours in the thresholded images
contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#ratio = image.shape
font = cv2.FONT_HERSHEY_SIMPLEX

for c in contours:
    area = cv2.contourArea(c)
    approx = cv2.approxPolyDP(c, 0.04*cv2.arcLength(c, True), True)
    x = approx.ravel()[0]
    y = approx.ravel()[1]

    if 2000 < area < 150000:

        if len(approx) == 4:
            text = cv2.putText(image, "Rectangle", (x , y), font, 1, (240, 0, 159))
            cv2.drawContours(image, approx, -1, (240, 0, 159), 3)
            x_, y_, w, h = cv2.boundingRect(approx)
            cv2.rectangle(image, (x_, y_), (x_ + w, y_ + h), (240, 0, 159), 5)



cv2.imshow("win", image)



#     if len(approx) == 4:
#         shape = "square"
#         (x, y, w, h) = cv2.boundingRect(approx)
#         ar = w / float(h)
#         cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
#     else:
#         shape = "unidentified"
#
#

# display image + contours


# logic?:
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

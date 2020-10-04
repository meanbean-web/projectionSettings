from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy


#comments for improvement: separate the main chunks of this code into separate definitions

#1: detect chessboard
#2: load image from user on key input


#DECLARE CAMERA MODULE
camera = PiCamera()
camera.resolution = (848, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(848, 480))
camera.vflip = True

time.sleep(0.2)

#DECLARE CHESSBOARD PROPERTIES

imageSize = None # Determined at runtime
CHESSBOARD_CORNERS_ROWCOUNT = 8
CHESSBOARD_CORNERS_COLCOUNT = 5
objpoints = [] # 3D point in real world space where chess squares are
imgpoints = [] # 2D point in image plane, determined by CV2
objp = numpy.zeros((CHESSBOARD_CORNERS_ROWCOUNT*CHESSBOARD_CORNERS_COLCOUNT,3), numpy.float32)
# The following line fills the tuples just generated with their values (0, 0, 0), (1, 0, 0), ...
objp[:,:2] = numpy.mgrid[0:CHESSBOARD_CORNERS_ROWCOUNT,0:CHESSBOARD_CORNERS_COLCOUNT].T.reshape(-1, 2)


#GET REAL TIME VIDEO STREAM FOR RASPI

counter = 0

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    counter += 1
    img = frame.array

    #CALCULATE HISTOGRAM

    roi = cv2.imread('image files/circleGrid.png')
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    target = img
    hsvt = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)

    M = cv2.calcHist([hsv], [0,1], None, [180,256], [0,180,0,256])
    I = cv2.calcHist([hsvt], [0,1], None, [180,256], [0,180,0,256])

    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #
    # # DETECT RED CIRCLES FROM THE PROJECTOR
    # circles_grid_size = (4, 7)
    # ret, circles = cv2.findCirclesGrid(img, circles_grid_size, flags=cv2.CALIB_CB_SYMMETRIC_GRID)
    # img = cv2.drawChessboardCorners(img, circles_grid_size, circles, ret)

    cv2.imshow("Frame", img)
    key = cv2.waitKey(1) & 0xFF

    rawCapture.truncate(0)

    if key == ord("q"):
        break

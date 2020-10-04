import projectionControl
import cameraCalibration
import cv2
import time
from picamera import PiCamera
import yaml


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


# 1: call real-time camera calibration function, read yaml calibration file
#after this is done

# get live video input from pi camera, project detected chessboard
counter = 0

while frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    liveCalib(frame, chessboard_corners_rowcount, chessboard_corners_colcount)
    if liveCalib ended:
        print('calibration successful, moving to the next step')

    
    # project detected chessboard, print reprojection error
    img = cv2.drawChessboardCorners(image, patternSize=, corners=, patternWasFound=)

    #check number of good frames

    #

    if reprojectionError > value:
        # call from projectionControl def projectCircleGrid
        pattern = cv2.imread('image files/circlesGrid.png')
        images = img, pattern
        cv2.calcBackProject()
    # call projectionControl
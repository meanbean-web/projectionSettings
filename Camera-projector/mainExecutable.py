#from cameraCalibration import calibration
#from projectionControl import projectCircles
import cv2
import time
from picamera import PiCamera
from picamera.array import PiRGBArray
import numpy
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

while camera.capture_continuous:
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        counter += 1
        img = frame.array
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # DETECT CHESSBOARD / aruco marker

        board, corners = cv2.findChessboardCorners(gray, (CHESSBOARD_CORNERS_ROWCOUNT, CHESSBOARD_CORNERS_COLCOUNT),
                                                   None)
        if board:
            # Add the points in 3D that we just discovered
            objpoints.append(objp)

            # Enhance corner accuracy with cornerSubPix
            corners_acc = cv2.cornerSubPix(
                image=gray,
                corners=corners,
                winSize=(11, 11),
                zeroZone=(-1, -1),
                criteria=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30,
                          0.001))  # Last parameter is about termination critera
            imgpoints.append(corners_acc)

            # If our image size is unknown, set it now
            if not imageSize:
                imageSize = gray.shape[::-1]

            # Draw the corners to a new image to show whoever is performing the calibration
            # that the board was properly detected
            img = cv2.drawChessboardCorners(img, (CHESSBOARD_CORNERS_ROWCOUNT, CHESSBOARD_CORNERS_COLCOUNT),
                                            corners_acc,
                                            board)

            # DETECT RED CIRCLES FROM THE PROJECTOR
            circles_grid_size = (4, 7)
            ret, circles = cv2.findCirclesGrid(img, circles_grid_size, flags=cv2.CALIB_CB_SYMMETRIC_GRID)
            img = cv2.drawChessboardCorners(img, circles_grid_size, circles, ret)
        # preview checkerboard detection frame + vectorial orientation

        cv2.imshow("Frame", img)
        key = cv2.waitKey(1) & 0xFF

        rawCapture.truncate(0)

        if key == ord("q"):
            break

        if counter < 40:
            print(counter)

        # CALIBRATE CAMERA
        # if the number of retrieved images is 40, then calibrate the camera > you might want to add the first 40 frames to a folder

        if counter == 40:
            calibration, cameraMatrix, distCoeffs, rvecs, tvecs = cv2.calibrateCamera(
                objectPoints=objpoints,
                imagePoints=imgpoints,
                imageSize=imageSize,
                cameraMatrix=None,
                distCoeffs=None)

            # Print matrix and distortion coefficient to the console
            print(cameraMatrix)
            print(distCoeffs)

    # if reprojectionError > value:
    #     # call from projectionControl def projectCircleGrid
    #     pattern = cv2.imread('image files/circlesGrid.png')
    #     images = img, pattern
    #     cv2.calcBackProject()
    # # call projectionControl
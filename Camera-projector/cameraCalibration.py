# calibrate camera, write values to yaml file
import cv2


def calibration (frame, counter, CHESSBOARD_CORNERS_ROWCOUNT, CHESSBOARD_CORNERS_COLCOUNT, objpoints, imgpoints, imageSize, objp):
    counter += 1
    img = frame.array
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # DETECT CHESSBOARD / aruco marker

    board, corners = cv2.findChessboardCorners(gray, (CHESSBOARD_CORNERS_ROWCOUNT, CHESSBOARD_CORNERS_COLCOUNT), None)
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
        img = cv2.drawChessboardCorners(img, (CHESSBOARD_CORNERS_ROWCOUNT, CHESSBOARD_CORNERS_COLCOUNT), corners_acc,
                                        board)

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

    # counter += 1
    # img = frame.array
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #
    # # LIVE CAMERA CALIBRATION
    # boards = [] #number of boards in which a checkerboard has been detected
    # goodBoards = [] #number of boards with a reprojection error smaller than
    # maxCameraError = 0 # see how you get this guy
    #
    # if maxCameraError < 0.5:
    #     goodBoards = #mark as goodBoard and trigger counter
    #
    # if goodBoards == 40: #when you collect 40 good boards / good chessboard views
    #     cv2.calibrateCamera()
    #     calibration = yaml.dump()
    #
    # return cameraCalib

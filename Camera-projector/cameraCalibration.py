# calibrate camera, write values to yaml file



def liveCalibrate(img, checkerboard):
    counter += 1
    img = frame.array
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # LIVE CAMERA CALIBRATION
    boards = [] #number of boards in which a checkerboard has been detected
    goodBoards = [] #number of boards with a reprojection error smaller than
    maxCameraError = 0 # see how you get this guy

    if maxCameraError < 0.5:
        goodBoards = #mark as goodBoard and trigger counter

    if goodBoards == 40: #when you collect 40 good boards / good chessboard views
        cv2.calibrateCamera()
        calibration = yaml.dump()

    return cameraCalib

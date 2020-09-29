import numpy
import cv2
import pickle
import glob
import time
import yaml
from picamera import PiCamera
from picamera.array import PiRGBArray


# DECLARE PICAMERA
camera = PiCamera ()
camera.resolution = (840, 480)
camera.vflip = True
camera.framerate = 32
rawCapture = PiRGBArray(camera, size= (840, 480))
time.sleep(0.5)  # allow picamera to warm up


imageSize = None # Determined at runtime

# CAPTURE CONTINUOUS STREAM

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array  # store each incoming image as a numpy array

    # cv2.imshow("Frame", image)

    # while (True):

    # Read frame by frame
    # cv2.imshow ("Frame", image)

    # Laterally flip the frame
    image = cv2.flip(image, 1)

    # Calculate the Average FPS
    image_counter += 1
    fps = (image_counter / (time.time() - start_time))

    # Create a clean copy of the frame
    copy = image.copy()

    # Downsize the frame.
    new_width = int(image.shape[1] / scale_factor)
    new_height = int(image.shape[0] / scale_factor)
    images = cv2.resize(copy, (new_width, new_height))

    for iname in images:
        # Open the image
        img = cv2.imread(iname)
        # Grayscale the image
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Find chessboard in the image, setting PatternSize(2nd arg) to a tuple of (#rows, #columns)
        board, corners = cv2.findChessboardCorners(gray, (CHESSBOARD_CORNERS_ROWCOUNT, CHESSBOARD_CORNERS_COLCOUNT),
                                                   None)

        # If a chessboard was found, let's collect image/corner points
        if board == True:
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
                                            corners_acc, board)
            # Pause to display each image, waiting for key press
            cv2.imshow('Chessboard', img)
            cv2.waitKey(1)
            # time.sleep(1)
        else:
            print("Not able to detect a chessboard in image: {}".format(iname))

    # cv2.imshow("Frame", image) #display each new incoming image
    key = cv2.waitKey(1) & 0xFF

    rawCapture.truncate(0)  # clear stream for next frame

    if key == ord("q"):
        break

    img.release()

    # Destroy any open CV windows
    cv2.destroyAllWindows()

    # Make sure at least one image was found
    if len(images) < 1:
        # Calibration failed because there were no images, warn the user
        print(
            "Calibration was unsuccessful. No images of chessboards were found. Add images of chessboards and use or alter the naming conventions used in this file.")
        # Exit for failure
        exit()

    # Make sure we were able to calibrate on at least one chessboard by checking
    # if we ever determined the image size
    if not imageSize:
        # Calibration failed because we didn't see any chessboards of the PatternSize used
        print(
            "Calibration was unsuccessful. We couldn't detect chessboards in any of the images supplied. Try changing the patternSize passed into findChessboardCorners(), or try different pictures of chessboards.")
        # Exit for failure
        exit()

    # Now that we've seen all of our images, perform the camera calibration
    # based on the set of points we've discovered
    calibration, cameraMatrix, distCoeffs, rvecs, tvecs = cv2.calibrateCamera(
        objectPoints=objpoints,
        imagePoints=imgpoints,
        imageSize=imageSize,
        cameraMatrix=None,
        distCoeffs=None)

    # Print matrix and distortion coefficient to the console
    print(cameraMatrix)
    print(distCoeffs)

    # Save values to be used where matrix+dist is required, for instance for posture estimation
    # I save files in a pickle file, but you can use yaml or whatever works for you

    # save it in yaml maybe, we'll see
    f = open('calibration-files/calibration.yaml', 'wb')
    yaml.dump((cameraMatrix, distCoeffs, rvecs, tvecs), f)
    f.close()

    # Print to console our success
    print('Calibration successful. Calibration file used: {}'.format('calibration.pckl'))

    # Display the image
    #cv2.imshow('frame', images)




# cv2.destroyAllWindows()




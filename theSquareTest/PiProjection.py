import imutils
import cv2
import time
from  picamera import PiCamera
from picamera.array import PiRGBArray
 
# 1: TURN PROJECTOR OFF BY DEFAULT

# 2: LOAD LIVE IMAGE DATA
# test image for now - we'll want it to be video stream later on

# declare picamera
camera = PiCamera ()
camera.resolution = (840, 480)
camera.vflip = True
camera.framerate = 32
rawCapture = PiRGBArray(camera, size= (840, 480))
time.sleep(0.5) #allow picamera to warm up

font = cv2.FONT_HERSHEY_SIMPLEX

# capture continuous image stream

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    original = frame.array #store each incoming image as a numpy array
    image = cv2.resize(original, (0, 0), fx=0.5, fy=0.5)

    image = cv2.flip(image, 1)
    # 3: EXTRACT CONTOURS
    # load the image, convert it to grayscale, blur it slightly and threshold it

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

    # find contours in the thresholded images
    contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, contours, -1, (240, 0, 159), 3)

    for c in contours:
        area = cv2.contourArea(c)
        approx = cv2.approxPolyDP(c, 0.04 * cv2.arcLength(c, True), True)
        x = approx.ravel()[0]
        y = approx.ravel()[1]

        if 2000 < area < 150000:

            if len(approx) == 4:
                text = cv2.putText(image, "Rectangle", (x, y), font, 1, (240, 0, 159))
                #cv2.drawContours(image, approx, -1, (240, 0, 159), 3)
                x_, y_, w, h = cv2.boundingRect(approx)
                cv2.rectangle(image, (x_, y_), (x_ + w, y_ + h), (240, 0, 159), 5)

    cv2.imshow("win", image)

    key = cv2.waitKey(1) & 0xFF

    rawCapture.truncate(0)  # clear stream for next frame

    if key == ord("q"):
        break

image.release()
cv2.destroyAllWindows()











# CHECK IF SQUARE
# if the contours has 4 sides and 4 intersections, it is a square.



# IF SQUARE, FIND CENTER POINT


# AVERAGE SQUARE CONTOURS
# return one clean contour

# COMPUTE SQUARE CENTER


# TURN PROJECTOR ON

# DISPLAY PNG IMAGE AT SQUARE CENTER
# you'll always want the size of your png image to be x% of the total area of the detected square.



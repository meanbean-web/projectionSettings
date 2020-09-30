from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

camera = PiCamera()
camera.resolution = (848, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(848, 480))
camera.vflip = True

img = cv2.imread('image displays/circleGrid.png')
print(img)

time.sleep(0.2)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #detect chessboard in the images supplied by the pi camera



    #full screen frame

    cv2.namedWindow("Frame", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Frame", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    #you need to add a break key for this






    cv2.imshow("Frame", gray)
    key = cv2.waitKey(1) & 0xFF

    rawCapture.truncate(0)

    if key == ord("q"):
        break
import cv2
import time

img = cv2.imread('circleGrid.png')
cv2.namedWindow('screen', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('screen', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.imshow('screen', img)
cv2.waitKey(1)
time.sleep(120)

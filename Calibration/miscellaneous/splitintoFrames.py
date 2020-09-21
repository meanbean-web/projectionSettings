import cv2
import numpy as np
import os

video = cv2.VideoCapture('cal.mp4')

print(video)

try:
    if not os.path.exists('cal-img-cb1'):
        os.makedirs('cal-img-cb1')
except OSError:
    print('Error creating directory of data')

# initialize current frame
currentFrame = 0
while (True):
    ret, frame = video.read()
    name = './cal-img-cb1/frame' + str(currentFrame) + '.jpg'
    print('Creating...' + name)
    cv2.imwrite(name, frame)

    # stop duplicate images
    currentFrame += 1

video.release()
cv2.destroyAllWindows
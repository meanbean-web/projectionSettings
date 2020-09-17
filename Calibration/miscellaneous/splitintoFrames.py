import cv2
import numpy as np
import os

video = cv2.VideoCapture('calibration-opt.mp4')

print(video)

try:
    if not os.path.exists('../cal-img'):
        os.makedirs('../cal-img')
except OSError:
    print('Error creating directory of data')

# initialize current frame
currentFrame = 0
while (True):
    ret, frame = video.read()
    name = './cal-img/frame' + str(currentFrame) + '.jpg'
    print('Creating...' + name)
    cv2.imwrite(name, frame)

    # stop duplicate images
    currentFrame += 1

video.release()
cv2.destroyAllWindows
# recording.py
from picamera import PiCamera
import time

camera = picamera.PiCamera()
camera.vflip = True
#camera.start_preview()
camera.framerate = 32
camera.start_recording(‘calibration.h264’)
camera.wait_recording(3000)
camera.stop_recording()
#camera.stop_preview()
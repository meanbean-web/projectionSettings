# recording.py
from picamera import PiCamera
import time

camera = PiCamera()
camera.vflip = True
#camera.start_preview()
camera.framerate = 32
camera.start_recording("calibration")
camera.wait_recording(3000)
camera.stop_recording()
#camera.stop_preview()
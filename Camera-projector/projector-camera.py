import cv2
import numpy
import yaml
import pickle

#IMPORT CAMERA CALIBRATION MATRIX
#read calibration variables from yaml file & pass them to the calibrateCamera

# with open(r'calibration-files/calibration.yaml') as file:
#     doc = yaml.load(file, Loader=yaml.FullLoader)

fs = cv2.FileStorage("calibration-files/calibration.pckl", cv2.FILE_STORAGE_READ)
fn = fs.getNode("camera_matrix")
print(fn.mat())

# cv2.calibrateCamera()

#cv2 project circle matrix (create matrix and color in here) & then display full screen

#get video stream from calibrated picamera
#within that video stream, we first need to detect and register the world transformations of the board

#detect corners & display circles in real time

#--------------------------------------------------------------------------------

#detect circle pattern in the live video-stream

#COMPUTE 3D POSITION OF PROJECTED CIRCLES

#use backprojection to search for the original pattern in the live video-stream
#create xyz plane coordinates & display as an extension of the checkerboard
#intersect the detected projected points with the extended plane

#get calibration coefficients for projector & camera






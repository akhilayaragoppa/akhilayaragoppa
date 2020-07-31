"""
A simulation of a invisibility cloak as seen in Harry Potter.

Note: Current setting works on a dark blue cloak in a room with good lighting :)
"""
import cv2
import numpy as np

cam = cv2.VideoCapture(0)   # 0 argument creates a default web-cam object
# Get properties from cv::VideoCaptureProperties ENUM
cam.set(3, 640)             # Width
cam.set(4, 480)             # Height (VGA size)
cam.set(10, 150)            # Brightness

success, imgCam = cam.read()

while True:
    success, img = cam.read()

    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([79, 65, 0])           # Dark Blue cloak
    upper = np.array([120, 255, 255])
    mask = cv2.inRange(imgHSV, lower, upper)
    mask_inv = cv2.bitwise_not(mask)

    img1 = cv2.bitwise_and(img,img, mask = mask_inv)
    img2 = cv2.bitwise_and(imgCam,imgCam, mask = mask)
    imgResult = cv2.add(img1,img2)
    cv2.imshow("Output", imgResult)
    if (cv2.waitKey(1) & 0XFF) == ord('q'):     # Quit when q is pressed
        break
import cv2
import numpy as np

myColors = [['Yellow',(0,255,255),18,61,164,45,246,255],
            ['Orange',(0,165,255),4,112,162,17,255,255],
            ['Green',(0,204,0),49,83,102,76,255,202],
            ['Blue',(255,51,51),93,96,141,118,255,255]]
points = []

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def findColors(img, myColors):

    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    points = []
    for color in myColors:
        lower = np.array(color[2:5])
        upper = np.array(color[5:])
        mask = cv2.inRange(imgHSV, lower, upper)
        #cv2.imshow(color[0],mask)
        x,y = getContours(mask)
        #cv2.circle(imgResult, (x,y), 10, color[1], cv2.FILLED)

        if x and y:
            points.append([x,y,color[1]])
    return points

def getContours(mask):
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    area_max = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 1000:
            #cv2.drawContours(imgResult, cnt, -1, (255, 200, 100), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            x, y, w, h = cv2.boundingRect(approx)

    return (x+w, y)

def drawOnImage(imgResult, points):
    for point in points:
        cv2.circle(imgResult, (point[0],point[1]), 10, point[2], cv2.FILLED)

cam = cv2.VideoCapture(0)   # 0 argument creates a default web-cam object
cam.set(3, 640)             # Width
cam.set(4, 480)             # Height (VGA size)
cam.set(10, 150)            # Brightness

while True:
    success, img = cam.read()
    imgResult = img.copy()

    pts = findColors(img, myColors)
    points.extend(pts)
    drawOnImage(imgResult, points)
    cv2.imshow("Virtual Paint", imgResult)
    if (cv2.waitKey(1) & 0XFF) == ord('q'):     # Quit when q is pressed
        break
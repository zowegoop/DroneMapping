from djitellopy import Tello
import KeyPressModule as kp
from time import sleep
import cv2
import numpy as np
import math

######## PARAMETERS ###########
fspeed = 117/10 # Foward Speed in cm/s  (15cm/s)
aspeed = 360/10 # Angular Speed Degrees/s
interval = 0.25


dInterval = fSpeed*interval
aInterval = aSpeed*interval
###############################

points = []

kp.init()
tello = Tello()
tello.connect()
print(tello.get_battery())
tello.streamon()

def getKeyboardInput():

    lr, fb, ud, yv = 0, 0, 0, 0

    speed = 50

    if kp.getKey("LEFT"): lr = -speed

    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): fb = speed

    elif kp.getKey("DOWN"): fb = -speed

    if kp.getKey("w"):ud = speed

    elif kp.getKey("s"): ud = -speed

    if kp.getKey("a"):yv = -speed

    elif kp.getKey("d"): yv = speed

    if kp.getKey("q"): tello.land(); sleep(3)

    if kp.getKey("e"): tello.takeoff()

    return [lr, fb, ud, yv]

def drawPoints(img, points):
    for point in points:
        cv2.circle(img, points, 10, (0, 0, 255), cv2.FILLED)

while True:

    vals = getKeyboardInput()

    tello.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    img = np.zeros((1000, 1000, 3), np.uint8)
    points.append = (vals[4], vals[5])
    drawPoints(img, points)

    cv2.imshow("Output", img)
    cv2.waitKey(1)

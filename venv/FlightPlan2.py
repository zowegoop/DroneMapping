#!/usr/bin/env python3

# Rescue mission in the mountains 2

# if running locally, you need to install the djitello module
# run this on your linux or mac machine
# pip3 install djitello

######## PARAMETERS ###########
fspeed = 117/10 # Foward Speed in cm/s  (15cm/s)
aspeed = 360/10 # Angular Speed Degrees/s
interval = 0.25


dInterval = fSpeed*interval
aInterval = aSpeed*interval
###############################

# Install the module
from djitellopy import Tello
from time import sleep

# Create our tello drone object
drone = Tello()

# Take off and up
drone.connect()
drone.takeoff()

# Move up to 6 ft
# Convert everything to centimeters
tello.send_rc_control(0,0,50,0)
sleep(3.8)

# Rotate 12 degrees counter clockwise
tello.send_rc_control(0,0,0,-50)
sleep(.43)

# Move forward 436cm (14.3 ft)
tello.send_rc_control(0,50,0,0)
sleep(4)

tello.send_rc_control(0,0,0,0)

# Land the drone
tello.land()
# Measure distance using an ultrasonic module
#
# Adapted from : Matt Hawkins https://www.raspberrypi-spy.co.uk/2012/12/ultrasonic-distance-measurement-using-python-part-1/
# Adapted from : https://www.fred-j.org/?p=366

import RPi.GPIO as GPIO
import time
import sys
import numpy as np


#define the pins
TRIG = 20
ECHO = 21
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
i = 0
dis = np.zeros(5)

#------------- PORTS --------------------
Motor_1_Forward = 25
Motor_1_Reverse = 24
Motor_2_Forward = 23
Motor_2_Reverse = 18
Motor_1_Enable = 17
Motor_2_Enable = 27

#------------- Initialisation --------------
GPIO.setup(Motor_1_Forward, GPIO.OUT)
GPIO.setup(Motor_1_Reverse, GPIO.OUT)
GPIO.setup(Motor_2_Forward, GPIO.OUT)
GPIO.setup(Motor_2_Reverse, GPIO.OUT)
GPIO.setup(Motor_1_Enable, GPIO.OUT)
GPIO.setup(Motor_2_Enable, GPIO.OUT)
GPIO.output(Motor_1_Enable, GPIO.HIGH)
GPIO.output(Motor_2_Enable, GPIO.HIGH)
  
#--------------------------------------------
def reject_outliers(data, m):
    #print(m * np.std(data))
    return data[abs(data - np.mean(data)) < m * np.std(data)]

def GO() :
    print("Moving forwards")
    GPIO.output(Motor_1_Forward, GPIO.HIGH)
    GPIO.output(Motor_2_Forward, GPIO.HIGH)
    GPIO.setup(Motor_1_Reverse, GPIO.LOW)
    GPIO.setup(Motor_2_Reverse, GPIO.LOW)
 
def BACKWARDS() :
    print("Moving backwards")
    GPIO.setup(Motor_1_Forward, GPIO.LOW)
    GPIO.setup(Motor_2_Forward, GPIO.LOW)
    GPIO.output(Motor_1_Reverse, GPIO.HIGH)
    GPIO.output(Motor_2_Reverse, GPIO.HIGH)
 
def RIGHT() :
    print("Turning right")
    GPIO.output(Motor_1_Forward, GPIO.HIGH)
    GPIO.output(Motor_2_Reverse, GPIO.HIGH)
    time.sleep(0.5)
    STOP()
 
def RIGHT_Cont() :
    print("Turning right continuously")
    GPIO.output(Motor_1_Forward, GPIO.HIGH)
    GPIO.output(Motor_2_Reverse, GPIO.HIGH)
    GPIO.setup(Motor_1_Reverse, GPIO.LOW)
    GPIO.setup(Motor_2_Forward, GPIO.LOW)
 
def LEFT() :
    print("Turning left")
    GPIO.output(Motor_1_Reverse, GPIO.HIGH)
    GPIO.output(Motor_2_Forward, GPIO.HIGH)
    time.sleep(0.5)
    STOP()
 
def LEFT_Cont() :
    print("Turning left continuously")
    GPIO.output(Motor_1_Reverse, GPIO.HIGH)
    GPIO.output(Motor_2_Forward, GPIO.HIGH)
    GPIO.setup(Motor_2_Reverse, GPIO.LOW)
    GPIO.setup(Motor_1_Forward, GPIO.LOW)
    
def STOP() :
    print("stop")
    GPIO.output(Motor_1_Forward, GPIO.LOW)
    GPIO.output(Motor_2_Forward, GPIO.LOW)
    GPIO.output(Motor_1_Reverse, GPIO.LOW)
    GPIO.output(Motor_2_Reverse, GPIO.LOW)

print("Running")

#---------------------------------------
while 1:
    # Set trigger to False (Low)
    GPIO.output(TRIG, False)

    # Allow module to settle
    time.sleep(0.5)

    # Send 10us pulse to trigger
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    start = time.time()

    while GPIO.input(ECHO)==0:
        start = time.time()

    while GPIO.input(ECHO)==1:
        stop = time.time()

    # Calculate pulse length
    elapsed = stop-start

    # Distance pulse travelled in that time is time
    # multiplied by the speed of sound (cm/s)
    distance = elapsed * 34300

    # That was the distance there and back so halve the value
    distance = distance / 2

    i+=1
    if i > 4:
        i = 0
        #print(f"Distance : {dis}")
        dis2 = reject_outliers(dis, 1)
        #print(f"Distance cleaned: {dis2}")
        avgdis = int(np.mean(dis2))
        print(f"Avg: {avgdis}")
        if avgdis > 40:
            BACKWARDS() 
        elif avgdis < 20:
            GO()
        else: 
            STOP()

    dis[i] = distance
    
    


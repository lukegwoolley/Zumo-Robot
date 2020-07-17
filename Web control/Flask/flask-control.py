#----------------------------------------
#                CREDIT
# motor code adapted from https://www.fred-j.org/?p=366

# flask Adapted excerpt from Getting Started with Raspberry Pi by Matt Richardson, Modified by Rui Santos Complete project details: https://randomnerdtutorials.com

# threading from following tutorial: https://realpython.com/intro-to-python-threading/
#----------------------------------------

import RPi.GPIO as GPIO
import time
import sys
import logging
import threading
import concurrent.futures
import numpy as np
from tasks import threaded_task 
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

#defines
i = 0
dis = np.zeros(3)
dis2 = 100 
  
#------------- PORTS --------------------
Motor_1_Forward = 25
Motor_1_Reverse = 24
Motor_2_Forward = 23
Motor_2_Reverse = 18
Motor_1_Enable = 17
Motor_2_Enable = 27
TRIG = 20
ECHO = 21

#create a dictionary for the commands  
func = {
   "GO" : "off",
   "BACKWARDS" : "off",
   "RIGHT" : "off",
   "LEFT": "off",
   "STOP" : "on",
}

#------------- Initialisation --------------
 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(Motor_1_Forward, GPIO.OUT)
GPIO.setup(Motor_1_Reverse, GPIO.OUT)
GPIO.setup(Motor_2_Forward, GPIO.OUT)
GPIO.setup(Motor_2_Reverse, GPIO.OUT)
GPIO.setup(Motor_1_Enable, GPIO.OUT)
GPIO.setup(Motor_2_Enable, GPIO.OUT)
GPIO.output(Motor_1_Enable, GPIO.HIGH)
GPIO.output(Motor_2_Enable, GPIO.HIGH)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
  
 
#--------------------------------------------
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
    GPIO.output(Motor_2_Reverse, GPIO.LOW)
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
    GPIO.output(Motor_1_Reverse, GPIO.LOW)
    GPIO.output(Motor_2_Forward, GPIO.HIGH)
    GPIO.setup(Motor_2_Reverse, GPIO.LOW)
    GPIO.setup(Motor_1_Forward, GPIO.LOW)
    
def STOP() :
    print("stop")
    GPIO.output(Motor_1_Forward, GPIO.LOW)
    GPIO.output(Motor_2_Forward, GPIO.LOW)
    GPIO.output(Motor_1_Reverse, GPIO.LOW)
    GPIO.output(Motor_2_Reverse, GPIO.LOW)

def read_sensor() :

    global dis2
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
    if i > 2:
        i = 0
        dis2 = np.min(dis) #the ultrasonic sensor only registers too high not really too low so this might be quicker
        print(f"Dis: {dis2}")
    dis[i] = distance
    

print("Running")
 
# --------------------------------------
@app.route("/")
def main():

    print("Start thread")
    thread = Thread(target=read_sensor,)
    thread.daemon = True
    thread.start()
    print("Thread started")
    # Pass the template data into the template main.html and return it to the user
    return render_template('main_press.html', func=func)

# The function below is executed when someone requests a URL with the mode and action in it:
@app.route("/<changeMode>/<action>")
def action(changeMode, action):
    # Convert the mode from the URL into a string:
    changeMode = str(changeMode)
    # If the action part of the URL is "on," execute the code indented below:
    if 10 < dis2 < 20:
       STOP()
    elif dis2 < 10:
       GO()
    else:
        if action == "on":
            if changeMode == "GO":
                GO()
            elif changeMode == "BACKWARDS":
                BACKWARDS()
            elif changeMode == "LEFT":
                LEFT_Cont()
            elif changeMode == "RIGHT":
                RIGHT_Cont()
            elif changeMode == "STOP":
                STOP()	  
            # Save the status message to be passed into the template:
            message = "Turned " + changeMode + " on."
            print(message)
        if action == "off":
            STOP()

   # Along with the pin dictionary, put the message into the template data dictionary:
    func[changeMode] = action

    return render_template('main_press.html', func=func)

if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True)

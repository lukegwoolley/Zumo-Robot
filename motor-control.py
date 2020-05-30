#----------------------------------------
#                CREDIT
# motor code adapted from https://www.fred-j.org/?p=366

#----------------------------------------

from RPIO import PWM
import RPIO
import RPi.GPIO as GPIO
import time
import sys
 
#------------- PORTS --------------------
Motor_1_Forward = 25
Motor_1_Reverse = 24
Motor_2_Forward = 23
Motor_2_Reverse = 18
 
#------------- Initialisation --------------
 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(Motor_1_Forward, GPIO.OUT)
GPIO.setup(Motor_1_Reverse, GPIO.OUT)
GPIO.setup(Motor_2_Forward, GPIO.OUT)
GPIO.setup(Motor_2_Reverse, GPIO.OUT)
  
 
#--------------------------------------------
def GO() :
    print "Moving forwards"
    GPIO.output(Motor_1_Forward, GPIO.HIGH)
    GPIO.output(Motor_2_Forward, GPIO.HIGH)
 
def BACKWARDS() :
    print "Moving backwards"
    GPIO.output(Motor_1_Reverse, GPIO.HIGH)
    GPIO.output(Motor_2_Reverse, GPIO.HIGH)
 
def RIGHT() :
    print "Turning right"
    GPIO.output(Motor_1_Forward, GPIO.HIGH)
    GPIO.output(Motor_2_Reverse, GPIO.HIGH)
    time.sleep(0.5)
    STOP()
 
def RIGHT_Cont() :
    print "Turning right continuously"
    GPIO.output(Motor_1_Forward, GPIO.HIGH)
    GPIO.output(Motor_2_Reverse, GPIO.HIGH)
 
def LEFT() :
    print "Turning left"
    GPIO.output(Motor_1_Reverse, GPIO.HIGH)
    GPIO.output(Motor_2_Forward, GPIO.HIGH)
    time.sleep(0.5)
    STOP()
 
def LEFT_Cont() :
    print "Turning left continuously"
    GPIO.output(Motor_1_Reverse, GPIO.HIGH)
    GPIO.output(Motor_2_Forward, GPIO.HIGH)
 
 
def STOP () :
    print "stop"
    GPIO.output(Motor_1_Forward, GPIO.LOW)
    GPIO.output(Motor_2_Forward, GPIO.LOW)
    GPIO.output(Motor_1_Reverse, GPIO.LOW)
    GPIO.output(Motor_2_Reverse, GPIO.LOW)
 
 def MENU() :
    print( "\n\r" )
    print("  F  --> Forwards\n" )
    print( "  B  --> Backwards\n" )
    print( "  R  --> Right\n" )
    print( "  RR --> Right continuously\n" )
    print( "  L  --> Left\n" )
    print( "  LL --> Left continuously\n" )
    print( "  S  --> Stop\n" )
    print( "  M  --> MENU\n" )
    print( "\n" )
 
print "Running"
 
# --------------------------------------
while 1:
      print "What would you like to do? \n"
      if input() == "finish" or input == "" or input() == "stop":
         print "Program terminated."
         break
 
      elif input() == "M" :
         MENU()
 
      # Robot Commands
      elif input() == "F" :
         FORWARD()
      elif input() == "R" :
         BACKWARDS()
      elif input() == "R" :
         RIGHT()
      elif input() == "RR" :
         RIGHT_Cont()
      elif input() == "L" :
         LEFT()
      elif input() == "LL" :
         LEFT_Cont()
      elif input() == "S" :
         STOP()

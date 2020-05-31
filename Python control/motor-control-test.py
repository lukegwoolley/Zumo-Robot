#----------------------------------------
#                CREDIT
# motor code adapted from https://www.fred-j.org/?p=366

#----------------------------------------

import time
import sys
 
 
 
#--------------------------------------------
def GO() :
    print("Moving forwards")
    
 
def BACKWARDS() :
    print("Moving backwards")
    
 
def RIGHT() :
    print("Turning right")
    time.sleep(0.5)
    STOP()
 
def RIGHT_Cont() :
    print("Turning right continuously")
    
 
def LEFT() :
    print("Turning left")
    time.sleep(0.5)
    STOP()
 
def LEFT_Cont() :
    print("Turning left continuously")
 
 
def STOP() :
    print("stop")
 
def MENU() :
    print("\n\r")
    print("  F  --> Forwards\n")
    print("  B  --> Backwards\n")
    print("  R  --> Right\n")
    print("  RR --> Right continuously\n")
    print("  L  --> Left\n")
    print("  LL --> Left continuously\n")
    print("  S  --> Stop\n")
    print("  M  --> MENU\n")
    print("\n")

print("Running")
 
# --------------------------------------
while 1:
      ival = input("What would you like to do? \n")
      if ival == "finish" or ival == "" or ival == "stop":
         print("Program terminated.")
         break
 
      elif ival == "M" :
         MENU()
 
      # Robot Commands
      elif ival == "F" :
         GO()
      elif ival == "R" :
         BACKWARDS()
      elif ival == "R" :
         RIGHT()
      elif ival == "RR" :
         RIGHT_Cont()
      elif ival == "L" :
         LEFT()
      elif ival == "LL" :
         LEFT_Cont()
      elif ival == "S" :
         STOP()

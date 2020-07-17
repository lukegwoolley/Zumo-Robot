import sys
import numpy as np

dis2 = 100

def testing():
    dis = [10, 30, 100]
    global dis2 
    dis2 = np.min(dis)
    print(dis2)

testing()

print(dis2)
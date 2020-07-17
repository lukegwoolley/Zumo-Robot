import sys
import numpy as np
from celery import Celery 

app = Celery('test', broker='pyamqp://guest@localhost//')

dis2 = 100
print(dis2)

@app.task
def testing():
    dis = [10, 30, 100]
    global dis2 
    dis2 = np.min(dis)
    print(dis2)

testing()

print(dis2)
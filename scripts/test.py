#from Control import MotorStop
import sys
sys.path.append("/home/cubesat/Documents/venv/lib/python3.11/site-packages/")
print(sys.path)
import ICM20948
import time
import math
from timeit import default_timer as timer
from adafruit_motorkit import MotorKit
import time
kit = MotorKit()
kit.motor3.throttle = 0
#motor=Motor.correction()
#motor.MotorStop()
#MotorStop()
time.sleep(2)
#while True:
	#Motor.Correction()

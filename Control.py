#from motor import (MotorRun,MotorStop)
import ICM20948
import time
import math
from timeit import default_timer as timer
from adafruit_motorkit import MotorKit
class Motor:
	def correction():
		def MotorRun(throttle):
			kit = MotorKit()
			kit.motor1.throttle = throttle
		def MotorStop():
			kit = MotorKit()
			kit.motor1.throttle = 0
		start=timer()
		while True:
			Time=timer()-start
			theta=Time/5553.5*360
			theta=math.fmod(theta,360)
			theta=360*math.sin(2*Time/5553.5*math.pi)
			time.sleep(3)
			object=ICM20948.ICM20948.aa()
			TT=theta-object
			#print("difference in angles = ",TT," degres")
			while TT<10 or TT>-10:
				object=ICM20948.ICM20948.aa()
				TT=theta-object
				print(TT)
				if TT>10:
					 MotorRun(1)
					 time.sleep(.1)
					 #print(":(")
				elif TT<-10:
					MotorRun(-1)
					time.sleep(.1)
					#print(":(")
				else:
					MotorStop()
					break
					#print(":)")
			#print("end loop")


import sys
import threading
import time
import select
import termios
import tty
from threading import Timer
import time
from picamera2 import Picamera2
import binascii
from timeit import default_timer as timer
global timer_task
picam = Picamera2()
config = picam.create_preview_configuration(main={"size":(480,480)})
picam.configure(config)
picam.options['quality']=1
picam.start()
global seconds
ite=0
def take_pic (continue_or_not = True):
	if continue_or_not:
		start=timer()

		global ite
		picam.capture_file("Images/r"+str(ite)+".jpg")

		filename="r"+str(ite)+".jpg"
		with open("Images/"+filename, 'rb') as f:
			content=f.read()
		f=open("Images/r"+str(ite)+'.txt','w')
		f.write(binascii.hexlify(content).decode())
		f.close
		ite=ite+1
		time.sleep(59.5)
		TotalTime=timer()-start
		print(TotalTime)
while True:
    take_pic()

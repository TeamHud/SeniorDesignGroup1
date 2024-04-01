import sys
import sx126x
import threading
import time
import select
import termios
import tty
from threading import Timer
import time
from picamera2 import Picamera2
import binascii
picam = Picamera2()
config = picam.create_preview_configuration(main={"size":(480,480)})
picam.configure(config)
picam.options['quality']=1
picam.start()

r=0
def take_pic (continue_or_not = True):
	if continue_or_not:
		global timer_task
		global seconds
		global r
		picam.capture_file("/home/cubesat/venv/scripts/CubeSat/Images/r"+str(r)+".jpg")
		time.sleep(0.05)
		timer_task = Timer(seconds,take_pic)
		timer_task.start()
		filename="r"+str(r)+".jpg"
		with open("/home/cubesat/venv/scripts/CubeSat/Images/"+filename, 'rb') as f:
			content=f.read()
		f=open("/home/cubesat/venv/scripts/CubeSat/Images/r"+str(r)+'.txt','w')
		f.write(binascii.hexlify(content).decode())
		f.close()
		r=r+1
		
	
try:
    print("Press \033[1;32mEsc\033[0m to exit")
    seconds = 5
    while True:
        timer_task = Timer(seconds,take_pic)
        timer_task.start()
        if sys.stdin.read(1) == '\x1b':
            timer_task.cancel()
except:
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

import sys
import sx126x
import threading
import time
import select
import termios
import tty
from threading import Timer
import time
from picamera2 import Picamera2, Preview
import binascii
#Import used libraries

picam = Picamera2()
config = picam.create_preview_configuration(main={"size":(480,480)})
picam.configure(config)
picam.options['quality']=5
picam.start()
#initilize picam and configure image capture settings
def take_pic (continue_or_not = True):
	if continue_or_not:
		global timer_task
		global seconds
		
		time.sleep(.05)
		picam.capture_file("ChristinSux.jpg")
		time.sleep(0.05)
		timer_task = Timer(seconds,take_pic)
		timer_task.start()
		filename="ChristinSux.jpg"
		with open(filename, 'rb') as f:
			content=f.read()
		f=open('text.txt','w')
		f.write(binascii.hexlify(content).decode())
		f.close()
#define the take_pic function for later use	
try:
    time.sleep(.1)
    print("Press \033[1;32mEsc\033[0m to exit")
    seconds = 60
    while True:
        timer_task = Timer(seconds,take_pic)
        timer_task.start()
        if sys.stdin.read(1) == '\x1b':
            timer_task.cancel()
#set task to run every 60 seconds and checks for break input		
except:
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

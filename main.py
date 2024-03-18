import sys
import sx126x
import threading
import time
import select
import termios
import tty
from threading import Timer
import subprocess
#import used libraries 

subprocess.Popen(["python",'Take.py'])
#load and run the script to take a picture

old_settings = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin.fileno())
node = sx126x.sx126x(serial_num = "/dev/ttyS0",freq=868,addr=0,power=22,rssi=True,air_speed=2400,relay=False)
#define transmission settings

def send_timer(continue_or_not = True):
    with open('/home/cubesat/sciprts/text.txt') as file:
        f=file.read()  
    n = 230
    out = [(f[i:i+n]) for i in range(0, len(f), n)]
    iteration = len(out)
    for i in range(iteration-1):
        get_t = [0,868, out[i]]
        offset_frequence = int(get_t[1])-(850 if int(get_t[1])>850 else 410)  
        if continue_or_not:
            global timer_task
            global seconds
            data = bytes([int(get_t[0])>>8]) + bytes([int(get_t[0])&0xff]) + bytes([offset_frequence]) + bytes([node.addr>>8]) + bytes([node.addr&0xff]) + bytes([node.offset_freq]) + str(" ").encode()+get_t[2].encode()
            node.send(data)
            time.sleep(0.1)
            timer_task = Timer(seconds,send_timer)
            timer_task.start()
            print(out[i])
#define the function that opens the file to be transmitted and transmits it.

try:
    time.sleep(1)
    print("Press \033[1;32mEsc\033[0m to exit")
    seconds = 60
    while True:
        timer_task = Timer(seconds,send_timer)
        timer_task.start()
        if sys.stdin.read(1) == '\x1b':
            timer_task.cancel()
            break
            sys.stdout.flush()
        node.receive()
#set up timer task to transmit every 60 seconds and set up break        
except:
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

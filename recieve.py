import sys
import sx126x
import time
import termios
import tty
from threading import Timer
import os
old_settings = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin.fileno())
node = sx126x.sx126x(serial_num = "/dev/ttyS0",freq=868,addr=0,power=22,rssi=True,air_speed=2400,relay=False)
print("press esc to stop recieving")
import os 
from os import listdir

for file_name in listdir('/home/cubesat/sciprts/images/'):
    if file_name.endswith('.txt'):
        os.remove('/home/cubesat/sciprts/images/' + file_name)
time.sleep(1)
t=0
while True:
    f=open('/home/cubesat/sciprts/images/r'+str(t)+'.txt','x')
    while True:
        time.sleep(.5)
        n=node.receive()
        if n != None:
            n=n[:-1]
            n=n[2:]
            
            f.close()
            f=open('/home/cubesat/sciprts/images/r'+str(t)+'.txt','w')
            f.write(n)
            f.close()
            print(n)
    if sys.stdin.read(0) == '\x1b':
        t=int(t)+1
        print("hi")
        break
        sys.stdout.flush()

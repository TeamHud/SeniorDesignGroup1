import sys
import sx126x
import time
import termios
import tty
from threading import Timer
import os
import glob
from os import listdir
import shutil
old_settings = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin.fileno())
node = sx126x.sx126x(serial_num = "/dev/ttyS0",freq=868,addr=0,power=22,rssi=True,air_speed=2400,relay=False)
#import used libraries and initilize the sx126x 

folder = '/home/groundstation/Downloads/SeniorDesignGroup1-main/recieved data'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))
#path to the folder for storing recieved data and clear it on initilization 

time.sleep(1)
t=0
f=open('recieved data/r0.txt','x')
#create and open starting file

while True:
    time.sleep(.5)
    n=node.receive()
#check for data from satellite

        if n != None:    
        words = set(n.split())
        n=n[:-1]
        n=n[3:]
        print (words)
#If reciever recieves data trim the data to remove addressing informtion
            
        if 'end' in words:
            t=t+1
            newfile='recieved data/''r'+str(t)+'.txt'
            f=open(newfile,'x')
            print(t)
#if the data package contains the 'end' string then open a new file  
            
        else:
            newfile='recieved data/''r'+str(t)+'.txt'
            f=open(newfile,'a')
            f.write(n)
            f.close()
            print(n)
#if the data does not contain an end sting continue writing the data to the oritinal file


# while True:
    # time.sleep(.5)
    # n=node.receive()
    # if n != None:
        
        # newfile='recieved data/''r'+str(t)+'.txt'
        # f=open(newfile,'x')
        # n=n[:-1]
        # n=n[3:]
        # f.close()
        # f=open(newfile,'w')
        # f.write(n)
        # f.close()
        # t=t+1
       # # print(t)
        # print(n)

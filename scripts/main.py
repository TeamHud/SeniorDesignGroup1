import sys 
import sx126x
import threading
import time
import select
import termios
import tty
from threading import Timer
import subprocess
from Control import Motor
from Voltage import Voltage,Current
subprocess.Popen(['python', 'Take.py'])
old_settings = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin.fileno())
node = sx126x.sx126x(serial_num = "/dev/ttyS0",freq=868,addr=0,power=22,rssi=True,air_speed=2400,relay=False)
global iteration
iteration = 0
r=0
def send_timer(continue_or_not = True):
    start_time = time.perf_counter()
    global r
    try:
        with open('Images/r'+str(r)+".txt") as file:
            f=file.read()
    except Exception as e:
        print(e)
    n = 230
    h = []
    for sect in splitter(f, 220):
        h.append(sect)
    # Sending Data #
    for index in h:
        sendData(index)
    
    sendData("end")
    stop_time = time.perf_counter()
    time_diff = stop_time - start_time
    #v=str(Voltage())+" "+str(Current())
    #node.send(v)
    #print("Time to transmit: " + str(time_diff))
    r += 1
        
def splitter(data_in, n):
    for start in range(0, len(data_in), n):
        yield data_in[start:start+n]

def sendData(data_in):
    get_t = [0,868,data_in]   
    offset_frequence = int(get_t[1])-(850 if int(get_t[1])>850 else 410) 
    data = bytes([int(get_t[0])>>8]) + bytes([int(get_t[0])&0xff]) + bytes([offset_frequence]) + bytes([node.addr>>8]) + bytes([node.addr&0xff]) + bytes([node.offset_freq]) + str(" ").encode()+get_t[2].encode()
    node.send(data)
    print("Data Sent: " + data_in)
    time.sleep(1.5)
sendData("end")
while True:
    #Motor.correction()
    send_timer()

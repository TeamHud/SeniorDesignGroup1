# import board
# import time
# import adafruit_ina260
# from sx126x import sx126x
# import sx126x
# node = sx126x.sx126x(serial_num = "/dev/ttyS0",freq=868,addr=0,power=22,rssi=True,air_speed=2400,relay=False)
# def Voltage():
        # i2c = board.I2C()
        # ina260 = adafruit_ina260.INA260(i2c)
        # return(ina260.voltage)
# def SendVoltage(Voltage):
    # get_t = [0,868,Voltage]   
    # offset_frequence = int(get_t[1])-(850 if int(get_t[1])>850 else 410) 
    # data = bytes([int(get_t[0])>>8]) + bytes([int(get_t[0])&0xff]) + bytes([offset_frequence]) + bytes([node.addr>>8]) + bytes([node.addr&0xff]) + bytes([node.offset_freq]) + str(" ").encode()+str(get_t[2]).encode()
    # node.send(data)
    # print(data)
# while True:
    # time.sleep(3)    
    # SendVoltage(Voltage())
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_ina260

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
ina260 = adafruit_ina260.INA260(i2c)
while True:
    print(
        "Current: %.2f mA Voltage: %.2f V Power:%.2f mW"
        % (ina260.current, ina260.voltage, ina260.power)
    )
    time.sleep(1)

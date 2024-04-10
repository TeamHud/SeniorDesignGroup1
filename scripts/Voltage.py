import time
import board
import adafruit_ina260
import math
def Voltage():
    i2c = board.I2C()  # uses board.SCL and board.SDA
    ina260 = adafruit_ina260.INA260(i2c)
    voltage=ina260.voltage
    return(voltage)
def Current():
    i2c = board.I2C()  # uses board.SCL and board.SDA
    ina260 = adafruit_ina260.INA260(i2c)
    current=ina260.current
    return(current)

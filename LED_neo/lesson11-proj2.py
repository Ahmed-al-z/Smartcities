from lcd1602 import LCD1602
from dht11 import *
import machine
from machine import I2C,Pin,ADC
from utime import sleep

ic=I2C(1,scl=Pin(7), sda=Pin(6), freq=400000)
d=LCD1602(ic, 2, 16)
d.display()
dht= DHT(16)
fan = machine.Pin(18,machine.Pin.OUT)

while True:
    temp = dht.readTemperature()
    print(temp)

    sleep(1)
    d.clear()
    d.setCursor(0,0)
    d.print("temp:" +str(temp))
    sleep(1)

    if temp > 26:
        fan.value(1)
    else :
        fan.value(0)
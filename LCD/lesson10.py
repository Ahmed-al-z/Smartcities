from lcd1602 import LCD1602
from dht11 import *
from machine import I2C,Pin,ADC
from utime import sleep

i2cc = I2C (1,scl=Pin(7), sda=Pin(6), freq=400000)
affiche=LCD1602(i2cc,2,16)
affiche.display()
dht= DHT (18)

while True:
    temp,humid = dht.readTempHumid()
    sleep(1)
    affiche.clear()
    affiche.setCursor(0,0)
    affiche.print("temp: " + str(temp))

    affiche.setCursor(0,1)
    affiche.print("humid: " + str(humid))
    sleep(1)
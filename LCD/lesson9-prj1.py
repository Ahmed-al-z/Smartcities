from machine import I2C,Pin
from lcd1602 import LCD1602

from utime import sleep

ic = I2C(1,scl=Pin(7), sda=Pin(6), freq=400000)
                                                    #g
d= LCD1602(ic,2,16)

d.display()
sleep(1)

d.clear()
d.print('NON')
sleep(1)

d.setCursor(0,1)
d.print('world')
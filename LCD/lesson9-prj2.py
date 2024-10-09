from lcd1602 import LCD1602
from machine import I2C,Pin,ADC
from utime import sleep

pot=ADC(0)

I2CC = I2C (1,scl=Pin(7), sda=Pin(6), freq=400000)

d=LCD1602(I2CC,2,16)
d.display()

while True:
    sleep(1)
    d.clear()
    d.setCursor(0,0)
    d.print(str(pot.read_u16()))# le print n'affiche pas de int que des str
    sleep(1)
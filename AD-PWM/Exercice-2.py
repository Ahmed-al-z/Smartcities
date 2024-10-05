from machine import Pin, PWM, ADC
from time import sleep
buzzer = PWM(Pin(27))
pot = ADC(0)
vol = pot.read_u16()

def DO(time):
    buzzer.freq(1046)
    buzzer.duty_u16(vol)
    sleep(time)

def RE(time):
    buzzer.freq(1175)
    buzzer.duty_u16(vol)
    sleep(time)

def MI(time):
    buzzer.freq(1318)
    buzzer.duty_u16(vol)
    sleep(time)

def FA(time):
    buzzer.freq(1397)
    buzzer.duty_u16(vol)
    sleep(time)

def SO(time):
    buzzer.freq(1568)
    buzzer.duty_u16(vol)
    sleep(time)

def LA(time):
    buzzer.freq(1760)
    buzzer.duty_u16(vol)
    sleep(time)

def SI(time):
    buzzer.freq(1967)
    buzzer.duty_u16(vol)
    sleep(time)

def N(time):
    buzzer.duty_u16(0)
    sleep(time)

try: 



    while True:
        vol = pot.read_u16()
        


        DO(0.25)
        vol = pot.read_u16()
        RE(0.25)
        vol = pot.read_u16()
        FA(0.25)
        vol = pot.read_u16()
        MI(0.25)
        vol = pot.read_u16()
        RE(0.25)
        vol = pot.read_u16()
        DO(0.25)
        vol = pot.read_u16()
        N(0.25)
        vol = pot.read_u16()
        FA(0.25)
        vol = pot.read_u16()
        FA(0.25)
        vol = pot.read_u16()
        SO(0.25)
        vol = pot.read_u16()
        LA(0.25)
        vol = pot.read_u16()
        SO(0.25)
        vol = pot.read_u16()
        FA(0.25)
        vol = pot.read_u16()
        N(0.25)
        vol = pot.read_u16()
        DO(0.25)
        vol = pot.read_u16()
        RE(0.25)
        vol = pot.read_u16()
        FA(0.25)
        vol = pot.read_u16()
        MI(0.25)
        vol = pot.read_u16()
        RE(0.25)
        vol = pot.read_u16()
        DO(0.25)
        vol = pot.read_u16()
        N(0.25)
        vol = pot.read_u16()
        
        FA(0.25)
        vol = pot.read_u16()
        FA(0.25)
        vol = pot.read_u16()
        SO(0.25)
        vol = pot.read_u16()
        LA(0.25)
        vol = pot.read_u16()
        SO(0.25)
        vol = pot.read_u16()
        FA(0.25)
        vol = pot.read_u16()
        N(0.25)
        vol = pot.read_u16()
        DO(0.25)
        vol = pot.read_u16()
        RE(0.25)
        vol = pot.read_u16()
        FA(0.25)
        vol = pot.read_u16()
        MI(0.25)
        vol = pot.read_u16()
        RE(0.25)
        vol = pot.read_u16()
        DO(0.25)
        vol = pot.read_u16()
        N(0.5)  

except KeyboardInterrupt:
    print("Arrêt du programme.")

finally:
    buzzer.duty_u16(0)  
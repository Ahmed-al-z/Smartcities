#pour faire ce code on doit d'abord detecter l'appuie sur le
#ensuite changer l'etat

import machine
import utime
from time import sleep
bp = machine.Pin(18,machine.Pin.IN)
led = machine.Pin(16,machine.Pin.OUT)

# donc je vais ajouter une variable pour l'etat du bp et une autre
#pour stocker l'etat precident

bp_etat = bp.value()
cycle = 0
PP_PREC = 0


while True:
    bp_etat = bp.value()

    if bp_etat == 1 and PP_PREC == 0:
        cycle +=1
    utime.sleep(0.2)
    PP_PREC = 1
    
    if cycle == 1:
        led.value(1)
        utime.sleep (1)
        led.value(0)
        
    elif cycle == 2:
        led.value(1)
        utime.sleep (0.5)
        led.value(0)
        
    elif cycle == 3:
        led.value(1)
        utime.sleep (0.2)
        led.value(0)
        
    bp_prec = bp_etat
#pour faire ce code on doit d'abord detecter l'appuie sur le
#ensuite changer l'etat

import machine
import utime

# Configuration des pins pour le bouton poussoir et la LED
bp = machine.Pin(18, machine.Pin.IN)
led = machine.Pin(16, machine.Pin.OUT)

# Variables pour stocker l'état du bouton et le cycle
cycle = 0
PP_PREC = 0  # Variable pour stocker l'état précédent du bouton

while True:
    bp_etat = bp.value()

    # Détection de l'appui sur le bouton
    if bp_etat == 1 and PP_PREC == 0:
        cycle += 1
        if cycle > 3:
            cycle = 1  # Réinitialisation du cycle après le 3ème appui
        PP_PREC = 1  # Marquer que le bouton est actuellement enfoncé ### a comparer avec l'autre code 

    # Réinitialisation de PP_PREC lorsque le bouton est relâché
    if bp_etat == 0:
        PP_PREC = 0

    # Gestion des différents états de la LED en fonction du cycle
    if cycle == 1:
        led.value(1)
        utime.sleep(1)
        led.value(0)
    elif cycle == 2:
        led.value(1)
        utime.sleep(0.5)
        led.value(0)
    elif cycle == 3:
        led.value(1)
        utime.sleep(0.2)
        led.value(0)

    utime.sleep(0.2)  # Pause pour éviter les rebonds du bouton
    
    ## autrre code : # Pour faire ce code, on doit d'abord détecter l'appui sur le
# ensuite changer l'état

import machine
import utime
from time import sleep
bp = machine.Pin(18, machine.Pin.IN)
led = machine.Pin(16, machine.Pin.OUT)

# Donc je vais ajouter une variable pour l'état du bp et une autre
# pour stocker l'état précédent

bp_etat = bp.value()
cycle = 0
PP_PREC = 0

while True:
    bp_etat = bp.value()

    if bp_etat == 1 and PP_PREC == 0:
        cycle += 1
        if cycle > 3:
            cycle = 1  # Pas de réinitialisation du cycle en cas de dépassement
    PP_PREC = 1  # Devrait être mis à 1 uniquement lors d'un nouvel appui

    if bp_etat == 0:
        PP_PREC = 0  # Cela fonctionne, mais devrait être géré différemment pour éviter les faux positifs

    if cycle == 1:
        led.value(1)
        utime.sleep(1)
        led.value(0)
        
    elif cycle == 2:
        led.value(1)
        utime.sleep(0.5)
        led.value(0)
        
    elif cycle == 3:
        led.value(1)
        utime.sleep(0.2)
        led.value(0)

    # bp_prec = bp_etat  


# je vais faire une fonction qui convertie la temp du pot 
#une fonction qui gere l'affichage a la quelle je fais appel dans la boucle while
#while
    # lecture et convertion ADC
    #ty
    #DHT11 lecture
    #excet erreur = none
    #ensuite des if pour appliquer le controle, decider de quoi activer et affichier

from lcd1602 import LCD1602
from dht11 import *
import machine
from machine import I2C,Pin,ADC,PWM
from utime import sleep
#definir les IO
capdht = DHT(18)
pot = ADC(0)
buzzer = PWM(Pin(27))
led = machine.Pin(16,machine.Pin.OUT)

#config I2C
I2CC = I2C (1,scl=Pin(7), sda=Pin(6), freq=400000)
affiche=LCD1602(I2CC,2,16)

def temp_pot(adc_valeur):
    min_temp= 15
    max_temp=35
    #convertion [y= min_y + ( x − min_x /max_x − min_x) × (max_y−min_y)]
    return min_temp + (adc_valeur/65535) * (max_temp - min_temp)

def affiche_lcd (temp_ambiante,temp_set, alarme = False): #on met entre parenthese les parametres

    affiche.clear()
    affiche.setCursor(0,0)
    affiche.print("set: {:.1f} C".format(temp_set) )
    affiche.setCursor(0,1)
    affiche.print("ambiante: {:.1f} C".format(temp_ambiante) )
    
    if alarme:
        affiche.clear()
        affiche.setCursor(6,0)
        affiche.print("Alarme")
        sleep (0.5)

def buzzer_on (frequence):
    buzzer.freq(frequence)
    buzzer.duty_u16(20000)

def buzzer_off ():
    buzzer.duty_u16(0)

while True: #la dif entre while True et while c'est que la 1er boucle a l'infini sauf si on l'arrete nous, 
            #et l'autre boucle tant que la condition est vrai exemple : while x > 5 et elle stop la boucle sans notre intervention
    #lire l'adc du pot
    adc_valeur = pot.read_u16()
    temp_set = temp_pot(adc_valeur)

    #lire le dht11
    try:  #on utilise Try pour ajouter une partie de code qui pourra avoir des erreurs comme le dht par exemple et on ajoute la lecture apres le try
        capdht.readTempHumid()
        temp_ambiante = capdht.readTemperature()
    
    except OSError as e:    #ici on a l'exception d'erreur de notre try qui est stocké dans la variable "e" (on peut utiliser "e" pour debouger etc)
        temp_ambiante = None


    #comparaison et gestion de type d'alarme
   
    if temp_ambiante is not None :

        if temp_ambiante > temp_set :
            led.toggle()
            sleep (1)
            buzzer_off()
            affiche_lcd(temp_ambiante,temp_set)

        elif temp_ambiante > temp_set + 3 : 
            buzzer_on(1000)
            led.toggle()
            sleep(0.5)
            affiche_lcd(temp_set,temp_ambiante,alarme = True)

        else:
            buzzer_off()
            led.value(0)
            affiche_lcd(temp_ambiante,temp_set)
    else:
        affiche.clear()
        affiche.print("erreur dht11")
        print(str(capdht.readTempHumid))
sleep(1)
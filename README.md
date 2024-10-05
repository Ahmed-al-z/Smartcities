# Smartcities
# Contexte

Dans le cadre du cours SmartCities, je suis chargé de réaliser plusieurs projets visant à m'initier à la programmation embarquée en MicroPython.
Ces projets seront réalisés à l'aide d'un kit de base Grove, en utilisant un Raspberry Pi Pico W comme plateforme principale.

# Répertoires

- [GPIO](https://github.com/Ahmed-al-z/Smartcities/tree/main/GPIO)
LED simple, bouton-poussoir, interruption.
- [AD-PWM](https://github.com/Ahmed-al-z/Smartcities/tree/main/AD-PWM)
lecture du potentiomètre, PWM (LED, musique, servo).
- [LCD](https://github.com/Ahmed-al-z/Smartcities/tree/main/LCD)
documentation des fonctions de la librairie, affichage de la valeur du potentiomètre.
- [LED_neo](https://github.com/Ahmed-al-z/Smartcities/tree/main/LED_neo)
utilisation des LEDs néopixel, documentation des fonctions de la librairie, arc-en-ciel.
- [sensors](https://github.com/Ahmed-al-z/Smartcities/tree/main/sensors)
température et humidité, luminosité, PIR.
- [network](https://github.com/Ahmed-al-z/Smartcities/tree/main/network)
Accès réseau avec le RPi Pico.

# RaspberryPi Pico W

Le Raspberry Pi Pico W est une version améliorée du Raspberry Pi Pico, équipée d'une connectivité sans fil Wi-Fi et Bluetooth. Tout comme le Pico standard, il est basé sur le microcontrôleur RP2040, avec deux cœurs ARM Cortex-M0+, 264 Ko de RAM et plusieurs interfaces UART, SPI, I2C, etc... Le Pico W est idéal pour les projets IoT nécessitant une connexion réseau, tout en conservant la même simplicité de programmation avec MicroPython ou C/C++.


Pinout
![Capture d'écran 2024-10-05 195229](https://github.com/user-attachments/assets/2a0d8cce-9a46-4b00-b57e-4c0b9782aa5a)


# MicroPython

MicroPython est une implémentation réduite du langage Python, spécialement conçue pour les microcontrôleurs et les systèmes embarqués. Il permet d'exécuter du code Python sur des appareils disposant de ressources limitées, comme les ESP32, Pyboard etc... MicroPython offre une grande flexibilité pour programmer directement en Python, en prenant en charge la plupart des bibliothèques standards du langage tout en restant léger. Il est idéal pour les projets d'IoT, la robotique et les systèmes embarqués.

# IDE

![téléchargement](https://github.com/user-attachments/assets/03055c78-8723-43f6-add2-5812baa0aed8)

Thonny est un environnement de développement intégré (IDE) conçu spécialement pour apprendre Python. Il se distingue par son interface intuitive.

![téléchargement](https://github.com/user-attachments/assets/301c3aa0-1f83-4012-a891-c3d70a85288b)

Visual Studio Code est un IDE qui permet de programmer dans plusieurs langages de programmation. J'ai commencé ma migration vers VS Code dans le but de centraliser mon travail sur un seul IDE.

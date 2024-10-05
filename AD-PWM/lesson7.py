from machine import Pin,ADC,PWM
pot = ADC(0)
led_pwm = PWM(Pin(18))

led_pwm.freq(500)

while True:
    val = pot.read_u16()
    led_pwm.duty_u16(val)
    print(val)

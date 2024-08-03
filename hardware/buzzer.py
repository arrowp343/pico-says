from time import sleep_ms
from machine import Pin, PWM

buzzer = PWM(Pin(15)) 

def buzz(frequency: int, volume: int = 1000):
    buzzer.duty_u16(volume)
    buzzer.freq(frequency)

def quiet():
    buzzer.duty_u16(0)

def test():
    tones = [800, 1200, 1600, 2000]
    try:
        for tone in tones:
            buzz(tone)
            sleep_ms(500)
    except Exception as err:
        print("Error!")
        print(err)
        quiet()    
    quiet()

#test()
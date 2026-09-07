from time import sleep_ms
from machine import Pin, PWM

right_buzzer = PWM(Pin(0)) 
left_buzzer = PWM(Pin(1))

def buzz(frequency: int, volume: int = 1000):
    left_buzzer.duty_u16(volume)
    left_buzzer.freq(frequency)
    right_buzzer.duty_u16(volume)
    right_buzzer.freq(frequency)

def quiet():
    left_buzzer.duty_u16(0)
    right_buzzer.duty_u16(0)

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

test()
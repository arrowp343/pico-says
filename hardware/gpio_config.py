from machine import Pin, PWM
from color import Color

def init():
    all_off()
    
global_brightness = 0.1



PARTY_LED_0 = Pin(17, Pin.OUT)  # |
PARTY_LED_1 = Pin(14, Pin.OUT)  # /
PARTY_LED_2 = Pin(16, Pin.OUT)  # -
PARTY_LED_3 = Pin(15, Pin.OUT)  # \

RED_LED = Pin(10, Pin.OUT)
YELLOW_LED = Pin(11, Pin.OUT)
BLUE_LED = Pin(12, Pin.OUT)
GREEN_LED = Pin(13, Pin.OUT)

RED_BUTTON = Pin(21, Pin.IN, Pin.PULL_UP)
YELLOW_BUTTON = Pin(20, Pin.IN, Pin.PULL_UP)
BLUE_BUTTON = Pin(19, Pin.IN, Pin.PULL_UP)
GREEN_BUTTON = Pin(18, Pin.IN, Pin.PULL_UP)

YELLOW_TONE = 800
GREEN_TONE = 1200
RED_TONE = 1600
BLUE_TONE = 2000

s7seg_a = Pin(4, Pin.OUT)
s7seg_b = Pin(5, Pin.OUT)
s7seg_c = Pin(7, Pin.OUT)
s7seg_d = Pin(8, Pin.OUT)
s7seg_e = Pin(9, Pin.OUT)
s7seg_f = Pin(3, Pin.OUT)
s7seg_g = Pin(2, Pin.OUT)
s7seg_dot = Pin(6, Pin.OUT)

yellow = Color(YELLOW_LED, YELLOW_BUTTON, YELLOW_TONE, global_brightness, "yellow")
green = Color(GREEN_LED, GREEN_BUTTON, GREEN_TONE, global_brightness, "green")
red = Color(RED_LED, RED_BUTTON, RED_TONE, global_brightness, "red")
blue = Color(BLUE_LED, BLUE_BUTTON, BLUE_TONE, global_brightness, "blue")

def all_off():
    PARTY_LED_0.value(0)
    PARTY_LED_1.value(0)
    PARTY_LED_2.value(0)
    PARTY_LED_3.value(0)
    yellow.off()
    green.off()
    red.off()
    blue.off()
    s7seg_a.value(0)
    s7seg_b.value(0)
    s7seg_c.value(0)
    s7seg_d.value(0)
    s7seg_e.value(0)
    s7seg_f.value(0)
    s7seg_g.value(0)
    s7seg_dot.value(0)
    
def party_led_off():
    PARTY_LED_0.value(0)
    PARTY_LED_1.value(0)
    PARTY_LED_2.value(0)
    PARTY_LED_3.value(0)

def switch_party_led(n: int):
    party_led_off()
    if n % 4 == 0:
        PARTY_LED_0.value(1)
    elif n % 4 == 1:
        PARTY_LED_1.value(1)
    elif n % 4 == 2:
        PARTY_LED_2.value(1)
    elif n % 4 == 3:
        PARTY_LED_3.value(1)

def rotate_party_led(diagonal: bool):
    party_led_off()
    if diagonal:
        PARTY_LED_0.value(1)
        PARTY_LED_2.value(1)
    else:
        PARTY_LED_1.value(1)
        PARTY_LED_3.value(1)

all_off()
yellow.on()
green.on()
red.on()
blue.on()

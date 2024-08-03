from machine import Pin, PWM
from color import Color

def init():
    all_off()
    
global_brightness = 0.1


PARTY_LED_0 = Pin(0, Pin.OUT)
PARTY_LED_1 = Pin(1, Pin.OUT)

YELLOW_LED = Pin(10, Pin.OUT)
GREEN_LED = Pin(11, Pin.OUT)
RED_LED = Pin(12, Pin.OUT)
BLUE_LED = Pin(13, Pin.OUT)

YELLOW_BUTTON = Pin(21, Pin.IN, Pin.PULL_UP)
GREEN_BUTTON = Pin(20, Pin.IN, Pin.PULL_UP)
RED_BUTTON = Pin(19, Pin.IN, Pin.PULL_UP)
BLUE_BUTTON = Pin(18, Pin.IN, Pin.PULL_UP)

YELLOW_TONE = 800
GREEN_TONE = 1200
RED_TONE = 1600
BLUE_TONE = 2000

s7seg_a = Pin(4, Pin.OUT)
s7seg_b = Pin(5, Pin.OUT)
s7seg_c = Pin(8, Pin.OUT)
s7seg_d = Pin(7, Pin.OUT)
s7seg_e = Pin(6, Pin.OUT)
s7seg_f = Pin(3, Pin.OUT)
s7seg_g = Pin(2, Pin.OUT)
s7seg_dot = Pin(9, Pin.OUT)

yellow = Color(YELLOW_LED, YELLOW_BUTTON, YELLOW_TONE, global_brightness, "yellow")
green = Color(GREEN_LED, GREEN_BUTTON, GREEN_TONE, global_brightness, "green")
red = Color(RED_LED, RED_BUTTON, RED_TONE, global_brightness, "red")
blue = Color(BLUE_LED, BLUE_BUTTON, BLUE_TONE, global_brightness, "blue")

def all_off():
    PARTY_LED_0.value(0)
    PARTY_LED_1.value(0)
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
all_off()
yellow.on()
green.on()
red.on()
blue.on()
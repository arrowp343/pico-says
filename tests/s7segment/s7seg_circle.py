import hardware.gpio_config as gpio
from time import sleep_ms

def s7seg_circle(speed: int):
    gpio.s7seg_a.value(1)
    sleep_ms(1000 // speed)
    gpio.s7seg_a.value(0)
    gpio.s7seg_b.value(1)
    sleep_ms(1000 // speed)
    gpio.s7seg_b.value(0)
    gpio.s7seg_c.value(1)
    sleep_ms(1000 // speed)
    gpio.s7seg_c.value(0)
    gpio.s7seg_d.value(1)
    sleep_ms(1000 // speed)
    gpio.s7seg_d.value(0)
    gpio.s7seg_e.value(1)
    sleep_ms(1000 // speed)
    gpio.s7seg_e.value(0)
    gpio.s7seg_f.value(1)
    sleep_ms(1000 // speed)
    gpio.s7seg_f.value(0)

while True:
    s7seg_circle(20)
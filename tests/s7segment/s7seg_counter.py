import hardware.s7seg_config as s7seg
from time import sleep_ms

speed = 100

def s7seg_counter(speed: int = 1):
    for counter in range(10):
        s7seg.number_to_s7seg(str(counter) + ".")
        sleep_ms(500 // speed)
        s7seg.number_to_s7seg(str(counter))
        sleep_ms(500 // speed)

while True:
    s7seg_counter(4)

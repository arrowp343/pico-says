import hardware.gpio_config as gpio

segments = [
    gpio.s7seg_a,
    gpio.s7seg_b,
    gpio.s7seg_c,
    gpio.s7seg_d,
    gpio.s7seg_e,
    gpio.s7seg_f,
    gpio.s7seg_g,
    gpio.s7seg_dot
]

number_mapping = [
#    a  b  c  d  e  f  g dot
    [1, 1, 1, 1, 1, 1, 0, 0], # number -> 0
    [0, 1, 1, 0, 0, 0, 0, 0], # number -> 1
    [1, 1, 0, 1, 1, 0, 1, 0], # number -> 2
    [1, 1, 1, 1, 0, 0, 1, 0], # number -> 3
    [0, 1, 1, 0, 0, 1, 1, 0], # number -> 4
    [1, 0, 1, 1, 0, 1, 1, 0], # number -> 5
    [1, 0, 1, 1, 1, 1, 1, 0], # number -> 6
    [1, 1, 1, 0, 0, 0, 0, 0], # number -> 7
    [1, 1, 1, 1, 1, 1, 1, 0], # number -> 8
    [1, 1, 1, 1, 0, 1, 1, 0]  # number -> 9
]

def number_to_s7seg(toDisplay: str):
    numDisplay = int(toDisplay.replace(".", ""))
    for i, segment in enumerate(segments):
        segment.value(number_mapping[numDisplay][i])
    if toDisplay.count(".") == 1:
        gpio.s7seg_dot.value(1)
    else:
        gpio.s7seg_dot.value(0)

def char_to_s7seg(toDisplay: str):
    if toDisplay == "-":
        clear_s7seg()
        gpio.s7seg_g.value(1)
    elif toDisplay == ".":
        clear_s7seg()
        gpio.s7seg_dot.value(1)

def clear_s7seg():
    for segment in segments:
        segment.value(0)

clear_s7seg()


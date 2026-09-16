import hardware.gpio_config as gpio
from hardware.s7seg_config import char_to_s7seg, number_to_s7seg as print_7seg
from hardware.gpio_config import yellow, green, red, blue, init
from time import sleep_ms
import random
from color import Color
from hardware.buzzer.buzzer import buzz, quiet
from gamemodes.normal import NormalMode




def winning_sequence():
    # TBD
    print("test winning")
    return

def losing_sequence(expected_color: Color):
    print("Wrong! You lost!")
    char_to_s7seg("-")
    buzz(1047)
    sleep_ms(250)
    buzz(262)
    sleep_ms(500)
    quiet()
    for i in range(3):
        sleep_ms(250)
        expected_color.on(250)
    sleep_ms(250)
    expected_color.on()
    while not green.pressed():
        tmp = 0
    # TBD
    return

init()

winning_sequence()

while True:
    game = NormalMode()
    result = game.start()
    if result == None:
        winning_sequence()
    else:
        losing_sequence(result)

    

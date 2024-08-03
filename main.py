import hardware.gpio_config as gpio
from hardware.s7seg_config import char_to_s7seg, number_to_s7seg as print_7seg
from hardware.gpio_config import yellow, green, red, blue, init
from time import sleep_ms
import random
from color import Color
from hardware.buzzer import buzz, quiet

def display(round: int):
    gpio.PARTY_LED_0.value(1)
    gpio.PARTY_LED_1.value(1)
    print_7seg(str(round))
    for color in sequence[:round]:
        color.on(500)
        sleep_ms(500)
    gpio.PARTY_LED_0.value(0)
    gpio.PARTY_LED_1.value(0)

def expect_color(expected_color: Color):
    print("expect color: " + str(expected_color))
    while True:
        if yellow.pressed() or green.pressed() or red.pressed() or blue.pressed():
            if expected_color.pressed():
                print("correct!")
                expected_color.on(500)
                break
            else:
                raise Exception("Wrong! You Lost")

def winning_sequence():
    # TBD
    return

def losing_sequence(expected_color: Color):
    print(str(err))
    char_to_s7seg("-")
    buzz(1047)
    sleep_ms(250)
    buzz(262)
    sleep_ms(500)
    quiet()
    for i in range(3):
        sleep_ms(250)
        expected_color.on(250)
    expected_color.on()
    while not green.pressed():
        tmp = 0
    # TBD
    return

while True:
    init()
    speed = 1

    sequence = [random.choice([yellow, green, red, blue]) for _ in range(10)]

    for round in range(1,10,1):
        print("round " + str(round))
        display(round)
        try:
            print("number of colors: " + str(len(sequence[:round])))
            for current_color in sequence[:round]:
                expect_color(current_color) 
        except Exception as err:
            losing_sequence(current_color)
            break
        sleep_ms(1000)
    sleep_ms(2000)

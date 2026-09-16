import hardware.gpio_config as gpio
from hardware.s7seg_config import char_to_s7seg, number_to_s7seg as print_7seg
from hardware.gpio_config import yellow, green, red, blue, init
from time import sleep_ms
import random
from color import Color
from hardware.buzzer.buzzer import buzz, quiet

class NormalMode:
    def __init__(self):
        return
    
    def display(self, round: int, sequence):
        print_7seg(str(round))
        for idx, color in enumerate(sequence[:round]):
            gpio.rotate_party_led(idx % 2 == 0)
            color.on(500)
            sleep_ms(500)
        gpio.PARTY_LED_0.value(0)
        gpio.PARTY_LED_1.value(0)
        gpio.PARTY_LED_2.value(0)
        gpio.PARTY_LED_3.value(0)
    
    def expect_color(self, expected_color: Color):
        print("expect color: " + str(expected_color))
        while True:
            if yellow.pressed() or green.pressed() or red.pressed() or blue.pressed():
                if expected_color.pressed():
                    print("correct!")
                    expected_color.on(500)
                    return None
                else:
                    return self.expect_color

    
    def start(self) -> Color:
        while(True):
            speed = 1
            sequence = [random.choice([yellow, green, red, blue]) for _ in range(10)]
        
            for round in range(1,10,1):
                print("round " + str(round))
                self.display(round, sequence)
                print("number of colors: " + str(len(sequence[:round])))
                for current_color in sequence[:round]:
                    if self.expect_color(current_color) != None:
                        return current_color
                        
                sleep_ms(1000)
            sleep_ms(2000)
import tests.party_leds as party
import tests.s7segment.s7seg_counter as numbers
import hardware.buzzer.buzzer as buzzer

while True:
    party.test_party()
    numbers.s7seg_counter(4)
    buzzer.test()
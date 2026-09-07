import hardware.gpio_config as config
from time import sleep_ms

speed = 1

config.PARTY_LED_0.value(0)
config.PARTY_LED_1.value(0)
config.PARTY_LED_2.value(0)
config.PARTY_LED_3.value(0)

def test_party():
    config.PARTY_LED_0.value(1)
    sleep_ms(500 // speed)
    config.PARTY_LED_0.value(0)
    config.PARTY_LED_1.value(1)
    sleep_ms(500 // speed)
    config.PARTY_LED_1.value(0)
    config.PARTY_LED_2.value(1)
    sleep_ms(500 // speed)
    config.PARTY_LED_2.value(0)
    config.PARTY_LED_3.value(1)
    sleep_ms(500 // speed)
    config.PARTY_LED_3.value(0)
    config.PARTY_LED_0.value(1)
    
config.PARTY_LED_0.value(1)
config.PARTY_LED_1.value(1)
config.PARTY_LED_2.value(1)
config.PARTY_LED_3.value(1)    
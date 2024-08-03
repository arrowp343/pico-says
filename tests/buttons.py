import hardware.gpio_config as gpio
#from buzzer import buzz, quiet
from hardware.gpio_config import yellow, green, red, blue, init

colors = [yellow, green, red, blue]

#Test Buttons
while True:
    for color in colors:
        if color.pressed():
            print(color.name + " pressed")
        while color.pressed():
            #buzz(color.tone)
            color.on(500)
        #quiet()
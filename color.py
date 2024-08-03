from machine import Pin, PWM
from time import sleep_ms
from hardware.buzzer import buzz, quiet

class Color:
    def __init__(self, led_pin: Pin, button: Pin, tone: int, brightness: float, name: str = "unnamed color",):
        self.name = name
        self.led = PWM(led_pin)
        self.led.freq(1000)
        self.button: Pin = button
        self.brightness = brightness
        self.tone: int = tone

    def __str__(self) -> str:
        return self.name

    def on(self, duration = 0):
        self.led.duty_u16(int(65025 * self.brightness))
        if duration > 0:
            buzz(self.tone)
            sleep_ms(duration)
            self.off()
            quiet()

    def off(self):
        self.led.duty_u16(int(0))

    def pressed(self):
        return not self.button.value()
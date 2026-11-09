from gpiozero import LED
from signal import pause

led = LED(24)

try:
    led.blink(on_time=0.5, off_time=0.5)
    pause()
finally:
    led.off()
    led.close()

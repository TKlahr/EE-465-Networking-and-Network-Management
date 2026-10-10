import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

last_state = GPIO.input(17)

try:
    while True:
        current_state = GPIO.input(17)

        if current_state != last_state:
            time.sleep(0.05)  # Debounce the button
            current_state = GPIO.input(17)

            if current_state != last_state:
                if current_state == GPIO.HIGH:
                    print("Button Pressed")
                else:
                    print("Button Released")

                last_state = current_state

        time.sleep(0.01)

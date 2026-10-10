import RPi.GPIO as GPIO
import subprocess
import time

# Configure GPIO17 as an input
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

last_state = GPIO.input(17)

print("Press the button to ping google.com")

try:
    while True:
        current_state = GPIO.input(17)

        # Detect a change in button state
        if current_state != last_state:
            time.sleep(0.05)  # Debounce
            current_state = GPIO.input(17)

            if current_state != last_state:
                if current_state == GPIO.HIGH:
                    print("\nButton Pressed - Pinging Google...")

                    subprocess.run(["ping", "-c", "1", "google.com"])

                last_state = current_state

        time.sleep(0.01)

except KeyboardInterrupt:
    print("\nProgram stopped.")

finally:
    GPIO.cleanup()

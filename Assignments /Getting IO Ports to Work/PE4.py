import RPi.GPIO as GPIO
import subprocess
import time

LED = 17
WIFI_OFF = 27
WIFI_ON = 22

DEBOUNCE = 0.1  # 100 milliseconds

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(WIFI_OFF, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(WIFI_ON, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def wifi_control(action):
    subprocess.run(
        ["nmcli", "radio", "wifi", action],
        check=True
    )


def has_ip():
    result = subprocess.run(
        ["ip", "-4", "-o", "addr", "show",
         "dev", "wlan0", "scope", "global"],
        capture_output=True,
        text=True
    )
    return result.returncode == 0 and bool(result.stdout.strip())


# Debounce state
buttons = {
    WIFI_OFF: {"last_raw": GPIO.HIGH, "stable": GPIO.HIGH,
               "changed": time.monotonic()},
    WIFI_ON: {"last_raw": GPIO.HIGH, "stable": GPIO.HIGH,
              "changed": time.monotonic()}
}

print("PE4 Running", flush=True)
print("Switch 1: Disable Wi-Fi", flush=True)
print("Switch 2: Enable Wi-Fi", flush=True)

led_state = False
last_blink = time.monotonic()

try:
    while True:
        now = time.monotonic()

        for pin, action in [(WIFI_OFF, "off"), (WIFI_ON, "on")]:
            state = buttons[pin]
            raw = GPIO.input(pin)

            if raw != state["last_raw"]:
                state["changed"] = now
                state["last_raw"] = raw

            if (raw != state["stable"] and
                    now - state["changed"] >= DEBOUNCE):

                state["stable"] = raw

                if raw == GPIO.LOW:
                    print(f"Button GPIO{pin} pressed", flush=True)
                    print(f"{'Disabling' if action == 'off' else 'Enabling'} Wi-Fi...",
                          flush=True)
                    wifi_control(action)

        if not has_ip():
            if now - last_blink >= 0.5:
                led_state = not led_state
                GPIO.output(LED, led_state)
                last_blink = now
        else:
            led_state = False
            GPIO.output(LED, GPIO.LOW)

        time.sleep(0.02)

except KeyboardInterrupt:
    print("Program stopped.", flush=True)

finally:
    GPIO.cleanup()

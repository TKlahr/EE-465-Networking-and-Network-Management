import RPi.GPIO as GPIO
import time

LED_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)

def get_ping_count():
    # Read incoming ICMP Echo Request count
    with open("/proc/net/snmp", "r") as file:
        lines = file.readlines()

    for i in range(len(lines) - 1):
        if lines[i].startswith("Icmp:"):
            headers = lines[i].split()
            values = lines[i + 1].split()

            if values[0] == "Icmp:":
                index = headers.index("InEchos")
                return int(values[index])

    return 0

last_count = get_ping_count()
last_ping_time = 0

print("Monitoring incoming pings...")
print("Press Ctrl+C to stop.")

try:
    while True:
        current_count = get_ping_count()

        if current_count > last_count:
            print("Ping detected! LED ON")
            GPIO.output(LED_PIN, GPIO.HIGH)
            last_ping_time = time.monotonic()

        last_count = current_count

        # Turn LED off 3 seconds after last ping
        if GPIO.input(LED_PIN) == GPIO.HIGH:
            if time.monotonic() - last_ping_time > 3:
                GPIO.output(LED_PIN, GPIO.LOW)
                print("Pinging stopped. LED OFF")

        time.sleep(0.2)

except KeyboardInterrupt:
    print("\nProgram stopped.")

finally:
    GPIO.cleanup()

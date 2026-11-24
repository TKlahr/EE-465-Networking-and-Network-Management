import os
import time
from urllib.parse import urlencode
from urllib.request import urlopen

api_key = os.environ["THINGSPEAK_WRITE_API_KEY"]


def get_temperature():
    with open("/sys/class/thermal/thermal_zone0/temp") as file:
        return float(file.read()) / 1000.0


def read_cpu_times():
    with open("/proc/stat") as file:
        values = list(map(int, file.readline().split()[1:9]))

    idle = values[3] + values[4]
    total = sum(values)

    return total, idle


def get_cpu_usage():
    total1, idle1 = read_cpu_times()
    time.sleep(1)
    total2, idle2 = read_cpu_times()

    total_delta = total2 - total1
    idle_delta = idle2 - idle1

    return 100 * (total_delta - idle_delta) / total_delta


print("Starting Raspberry Pi CPU monitoring...")

try:
    while True:
        try:
            temperature = get_temperature()
            cpu_usage = get_cpu_usage()

            print(f"CPU Temperature: {temperature:.2f} C")
            print(f"CPU Usage: {cpu_usage:.2f}%")

            params = urlencode({
                "api_key": api_key,
                "field1": temperature,
                "field2": cpu_usage
            }).encode()

            with urlopen(
                "https://api.thingspeak.com/update",
                data=params,
                timeout=15
            ) as response:
                result = response.read().decode().strip()

                if result == "0":
                    print("Update failed.")
                else:
                    print(f"Data sent. Entry ID: {result}")

        except Exception as error:
            print(f"Error: {error}")

        print("----------------------------")
        time.sleep(20)

except KeyboardInterrupt:
    print("\nMonitoring stopped.")

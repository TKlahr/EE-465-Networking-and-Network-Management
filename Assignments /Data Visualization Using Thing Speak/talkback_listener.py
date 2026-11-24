import os
import time
import json
import subprocess
from urllib.parse import urlencode
from urllib.request import urlopen

GPIO = 24

talkback_id = os.environ["THINGSPEAK_TALKBACK_ID"]
talkback_key = os.environ["THINGSPEAK_TALKBACK_KEY"]

url = (
    f"https://api.thingspeak.com/talkbacks/"
    f"{talkback_id}/commands/execute.json"
)


def set_led(state):
    subprocess.run(
        ["pinctrl", "set", str(GPIO), "op", state],
        check=True
    )


# Initialize LED to OFF
set_led("dl")

print("Listening for ThingSpeak TalkBack commands...")
print("Controlling LED on GPIO 24")

try:
    while True:
        try:
            params = urlencode({
                "api_key": talkback_key
            }).encode()

            with urlopen(url, data=params, timeout=15) as response:
                result = response.read().decode().strip()

            data = json.loads(result) if result else {}

            command = data.get("command_string", "") if isinstance(data, dict) else ""

            if command == "ON":
                set_led("dh")
                print("Command received: LED ON")

            elif command == "OFF":
                set_led("dl")
                print("Command received: LED OFF")

            else:
                print("No command in queue")

        except Exception as error:
            print(f"Error: {error}")

        time.sleep(5)

except KeyboardInterrupt:
    print("\nTalkBack listener stopped.")

finally:
    set_led("dl")

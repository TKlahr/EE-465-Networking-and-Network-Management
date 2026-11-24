import os
import time
import json
from urllib.parse import urlencode
from urllib.request import urlopen

talkback_id = os.environ["THINGSPEAK_TALKBACK_ID"]
talkback_key = os.environ["THINGSPEAK_TALKBACK_KEY"]

url = (
    f"https://api.thingspeak.com/talkbacks/"
    f"{talkback_id}/commands/execute.json"
)

print("Listening for ThingSpeak TalkBack commands...")

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
                print("LED ON")
            elif command == "OFF":
                print("LED OFF")
            else:
                print("No command in queue")

        except Exception as error:
            print(f"Error: {error}")

        time.sleep(5)

except KeyboardInterrupt:
    print("\nTalkBack listener stopped.")

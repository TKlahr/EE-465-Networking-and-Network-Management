import os
import time
import random
from urllib.parse import urlencode
from urllib.request import urlopen

api_key = os.environ["THINGSPEAK_WRITE_API_KEY"]

while True:
    myRandom1 = random.randint(0, 100)
    myRandom2 = random.random()

    print(f"Field 1: {myRandom1}")
    print(f"Field 2: {myRandom2:.4f}")

    params = urlencode({
        "api_key": api_key,
        "field1": myRandom1,
        "field2": myRandom2
    }).encode()

    try:
        with urlopen(
            "https://api.thingspeak.com/update",
            data=params,
            timeout=15
        ) as response:
            result = response.read().decode()

            if result == "0":
                print("Update failed.")
            else:
                print(f"Data sent. Entry ID: {result}")

    except Exception as error:
        print(f"Error: {error}")

    time.sleep(20)

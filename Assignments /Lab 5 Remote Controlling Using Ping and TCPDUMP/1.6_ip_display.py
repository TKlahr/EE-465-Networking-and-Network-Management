import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw
from gpiozero import Button
import subprocess
import time

# Initialize OLED
i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(
    128, 64, i2c, addr=0x3C
)

# Initialize button on GPIO 17
button = Button(17, pull_up=True, bounce_time=0.05)

# Get Raspberry Pi IP address using Linux command
def get_ip():
    try:
        result = subprocess.run(
            ["ip", "-4", "-o", "addr", "show", "wlan0"],
            capture_output=True,
            text=True,
            check=True
        )

        if not result.stdout.strip():
            return "Not Connected"

        return result.stdout.split()[3].split("/")[0]

    except (subprocess.CalledProcessError, OSError, IndexError):
        return "Not Connected"

# Get Raspberry Pi MAC address
def get_mac():
    try:
        with open("/sys/class/net/wlan0/address") as f:
            return f.read().strip().upper()
    except OSError:
        return "Not Connected"

# Continuously update display
try:
    while True:

        image = Image.new("1", (128, 64), 0)
        draw = ImageDraw.Draw(image)

        draw.text((5, 5), "EE 465 Networking", fill=255)

        if button.is_pressed:
            draw.text((5, 25), "MAC Address:", fill=255)
            draw.text((5, 45), get_mac(), fill=255)
        else:
            draw.text((5, 25), "IP Address:", fill=255)
            draw.text((5, 45), get_ip(), fill=255)

        oled.image(image)
        oled.show()

        time.sleep(0.2)

except KeyboardInterrupt:
    print("Program stopped")

finally:
    button.close()

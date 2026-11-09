import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw
from gpiozero import Button
import socket
import time
import uuid

# Initialize OLED
i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(
    128, 64, i2c, addr=0x3C
)

# Initialize button on GPIO 17
button = Button(17, pull_up=True, bounce_time=0.05)

# Get Raspberry Pi IP address
def get_ip():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("192.0.2.1", 80))
            return s.getsockname()[0]
    except OSError:
        return "Not Connected"

# Get Raspberry Pi MAC address
def get_mac():
    mac = uuid.getnode()
    return ":".join(
        f"{(mac >> i) & 0xff:02X}"
        for i in range(40, -1, -8)
    )

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

import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw
import socket
import time

# Initialize OLED display
i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(
    128, 64, i2c, addr=0x3C
)

# Get Raspberry Pi IP address
def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("192.0.2.1", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except OSError:
        return "Not Connected"

# Continuously update OLED
while True:
    ip = get_ip()

    image = Image.new("1", (128, 64), 0)
    draw = ImageDraw.Draw(image)

    draw.text((5, 5), "EE 465 Networking", fill=255)
    draw.text((5, 25), "IP Address:", fill=255)
    draw.text((5, 45), ip, fill=255)

    oled.image(image)
    oled.show()

    time.sleep(2)

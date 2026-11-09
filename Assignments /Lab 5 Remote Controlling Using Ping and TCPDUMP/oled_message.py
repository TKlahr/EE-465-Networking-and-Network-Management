import sys
import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

# Initialize OLED
i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Get message from Bash script
message = sys.argv[1] if len(sys.argv) > 1 else "Waiting..."

# Create blank image
image = Image.new("1", (128, 64))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

# Display message
draw.text((10, 2), "EE 465 Project 3.1", font=font, fill=255)
draw.text((10, 35), message, font=font, fill=255)

# Update OLED
oled.image(image)
oled.show()

print("OLED:", message)

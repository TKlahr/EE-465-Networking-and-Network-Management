import os
import smtplib
import ssl
import time
from email.message import EmailMessage

ALERT_THRESHOLD = 40.0
RESET_THRESHOLD = 38.0
CHECK_INTERVAL = 5

GMAIL_USER = os.environ["GMAIL_USER"]
GMAIL_PASS = os.environ["GMAIL_APP_PASSWORD"].replace(" ", "")
ALERT_TO = os.environ.get("ALERT_TO", GMAIL_USER)


def get_cpu_temperature():
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as file:
        return float(file.read()) / 1000.0


def send_alert(temperature):
    msg = EmailMessage()
    msg["From"] = GMAIL_USER
    msg["To"] = ALERT_TO
    msg["Subject"] = "Raspberry Pi Temperature Alert"

    msg.set_content(
        f"Warning! Raspberry Pi CPU temperature is "
        f"{temperature:.1f} C, exceeding 40 C."
    )

    with smtplib.SMTP("smtp.gmail.com", 587, timeout=20) as server:
        server.starttls(context=ssl.create_default_context())
        server.login(GMAIL_USER, GMAIL_PASS)
        server.send_message(msg)

    print("Alert email sent successfully!")


alert_sent = False

print("Monitoring Raspberry Pi CPU temperature...")
print("Alert threshold: 40 C")

try:
    while True:
        try:
            temperature = get_cpu_temperature()
            print(f"CPU Temperature: {temperature:.1f} C")

            if temperature > ALERT_THRESHOLD and not alert_sent:
                send_alert(temperature)
                alert_sent = True

            elif temperature <= RESET_THRESHOLD and alert_sent:
                alert_sent = False
                print("Temperature cooled. Alert reset.")

        except Exception as error:
            print(f"Error: {error}")

        time.sleep(CHECK_INTERVAL)

except KeyboardInterrupt:
    print("\nMonitoring stopped."

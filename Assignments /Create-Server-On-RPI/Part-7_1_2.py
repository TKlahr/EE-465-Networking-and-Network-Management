from gpiozero import Button
from signal import pause
import subprocess

button = Button(17, pull_up=True)

def play_audio():
    print("Button pressed - playing audio!")
    subprocess.run(["aplay", "-D", "plughw:2,0", "/home/tklahr/recording.wav"])

button.when_pressed = play_audio

print("Waiting for button press...")
pause()

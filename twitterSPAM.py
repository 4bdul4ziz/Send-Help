import time
import random
from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller

print("Spamming sequence starts in 7 seconds.")

i = 1

time.sleep(7)

while i:

    mouse = Controller()  # Clicking the typing sequence

    mouse.position = (398, 161)

    mouse.press(Button.left)
    mouse.release(Button.left)

    text = ["#enoughvit"]  # Typing the shit

    keyboard = Controller()

    keyboard.type(text)

    keyboard.press(Key.enter)

    keyboard.release(Key.enter)

    time.sleep(3)

    mouse.position = (857, 221)  # Tweeting it

    mouse.press(Button.left)
    mouse.release(Button.left)

    time.sleep(5)

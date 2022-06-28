import time
from pynput.keyboard import Key, Controller

i = 1
time.sleep(7)
while i:

    text = "+:sussers:"

    keyboard = Controller()

    keyboard.type(text)

    keyboard.press(Key.enter)

    keyboard.release(Key.enter)

    time.sleep(1)

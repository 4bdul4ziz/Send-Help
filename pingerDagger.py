import time

from pynput.keyboard import Controller, Key

print("Countdown: 7s")
i = 1
time.sleep(7)
while i:

    text = "<@901841816960249896>"

    keyboard = Controller()

    keyboard.type(text)

    keyboard.press(Key.enter)

    keyboard.release(Key.enter)
            
    time.sleep(1)


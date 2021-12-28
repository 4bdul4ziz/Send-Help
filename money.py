import time
from pynput.keyboard import Key, Controller

print("Auto-type starts in 7 seconds...")
i = 1
time.sleep(7)
while i:

    text = "pls se max"

    keyboard = Controller()

    keyboard.type(text)

    keyboard.press(Key.enter)

    keyboard.release(Key.enter)
            
    time.sleep(11)

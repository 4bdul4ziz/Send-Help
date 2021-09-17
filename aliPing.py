import time
from pynput.keyboard import Key, Controller

print("Pinging in 7 seconds...")
i = 1
time.sleep(7)
while i:

    text = "<@600653864634679297>"

    keyboard = Controller()

    keyboard.type(text)

    keyboard.press(Key.enter)

    keyboard.release(Key.enter)
            
    time.sleep(1)

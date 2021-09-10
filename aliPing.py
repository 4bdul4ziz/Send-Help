import time
from pynput.keyboard import Key, Controller

print("Pinging Ali in 7 seconds...")
i = 1
time.sleep(7)
while i:

    text = "<@388753316848336896>"

    keyboard = Controller()

    keyboard.type(text)

    keyboard.press(Key.enter)

    keyboard.release(Key.enter)
            
    time.sleep(1)

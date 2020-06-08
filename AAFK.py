from pynput.keyboard import Key, Controller
import random
import time

print('Starting Anti-AFK Script...')
print('You can go now in your game...')
print('Grabbing keyboard controller now...')
keyboard = Controller()
print('Grabbed keyboard controller...')
print('Starting Anti-AFK-Protocol in 10 seconds...')

time.sleep(10)
while True:
    print("Pressing 'A'...")
    keyboard.press('a')
    time.sleep(1)
    print("Releasing 'A'...\n")
    keyboard.release('a')
    time.sleep(5)
    print("Pressing 'D'...")
    keyboard.press('d')
    time.sleep(1)
    print("Releasing 'D'...\n")
    keyboard.release('d')
    time.sleep(5)

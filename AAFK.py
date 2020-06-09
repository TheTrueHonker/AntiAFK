from pynput.keyboard import Key, Controller
import threading as th
import random
import time
import msvcrt
import sys
import os

def f_exit():
    while True:
        if msvcrt.kbhit() and msvcrt.getch() == chr(27).encode():
            os._exit(1)

if __name__ == '__main__':
    print('Starting Anti-AFK Script...')
    th.Thread(target=f_exit,args=(),name='exit_thread',daemon=True).start()
    print('Grabbing keyboard controller now...')
    keyboard = Controller()
    print("Press 'ESC' to exit...")
    print('You can go now in your game...')
    print('Starting Anti-AFK-Protocol in 10 seconds...')
    time.sleep(10)
    print('Starting Anti-AFK-Protocol now...')
    while True:
        keyboard.press('a')
        time.sleep(random.randint(1, 2))
        keyboard.release('a')
        time.sleep(random.randint(2,5))
        keyboard.press('d')
        time.sleep(random.randint(1, 2))
        keyboard.release('d')
        time.sleep(random.randint(2,5))

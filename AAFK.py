from pynput.keyboard import Key, Controller
import threading as th
import random
import time
import msvcrt
import os
import argparse


def f_exit():
    while True:
        if msvcrt.kbhit() and msvcrt.getch() == chr(27).encode():
            os._exit(1)


if __name__ == '__main__':
    # Setup Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-min", type=int, help="Minimum time to wait till the next key-press")
    parser.add_argument("-max", type=int, help="Maximum time to wait till the next key-press")
    args = parser.parse_args()
    if args.min and args.max:
        if args.max <= args.min:
            print("[!] MAX can not be lower or equal than MIN!")
            exit(0)

    # Initialize argument-variables
    t_min = 2
    t_max = 5

    # Get Arguments
    if args.min:
        t_min = args.min
    if args.max:
        t_max = args.max

    # Initialize variables and thread
    print('Starting Anti-AFK Script...')
    th.Thread(target=f_exit, args=(), name='exit_thread', daemon=True).start()
    print('Grabbing keyboard controller now...')
    keyboard = Controller()
    print("Press 'ESC' to exit...")
    print('You can go now in your game...')
    print('Starting Anti-AFK-Protocol in 10 seconds...')
    time.sleep(10)
    print('Starting Anti-AFK-Protocol now...')

    # Start Anti-AFK-Mechanism
    while True:
        keyboard.press('a')
        time.sleep(random.randint(1, 2))
        keyboard.release('a')
        time.sleep(random.randint(t_min, t_max))
        keyboard.press('d')
        time.sleep(random.randint(1, 2))
        keyboard.release('d')
        time.sleep(random.randint(t_min, t_max))

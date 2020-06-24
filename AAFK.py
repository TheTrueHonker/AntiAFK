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
    parser.add_argument("-keymin", type=int, help="Minimum time a key is pressed")
    parser.add_argument("-keymax", type=int, help="Maximum time a key is pressed")
    parser.add_argument("-key1", type=str, help="First key, that should be pressed")
    parser.add_argument("-key2", type=str, help="Second key, that should be pressed")
    parser.add_argument("-v", "--verbose", action='store_true', help="Shows additional information")
    args = parser.parse_args()
    if args.min and args.max:
        if args.max <= args.min:
            print("[!] MAX can not be lower or equal than MIN!")
            exit(0)

    # Initialize argument-variables
    t_min = 2
    t_max = 5
    k_min = 1
    k_max = 2
    key1 = 'a'
    key2 = 'd'
    verbose = False

    # Get Arguments
    if args.min:
        t_min = args.min
    if args.max:
        t_max = args.max
    if args.keymin:
        k_min = args.keymin
    if args.keymax:
        k_max = args.keymax
    if args.key1:
        key1 = args.key1
    if args.key2:
        key2 = args.key2
    if args.verbose:
        verbose = True

    # Initialize variables and thread
    print('Starting Anti-AFK Script...')
    th.Thread(target=f_exit, args=(), name='exit_thread', daemon=True).start()
    print('Grabbing keyboard controller now...')
    keyboard = Controller()
    print("Press 'ESC' to exit...")
    print('The program is now working, you can go in game and go afk...')
    print('Starting Anti-AFK-Protocol in 10 seconds...')
    time.sleep(10)
    print('Starting Anti-AFK-Protocol now...')

    # Start Anti-AFK-Mechanism
    while True:
        if verbose:
            print("Pressing %s..." % key1)
        keyboard.press(key1)
        time.sleep(random.randint(k_min, k_max))
        if verbose:
            print("Releasing %s..." % key1)
        keyboard.release(key1)
        time.sleep(random.randint(t_min, t_max))
        if verbose:
            print("Pressing %s..." % key2)
        keyboard.press(key2)
        time.sleep(random.randint(k_min, k_max))
        if verbose:
            print("Releasing %s..." % key2)
        keyboard.release(key2)
        time.sleep(random.randint(t_min, t_max))

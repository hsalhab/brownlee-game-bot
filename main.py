import time

import keyboard as kb
import random as rand

import Constants

# update seed every once in a while to avoid predictability
rand.seed(41)

# sleep for 5 secs at the start to allow time to switch to game window
time.sleep(5)

def wait(duration):
    """
    Makes execution "pause" for a certain amount of MAX_SLEEP_TIME

    INPUT:
        time: amount of time to wait for in seconds
    """

    current = time.time()
    later = current + duration
    while time.time() < later:
        pass
    return

def main():
    while True:
        sleep_time = rand.randint(Constants.SECONDS_IN_MINUTE * Constants.MIN_SLEEP_TIME,
                                  Constants.SECONDS_IN_MINUTE * Constants.MAX_SLEEP_TIME)

        for i in range(rand.randint(Constants.MIN_KEYS_PER_CYCLE, Constants.MAX_KEYS_PER_CYCLE)):
            key = rand.choice(Constants.MOVEMENT_KEYS)
            press_time = rand.randint(Constants.MIN_KEY_PRESS, Constants.MAX_KEY_PRESS)
            release_time = rand.randint(Constants.MIN_KEY_RELEASE, Constants.MAX_KEY_RELEASE)

            time.sleep(press_time)
            kb.press(key)
            print("key {} pressed".format(key))

            wait(release_time)
            kb.release(key)
            print("key {} released".format(key))

        time.sleep(sleep_time)

if __name__ == "__main__":
    main()

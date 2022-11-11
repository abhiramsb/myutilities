import pyautogui
import time
import string
import random

def no_lock():
    try:
        print ('Press CTRL+C to stop/')
        while True:
            pyautogui.press(random.choice(string.ascii_letters))
            time.sleep(random.randint(3,30))
    except Exception as ex:
        print('no_lock | Error: ',ex)

def main():
    try:
        print('\nPrevent Windows screenlock')
        print ('Running')
        no_lock()
    except KeyboardInterrupt:
        print('\nStopped')
    except Exception as ex:
        print ('main | error: ',ex)

if __name__ == "__main__":
    main()
            

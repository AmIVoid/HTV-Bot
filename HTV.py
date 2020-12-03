from pyautogui import *
import pyautogui
import time
from time import sleep
import win32api, win32con


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)                                            # Pause for click to register
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while True:

    time.sleep(60 * 30)                                         # Checks for ad every 30 minutes

    if pyautogui.pixel(3668, 1053)[0] == 243:                   # Checks if an ad is avaliable
        click(3668, 1053)                                       # Ad button
        time.sleep(2)
        click(3668, 1000)                                       # Ad content
        time.sleep(2)
        click(3665, 660)                                        # Close Play Store
        time.sleep(2)
        click(3500, 753)                                        # Close ad content
        time.sleep(2)
        click(3800, 930)                                        # Collect coins
        print("Found an ad")                                    # Prints to console to say if an ad was found
    else:
        print("No ad found")                                    # Prints to console to say no ad was found

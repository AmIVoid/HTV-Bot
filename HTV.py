from pyautogui import *
import pyautogui
import time
from time import sleep
import win32api, win32con

adCounter = 0

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)                                            # Pause for click to register
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while True:

    time.sleep(60 * 30)                                         # Checks for ad every 30 minutes

    if pyautogui.pixel(3668, 1085)[0] == 243:                   # Checks if an ad is avaliable
        time.sleep(1)
        click(3668, 1085)                                       # Ad button
        time.sleep(2)
        click(3668, 1000)                                       # Ad content
        time.sleep(2)
        click(3665, 660)                                        # Close Play Store
        time.sleep(2)
        click(3500, 753)                                        # Close ad content
        time.sleep(2)
        click(3800, 930)                                        # Collect coins
        adCounter+= 1                                           # Adds 1 to the ad counter
        print("An ad was found")                                # Prints to console to say if an ad was found
        print("Found " + str(adCounter) + " ads")               # Prints to console how many ads have been found
    else:
        print("No ad found")                                    # Prints to console to say no ad was found
        print("Found " + str(adCounter) + " ads")               # Prints to console how many ads have been found
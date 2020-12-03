# HTV Bot
A quick and dirty python bot to automate collecting coins in the HAnime.tv android app.

Runs a check every 30 minutes to see if an ad is avaliable.

# Purpose
I quickly made this because I'm too lazy to open an app every 3 hours to collect coins.

I may come back later when I'm sick of always having a bluestacks window open on my monitor and create a better bot for this.
# Disclaimer
I don't recommend anyone uses this bot because it's absolute garbage.

# Running this bot
## In my instance I'm running bluestacks pinned to the top of the display in the corner of my 3rd monitor with HTV always open.

Before running open a command prompt in the folder you extract this to and run `pip install -r requirements.txt`

The code is commented to show important parts if you want to edit with your own X, Y values.

To get X, Y values for your device open a command prompt and run `python` then `import pyautogui` and finally `pyautogui.displayMousePosition()`

This will display the X and Y values of your cursor after which you will have to not down the locations for all the relevant screen locations e.g: Ad button, Ad content, Close play store, etc.
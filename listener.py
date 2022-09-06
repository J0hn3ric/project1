import sys
from pynput import keyboard
import time

control = keyboard.Controller()

def combo():
    time.sleep(1.2)
    control.tap(keyboard.Key.cmd_l)
    print("windows button pressed")

def esc():
    print("exit")
    sys.exit(0)

with keyboard.GlobalHotKeys({
        '<ctrl>+<alt>+h': combo,
        'x': esc}) as hotkeys:
    hotkeys.join()

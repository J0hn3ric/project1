
import sys
from pynput import keyboard
import time

control = keyboard.Controller()

COMBINATION = {keyboard.Key.ctrl, keyboard.Key.alt, keyboard.KeyCode.from_char('l')}

current = set()


def on_press(key):
    key=listener.canonical(key)
    if key in COMBINATION:
        current.add(key)
        if all(k in current for k in COMBINATION):
            time.sleep(1.2)
            control.tap(keyboard.Key.cmd_l)
            current.remove(key)
            print("windows key pressed")
    if key == keyboard.KeyCode.from_char('x'):
        print("exit")
        listener.stop()
        sys.exit(0)


def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# import pyautogui as pag
# import random
# import time

from pynput import mouse


def on_move(x, y):
    print(f'mouse moved ({x},{y})')


def on_click(x, y, button, pressed):
    print('{0}'.format('clicked' if pressed else 'released'))
    if not pressed:
        return False


with mouse.Listener(
        on_move=on_move,
        on_click=on_click) as listener:
    listener.join()

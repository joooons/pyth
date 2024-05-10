import pyautogui as pag
import random
import time
from pynput import mouse

count = 0


def on_move(x, y):
    print(f'mouse moved ({x},{y})')


def on_click(x, y, button, pressed):
    global count
    if pressed:
        count += 1
        print(count)
    if not pressed:
        if count > 4:
            print('released')
            return False


def main():

    with mouse.Listener(
            # on_move=on_move,
            on_click=on_click) as listener:
        listener.join()


if __name__ == "__main__":
    main()

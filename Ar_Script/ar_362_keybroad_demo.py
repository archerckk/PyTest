from pynput.keyboard import Key, Controller
from pynput import keyboard


k = Controller()

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))


def on_release(key):
    print('{0} released'.format(
        key))
    if key==keyboard.Key.print_screen:
        with k.pressed(Key.cmd_l):
            k.press(Key.cmd_l)
            k.press(Key.print_screen)
    if key == keyboard.Key.pause:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
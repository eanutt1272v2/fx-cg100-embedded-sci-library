# Simulate Langton's ant on the Casio fx-CG100.

from casioplot import clear_screen, set_pixel, show_screen

try:
    from casioplot import getkey
except ImportError:
    getkey = None


def read_text(prompt, default=None):
    while True:
        raw = input(prompt).strip()
        if raw:
            return raw
        if default is not None:
            return default
        print("Please enter a value.")


def read_int(prompt, default=None, min_value=None, max_value=None):
    while True:
        raw = input(prompt).strip()
        if raw == "" and default is not None:
            value = int(default)
        else:
            try:
                value = int(raw)
            except ValueError:
                print("Invalid integer. Try again.")
                continue
        if min_value is not None and value < min_value:
            print("Value must be >= " + str(min_value))
            continue
        if max_value is not None and value > max_value:
            print("Value must be <= " + str(max_value))
            continue
        return value


def read_float(prompt, default=None, min_value=None, max_value=None):
    while True:
        raw = input(prompt).strip()
        if raw == "" and default is not None:
            value = float(default)
        else:
            try:
                value = float(raw)
            except ValueError:
                print("Invalid float. Try again.")
                continue
        if min_value is not None and value < min_value:
            print("Value must be >= " + str(min_value))
            continue
        if max_value is not None and value > max_value:
            print("Value must be <= " + str(max_value))
            continue
        return value


def wait_for_exit():
    if getkey is not None:
        getkey()
    else:
        input("\nPress any key to exit: ")


def main():
    W, H = 384, 192
    grid = {}
    ax, ay = W // 2, H // 2

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    direction = 0
    steps = read_int("Steps (e.g. 5000): ")

    clear_screen()
    for _ in range(steps):
        cell = grid.get((ax, ay), 0)
        if cell == 0:
            direction = (direction + 1) % 4
            grid[(ax, ay)] = 1
            set_pixel(ax, ay, (0, 0, 0))
        else:
            direction = (direction - 1) % 4
            grid[(ax, ay)] = 0
            set_pixel(ax, ay, (255, 255, 255))
        ax = (ax + dx[direction]) % W
        ay = (ay + dy[direction]) % H

    show_screen()
    wait_for_exit()


main()

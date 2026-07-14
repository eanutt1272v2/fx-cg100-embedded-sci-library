# Render the Koch snowflake fractal.

from turtle import forward, goto, hideturtle, left, pencolor, pendown, penup, right, speed

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


def koch(length, depth):
    if depth == 0:
        forward(length)
    else:
        koch(length / 3, depth - 1)
        left(60)
        koch(length / 3, depth - 1)
        right(120)
        koch(length / 3, depth - 1)
        left(60)
        koch(length / 3, depth - 1)


def wait_for_exit():
    if getkey is not None:
        getkey()
    else:
        input("\nPress any key to exit: ")


def main():
    speed(0)
    hideturtle()
    penup()
    goto(-90, 50)
    pendown()
    pencolor("blue")
    depth = read_int("Depth (1-4): ")
    side = 170

    for _ in range(3):
        koch(side, depth)
        right(120)
    wait_for_exit()


main()

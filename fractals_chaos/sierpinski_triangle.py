# Render the Sierpinski triangle fractal on the Casio fx-CG100.

import sys

from turtle import backward, forward, goto, hideturtle, left, pencolor, pendown, penup, right, speed

is_calculator = sys.platform == "casio" or "casio" in sys.platform.lower()

if is_calculator:
    try:
        from casioplot import getkey
    except ImportError:
        getkey = None
else:
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


def sierpinski(length, depth):
    if depth == 0:
        for _ in range(3):
            forward(length)
            left(120)
    else:
        sierpinski(length / 2, depth - 1)
        forward(length / 2)
        sierpinski(length / 2, depth - 1)
        backward(length / 2)
        left(60)
        forward(length / 2)
        right(60)
        sierpinski(length / 2, depth - 1)
        left(60)
        backward(length / 2)
        right(60)


def wait_for_exit():
    if getkey is not None:
        getkey()
    else:
        input("\nPress any key to exit: ")


def main():
    speed(0)
    hideturtle()
    penup()
    goto(-80, -70)
    pendown()
    pencolor("blue")
    depth = read_int("Depth (1-5): ")
    sierpinski(160, depth)
    wait_for_exit()


main()

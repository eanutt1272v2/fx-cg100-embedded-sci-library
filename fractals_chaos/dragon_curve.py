# Render the Dragon curve fractal.

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


def dragon(seq, iters):
    for _ in range(iters):
        new = seq + "R"
        for idx in range(len(seq) - 1, -1, -1):
            c = seq[idx]
            if c == "R":
                new += "L"
            elif c == "L":
                new += "R"
            else:
                new += c
        seq = new
    return seq


def wait_for_exit():
    if getkey is not None:
        getkey()
    else:
        input("\nPress any key to exit: ")


def main():
    iters = read_int("Iterations (8-12): ")
    seq = dragon("", iters)

    speed(0)
    hideturtle()
    pencolor("blue")
    penup()
    goto(-20, 10)
    pendown()
    step = max(1, 120 // (2 ** (iters // 2)))

    for c in seq:
        forward(step)
        if c == "R":
            right(90)
        elif c == "L":
            left(90)
    wait_for_exit()


main()

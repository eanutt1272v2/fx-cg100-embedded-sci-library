# Draw and explore basic geometric shapes.

from casioplot import clear_screen, draw_string, show_screen
from shapes_lib import SHAPES_2D, SHAPES_3D

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
            value = default
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
            value = default
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


SHAPES = SHAPES_2D + SHAPES_3D


def clip_text(text, width):
    if len(text) <= width:
        return text
    return text[: width - 1] + "~"


def draw_menu():
    clear_screen()
    draw_string(0, 0, "Shape Property Calculation (SELECT, 0: Exit Menu)", (0, 0, 0), "small")
    draw_string(0, 10, "--- 2D Shapes ---", (0, 0, 0), "small")
    draw_string(192, 10, "--- 3D Shapes ---", (0, 0, 0), "small")

    y0 = 22
    line_h = 12
    max_rows = 15

    for i in range(len(SHAPES_2D)):
        if i >= max_rows:
            break
        label = str(i + 1) + ": " + SHAPES_2D[i][0]
        draw_string(0, y0 + i * line_h, clip_text(label, 28), (0, 0, 0), "small")

    offset = len(SHAPES_2D)
    for i in range(len(SHAPES_3D)):
        if i >= max_rows:
            break
        label = str(offset + i + 1) + ": " + SHAPES_3D[i][0]
        draw_string(192, y0 + i * line_h, clip_text(label, 28), (0, 0, 0), "small")

    show_screen()


def wait_for_exit():
    if getkey is not None:
        getkey()
    else:
        input("\nPress any key to exit: ")


def main():
    while True:
        draw_menu()
        
        if getkey is not None:
            getkey()
        else:
            input("\nPress EXE to enter Selection console...")
            
        clear_screen()
        
        try:
            choice = read_int("SELECT (0: Exit Menu): ", default=0)
            if choice == 0:
                break
            if choice < 0 or choice > len(SHAPES):
                raise ValueError("SELECTION out of range")
                
            label, func, params = SHAPES[choice - 1]
            args = []
            for p in params:
                args.append(read_float(p + ": "))
                
            results = func(*args)
            print("\n-- " + label + " --")
            for r in results:
                print(r)
                
        except Exception as exc:
            print("Error: " + str(exc))
            
        input("\nPress EXE or OK for menu: ")
        
    wait_for_exit()


main()

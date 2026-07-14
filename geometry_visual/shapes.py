# Draw and explore basic geometric shapes.

from shapes_lib import SHAPES_2D, SHAPES_3D

SHAPES = SHAPES_2D + SHAPES_3D


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


def show_menu():
    print("\nShape Property Calculation")
    print("0. Exit")

    # --- 2D Shapes ---
    print("\n--- 2D Shapes ---")
    for i in range(0, len(SHAPES_2D), 2):
        item1 = str(i + 1) + ". " + SHAPES_2D[i][0]
        if i + 1 < len(SHAPES_2D):
            item2 = str(i + 2) + ". " + SHAPES_2D[i + 1][0]
            padding = " " * max(0, 25 - len(item1))
            print(item1 + padding + item2)
        else:
            print(item1)

    # --- 3D Shapes ---
    print("\n--- 3D Shapes ---")
    offset = len(SHAPES_2D)
    for i in range(0, len(SHAPES_3D), 2):
        item1 = str(offset + i + 1) + ". " + SHAPES_3D[i][0]
        if i + 1 < len(SHAPES_3D):
            item2 = str(offset + i + 2) + ". " + SHAPES_3D[i + 1][0]
            padding = " " * max(0, 25 - len(item1))
            print(item1 + padding + item2)
        else:
            print(item1)


def main():
    while True:
        show_menu()
        choice = input("Select an option: ").strip()
        if choice == "0":
            break
        if not choice.isdigit():
            print("Enter a number from 0 to " + str(len(SHAPES)))
            continue
        choice = int(choice)
        if choice < 1 or choice > len(SHAPES):
            print("Selection out of range")
            continue
        try:
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
        input("\nPress EXE to return to the menu: ")

    print("Exiting...")
    input("Press EXE to finish: ")


main()

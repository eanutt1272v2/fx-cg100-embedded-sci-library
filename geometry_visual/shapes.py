# Calculate basic properties of various 2D and 3D geometric shapes on the Casio fx-CG100.

from shapes_lib import SHAPES_2D, SHAPES_3D


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


def show_main_menu():
    print("\n=========================")
    print("Geometry Calculator")
    print("=========================")
    print("1. 2D Shapes")
    print("2. 3D Shapes")
    print("0. Exit")


def show_2d_menu():
    print("\n--- 2D Shapes Menu ---")
    print("0. Back to Main Menu")
    for i in range(0, len(SHAPES_2D), 2):
        item1 = str(i + 1) + ". " + SHAPES_2D[i][0]
        if i + 1 < len(SHAPES_2D):
            item2 = str(i + 2) + ". " + SHAPES_2D[i + 1][0]
            padding = " " * max(0, 20 - len(item1))
            print(item1 + padding + item2)
        else:
            print(item1)


def show_3d_menu():
    print("\n--- 3D Shapes Menu ---")
    print("0. Back to Main Menu")
    for i in range(0, len(SHAPES_3D), 2):
        item1 = str(i + 1) + ". " + SHAPES_3D[i][0]
        if i + 1 < len(SHAPES_3D):
            item2 = str(i + 2) + ". " + SHAPES_3D[i + 1][0]
            padding = " " * max(0, 20 - len(item1))
            print(item1 + padding + item2)
        else:
            print(item1)


def handle_shape_selection(shapes_list):
    while True:
        choice = input("Select an option: ").strip()
        if choice == "0":
            return False  # Go back to main menu
        if not choice.isdigit():
            print("Enter a number from 0 to " + str(len(shapes_list)))
            continue
        choice = int(choice)
        if choice < 1 or choice > len(shapes_list):
            print("Selection out of range")
            continue

        try:
            label, func, params = shapes_list[choice - 1]
            args = []
            for p in params:
                args.append(read_float(p + ": "))
            results = func(*args)
            print("\n-- " + label + " --")
            for r in results:
                print(r)
        except Exception as exc:
            print("Error: " + str(exc))

        input("\nPress EXE to return to sub-menu: ")
        return True


def main():
    while True:
        show_main_menu()
        main_choice = input("Select category: ").strip()

        if main_choice == "0":
            break
        elif main_choice == "1":
            while True:
                show_2d_menu()
                if not handle_shape_selection(SHAPES_2D):
                    break
        elif main_choice == "2":
            while True:
                show_3d_menu()
                if not handle_shape_selection(SHAPES_3D):
                    break
        else:
            print("Invalid selection. Choose 0, 1, or 2.")

    print("Exiting...")
    input("Press EXE to finish: ")


main()

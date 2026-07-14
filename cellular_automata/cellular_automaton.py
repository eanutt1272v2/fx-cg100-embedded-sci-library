# Simulate cellular automata on the Casio fx-CG100.

from casioplot import clear_screen, set_pixel, show_screen

try:
    from casioplot import getkey
except ImportError:
    getkey = None

def wait_for_exit(getkey):
    if getkey is not None:
        getkey()
    else:
        input("\nPress any key to exit: ")

def main():
    print("Rule (e.g. 30, 90, 110):")
    try:
        rule_num = int(input("> "))
    except ValueError:
        rule_num = 30

    rule = [(rule_num >> i) & 1 for i in range(8)]

    W = 384
    H = 192

    cells = [0] * W
    next_cells = [0] * W
    cells[W // 2] = 1

    clear_screen()

    for row in range(H):
        for x in range(W):
            if cells[x]:
                set_pixel(x, row, (0, 0, 180))

        next_cells[0] = rule[(cells[-1] << 2) | (cells[0] << 1) | cells[1]]
        for x in range(1, W - 1):
            next_cells[x] = rule[(cells[x-1] << 2) | (cells[x] << 1) | cells[x+1]]
        next_cells[W-1] = rule[(cells[W-2] << 2) | (cells[W-1] << 1) | cells[0]]

        cells, next_cells = next_cells, cells

    show_screen()
    wait_for_exit(getkey)

main()

# Render the Burning Ship fractal.

from casioplot import clear_screen, draw_string, set_pixel, show_screen
from math import log

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


cmap_data = [
    (
        "cividis",
        [25.77607, -83.187239, 102.370492, -58.977031, 15.42921, -0.384689, -0.008973],
        [0.688122, -2.14075, 2.600914, -1.404197, 0.385562, 0.639494, 0.136756],
        [-28.262533, 93.974216, -121.303164, 74.863561, -22.36376, 2.982654, 0.29417],
    ),
    (
        "inferno",
        [25.092619, -71.287667, 77.157454, -41.709277, 11.617115, 0.105874, 0.000214],
        [-12.222155, 32.55388, -33.415679, 17.457724, -3.947723, 0.566364, 0.001635],
        [-23.11565, 73.588132, -82.253923, 44.645117, -16.257323, 4.117926, -0.03713],
    ),
    (
        "magma",
        [18.664253, -50.758572, 52.170684, -27.666969, 8.345901, 0.250486, -0.002067],
        [-11.490027, 29.05388, -27.944584, 14.253853, -3.596031, 0.694455, -0.000688],
        [-5.570769, 4.269936, 12.881091, -13.646583, 0.329057, 2.495287, -0.009548],
    ),
    (
        "mako",
        [-23.67438, 57.794682, -48.335836, 19.26673, -5.833466, 1.620032, 0.032987],
        [-2.172825, 8.555513, -12.79364, 8.153931, -1.651402, 0.848348, 0.013232],
        [14.259791, -47.319049, 65.176477, -44.241782, 12.702365, 0.292971, 0.040283],
    ),
    (
        "plasma",
        [-3.623823, 9.974645, -11.065106, 6.094711, -2.653255, 2.142438, 0.064053],
        [-22.914405, 71.408341, -82.644718, 42.308428, -7.461101, 0.244749, 0.024812],
        [18.193381, -54.020563, 60.093584, -28.491792, 3.108382, 0.742966, 0.5349],
    ),
    (
        "rocket",
        [-12.453563, 44.789992, -57.268147, 30.376433, -6.401815, 1.947267, -0.003174],
        [52.250665, -158.313952, 173.768416, -81.403784, 15.073064, -0.476821, 0.037717],
        [-10.648435, 11.402042, 14.869938, -21.550609, 6.253872, 0.400542, 0.112123],
    ),
    (
        "turbo",
        [-54.09554, 220.424075, -334.841257, 228.660253, -66.727306, 7.00898, 0.080545],
        [-21.578703, 67.510842, -69.296265, 25.101273, -4.927799, 3.147611, 0.069393],
        [110.735079, -305.386975, 288.708703, -91.680678, -10.16298, 7.655918, 0.219622],
    ),
    (
        "viridis",
        [-5.432077, 4.751787, 6.203736, -4.599932, -0.327241, 0.107708, 0.274455],
        [4.641571, -13.749439, 14.153965, -5.758238, 0.214814, 1.39647, 0.005768],
        [26.272108, -65.320968, 56.6563, -19.291809, 0.091977, 1.386771, 0.332664],
    ),
]


def horner(c, t):
    v = c[0]
    for i in range(1, 7):
        v = v * t + c[i]
    return v


def cmap(t, rc, gc, bc):
    if t < 0.0:
        t = 0.0
    elif t > 1.0:
        t = 1.0
    r = int(horner(rc, t) * 255.0)
    g = int(horner(gc, t) * 255.0)
    b = int(horner(bc, t) * 255.0)
    if r < 0:
        r = 0
    elif r > 255:
        r = 255
    if g < 0:
        g = 0
    elif g > 255:
        g = 255
    if b < 0:
        b = 0
    elif b > 255:
        b = 255
    return (r, g, b)


def wait_for_exit():
    if getkey is not None:
        getkey()
    else:
        input("\nPress Enter to exit: ")


def main():
    if clear_screen is None:
        print("Bypassing execution: Connect native environment framework.")
        return

    param_cr = read_float("cr (-0.5): ", default=-0.5)
    param_ci = read_float("ci (-0.5): ", default=-0.5)
    R = read_float("R (2.0): ", default=2.0)
    if R <= 0.0:
        R = 2.0

    max_iter = read_int("max_iter (32-256): ", default=64)
    if max_iter < 32:
        max_iter = 32
    elif max_iter > 256:
        max_iter = 256

    print("cmap_data:")
    for i in range(len(cmap_data)):
        print(str(i + 1) + " " + cmap_data[i][0])
    cm_idx = read_int("Select (1-" + str(len(cmap_data)) + "): ") - 1
    if cm_idx < 0 or cm_idx >= len(cmap_data):
        cm_idx = 0
    cm_name, RC, GC, BC = cmap_data[cm_idx]

    SCR_H = 190
    PY = 10
    SZ = SCR_H - PY
    LEG_X = SZ + 4
    LEG_W = 10
    LEG_LABEL_X = LEG_X + LEG_W + 2
    LEG_H = SZ

    step = R / (SZ / 2.0)

    x_min = param_cr - step * (SZ / 2.0)
    y_max = param_ci + step * (SZ / 2.0)
    y_min = param_ci - step * (SZ / 2.0)

    clear_screen()

    hdr = (
        "Burning Ship: "
        + "cm="
        + cm_name
        + " max_iter="
        + str(max_iter)
        + " R="
        + str(int(R) if R == int(R) else round(R, 1))
        + " c=("
        + str(param_cr)
        + ","
        + str(param_ci)
        + ")"
    )
    draw_string(0, 0, hdr, (0, 0, 160), "small")

    sp = set_pixel
    ss = show_screen
    log2 = log(2.0)

    for py in range(SZ):
        current_ci = y_min + step * py
        for px in range(SZ):
            current_cr = x_min + step * px
            zr = 0.0
            zi = 0.0
            n = 0
            while n < max_iter and zr * zr + zi * zi < 4.0:
                ar = abs(zr)
                ai = abs(zi)
                zr, zi = ar * ar - ai * ai + current_cr, 2.0 * ar * ai + current_ci
                n += 1
            if n == max_iter:
                col = (0, 0, 0)
            else:
                mod2 = zr * zr + zi * zi
                if mod2 < 1e-30:
                    mod2 = 1e-30
                smooth = n + 1.0 - log(log(mod2) / log2) / log2
                t = smooth / max_iter
                if t < 0.0:
                    t = 0.0
                elif t > 1.0:
                    t = 1.0
                col = cmap(t, RC, GC, BC)
            sp(px, PY + py, col)

        ss()

    for ly in range(LEG_H):
        t = 1.0 - ly / LEG_H
        col = cmap(t, RC, GC, BC)
        for dx in range(LEG_W):
            sp(LEG_X + dx, PY + ly, col)

    for i in range(5):
        t = i / 4.0
        ty = PY + int((1.0 - t) * (LEG_H - 1))
        sp(LEG_X + LEG_W, ty, (0, 0, 0))
        sp(LEG_X + LEG_W + 1, ty, (0, 0, 0))
        label = str(int(t * max_iter)) + " [iters]"
        lly = ty - 4
        if lly < PY:
            lly = PY
        if lly > PY + LEG_H - 8:
            lly = PY + LEG_H - 8
        draw_string(LEG_LABEL_X, lly, label, (0, 0, 0), "small")

    ss()
    wait_for_exit()


main()
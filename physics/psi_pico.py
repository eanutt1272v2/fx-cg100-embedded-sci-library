# Visualise hydrogenic wavefunctions on Casio fx-CG100.

from casioplot import clear_screen, draw_string, set_pixel, show_screen
from math import log, exp, pi, sqrt

from psi_pico_lib import (
    cmap_data, cmap, fmt_density, read_float, read_int, wait_for_exit, 
    HydrogenicWavefunction
)

try:
    from casioplot import getkey
except ImportError:
    getkey = None


n = read_int("n (default=4): ", min_value=1, default=4)
l = read_int("l (0..n-1, default=1): ", min_value=0, max_value=n - 1, default=1)
m = read_int("m (-l..l, default=0): ", min_value=-l, max_value=l, default=0)

print("Slice Plane Setup:")
print("1: XZ plane")
print("2: XY plane")
print("3: YZ plane")
plane_choice = read_int("Select plane (1-3, default=1): ", min_value=1, max_value=3, default=1)
plane_names = {1: "XZ", 2: "XY", 3: "YZ"}
plane_str = plane_names[plane_choice]

offset = read_float("Slice offset [a0] (default=0.0): ", default=0.0)
phi_deg = read_float("phi_deg (real Ylm, default=33): ", default=33.0)
phi_slice = phi_deg * pi / 180.0
Z = read_float("Z (1=H): ")
if Z <= 0.0: Z = 1.0

R = read_float("R [a0] (0=auto): ")
alpha = read_float("alpha (default=100): ", default=100.0)

print("Units Setup:")
print("1: [a0^-3]")
print("2: [m^-3]")
unit_choice = read_int("Select unit (1-2): ", min_value=1, max_value=2)

print("cmap_data:")
for i in range(len(cmap_data)):
    print(str(i + 1) + " " + cmap_data[i][0])
cm_idx = read_int("Select (1-" + str(len(cmap_data)) + "): ") - 1
if cm_idx < 0 or cm_idx >= len(cmap_data):
    cm_idx = 0
cm_name, RC, GC, BC = cmap_data[cm_idx]

if R <= 0.0:
    inner_term = n * n - l * (l + 1)
    if inner_term < 0: inner_term = 0
    r_turn = (n * n + n * sqrt(inner_term)) / Z
    
    R = r_turn * 1.35
    
    abs_offset = abs(offset)
    if abs_offset > 0.0:
        R = sqrt(R * R + abs_offset * abs_offset)
else:
    R = R

SCR_H = 190
PY = 10
SZ = SCR_H - PY
SAMP = SZ
LEG_X = SZ + 4
LEG_W = 10
LEG_LABEL_X = LEG_X + LEG_W + 2
LEG_H = SZ

A0_M = 5.29177210903e-11
A0_3 = A0_M * A0_M * A0_M
unit_scale = A0_3 if unit_choice == 2 else 1.0
unit_str = " [m^-3]" if unit_choice == 2 else " [a0^-3]"

wf = HydrogenicWavefunction(n, l, m, Z, phi_slice, plane_choice, offset)

step = 2.0 * R / (SAMP - 1)
peak = 1e-30

for sy in range(SAMP):
    v = R - step * sy
    for sx in range(SAMP):
        u = -R + step * sx
        x3, y3, z3 = wf.get_coords(u, v)
        d = wf.density_3d(x3, y3, z3)
        if d > peak: peak = d

if alpha <= 0.0: alpha = 1e-6
log_alpha_plus_1 = log(1.0 + alpha)


def main():
    clear_screen()
    Zs = str(int(Z)) if Z == int(Z) else str(Z)
    
    hdr = (
        "Psi: "
        "|" + str(n) + str(l) + str(m) + ">"
        + " Z="
        + Zs
        + " pl:"
        + plane_str
        + " off:"
        + str(offset) 
        + " cm="
        + cm_name
        + " R="
        + str(int(R) if R == int(R) else round(R, 1))
        + " a="
        + str(int(alpha))
        + " phi="
        + str(int(phi_deg))
    )

    draw_string(0, 0, hdr, (0, 0, 160), "small")

    sp = set_pixel
    ss = show_screen

    for sy in range(SAMP):
        v = R - step * sy
        py = PY + sy
        for sx in range(SAMP):
            u = -R + step * sx
            x3, y3, z3 = wf.get_coords(u, v)
            d = wf.density_3d(x3, y3, z3)
            norm = max(0.0, min(1.0, d / peak))
            val = log(1.0 + alpha * norm) / log_alpha_plus_1
            sp(sx, py, cmap(val, RC, GC, BC))
        ss()

    leg_den = LEG_H - 1 if LEG_H > 1 else 1
    for py in range(LEG_H):
        t = 1.0 - py / leg_den
        col = cmap(t, RC, GC, BC)
        for dx in range(LEG_W): sp(LEG_X + dx, PY + py, col)

    for i in range(5):
        t = i / 4.0
        ty = PY + int((1.0 - t) * leg_den)
        sp(LEG_X + LEG_W, ty, (0, 0, 0))
        sp(LEG_X + LEG_W + 1, ty, (0, 0, 0))
        t_row = 1.0 - (ty - PY) / leg_den
        if t_row <= 0.0:
            d_tick = 0.0
        else:
            norm_tick = (exp(t_row * log_alpha_plus_1) - 1.0) / alpha
            d_tick = (peak * norm_tick) / unit_scale
        
        label = fmt_density(d_tick) + unit_str
        ly = max(PY, min(PY + LEG_H - 8, ty - 4))
        draw_string(LEG_LABEL_X, ly, label, (0, 0, 0), "small")

    ss()
    wait_for_exit(getkey)


main()

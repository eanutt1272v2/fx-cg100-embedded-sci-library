# Visualise hydrogenic wavefunctions on the Casio fx-CG100.

from casioplot import clear_screen, draw_string, set_pixel, show_screen
from math import log, exp, pi, sqrt, sin, cos

from psi_fx_lib import cmap_data, cmap, fmt_density, read_float, read_int, wait_for_exit, HydrogenicWavefunction

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
if Z <= 0.0:
    Z = 1.0

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
    if inner_term < 0:
        inner_term = 0
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

density_3d_local = wf.density_3d

if l == 0:
    peak = density_3d_local(0.0, 0.0, 0.0)
else:
    r_ref = (n * n) / Z
    best_ang_d = -1.0
    th_max, ph_max = 0.0, 0.0

    for r_probe in (0.6 * r_ref, 1.0 * r_ref, 1.4 * r_ref):
        for i in range(36):
            th = (i / 35.0) * pi
            sin_th = sin(th)
            z_coord = r_probe * cos(th)
            for j in range(18):
                ph = (j / 17.0) * 2.0 * pi
                x_coord = r_probe * sin_th * cos(ph)
                y_coord = r_probe * sin_th * sin(ph)

                d = density_3d_local(x_coord, y_coord, z_coord)
                if d > best_ang_d:
                    best_ang_d = d
                    th_max, ph_max = th, ph

    sin_tm = sin(th_max)
    cos_tm = cos(th_max)
    cos_pm = cos(ph_max)
    sin_pm = sin(ph_max)

    peak = 1e-30
    r_limit = r_ref * 2.5
    r_step = r_limit / 200.0

    for i in range(201):
        r = i * r_step
        d = density_3d_local(r * sin_tm * cos_pm, r * sin_tm * sin_pm, r * cos_tm)
        if d > peak:
            peak = d

if peak < 1e-30:
    peak = 1e-30

if alpha <= 0.0:
    alpha = 1e-6
log_alpha_plus_1 = log(1.0 + alpha)


def main():
    clear_screen()
    Zs = str(int(Z)) if Z == int(Z) else str(Z)

    hdr = (
        "Psi: "
        + "|"
        + str(n)
        + str(l)
        + str(m)
        + ">"
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
    get_coords_local = wf.get_coords
    density_3d_local = wf.density_3d

    color_lut = []
    for i in range(256):
        norm = i / 255.0
        val = log(1.0 + alpha * norm) / log_alpha_plus_1
        color_lut.append(cmap(val, RC, GC, BC))

    for sy in range(SAMP):
        v = R - step * sy
        py = PY + sy
        for sx in range(SAMP):
            u = -R + step * sx
            x3, y3, z3 = get_coords_local(u, v)
            d = density_3d_local(x3, y3, z3)

            idx = int((d / peak) * 255)
            if idx > 255:
                idx = 255
            elif idx < 0:
                idx = 0

            sp(sx, py, color_lut[idx])
        ss()

    leg_den = LEG_H - 1 if LEG_H > 1 else 1
    for py in range(LEG_H):
        t = 1.0 - py / leg_den
        col = cmap(t, RC, GC, BC)
        for dx in range(LEG_W):
            sp(LEG_X + dx, PY + py, col)

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

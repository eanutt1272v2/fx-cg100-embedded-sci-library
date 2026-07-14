from math import sqrt, log, exp, pi, sin, cos, atan2


_lanczos_coeffs = (
    0.99999999999980993,
    676.5203681218851,
    -1259.1392167224028,
    771.32342877765313,
    -176.61502916214059,
    12.507343278686905,
    -0.13857109526572012,
    9.9843695780195716e-6,
    1.5056327351493116e-7,
)


cmap_data = [
    (
        "cividis",
        [
            25.77607,
            -83.187239,
            102.370492,
            -58.977031,
            15.42921,
            -0.384689,
            -0.008973,
        ],
        [0.688122, -2.14075, 2.600914, -1.404197, 0.385562, 0.639494, 0.136756],
        [-28.262533, 93.974216, -121.303164, 74.863561, -22.36376, 2.982654, 0.29417],
    ),
    (
        "inferno",
        [
            25.092619,
            -71.287667,
            77.157454,
            -41.709277,
            11.617115,
            0.105874,
            0.000214,
        ],
        [-12.222155, 32.55388, -33.415679, 17.457724, -3.947723, 0.566364, 0.001635],
        [-23.11565, 73.588132, -82.253923, 44.645117, -16.257323, 4.117926, -0.03713],
    ),
    (
        "magma",
        [
            18.664253,
            -50.758572,
            52.170684,
            -27.666969,
            8.345901,
            0.250486,
            -0.002067,
        ],
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


def read_text(prompt, default=None):
    while True:
        raw = input(prompt).strip()
        if raw:
            return raw
        if default is not None:
            return default
        print("please enter a value.")


def read_int(prompt, default=None, min_value=None, max_value=None):
    while True:
        raw = input(prompt).strip()
        if raw == "" and default is not None:
            value = int(default)
        else:
            try:
                value = int(raw)
            except ValueError:
                print("invalid integer. try again.")
                continue
        if min_value is not None and value < min_value:
            print("value must be >= " + str(min_value))
            continue
        if max_value is not None and value > max_value:
            print("value must be <= " + str(max_value))
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
                print("invalid float. try again.")
                continue
        if min_value is not None and value < min_value:
            print("value must be >= " + str(min_value))
            continue
        if max_value is not None and value > max_value:
            print("value must be <= " + str(max_value))
            continue
        return value


def lgamma(x):
    if x < 0.5:
        return log(pi / sin(pi * x)) - lgamma(1.0 - x)
    x -= 1.0
    base_a = _lanczos_coeffs[0]
    t = x + 7.5
    for i in range(1, 9):
        base_a += _lanczos_coeffs[i] / (x + i)
    return 0.5 * log(2 * pi) + (x + 0.5) * log(t) - t + log(base_a)


def horner(coeffs, t):
    v = coeffs[0]
    for i in range(1, len(coeffs)):
        v = v * t + coeffs[i]
    return v


def cmap(t, rc, gc, bc):
    r = max(0, min(255, int(horner(rc, t) * 255.0)))
    g = max(0, min(255, int(horner(gc, t) * 255.0)))
    b = max(0, min(255, int(horner(bc, t) * 255.0)))
    return (r, g, b)


def fmt_density(d):
    if d <= 0.0:
        return "0"
    exp_n = 0
    v = d
    while v >= 10.0:
        v /= 10.0
        exp_n += 1
    while v < 1.0:
        v *= 10.0
        exp_n -= 1
    m = round(v * 100.0) / 100.0
    if m >= 10.0:
        m /= 10.0
        exp_n += 1
    return "{:.2f}".format(m) + "e" + str(exp_n)


def wait_for_exit(getkey):
    if getkey is not None:
        getkey()
    else:
        input("\npress any key to exit: ")


def _al(ll, mm, x):
    pmm = 1.0
    if mm > 0:
        xx = 1.0 - x * x
        s = sqrt(xx) if xx > 0.0 else 0.0
        fact = 1.0
        for _ in range(1, mm + 1):
            pmm *= -fact * s
            fact += 2.0
    if ll == mm:
        return pmm
    pmmp1 = x * (2 * mm + 1) * pmm
    if ll == mm + 1:
        return pmmp1
    for lll in range(mm + 2, ll + 1):
        pll = (x * (2 * lll - 1) * pmmp1 - (lll + mm - 1) * pmm) / (lll - mm)
        pmm, pmmp1 = pmmp1, pll
    return pmmp1


def _lag(p, alp, x):
    if p < 0:
        return 0.0
    L0 = 1.0
    if p == 0:
        return L0
    L1 = 1.0 + alp - x
    if p == 1:
        return L1
    for k in range(1, p):
        L2 = ((2 * k + 1 + alp - x) * L1 - (k + alp) * L0) / (k + 1)
        L0, L1 = L1, L2
    return L1


class HydrogenicWavefunction:
    def __init__(self, n, l, m, Z, phi_slice, plane_choice, offset, is_real=True):
        self.n, self.l, self.m, self.abs_m = n, l, m, abs(m)
        self.plane_choice, self.offset, self.phi_slice = (
            plane_choice,
            offset,
            phi_slice,
        )
        self.is_real = is_real
        self.p_rad, self.alpha_l, self.rho_k = n - l - 1, 2 * l + 1, 2.0 * Z / n
        self.log_norm_r = 0.5 * (
            3 * log(self.rho_k)
            + lgamma(n - l)
            - log(2.0 * n)
            - lgamma(n + l + 1)
        )
        self.norm_r = exp(self.log_norm_r)
        self.log_norm_y = 0.5 * (
            log((2 * l + 1) / (4 * pi))
            + lgamma(l - self.abs_m + 1)
            - lgamma(l + self.abs_m + 1)
        )
        if self.is_real and m != 0:
            self.log_norm_y += 0.5 * log(2.0)
        self.y_norm = exp(self.log_norm_y)

    def get_coords(self, u, v):
        if self.plane_choice == 1:
            return u, self.offset, v
        if self.plane_choice == 2:
            return u, v, self.offset
        return self.offset, u, v

    def density_3d(self, x_3d, y_3d, z_3d):
        r2 = x_3d * x_3d + y_3d * y_3d + z_3d * z_3d
        if r2 <= 1e-24:
            if self.l != 0 or self.abs_m > 0:
                return 0.0
            d = (
                self.norm_r
                * _lag(self.p_rad, self.alpha_l, 0.0)
                * self.y_norm
                * _al(self.l, self.abs_m, 1.0)
            )
            return d * d
        r = sqrt(r2)
        rho = self.rho_k * r
        ea = -0.5 * rho + (self.l * log(rho) if self.l > 0 else 0.0)
        if ea < -700.0:
            return 0.0
        rv = self.norm_r * exp(ea) * _lag(self.p_rad, self.alpha_l, rho)
        ct = max(-1.0, min(1.0, z_3d / r))
        yv = self.y_norm * _al(self.l, self.abs_m, ct)
        if self.is_real:
            if self.m == 0:
                phase = 1.0
            else:
                p = atan2(y_3d, x_3d)
                phase = cos(self.m * p) if self.m > 0 else sin(self.abs_m * p)
            val = rv * yv * phase
            return val * val
        return rv * yv * rv * yv
        

import math

PI = math.pi


def fmt(v):
    if abs(v) < 1e-12:
        v = 0.0
    return "{:.10g}".format(v)


def pack(*pairs):
    return tuple(name + ":" + fmt(value) for name, value in pairs)


def require_positive(*values):
    for value in values:
        if value <= 0:
            raise ValueError("All dimensions must be > 0")


def int_ge(value, minimum, name):
    if int(value) != value:
        raise ValueError(name + " must be an integer >= " + str(minimum))
    ivalue = int(value)
    if ivalue < minimum:
        raise ValueError(name + " must be an integer >= " + str(minimum))
    return ivalue


def area_triangle_heron(a, b, c):
    require_positive(a, b, c)
    s = 0.5 * (a + b + c)
    area_sq = s * (s - a) * (s - b) * (s - c)
    if area_sq <= 0:
        raise ValueError("Invalid triangle side lengths")
    return math.sqrt(area_sq)


def area_regular_polygon(n, s):
    n = int_ge(n, 3, "n")
    require_positive(s)
    return n * s * s / (4.0 * math.tan(PI / n))


def perimeter_regular_polygon(n, s):
    n = int_ge(n, 3, "n")
    require_positive(s)
    return n * s


def prism_metrics(base_area, base_perimeter, length):
    require_positive(base_area, base_perimeter, length)
    volume = base_area * length
    surface_area = 2.0 * base_area + base_perimeter * length
    return volume, surface_area


def pyramid_metrics(base_area, base_perimeter, height, slant_height):
    require_positive(base_area, base_perimeter, height, slant_height)
    volume = base_area * height / 3.0
    surface_area = base_area + 0.5 * base_perimeter * slant_height
    return volume, surface_area


def f_square(side):
    require_positive(side)
    return pack(("A", side * side), ("P", 4.0 * side), ("Diag", side * math.sqrt(2.0)))


def f_rectangle(width, height):
    require_positive(width, height)
    return pack(("A", width * height), ("P", 2.0 * (width + height)), ("Diag", math.sqrt(width * width + height * height)))


def f_triangle_bh(base, height):
    require_positive(base, height)
    return pack(("A", 0.5 * base * height))


def f_triangle_sss(a, b, c):
    return pack(("A", area_triangle_heron(a, b, c)), ("P", a + b + c))


def f_equilateral_triangle(side):
    require_positive(side)
    return pack(("A", math.sqrt(3.0) * side * side / 4.0), ("P", 3.0 * side), ("H", math.sqrt(3.0) * side / 2.0))


def f_parallelogram(base, height, side):
    require_positive(base, height, side)
    return pack(("A", base * height), ("P", 2.0 * (base + side)))


def f_trapezium(a, b, height, side1, side2):
    require_positive(a, b, height, side1, side2)
    return pack(("A", 0.5 * (a + b) * height), ("P", a + b + side1 + side2))


def f_rhombus(d1, d2):
    require_positive(d1, d2)
    side = 0.5 * math.sqrt(d1 * d1 + d2 * d2)
    return pack(("A", 0.5 * d1 * d2), ("P", 4.0 * side), ("Side", side))


def f_kite(d1, d2, side1, side2):
    require_positive(d1, d2, side1, side2)
    return pack(("A", 0.5 * d1 * d2), ("P", 2.0 * (side1 + side2)))


def f_circle(r):
    require_positive(r)
    return pack(("A", PI * r * r), ("C", 2.0 * PI * r))


def f_semicircle(r):
    require_positive(r)
    return pack(("A", 0.5 * PI * r * r), ("Arc", PI * r), ("P", PI * r + 2.0 * r))


def f_sector(r, deg):
    require_positive(r)
    if deg <= 0 or deg > 360:
        raise ValueError("Degrees must be in the range 0 < deg <= 360")
    theta = deg * PI / 180.0
    arc = r * theta
    return pack(("A", 0.5 * r * r * theta), ("Arc", arc), ("P", 2.0 * r + arc))


def f_ellipse(a, b):
    require_positive(a, b)
    h = ((a - b) * (a - b)) / ((a + b) * (a + b))
    perim = PI * (a + b) * (1.0 + (3.0 * h) / (10.0 + math.sqrt(4.0 - 3.0 * h)))
    return pack(("A", PI * a * b), ("P~", perim))


def f_regular_polygon(n, s):
    n = int_ge(n, 3, "n")
    require_positive(s)
    area = area_regular_polygon(n, s)
    perim = perimeter_regular_polygon(n, s)
    apothem = s / (2.0 * math.tan(PI / n))
    return pack(("A", area), ("P", perim), ("Apothem", apothem))


def f_annulus(R, r):
    require_positive(R, r)
    if R <= r:
        raise ValueError("Outer radius must be greater than inner radius")
    return pack(("A", PI * (R * R - r * r)), ("OuterC", 2.0 * PI * R), ("InnerC", 2.0 * PI * r))


def f_cube(side):
    require_positive(side)
    return pack(("V", side * side * side), ("SA", 6.0 * side * side), ("Diag", side * math.sqrt(3.0)))


def f_cuboid(length, width, height):
    require_positive(length, width, height)
    return pack(("V", length * width * height), ("SA", 2.0 * (length * width + length * height + width * height)), ("Diag", math.sqrt(length * length + width * width + height * height)))


def f_prism(base_area, base_perimeter, length):
    volume, surface_area = prism_metrics(base_area, base_perimeter, length)
    return pack(("V", volume), ("SA", surface_area))


def f_triangular_prism(a, b, c, length):
    base_area = area_triangle_heron(a, b, c)
    base_perimeter = a + b + c
    volume, surface_area = prism_metrics(base_area, base_perimeter, length)
    return pack(("V", volume), ("SA", surface_area), ("BaseA", base_area))


def f_cylinder(r, h):
    require_positive(r, h)
    return pack(("V", PI * r * r * h), ("CSA", 2.0 * PI * r * h), ("SA", 2.0 * PI * r * (r + h)))


def f_cone(r, h):
    require_positive(r, h)
    slant = math.sqrt(r * r + h * h)
    return pack(("V", PI * r * r * h / 3.0), ("CSA", PI * r * slant), ("SA", PI * r * (r + slant)), ("Slant", slant))


def f_frustum_cone(R, r, h):
    require_positive(R, r, h)
    if R <= r:
        raise ValueError("R must be greater than r")
    slant = math.sqrt((R - r) * (R - r) + h * h)
    csa = PI * (R + r) * slant
    sa = csa + PI * (R * R + r * r)
    volume = PI * h * (R * R + R * r + r * r) / 3.0
    return pack(("V", volume), ("CSA", csa), ("SA", sa), ("Slant", slant))


def f_sphere(r):
    require_positive(r)
    return pack(("V", 4.0 * PI * r * r * r / 3.0), ("SA", 4.0 * PI * r * r))


def f_hemisphere(r):
    require_positive(r)
    return pack(("V", 2.0 * PI * r * r * r / 3.0), ("CSA", 2.0 * PI * r * r), ("SA", 3.0 * PI * r * r))


def f_pyramid(base_area, base_perimeter, h, slant):
    volume, surface_area = pyramid_metrics(base_area, base_perimeter, h, slant)
    return pack(("V", volume), ("SA", surface_area))


def f_tetrahedron(side):
    require_positive(side)
    return pack(("V", side * side * side / (6.0 * math.sqrt(2.0))), ("SA", math.sqrt(3.0) * side * side))


def f_torus(R, r):
    require_positive(R, r)
    if R <= r:
        raise ValueError("Major radius must be greater than minor radius")
    return pack(("V", 2.0 * PI * PI * R * r * r), ("SA", 4.0 * PI * PI * R * r))


def f_frustum_pyramid(base_area, top_area, base_perimeter, top_perimeter, height, slant_height):
    require_positive(base_area, top_area, base_perimeter, top_perimeter, height, slant_height)
    if base_area <= top_area:
        raise ValueError("Base area must be greater than top area")
    volume = height * (base_area + top_area + math.sqrt(base_area * top_area)) / 3.0
    lateral = 0.5 * (base_perimeter + top_perimeter) * slant_height
    surface_area = base_area + top_area + lateral
    return pack(("V", volume), ("SA", surface_area), ("Lateral", lateral))


def f_spherical_shell(R, r):
    require_positive(R, r)
    if R <= r:
        raise ValueError("Outer radius must be greater than inner radius")
    return pack(("V", 4.0 * PI * (R * R * R - r * r * r) / 3.0), ("SA", 4.0 * PI * (R * R + r * r)))


SHAPES_2D = [
    ("Square", f_square, ["Side"]),
    ("Rectangle", f_rectangle, ["Width", "Height"]),
    ("Triangle (b,h)", f_triangle_bh, ["Base", "Height"]),
    ("Triangle (3 sides)", f_triangle_sss, ["a", "b", "c"]),
    ("Equilateral Triangle", f_equilateral_triangle, ["Side"]),
    ("Parallelogram", f_parallelogram, ["Base", "Height", "Side"]),
    ("Trapezium", f_trapezium, ["a", "b", "h", "c", "d"]),
    ("Rhombus", f_rhombus, ["Diag1", "Diag2"]),
    ("Kite", f_kite, ["Diag1", "Diag2", "a", "b"]),
    ("Circle", f_circle, ["Radius"]),
    ("Semicircle", f_semicircle, ["Radius"]),
    ("Sector", f_sector, ["Radius", "Degrees"]),
    ("Ellipse", f_ellipse, ["Semi-major a", "Semi-minor b"]),
    ("Regular Polygon", f_regular_polygon, ["n", "Side"]),
    ("Annulus", f_annulus, ["Outer R", "Inner r"]),
]

SHAPES_3D = [
    ("Cube", f_cube, ["Side"]),
    ("Cuboid", f_cuboid, ["Length", "Width", "Height"]),
    ("Prism (general)", f_prism, ["Base Area", "Base Perim", "Length"]),
    ("Triangular Prism", f_triangular_prism, ["a", "b", "c", "Length"]),
    ("Cylinder", f_cylinder, ["Radius", "Height"]),
    ("Cone", f_cone, ["Radius", "Height"]),
    ("Frustum Cone", f_frustum_cone, ["R", "r", "Height"]),
    ("Sphere", f_sphere, ["Radius"]),
    ("Hemisphere", f_hemisphere, ["Radius"]),
    ("Pyramid (general)", f_pyramid, ["Base Area", "Base Perim", "Height", "Slant"]),
    ("Regular Tetrahedron", f_tetrahedron, ["Side"]),
    ("Torus", f_torus, ["Major R", "Minor r"]),
    ("Frustum Pyramid", f_frustum_pyramid, ["Base Area", "Top Area", "Base Perim", "Top Perim", "Height", "Slant"]),
    ("Spherical Shell", f_spherical_shell, ["Outer R", "Inner r"]),
]

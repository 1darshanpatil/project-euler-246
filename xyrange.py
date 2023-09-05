import math
from sympy import Point
from phi import angles


def rangexy(e, cr_angle):
    hrad = e.hradius
    vrad = e.vradius

    x = math.ceil(hrad)
    if e.contains(Point(x, 0)):
        x += 1
    y = math.ceil(vrad)
    if e.contains(Point(0, y)):
        y += 1
    start = [x, y]
    runx, runy = True, True
    while (runx or runy):
        if runx:
            lines = e.tangent_lines(Point(x, 0))
            if angles(lines) > cr_angle:
                x += 1
            else:
                runx = False
        if runy:
            lines = e.tangent_lines(Point(0, y))
            if angles(lines) > cr_angle:
                y += 1
            else:
                runy = False
        print(x, y)

    end = [x, y]
    return start, end

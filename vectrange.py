import math
from sympy import Ellipse, Point
import phi
import sympy as sp


def solve_one_var(Y, a, b):
    try:
        z = sp.symbols('z')
        eq = (z / a) ** 2 + (Y / b) ** 2 - 1
        res = sp.solve(eq, z)
        res = max(res)
        cei = math.ceil(res)
        if cei == res:
            print("##############################################################################################################")
            print(res, cei, Y)
        return cei
    except TypeError:
        return 0


def linrange(cr_angle, xe, ye, e):
    lst = []
    x_last = xe
    cnt = 0
    for y in range(ye):
        x_cnt = True
        x = x_last
        a, b = e.hradius, e.vradius
        while x_cnt:
            lines = e.tangent_lines(Point(x, y))
            if phi.angles(lines) >= cr_angle:
                x_cnt = False
                x_last = x
                z = solve_one_var(y, a, b)
                cnt_along_x = x_last - z
                if x * y:
                    cnt += 4 * cnt_along_x
                else:
                    cnt += 2 * cnt_along_x
            x -= 1
        print("x, y, z, cnt: ", x, y, z, cnt)


harad = 7500
varad = 2500*math.sqrt(5)

# harad, varad = 5, 7.5
e = Ellipse(Point(0, 0), harad, varad)
cr_angle = 45
xe, ye = 15440, 18950
# xe, ye = 18, 14
linrange(cr_angle, xe, ye, e)

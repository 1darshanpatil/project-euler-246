import itertools

import phi
import sympy
import math
# vrad = 70
vrad= math.sqrt(7500**2 - 5000**2)
hrad = 7500

e = sympy.Ellipse(sympy.Point(0, 0), hrad, vrad)


cr_angle = 45
xe, ye = 15440, 18950

cnt = 0

for x, y in itertools.product(range(xe), range(ye)):
    pt = sympy.Point(x, y)
    if (x/hrad)**2 + (y/vrad) ** 2 > 1:
        lines = e.tangent_lines(pt)
        theta = phi.angles(lines)
        if theta > cr_angle:
            if x * y == 0:
                cnt += 2
            else:
                cnt += 4
        print(pt, theta, cnt)


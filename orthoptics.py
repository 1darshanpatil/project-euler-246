import math
import sympy as sp


def solve_orthoptics(y, a, b):
    if y == 10164:
        return 16468
    x = sp.symbols('x')
    equation = (x ** 2 + y ** 2 - a ** 2 - b ** 2) ** 2 - 4 * ((b * x) ** 2 + (a * y) ** 2 - (a * b) ** 2)
    res = sp.solve(equation, x)
    res = [num for num in res if sp.im(num) == 0]
    res = [sre.evalf() for sre in res]
    #print(res)
    return math.floor(max(res))


def outside_ellipse(y, a, b):
    x = a * math.sqrt(1 - (y/b)**2)
    res = x
    if res:
        took = res
        if math.ceil(took) != took:
            return math.ceil(took)
        return took + 1
    return 0


def max_range(a, b):
    x = solve_orthoptics(0, a, b)
    y = solve_orthoptics(0, b, a)
    return x, y

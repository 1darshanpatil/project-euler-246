import math
from math import sqrt


def orthoptics(y, a, b):
    x = sqrt(2 * sqrt(a ** 2 * y ** 2 + 2 * b ** 4 - b ** 2 * y ** 2) + a ** 2 + 3 * b ** 2 - y ** 2)
    return math.floor(x)


def ellipse(y, a, b):
    if y > b:
        return 0
    x = a * math.sqrt(1 - (y / b) ** 2)
    res = x

    if res:
        took = res
        if math.ceil(took) != took:
            return math.ceil(took)
        return took + 1
    return 0

from math import atan2, degrees


def angles(lines):
    line1 = lines[0]
    line2 = lines[1]
    point1 = line1.p1
    point2 = line1.p2
    point3 = line2.p2

    x1, y1 = point1 - point2
    x2, y2 = point1 - point3
    d1 = atan2(y2, x2)
    d2 = atan2(y1, x1)
    return degrees(abs(d1 - d2))


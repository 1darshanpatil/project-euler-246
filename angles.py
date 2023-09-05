import math


def axis_angle(axes, cord, major_along_x=True):
	major, minor = sorted(axes, reverse=major_along_x)
	x = cord
	try:
		d = math.sqrt((minor * x) ** 2 - (minor * major) ** 2)
		din = major ** 2 - x ** 2
	except ZeroDivisionError:
		return "The angle is not defined."
	phi = math.degrees(math.atan(d / din))
	return math.fabs(phi)


if __name__ == "__main__":
    axes = (100, 10)
    cord = 11
    angle = axis_angle(axes, cord, major_along_x=False)
    print(angle)
    print(180 - angle)

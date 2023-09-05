import math
import operator


def phi(a, b, x, y):
	p = x * y
	D = (a * y) ** 2 + (b * x) ** 2 - (a * b) ** 2
	d = math.sqrt(D)
	r = a ** 2 - x ** 2
	try:
		tan_phi = (2 * d * r) / (r ** 2 + p ** 2 - D)
	except ZeroDivisionError:
		return 90
	phi_angle = math.degrees(math.atan(tan_phi))
	return operator.abs(phi_angle)

if __name__ == "__main__":
	a, b, x, y = list(map(float, input("Enter the values of a, b, x, y: ").split(" ")))
	phi(a, b, x, y)

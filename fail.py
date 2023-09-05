import orthoptics
import math

a = 7500
b = math.sqrt(5) * 2500

# a, b = 2, 3


xe, ye = orthoptics.max_range(a, b)
print(xe, ye)
cnt = 0
print("y, x_ell, x_ort, z, lattice, cnt")
for y in range(ye+1):
    x_ort = orthoptics.solve_orthoptics(y, a, b)
    x_ell = orthoptics.outside_ellipse(y, a, b)
    z = x_ort - x_ell + 1
    if y == 0:
        lattice = 2 * z
    elif y > b:
        lattice = 4 * z - 2
    elif y <= b:
        lattice = 4 * z
    cnt += lattice
    print(f"{y}, {x_ell}, {x_ort}, {z}, {lattice}, {cnt}")


print(cnt)

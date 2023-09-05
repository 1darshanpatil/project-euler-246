import linear
import orthoptics


a = 7500
b=2500*5**.5

xe, ye = orthoptics.max_range(a, b)
print(xe, ye)
cnt = 0
print("y, x_ell, x_ort, z, lattice, cnt")
for y in range(ye+1):
    x_ort = linear.orthoptics(y, a, b)
    x_ell = linear.ellipse(y, a, b)
    z = x_ort - x_ell + 1
    if y == 0:
        lattice = 2 * z
    elif y > b:
        lattice = 4 * z - 2
    elif y <= b:
        lattice = 4 * z
    cnt += lattice
    print(f"{y}, {x_ell}, {x_ort}, {z}, {lattice}, {cnt}")
import math

def orthoptics(y, a, b):
    x = math.sqrt(2 * math.sqrt(a ** 2  * y ** 2 + 2 * b ** 4 - b ** 2 * y ** 2) + a**2 + 3 * b**2 - y**2)
    return math.floor(x)


def ellipse(y, a, b):
    if y > b:
        return 0
    if y == b:
        return 1
    x = a * math.sqrt(1 - (y/b) ** 2)
    res = x
    
    if res:
        took = res
        if math.ceil(took) != took:
            return math.ceil(took)
        return took + 1
    return 0


def max_range_linear(a, b):
    x = orthoptics(0, a, b)
    y = orthoptics(0, b, a)
    return x, y



if __name__ == "__main__":
    a, b = 7500, 2500*5**.5
    #a, b = 3, 2
    xe, ye = max_range_linear(a, b)
    print(xe, ye)
    cnt = 0
    print("y, x_ell, x_orth, z, lattice, cnt")
    for y in range(ye + 1):
        x_orth =  orthoptics(y, a, b)
        x_ell =  ellipse(y, a, b)
        z = x_orth - x_ell + 1
        if y == 0:
            lattice = 2 * z

        elif y > b:
            lattice = 4 * z - 2

        elif y <= b:
            lattice = 4 * z
        
        cnt += lattice

        print(f"{y}, {x_ell}, {x_orth}, {z}, {lattice}, {cnt}")

        

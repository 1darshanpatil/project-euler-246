import sympy as sp
import pandas as pd
import orthoptics


def store_solution(func, a, b):
    ymn, ymx = 0, int(b)
    results = []
    for y in range(ymn, ymx+1):
        x_sol = func(y, a, b)
        results.append((y, x_sol))
        print(y, x_sol)

    df = pd.DataFrame(results, columns=['y', 'x'])
    df.to_csv('big_ellipse.csv', index=False)



if __name__ == "__main__":
    a = 7500
    b = 2500*5**.5
    store_solution(orthoptics.outside_ellipse, a, b)


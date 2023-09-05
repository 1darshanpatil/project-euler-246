import orthoptics
import pandas as pd


def store_solutions(func, y_range, a, b):
    ymn, ymx = y_range
    results = []
    for y in range(ymn, ymx+1):
        x_sol = func(y, a, b)
        results.append((y, x_sol))
        print(y, x_sol)

    df = pd.DataFrame(results, columns=['y', 'x'])
    df.to_csv('big_solutions.csv', index=False)


y_range = (0, 18949)
a = 7500
b = 2500*5**.5
store_solutions(orthoptics.solve_orthoptics, y_range, a, b)

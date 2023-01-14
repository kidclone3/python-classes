import numpy as np
import numpy.typing as npt
def Gauss(a: np.ndarray, b: np.ndarray):
    n = b.size
    # column first, row second.
    # a[0] /= a[0][0]
    for j in range(n-1): 
        for i in range(j+1, n):
            # a[i][j] = - p * a[i][j] + a[i-1][j]
            if (a[j][j] != 0):
                p = a[j][j] / a[i][j]
                # print(a[i])
                # tmp = a[i].copy()
                # tmp *= -p
                a[i] *= (-p)
                # print(a[i])
                a[i] += a[j]
                # print(a[i])
                #  + a[j]
                # for k in range(n):
                #     a[i][k] = a[i][k]*(-p) + a[j][k]
                b[i] = -b[i]*p + b[j]
                # print(p)
                # print(a)
        # a[j] /= a[j][j]
a = np.array([[2, 1, -1], [-3,-1,2], [-2,1,2]], dtype=np.float64)
b = np.array([8,-11,-3], dtype = np.float64)
x = np.linalg.solve(a, b)

print(Gauss(a, b))
print(a)
print(b)

print(x)

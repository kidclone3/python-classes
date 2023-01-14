import numpy as np

a = [int(_) for _ in input("Nhập bộ các số a1, a2, a3:\n").split()]
print(a)
b = [int(_) for _ in input("Nhập bộ các số b1, b2, b3:\n").split()]
print(b)
c = [int(_) for _ in input("Nhập bộ các số c1, c2, c3:\n").split()]
print(c)
d = [int(_) for _ in input("Nhập bộ các số d1, d2, d3:\n").split()]
print(d)

matrix = np.array([a, b, c])
result = np.array(d)

x = np.linalg.solve(matrix, result)
print("Kết quả là: ", *x)
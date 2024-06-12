import numpy as np

# Create matrix A and vector b
A = [[4, 1, 2],
              [3, 5, 1],
              [1, 1, 3]]

b = [4, 7, 3]

n = len(A)

max_iterations = 1000

# Tolerance
tolerance1 = 1e-4
tolerance2 = 1e-6

# Initialize x
x = [0 for _ in range(n)]

def vector_dot_product(v1, v2):
    return sum(val1 * val2 for val1, val2 in zip(v1, v2))
def vector_norm(v):
    return sum(val ** 2 for val in v) ** 0.5
def vector_subtraction(v1, v2):
    return [val1 - val2 for val1, val2 in zip(v1, v2)]

for i in range(max_iterations):
    x_new = [0 for _ in range(n)]
    for j in range(n):
        x_new[j] = (b[j] - vector_dot_product(A[j], x) + A[j][j] * x[j]) / A[j][j]
    error = vector_norm(vector_subtraction(x_new,x))
    x = x_new
    
    if error < tolerance1:
        print(f"Error less than 10^-4 after {i+1} iterations.")
        break
    elif error < tolerance2:
        print(f"Error less than 10^-6 after {i+1} iterations.")
        break
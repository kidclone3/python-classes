import numpy as np
import time
from utils import time_it
from pprint import pprint
from typing import List
from copy import deepcopy

def vector_norm(v):
    return sum(val ** 2 for val in v) ** 0.5

def vector_scalar_division(v, scalar):
    return [val / scalar for val in v]

def vector_dot_product(v1, v2):
    return sum(val1 * val2 for val1, val2 in zip(v1, v2))

def vector_subtraction(v1, v2):
    return [val1 - val2 for val1, val2 in zip(v1, v2)]

def vector_scalar_multiply(v, scalar):
    return [val * scalar for val in v]

def update_matrix(matrix, values, col):
    for i in range(len(matrix)):
        matrix[i][col] = values[i]
    return matrix

# Define the Gram-Schmidt process for QR decomposition
@time_it
def qr_decomposition(A:List[List[float]]):
    m,n= len(A), len(A[0])
    A= deepcopy(A)
    Q= [[0 for _ in range(n)] for _ in range(m)]
    R= [[0 for _ in range(n)] for _ in range(n)]

    for k in range(n):
        R[k][k] = vector_norm([A[i][k] for i in range(m)])
        Q = update_matrix(Q, vector_scalar_division([A[i][k] for i in range(m)], R[k][k]), k)
        for j in range(k + 1, n):
            R[k][j] = vector_dot_product(Q[k], [A[i][j] for i in range(m)])
            A = update_matrix(A, vector_subtraction([A[i][j] for i in range(m)], vector_scalar_multiply(Q[k], R[k][j])), j)

    return Q, R

if __name__ == "__main__":
    # Create matrix A and vector b (modify the data of A and b as needed).
    A = np.array([
        [12, -51, 4],
        [6, 167, -68],
        [-4, 24, -41]
    ])

    b = np.array([1, 2, 3])


    start = time.time()
    # QR decomposition
    Q, R = np.linalg.qr(A)
    print(f"Time elapsed: {time.time() - start}s")
    print("\nQ:")
    pprint(Q)
    print("\nR:")
    pprint(R)

    Q1, R1 = qr_decomposition(A.tolist())
    print("\nQ1:")
    pprint(Q1)
    print("\nR1:")
    pprint(R1)


    # Solve the equation Ax = b by solving the equation R*x = Q^T*b.
    x = np.linalg.solve(R, np.dot(Q.T, b))

    #  Calculate the error
    computed_b = np.dot(A, x)
    error = np.linalg.norm(computed_b - b)

    # Evaluate the error with magnitudes smaller than 10^-4 and 10^-6.
    tolerance1 = 1e-4
    tolerance2 = 1e-6

    if error < tolerance2:
        print("Error smaller than 10^-6.")
    elif error < tolerance1:
        print("Error smaller than 10^-4.")
    else:
        print(f"Error {error=}")

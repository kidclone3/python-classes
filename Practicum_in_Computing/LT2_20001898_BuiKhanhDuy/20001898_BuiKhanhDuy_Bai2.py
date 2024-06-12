import numpy as np
import time
from scipy.linalg import inv, eig
from utils import time_it
from pprint import pprint



@time_it
def use_library(matrix_A, matrix_B):
    matrix_sum = matrix_A + matrix_B
    print("\nMatrix Sum (A + B):")
    print(matrix_sum)

    matrix_product = np.dot(matrix_A, matrix_B)
    print("\nMatrix Product (AB):")
    print(matrix_product)

    # Matrix transpose
    matrix_transpose = np.transpose(matrix_A)
    print("\nMatrix Transpose (A^T):")
    print(matrix_transpose)

    # Inverse matrix using scipy.linalg.inv
    matrix_inverse = inv(matrix_A)
    print("\nMatrix Inverse (A^-1) using library:")
    print(matrix_inverse)

    # Eigenvalues and eigenvectors using scipy.linalg.eig
    eigenvalues, eigenvectors = eig(matrix_A) # type: ignore
    print("\nEigenvalues of A:")
    print(eigenvalues)
    print("\nEigenvectors of A:")
    print(eigenvectors)

@time_it
def without_library(matrix_A, matrix_B):
    def addition(matrix_A, matrix_B):
        if len(matrix_A) != len(matrix_B) or len(matrix_A[0]) != len(matrix_B[0]):
            raise ValueError("Matrix dimensions must match for addition.")
        result = []
        for i in range(len(matrix_A)):
            row = []
            for j in range(len(matrix_A[0])):
                row.append(matrix_A[i][j] + matrix_B[i][j])
            result.append(row)
        return result

    def multiplication(matrix_A, matrix_B):
        if len(matrix_A[0]) != len(matrix_B):
            raise ValueError("Number of columns in matrix_A must match number of rows in matrix_B.")
        
        result = []
        for i in range(len(matrix_A)):
            row = []
            for j in range(len(matrix_B[0])):
                sum = 0
                for k in range(len(matrix_B)):
                    sum += matrix_A[i][k] * matrix_B[k][j]
                row.append(sum)
            result.append(row)
        return result
    def transpose(matrix_A):
        result = [[matrix_A[j][i] for j in range(len(matrix_A))] for i in range(len(matrix_A[0]))]
        return result

    def inverse(matrix_A):
        n = len(matrix_A)
        identity = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        augmented_matrix = [row + identity[i] for i, row in enumerate(matrix_A)]

        # Forward elimination
        for i in range(n):
            # Find the pivot row
            max_row = max(range(i, n), key=lambda k: abs(augmented_matrix[k][i]))

            # Swap the current row with the pivot row
            augmented_matrix[i], augmented_matrix[max_row] = augmented_matrix[max_row], augmented_matrix[i]

            pivot = augmented_matrix[i][i]
            if pivot == 0:
                raise ValueError("Matrix is singular and cannot be inverted.")

            # Normalize the current row
            for j in range(i, 2 * n):
                augmented_matrix[i][j] /= pivot

            # Eliminate other rows
            for j in range(n):
                if j != i:
                    factor = augmented_matrix[j][i]
                    for k in range(i, 2 * n):
                        augmented_matrix[j][k] -= factor * augmented_matrix[i][k]

        # Extract the inverse matrix
        inverse_matrix = [row[n:] for row in augmented_matrix]

        return inverse_matrix

    matrix_sum = addition(matrix_A, matrix_B)
    print("\nMatrix Sum (A + B):")
    pprint(matrix_sum)

    matrix_product = multiplication(matrix_A, matrix_B)
    print("\nMatrix Product (AB):")
    pprint(matrix_product)

    # Matrix transpose
    matrix_transpose = transpose(matrix_A)
    print("\nMatrix Transpose (A^T):")
    pprint(matrix_transpose)

    # Inverse matrix 
    matrix_inverse = inverse(matrix_A)
    print("\nMatrix Inverse (A^-1):")
    pprint(matrix_inverse)

if __name__ == "__main__":
    # Generate two random matrices
    matrix_size = 3
    matrix_A = np.random.rand(matrix_size, matrix_size)
    matrix_B = np.random.rand(matrix_size, matrix_size)

    print("Matrix A:")
    print(matrix_A)

    print("\nMatrix B:")
    print(matrix_B)
    use_library(matrix_A, matrix_B)
    without_library(matrix_A.tolist(), matrix_B.tolist())
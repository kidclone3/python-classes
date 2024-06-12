import numpy as np
from utils import time_it

@time_it
def check_linearly_independent(matrix):
    # Using numpy.linalg.matrix_rank
    rank = np.linalg.matrix_rank(matrix)

    print(f"{rank=}")
    if rank == matrix.shape[0]:
        print("This vectors are linearly independent.")
    else:
        print("This vectors are linearly dependent.")

    dimension = matrix.shape[1]
    print(f"The dimension of this vector space. {dimension}.")
    print("\n------------------\n")

@time_it
def is_linearly_independent(matrix):
    # Using Gauss Elimination, without library
    def gauss_elimination(matrix):
        for col in range(len(matrix[0])):
            for row in range(col + 1, len(matrix)):
                factor = -matrix[row][col] / (matrix[col][col] if matrix[col][col] != 0 else 1)
                for i in range(col, len(matrix[0])):
                    matrix[row][i] += factor * matrix[col][i]

    copy_matrix = [list(row) for row in matrix]
    gauss_elimination(copy_matrix)
    # Kiểm tra rank của ma trận
    rank = sum(1 for row in copy_matrix if any(val != 0 for val in row))

    return rank == len(matrix[0])

if __name__ == "__main__":
    # Tạo các vector đầu vào
    matrix = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    print(is_linearly_independent(matrix.tolist()))
    check_linearly_independent(matrix)

    matrix2 = np.array([
        [1, 2, 3],
        [2, 4, 6],
        [3, 6, 9]
    ])
    print(is_linearly_independent(matrix2.tolist()))
    check_linearly_independent(matrix2)

    matrix3 = np.array([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ])

    print(is_linearly_independent(matrix3.tolist()))
    check_linearly_independent(matrix3)
    
    """
    Conclusion: Library is faster than my implementation, approximately 10 times.
    """
import numpy as np
import time
import matplotlib.pyplot as plt

# Function for compact SVD decomposition of matrix A.
def compact_svd(A):
    U, S, VT = np.linalg.svd(A, full_matrices=False)
    return U, S, VT

# Function for full SVD decomposition of matrix A.
def full_svd(A):
    U, S, VT = np.linalg.svd(A, full_matrices=True)
    return U, S, VT

# Test function with small matrix
def test_small_matrix():
    A = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
    
    U1, S1, VT1 = compact_svd(A)
    U2, S2, VT2 = full_svd(A)
    
    print("Compact SVD:")
    print("U1 =", U1)
    print("S1 =", S1)
    print("VT1 =", VT1)
    
    print("\nFull SVD:")
    print("U2 =", U2)
    print("S2 =", S2)
    print("VT2 =", VT2)

# Test function with large matrix
def test_large_matrix(matrix_col, matrix_row):
    A = np.random.rand(matrix_col, matrix_row)
    
    start_time = time.time()
    compact_svd(A)
    elapsed_time = time.time() - start_time
    
    return elapsed_time

# Hàm để vẽ biểu đồ thể hiện sự phụ thuộc của thời gian vào kích thước dữ liệu
def plot_time_vs_size():
    matrix_rows = [_ for _ in range(10, 10000, 10)]
    times = []
    
    for size in matrix_rows:
        elapsed_time = test_large_matrix(size, 3)
        times.append(elapsed_time)
    
    plt.plot(matrix_rows, times)
    plt.xlabel('Size of matrix (number of rows)')
    plt.ylabel('Time (s)')
    plt.title('The dependency of time on the data size.')
    plt.show()


if __name__ == "__main__":
    test_small_matrix()

    plot_time_vs_size()

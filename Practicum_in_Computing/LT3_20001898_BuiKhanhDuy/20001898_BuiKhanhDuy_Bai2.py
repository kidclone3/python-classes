import numpy as np
import time
import matplotlib.pyplot as plt

# Function to solve an unstable system of equations
def solve_singular_eqn(A, b):
    try:
        x = np.linalg.solve(A, b)
        return x
    except np.linalg.LinAlgError:
        return None

# Test function with a small-sized system of equations
def test_small_eqn():
    A = np.array([[2, 3],
                  [4, 6]])
    b = np.array([5, 12])
    
    x = solve_singular_eqn(A, b)
    
    if x is not None:
        print("Solutions of the system of equations")
        print(x)
    else:
        print("The system of equations has no solution")

# Test function with a big-sized system of equations
def test_large_eqn(matrix_size):
    A = np.random.rand(matrix_size, matrix_size)
    b = np.random.rand(matrix_size)
    
    start_time = time.time()
    solve_singular_eqn(A, b)
    elapsed_time = time.time() - start_time
    
    return elapsed_time

def plot_time_vs_size():
    matrix_sizes = [_ for _ in range(10, 1000, 10)]
    times = []
    
    for size in matrix_sizes:
        elapsed_time = test_large_eqn(size)
        times.append(elapsed_time)
    
    plt.plot(matrix_sizes, times)
    plt.xlabel('Size of matrix (number of rows)')
    plt.ylabel('Time (s)')
    plt.title('The dependency of time on the data size.')
    plt.show()

if __name__ == "__main__":
    test_small_eqn()

    plot_time_vs_size()

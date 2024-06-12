import numpy as np
import time
import matplotlib.pyplot as plt

# Function to find the least squares fit for a parabola
def least_squares_fit(X, y):
    A = np.column_stack((X**2, X, np.ones_like(X)))  # Create the matrix of features
    coeff = np.linalg.lstsq(A, y, rcond=None)[0]  # Find the coefficient vector
    
    return coeff

# Function to generate synthetic data
def generate_data(num_points):
    X = np.linspace(0, 10, num_points)
    y = 2 * X**2 + 3 * X + 1 + np.random.randn(num_points)  # Add noise
    
    return X, y

# Function to evaluate computation speed
def evaluate_computation_speed(data_sizes):
    times = []
    
    for size in data_sizes:
        X, y = generate_data(size)
        start_time = time.time()
        least_squares_fit(X, y)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)
    
    return times

# Function to plot a graph showing the time dependency on data size
def plot_time_vs_data_size():
    data_sizes = [10, 100, 1000, 10000, 100000]
    times = evaluate_computation_speed(data_sizes)
    
    plt.plot(data_sizes, times)
    plt.xlabel('Number of data points')
    plt.ylabel('Time (seconds)')
    plt.xscale('log')  # To make the x-axis scale logarithmic
    plt.title('Time Dependency on Data Size')
    plt.show()

if __name__ == "__main__":
    # Plot a graph showing the time dependency on data size
    plot_time_vs_data_size()

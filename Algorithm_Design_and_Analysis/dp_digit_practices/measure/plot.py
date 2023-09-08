# read data from file time1.txt and time2.txt, then draw plot of data
# each file contain 10 lines of numbers
import matplotlib.pyplot as plt
import numpy as np

def read_data(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        data = []
        for line in lines:
            data.append(int(line))
        return data
    
def draw_plot(data1, data2):
    x = np.arange(1, 11)
    plt.plot(x, data1, label='iterative')
    plt.plot(x, data2, label='recursive')
    plt.xlabel('n')
    plt.ylabel('time (ms)')
    plt.title('Running time of DP algorithm')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    data1 = read_data('time1.txt')
    data2 = read_data('time2.txt')
    draw_plot(data1, data2)
    print(np.mean(data1))
    print(np.mean(data2))

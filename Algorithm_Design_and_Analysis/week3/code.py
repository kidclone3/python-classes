import random
import time
import matplotlib.pyplot as plt

def selection_sort(a):
    n = len(a)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]

# Sinh dãy số ngẫu nhiên với số lượng phần tử từ 10^1 đến 10^4
N = [10**i for i in range(1, 5)]
times = []

for n in N:
    a = [random.randint(0, 100) for _ in range(n)]
    start_time = time.time()
    selection_sort(a)
    end_time = time.time()
    times.append(end_time - start_time)

# Vẽ biểu đồ sự phụ thuộc thời gian vào kích thước n
plt.plot(N, times)
plt.xlabel('Size of array')
plt.ylabel('Time (s)')
plt.xscale('log')
plt.show()
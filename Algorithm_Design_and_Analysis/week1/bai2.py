import time
import heapq
import sys
sys.setrecursionlimit(1000000)
from gen import gen_array

def bubbleSort(a):
    b = a.copy()
    n = len(b)
    for i in range(n):
        for j in range(i):
            if b[i] < b[j]:
                b[i], b[j] = b[j], b[i]
    return b

def insertionSort(a):
    b = a.copy()
    n = len(b)
    for i in range(1, n):
        j = i
        while j > 0 and b[j] < b[j - 1]:
            b[j], b[j - 1] = b[j - 1], b[j]
            j -= 1
    return b

def selectionSort(a):
    b = a.copy()
    n = len(b)
    for i in range(n):
        minIndex = i
        for j in range(i + 1, n):
            if b[j] < b[minIndex]:
                minIndex = j
        b[i], b[minIndex] = b[minIndex], b[i]
    return b

def quickSort(a):
    b = a.copy()
    n = len(b)
    if n <= 1:
        return b
    pivot = b[0]
    left = []
    right = []
    for i in range(1, n):
        if b[i] < pivot:
            left.append(b[i])
        else:
            right.append(b[i])
    return quickSort(left) + [pivot] + quickSort(right)

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def mergeSort(a):
    b = a.copy()
    n = len(b)
    if n <= 1:
        return b
    mid = n // 2
    left = b[:mid]
    right = b[mid:]
    return merge(mergeSort(left), mergeSort(right))

def heapSort(a):
    b = a.copy()
    n = len(b)
    heapq.heapify(b)
    return [heapq.heappop(b) for i in range(n)]

def measureTime(N, a, func):
    measure_result = []
    for i in range(N):
        start = time.process_time()
        func(a[i])
        end = time.process_time()
        measure_result.append(end - start)
    return measure_result

if __name__ == "__main__":
    N = 6
    # generate array:
    a = []
    for i in range(N):
        gen_array(i)
        a.append([int(x) for x in open(f"input_n_{i}.txt").read().split()])

    measureResult = dict()
    measureResult["bubbleSort"]= measureTime(4, a, bubbleSort)
    measureResult["insertionSort"] = measureTime(4, a, insertionSort)
    measureResult["selectionSort"] = measureTime(4, a, selectionSort)

    measureResult["quickSort"] = measureTime(N, a, quickSort)
    measureResult["mergeSort"] =measureTime(N, a, mergeSort)
    measureResult["heapSort"] = measureTime(N, a, heapSort)
    measureResult["builtinSort"] = measureTime(N, a, sorted)

    labels = ["1^0", "1^1", "1^2", "1^3", "1^4", "1^5"]
        
    format_label = "{:<15}" + "{:>10}" * (len(labels))
    with open("output2.txt", "w") as f:
        print(format_label.format("", *labels))
        print(format_label.format("", *labels), file=f)
        for func, row in measureResult.items():
            print("{:<15}".format(func), end = "")
            print("{:<15}".format(func), end = "", file=f)
            print(*["{:10.5f}".format(x) for x in row])
            print(*["{:10.5f}".format(x) for x in row], file=f)


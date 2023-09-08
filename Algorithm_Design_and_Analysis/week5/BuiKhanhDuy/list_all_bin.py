def binary_list(n):
    for i in range(1<<n):
        print(bin(i)[2:].zfill(n))
binary_list(3)
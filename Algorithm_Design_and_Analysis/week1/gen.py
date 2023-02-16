import random

def gen_array(n):
    with open(f"input_n_{n}.txt", "w") as f:
        n = 10**n
        # print(n, file=f)
        a = [random.randint(0, 1000) for i in range(n)]
        print(*a, file=f)
import random

t = 10
mx = 2**31
mxK = 81
print(t)
for i in range(t):
    l = random.randint(1, mx)
    r = random.randint(l, mx)
    k = random.randint(1, mxK)
    print(l, r, k)

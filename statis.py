import math


a = []
with open("in2", "r+") as f:
    for i in f.readlines():
        for j in i.split():
            a.append(int(j))
        # a.append(int(f.readline()))
# print(a)
n = len(a)
xx = sum(a)/len(a)
dy = math.sqrt(sum([(x - xx)**2 for x in a]) / (n-1))
print(a)
print(xx)
print(dy)

epsilon = 1.96 * dy/math.sqrt(dy)
print(epsilon)
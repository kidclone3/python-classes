xi = [-2, 1, 4, -1, 3, -4]
yi = [-1, 2, 59, 4, 24, -53]
# xy = zip(xi, yi)
# xy = sorted(list(xy), key = lambda x:x[0])
# xi = [_[0] for _ in xy]
# yi = [_[1] for _ in xy]
print(yi)
n = 6
y = [[0]*n for _ in range(6)]
for i in range(n):
    y[i][0] = yi[i]
for i in range(1, n):
    for j in range(1, i+1):
        y[i][j] = (y[i][j-1] - y[j-1][j-1]) / (xi[i] - xi[j-1])
for i in range(n):
    for j in range(n):
        print(y[i][j], end = " ")
    print()

xx = 10
P = [0]*n
P[0] = y[n-1][n-1]
for i in range(1, n):
    P[i] = (xx - xi[n-i+1])*P[i-1]
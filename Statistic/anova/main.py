N = 4
f = open("input.txt", "r")
n = list()
for t in range(N):
    tmp = [int(_) for _ in f.readline().split()]
    n.append(tmp)
print(n)

xx = [0 for i in range(N)]
for t in range(N):
    xx[t] = sum(n[t])/len(n[t])

NN = sum(len(i) for i in n)
x_to = sum([sum(i) for i in n])/NN

print("xx", xx)
print("x_to", x_to)

SS_F = 0
for i in range(N):
    SS_F = SS_F + len(n[i])*(xx[i]-x_to)**2
print("SS_F", SS_F)

SS_E = 0
for t in range(N):
    for i in n[t]:
        SS_E = SS_E + (i - xx[t])**2
print("SS_E", SS_E)

k = 4
MS_F = SS_F/(k-1)
MS_E = SS_E/(NN-k)

F_0 = MS_F/MS_E

print("F_0", F_0)
ans = ['S', ' O', ' R', ' T', ' I', ' N', ' G']
ans = [_.strip() for _ in ans]
for i in range(len(ans)-1):
    for j in range(i+1, len(ans)):
        if (ans[i] > ans[j]):
            print("i=", i, "j=", j, end=" => ")
            ans[i], ans[j] = ans[j], ans[i]
            print(ans)
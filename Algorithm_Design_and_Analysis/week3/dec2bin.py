def dec2bin(x):
    if x == 0:
        return str(0)
    if x == 1:
        return str(1)
    ans = dec2bin(x//2)
    return ans + str(1) if x % 2 == 1 else ans + str(0)
print(dec2bin(20))
    
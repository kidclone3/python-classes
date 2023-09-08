def phantich(x, n):
    if x > n:
        if n != 1: return [n]
        else: return []
    
    else:
        if n % x == 0:
            while n % x == 0:
                n //= x
            return [x] + phantich(x+1, n)
        else:
            return phantich(x+1, n)
print(phantich(2, 20794))
        
def solve_it(n,x):
    count = 0

    u = math.ceil(x/3)
    while u<=n and u<=x-3:
        v = (x-u)//2 + 1
        while v < (x-u):
            w = (x-u) - v
            if u > v > w:
                count +=1
            v+=1
        u+=1
    return count
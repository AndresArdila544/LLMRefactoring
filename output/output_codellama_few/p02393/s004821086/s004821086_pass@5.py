def get_sorted(a,b,c):
    if a > b:
        tmp = a
        a = b
        b = tmp
    if b > c:
        tmp = b
        b = c
        c = tmp
    return a,b,c

print(*get_sorted(map(int,input().split())),sep=' ')
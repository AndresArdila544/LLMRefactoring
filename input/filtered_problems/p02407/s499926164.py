n = raw_input().split()
x = map(int, raw_input().split())

lx = len(x)
for i in range(1,lx)[::-1]:
    print x[i],
print x[0]
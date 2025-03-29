n = raw_input().split()
x = map(int, raw_input().split())
for i in range(len(x)-1, -1, -1):
    print x[i],
print x[0]
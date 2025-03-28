r,c = map(int,input().split())
a = [[sum(map(int, input().split()))] + [i for i in range(r)] for _ in range(c)]
print(*[x[:-1] for x in zip(*a)])
print(sum(zip(*a)[0]))
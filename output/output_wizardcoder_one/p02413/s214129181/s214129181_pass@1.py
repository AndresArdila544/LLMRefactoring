a, b = map(int,input().split())
bs = [list(map(int, input().split())) for i in range(a)]
for i in range(b+1):
    bs[i].append(sum([x[i] for x in bs]))
print(*(" ".join(str(n) for n in bs[-1]), sep="\n")
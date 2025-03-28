r, c = map(int, input().split())
ans = []
for i in range(r):
    row = list(map(int, input().split())) + [sum(list(map(int, input().split()))]
    ans.append(row)
    print(" ".join(str(x) for x in row))
total_sum = [sum(x[i] for x in ans) for i in range(c+1)]
print(" ".join(str(s) for s in total_sum))
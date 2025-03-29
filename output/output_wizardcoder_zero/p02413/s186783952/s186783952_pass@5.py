r,c=map(int,input().split())
a = []
for i in range(r): a.append([sum(list(map(int, input().split()))]+[sum(a[i])] for i in range(r)]); print(*zip(*a)[::-1][c], sum(zip(*a)[::1][-1])
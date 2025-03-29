n = list(map(int, input().split()))
for i in range(len(n)-1, 0, -1): print(n[i], end='') if i > 0 else print(n[0])
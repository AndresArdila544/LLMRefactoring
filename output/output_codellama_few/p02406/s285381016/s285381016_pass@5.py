a = []
n = int(input())
for i in range (1, n + 1):
    if (i % 3) == 0:
        a.append(i)
        continue
    if '3' in str(i):
        a.append(i)
        continue
print(' ', end='')
print(*a)
n = int(input())
lst = []
for _ in range(n):
    lst.append([*map(int, input().split())] for _ in range(2))
print(*sorted([sum(i) for i in zip(*lst)]), sep=' ')
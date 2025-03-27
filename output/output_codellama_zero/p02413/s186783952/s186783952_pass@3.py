r, c = map(int, input().split())
a = [[sum(list(map(int, input().split())))]]
for _ in range(c-1): a.append([sum(map(int, input().split()))])
print(*a[::-1], sep=' ')
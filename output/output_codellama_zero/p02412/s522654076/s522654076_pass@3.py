a, b = map(int, input().split())
while a != 0 or b != 0:
    c = sum([1 for i in range(a + 1) for j in range(i + 1, a + 1) for k in range(j + 1, a + 1) if i + j + k == b])
    a, b = map(int, input().split())
    print(c)
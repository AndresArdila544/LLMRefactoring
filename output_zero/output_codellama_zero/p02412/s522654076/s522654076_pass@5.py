a, b = map(int, input().split())
while a != 0 or b != 0:
    c = sum(i + j + k == b for i in range(1, a + 1) for j in range(i + 1, a + 1) for k in range(j + 1, a + 1))
    a, b = map(int, input().split())
    print(c)
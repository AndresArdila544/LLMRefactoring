n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
b = [int(input()) for i in range(m)]
for row in a:
    print(sum(x*y for x, y in zip(b,row))
n = int(input())
for m in 'SHDC':
    for n in range(1, 13+1):
        if (m, n) not in [(x[0], x[1]) for x in [list(map(int, input().split())) for _ in range(n)]]:
            print(m, n)
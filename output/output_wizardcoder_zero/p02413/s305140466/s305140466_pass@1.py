n, r = map(int, input().split())
last_list = [0] * r
for _ in range(n):
    x = list(map(int, input().strip().split()))
    for i in range(r):
        last_list[i] += x[i]
        print(x[i], end=" ")
    print(sum(last_list), *last_list)
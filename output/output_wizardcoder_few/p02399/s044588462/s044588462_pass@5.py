Refactored version:
n, m = map(int, input().split())
a_list = list(map(int, input().split()))[:m]
b_list = [list(map(int, input().split()) for _ in range(m)]
for i in range(n):
    d = a_list[i] // b_list[0][i]
    r = a_list[i] % b_list[0][i]
    f = a_list[i]/b_list[0][i]
    print(*[str(d), str(r), str(f)], sep=' ')
c, r = map(int, input().split())
last_list = [0] * r
for _ in range(c):
    n = 0
    x = input()
    sum_list = list(map(int, x.split()))
    for i in range(r):
        last_list[i] += sum_list[i]
        n += sum_list[i]
    print(x, end = " ")
    print(n)

sum = 0   
for a in last_list:
    sum += a
print(*last_list, sum)
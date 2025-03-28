n = int(input())
min_num, max_num, sum_num = 1000000, -100000, 0
for i in range(n):
    num = int(input().split()[i])
    min_num = min(num, min_num)
    max_num = max(num, max_num)
    sum_num += num
print(min_num, max_num, sum_num)
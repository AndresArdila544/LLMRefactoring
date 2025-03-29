lst1 = []
lst2 = []
for _ in range(n):
    lst1.append([int(x) for x in input().split()])
bi_list = [int(input()) for _ in range(m)]
for i in range(n):
    row_sum = sum(x[j] * y for j, y in enumerate(bi_list))
    print(row_sum)
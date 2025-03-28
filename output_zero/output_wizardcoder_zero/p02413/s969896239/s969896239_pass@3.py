nums = [int(x) for x in input().split()]
table = []
for i in range(nums[0]):
    table.append([sum(map(int, input().split()), int])
for j in range(nums[1]+1):
    print(*table[i][j], end=' ') if j < nums[1] else print(table[i][-1])
nums = list(map(int, input().split()))
table = []
for i in range(nums[0]):
    table.append(list(map(int, input().split()) + [sum(table[i])])
for i in range(nums[0]+1):
    for j in range(nums[1]+1):
        print(table[i][j], end=' ') if j < nums[1] else print(table[i][j])
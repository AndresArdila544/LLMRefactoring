```
nums = list(map(int, input().split()))
table = []
for i in range(nums[0]):
    table.append(list(map(int, input().split())))
    table[i].append(sum(table[i][:]))
for i in range(1, nums[0]+1):
    for j in range(1, nums[1]+1):
        print(table[i][j], end = ' ')
        if j == nums[1]:
            print()
```
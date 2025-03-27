nums = list(map(int, input().split()))
table = []
for i in range(nums[0]):
    table.append([sum(map(int, input().split()))])
for i in range(nums[1]+1):
    t = 0
    for j in range(nums[0]):
        t += table[j][i]
    table[nums[0]].append(t)
for i in range(nums[0]+1):
    print(*table[i], sep=' ')
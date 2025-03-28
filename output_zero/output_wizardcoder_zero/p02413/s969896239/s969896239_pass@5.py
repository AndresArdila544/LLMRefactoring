nums = list(map(int, input().split()))
for i in range(nums[0]):
    table += [list(map(int, input().split())) + [sum(table[i])] if i < nums[1] else []]
print(*[row[:-1] + [row[-1]] for row in table[:nums[0]+1]])
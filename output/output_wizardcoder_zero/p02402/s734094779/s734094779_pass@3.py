n = int(input())
nums = list(map(int, input().split()))
ma, mi, su = nums[0], nums[0], 0

for v in range(1, n):
    if nums[v] > ma:
        ma = nums[v]
    elif nums[v] < mi:
        mi = nums[v]
    su += nums[v]
print(mi, ma, su)
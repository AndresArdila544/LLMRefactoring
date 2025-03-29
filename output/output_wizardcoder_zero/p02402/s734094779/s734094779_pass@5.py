n = int(input())
nums = list(map(int, input().split()))
mi, ma = nums[0], nums[0]
su = sum(nums)
for i in range(1, n):
    if nums[i] > ma:
        ma = nums[i]
    elif nums[i] < mi:
        mi = nums[i]
print(mi, ma, su)
n = int(input())
nums = input().split()
su = 0
ma = -1000000
mi = 1000000

for v in range(n):
    num = int(nums[v])
    if num > ma:
        ma = num
    if num < mi:
        mi = num
    su += num

print(mi, ma, su)

n = int(input())
nums = input().split()
ma = mi = su = 0
for num in map(int, nums):
    ma = max(ma, num)
    mi = min(mi, num)
    su += num
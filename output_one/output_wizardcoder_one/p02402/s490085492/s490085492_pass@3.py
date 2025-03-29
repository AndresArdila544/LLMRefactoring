import sys
n = int(input().split())
nums = list(map(int, input().strip().split()))
print(" ".join([str(min(nums)), max(nums), sum(nums) // len(nums)]))
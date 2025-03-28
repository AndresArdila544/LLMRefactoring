Here is a refactored version of the original program:

nums = input().split()
if all(int(i) < int(j) for i, j in zip(nums, nums[1:])):
    print('Yes')
else:
    print('No')
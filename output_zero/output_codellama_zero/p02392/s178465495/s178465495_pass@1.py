nums = input().split()
if all(i<j for i,j in zip(nums, nums[1:])):
    print('Yes')
else:
    print('No')
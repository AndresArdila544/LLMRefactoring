Here is a refactored version of your original Python program:

nums = input().split()
a = int(nums[0])
b = int(nums[1])
c = int(nums[2])
if b < a < c or b < c < a:
    print('No')
else:
    print('Yes')
nums = list(map(int, input().split()))
if all(nums[i] < nums[(i+1)%len(nums)] for i in range(len(nums)-1)):
    print('Yes')
else:
    print('No')
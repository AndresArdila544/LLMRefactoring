n = int(input())
nums = []
for i in range(1, n + 1):
    if i % 3 == 0 or '3' in str(i):
        nums.append(str(i))
print(" ".join(nums))
Here is the refactored version of the code:
a = int(input())
nums = list(map(int, input().split()))
print(*(min(nums), max(nums), sum(nums)), sep=", ")
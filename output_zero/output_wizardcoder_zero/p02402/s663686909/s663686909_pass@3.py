nums = [int(input())] + list(map(int, input().split()))
print(*[min(nums), max(nums), sum(nums)]
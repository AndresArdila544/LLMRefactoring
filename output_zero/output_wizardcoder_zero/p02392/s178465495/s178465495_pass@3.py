nums = input().split()
a, b, c = map(int, nums)
if a < min(b, c):
    print('Yes') if a < b else print('No')
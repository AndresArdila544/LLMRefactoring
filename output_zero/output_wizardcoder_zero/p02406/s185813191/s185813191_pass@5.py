n = int(input())
for i in range(1, n+1):
    if not (i % 3) and str(i).__contains__('3'):
        print('', i, end='')
print()
# The original code checks for divisibility by 3 and the string '3' in the integer representation of i. Here we use `not` to check if `i` is not divisible by 3 and the `__contains__()` method to check if '3' is present in the string representation of i. Using string concatenation instead of the `end=''` parameter, which is more efficient as well.
Here is the refactored version of the code:
a, b = map(int, raw_input().split())
print a / b, a % b, '%.8f' % (1.*a / b)
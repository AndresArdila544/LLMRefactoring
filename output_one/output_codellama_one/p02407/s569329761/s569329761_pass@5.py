Here is a refactored version of the original code:

n = int(input())
an = input().split()
out_c1 = ' '.join(reversed(an))[1:]
print(out_c1)
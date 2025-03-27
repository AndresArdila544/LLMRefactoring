Here is a refactored version of the program with fewer lines and improved readability:

n = int(input())
an = input().split()
out_c1 = ' '.join(reversed(an))
print(out_c1[1:])
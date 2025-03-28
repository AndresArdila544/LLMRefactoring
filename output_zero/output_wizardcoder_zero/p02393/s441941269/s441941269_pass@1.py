a, b, c = map(int, input().split())
s = min(a, b) # find the minimum of a and b
g = max(a, b) # find the maximum of a and b
print(' '.join([str(x) for x in sorted((c, s, g))]) # print in ascending order using list comprehension
Here is a refactored version of the original Python program:
a, b, c = map(int, raw_input().split())
lst = []
for i in range(a, b + 1):
    if c % i == 0: lst.append(i)
print len(lst)
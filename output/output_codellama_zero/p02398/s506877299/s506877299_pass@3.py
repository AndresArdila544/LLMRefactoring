Here's the refactored version of your original program:

a, b, c = map(int, raw_input().split())
lst = [i for i in range(a, b+1) if c % i == 0]
print len(lst)
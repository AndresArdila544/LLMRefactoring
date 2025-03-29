from sys import stdin
w = str(input()).lower()
t = stdin.read().split()
print(sum([1 for i in t if w == i.lower()]))
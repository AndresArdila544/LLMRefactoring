Refactored version:
from sys import stdin;
w = str(input()).lower();
t = [x.lower() for x in stdin.read().split()];
print(len([1 for i in t if i == w]))
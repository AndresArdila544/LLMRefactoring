from sys import stdin
w = str(input()).lower()
print(len([i for i in (stdin.read().split()) if i == w]))
import sys
stdin = sys.stdin.read().lower()
w = str(input()).lower()
t = stdin.split()
counter = 0
for i in t:
    if i == w:
        counter += 1
print(counter)
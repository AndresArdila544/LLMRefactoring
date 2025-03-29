import sys

try:
    while True:
        list.append(input().lower())
except EOFError:
    pass

for c in "abcdefghijklmnopqrstuvwxyz":
    print(f"{c}: {list.count(c)}")
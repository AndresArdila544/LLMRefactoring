import sys

table = "abcdefghijklmnopqrstuvwxyz"
sentence1 = sys.stdin.read().lower()
for i in table:
    print(f'{i}: {sentence1.count(i)}')
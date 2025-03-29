import sys
s = input().lower()
print(*[f'{chr(i)}:{s.count(chr(i))}' for i in range(97, 123)])
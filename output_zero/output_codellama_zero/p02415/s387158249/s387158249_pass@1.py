import re

s1 = input()
s2 = re.sub(r'[a-z]', lambda c: chr(ord(c) - ord('a') + ord('A')), s1)
print(s2)
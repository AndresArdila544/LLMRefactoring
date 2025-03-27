Here is the refactored code:

s = input()
LOWER = "abcdefghijklmnopqrstuvwxyz"
trans = str.maketrans({c: c.upper() for c in LOWER})
print(s.translate(trans))
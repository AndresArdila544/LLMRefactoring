s = input()
LOWER = "abcdefghijklmnopqrstuvwxyz"
trans = {c: c.upper() for c in LOWER}
print(s.translate(str.maketrans(trans)))
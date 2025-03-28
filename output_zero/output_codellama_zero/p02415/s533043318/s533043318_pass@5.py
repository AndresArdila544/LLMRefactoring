Here is the refactored version:
s = input()
LOWER = "abcdefghijklmnopqrstuvwxyz"
trans = {i: str.upper(i) for i in LOWER}
trans.update({str.upper(i): i for i in LOWER})
print(s.translate(str.maketrans(trans)))
s = input()
LOWER = "abcdefghijklmnopqrstuvwxyz"
trans = {}
for i in range(len(LOWER)):
    trans[LOWER[i]] = str.upper(LOWER[i])
    trans[str.upper(LOWER[i])] = LOWER[i]
print(s.translate(str.maketrans(trans)))


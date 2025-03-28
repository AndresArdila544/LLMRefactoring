s = input()
transtable = str.maketrans(str.lower(LOWER) + LOWER, LOWER * 2)
print(s.translate(transtable))
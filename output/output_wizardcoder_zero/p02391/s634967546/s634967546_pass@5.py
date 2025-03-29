I = input()
a, b = map(int, I.split())
print("{0} {1} {2}".format("a < b" if a < b else "a > b" if a > b else "a == b", a, b)
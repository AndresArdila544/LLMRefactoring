w = input()
tmp = input()
while tmp != "END_OF_TEXT":
    s += tmp.lower().split()
    tmp = input()
print(s.count(w))
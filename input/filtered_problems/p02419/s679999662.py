w = input()

s = []
while True:
    tmp = input()
    if tmp == "END_OF_TEXT":
        break
    s += tmp.lower().split()

print(s.count(w))

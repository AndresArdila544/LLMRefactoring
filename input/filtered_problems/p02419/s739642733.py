w = input()
c = 0
while True:
    s = input()
    if s == "END_OF_TEXT":
        break
    c += s.lower().split().count(w)
print(c)


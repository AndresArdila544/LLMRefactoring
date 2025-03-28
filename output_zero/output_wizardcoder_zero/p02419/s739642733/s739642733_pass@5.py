w = input()
c = 0
while True:
    s = input()
    if s == "END_OF_TEXT":
        break
    c += len([word for word in s.lower().split() if word == w])
print(c)
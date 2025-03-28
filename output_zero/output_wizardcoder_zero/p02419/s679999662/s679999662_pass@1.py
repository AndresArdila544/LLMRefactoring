w = input()
s = []
while True:
    tmp = input().lower()
    if tmp == "END_OF_TEXT":
        break
    s += [word for word in tmp.split()]
print(sum([1 for word in s if word == w]))
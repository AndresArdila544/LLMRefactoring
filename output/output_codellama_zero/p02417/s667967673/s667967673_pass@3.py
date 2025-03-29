list = []
while True:
    try:
        list.append(input().lower())
    except EOFError:
        pass
w = ''.join(list)
for c in "abcdefghijklmnopqrstuvwxyz":
    print(c, ":", w.count(c))
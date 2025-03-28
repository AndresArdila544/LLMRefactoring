w = input()
t = []
while True:
    s = input()
    if s == "END_OF_TEXT":
        break
    t += list(s.split())
    cnt = 0
    for p in t:
        if w == p.lower():
            cnt += 1
print(cnt)
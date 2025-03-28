w = input()
t = []
while True:
    s = input()
    if s == "END_OF_TEXT":
        break
    t += list(s.split())
print(sum(1 for p in t if w.lower() == p.lower()))
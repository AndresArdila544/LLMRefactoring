w = input()
while True:
    s = input()
    if s == "END_OF_TEXT":
        break
    c += len(w in s.lower().split())
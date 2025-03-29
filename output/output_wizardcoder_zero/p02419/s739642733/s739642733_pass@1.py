w = input()
c = 0
while True:
    s = input().lower()
    if "end_of_text" in s:
        break
    c += s.split().count(w)
print(c)
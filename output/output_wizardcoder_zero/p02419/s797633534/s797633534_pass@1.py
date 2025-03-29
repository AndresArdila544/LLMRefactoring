w = input().lower()
count = 0
while True:
    t = input()
    if t == "END_OF_TEXT":
        break
    count += t.lower().split().count(w)
print(count)
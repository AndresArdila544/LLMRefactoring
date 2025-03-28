w = input().lower()
while True:
    t = input()
    if t == "END_OF_TEXT":
        break
    ans += t.lower().split().count(w)
print(ans)
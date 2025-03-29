Here is the refactored Python program:

w = input().lower()
for t in iter(lambda: input(), "END_OF_TEXT"):
    ans += t.lower().split().count(w)
print(ans)
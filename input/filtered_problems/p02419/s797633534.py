w = input().lower()
ans = 0
while 1:
  t = input()
  if t == "END_OF_TEXT":
    break
  ans += t.lower().split().count(w)
print(ans)

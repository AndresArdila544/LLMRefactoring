w = input()
t = []
while True:
  s = input()
  if s == "END_OF_TEXT":
    break
  t += list(s.split())
cnt = sum([1 for p in t if w.lower() == p.lower()])
print(cnt)
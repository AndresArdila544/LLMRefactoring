w = input()
t = []
while True:
  s = input().lower()
  if s == "end_of_text":
    break
  t += list(s)
print(t.count(w))
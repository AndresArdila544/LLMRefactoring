w = input()
t = []
while True:
  s = input()
  if s == "END_OF_TEXT":
    break
  t += list(s.split()) # list comprehension of list of words splitted by spaces

cnt = 0
for p in t: # iterate through all the words
  if w == p.lower():
    cnt += 1
  
print(cnt)
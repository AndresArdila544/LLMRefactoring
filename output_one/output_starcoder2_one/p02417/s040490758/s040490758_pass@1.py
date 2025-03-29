The original program: 
import string

a = {}
for c in string.ascii_lowercase:
    a[c] = 0
s = ""
while True:
    try:
        s += input()
    except EOFError:
        break
s = s.lower()
for i in range(len(s)):
    if not (s[i] in a):
        continue
    a[s[i]] += 1
for c,v in sorted(a.items(), key=lambda x:x[0]):
    print("%c : %d" % (c, v))
```
for c in input():
    s2 += chr((ord(c) - ord('a') + ord('A')) if ord('a') <= ord(c) <= ord('z') else (ord(c) - ord('A') + ord('a')))
print(s2)
```
```
# coding: utf-8!
s = input().rstrip().split(' ')
a, b = map(int, s)
print("a > b" if a > b else "a < b" if a < b else "a == b")
```
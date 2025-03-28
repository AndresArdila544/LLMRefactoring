```
I = input()
a, b = list(map(int, I.split()))
print("a" if a < b else "b" if a > b else "a == b") 
```
```python
for char in range(ord("a"), ord("z")+1):
    print(f"{chr(char)} : {s.lower().count(chr(char))}")
```
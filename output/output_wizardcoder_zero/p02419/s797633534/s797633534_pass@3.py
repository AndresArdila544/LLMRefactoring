```python
w = input().lower()
total_count = 0
while True:
    line = input()
    if line == "END_OF_TEXT":
        break
    else:
        total_count += line.lower().split().count(w)
print(total_count)
```
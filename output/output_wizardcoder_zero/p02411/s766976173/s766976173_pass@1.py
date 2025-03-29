```python
while True:
    m, f, r = map(int, input().split())
    if m != -1 and f != -1 and r != -1:
        x = max(0, m) + max(0, f)
        grade = 'A' if 80 <= x else 'F' if x < 65 else 'B' if 65 <= x < 50 else 'C' if 50 <= x and r >= 50 else 'D'
        print(grade)
    else:
        break
```
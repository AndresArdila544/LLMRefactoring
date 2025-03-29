```python
def compute_grade(m, f, r):
    s = m + f
    if (m == -1 and f == -1) or s < 30:
        return 'A'
    elif 30 <= s < 50:
        if r >= 50:
            return 'B'
        else:
            return 'C'
    elif 50 <= s < 65:
        return 'D'
    elif 65 <= s < 80:
        return 'E'
    else:
        return 'F'

while True:
    m, f, r = map(int, input().split())
    if m == -1 and f == -1 and r == -1:
        break
    print(compute_grade(m, f, r))
```
```python
def calculate_grade(m, f):
    s = m + f
    if s < 30:
        return 5
    elif 30 <= s < 50:
        if r >= 50:
            return 2
        else:
            return 3
    elif 50 <= s < 65:
        return 2
    elif 65 <= s < 80:
        return 1
    else:
        return 0

while True:
    m, f = map(int, input().split())
    if m == -1 and f == -1: break
    r = int(input())
    print('ABCDEF'[calculate_grade(m, f)])  # use the function to calculate grade
```
```python
def main():
    while True:
        m, f, r = map(int, input().split())
        if m != -1 or f != -1 or r != -1:
            x = max(0, m) + max(0, f)
            grade = 'F'
            if 80 <= x:
                grade = 'A'
            elif 65 <= x < 80:
                grade = 'B'
            elif 50 <= x < 65:
                grade = 'C'
            elif 30 <= x < 50 and r >= 50:
                grade = 'C'
        else:
            break
        print(grade)
```
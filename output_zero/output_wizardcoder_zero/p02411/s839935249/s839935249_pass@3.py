```python
def calculate_grades(m, f, r):
    if m < 0 or f < 0:
        return "F"
    elif m + f >= 80:
        return "A"
    elif m + f >= 65:
        return "B"
    elif m + f >= 50:
        if r >= 50:
            return "C"
        else:
            return "D"
    else:
        return "F"

def main():
    while True:
        m, f = map(int, input().split())
        if m == -1 and f == -1:
            break
        print(calculate_grades(m, f))

if __name__ == '__main__':
    main()
```
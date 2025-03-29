```python
def print_hashes(a, b):
    for i in range(a):
        k = b // 2
        if i % 2 == 0 and b % 2 == 0:
            print("#." * k)
        elif i % 2 != 0 and b % 2 != 0:
            print(".#" * k + ".")
    print()

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print_hashes(a, b)
```
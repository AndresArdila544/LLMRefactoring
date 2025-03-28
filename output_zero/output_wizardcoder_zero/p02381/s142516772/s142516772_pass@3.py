Here is a refactored version of the program using list comprehension for better readability and reducing lines:

```python
while True:
    n = int(input())
    if not n:
        break
    a = list(map(float, input().split()))
    print((sum([(i - sum(a) / n) ** 2 for i in a]) / n) ** 0.5)
```
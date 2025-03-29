```python
while True:
    n = list(map(int, input().split()))
    if sum(n) == 0: break
    print(" ".join(str(sorted(n)))
```

This code is refactored to remove the unnecessary "list" function and join method, as well as removing the unnecessary parentheses around the "sum" function. Additionally, I removed the space between the sorted() and (), which makes the code more concise.

```python
while True:
    n = map(int, input().split())
    if sum(n) == 0: break
    print(*sorted(n))
```
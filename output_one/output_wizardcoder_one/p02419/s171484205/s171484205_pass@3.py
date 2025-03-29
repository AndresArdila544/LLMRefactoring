```python
w = input().lower()
print(sum(map(lambda i: 1 if str(i).lower() == w else 0, stdin.readline().split()))
```
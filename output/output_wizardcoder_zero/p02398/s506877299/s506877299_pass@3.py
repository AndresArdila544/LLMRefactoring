```python
a, b = map(int, input().split())
lst = [x for x in range(a, b+1) if a%x == 0 or b%x == 0]
print(len(lst))
```
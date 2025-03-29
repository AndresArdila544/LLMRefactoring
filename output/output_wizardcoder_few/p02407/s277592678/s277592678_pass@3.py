```python
z = int(input())
a = list(map(int, input().split()))[::-1]
print(" ".join(str(i) for i in a))
```
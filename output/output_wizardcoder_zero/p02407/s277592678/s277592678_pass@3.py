```python
z = int(input())
a = list(map(int, input().split()))[::-1] # reverse the list using slicing
print(" ".join(map(str, a))
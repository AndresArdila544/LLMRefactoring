```python
a, b, c = map(int, input().split())
print((b-a+1) - (c // a))  # count will be (total number of numbers from a to b) minus (number of multiples of a that are less than or equal to c).
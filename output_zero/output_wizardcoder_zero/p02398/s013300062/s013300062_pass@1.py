```python
a, b, c = map(int, input().split())
s = sum([1 for i in range(a, b+1) if a % i == 0 or i % c == 0]) - 2
print(s)
```

The program uses list comprehension to create a new list of numbers from `a` to `b`, and then counts the number of elements that satisfy either the condition that they are divisible by `a` or by `c`. The `-2` at the end is to exclude the values of 0 and itself, since we don't want those in our count.
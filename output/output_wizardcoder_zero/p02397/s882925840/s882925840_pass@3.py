```python
while True:
    a = list(map(int, input().split()))
    if not all(a): # check if both elements of 'a' are non-zero and break out of loop when both are zero
        break
    min_a, max_a = sorted(a)
    print("{} {}".format(*min_a)) # use tuple unpacking to assign values to variables without need for if statements
```
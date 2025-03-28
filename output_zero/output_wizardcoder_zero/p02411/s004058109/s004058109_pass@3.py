Here is a refactored version of the code that reduces its complexity by using list comprehension to store input values and conditional statements instead of multiple if-else statements:
```python
while True:
    m, f, r = [int(i) for i in input().split()]
    if m == f == r == -1:
        break

    s = m + f
    
    if max(m,f,r) < 0 or s < 30:
        print('F')
    elif s >= 50 and min(m,f,r) < 50:
        print('D')
    elif s >= 65:
        print('B' if s < 80 else 'A')
```
This is a more concise version of the original code that uses list comprehension to store input values and simplifies the conditional statements using the `max` and `min` functions. The final line is now a single expression that evaluates the conditions in a cleaner way.
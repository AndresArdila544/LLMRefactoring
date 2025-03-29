```python
while True:
    a, op, b = map(str, input().split())
    c, d = int(a), int(b)
    print("{:.0f}".format({'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y}.get(op)(c, d)
           if op in {'+', '-', '*', '/'}
           else break)  # breaks loop when ? is input
``` 

```python
while True:
    a, op, b = map(str, input().split())
    c, d = int(a), int(b)
    if op in {'+', '-', '*', '/'}:
        print("{:.0f}".format({'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y}[op](c, d)
    else:
        break  # breaks loop when ? is input
``` 

# using dictionary comprehension to avoid repetitive if-else statements for +, -, and * operations. lambda function used to define the operation without using if-else blocks.
# print statement uses format specifier to output the result rounded off to 0 decimal places (integer value).
```python
while True:
    h, w = map(int, input().split())
    if h == 0:
        break
    for i in range(h):
        print("#" * w)
``` 

This code achieves the same functionality as the original one by using a single `for` loop to print `#` symbols for each row of input height and width values, without using the unnecessary nested loop.
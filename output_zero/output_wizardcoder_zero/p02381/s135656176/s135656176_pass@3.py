```python
import math

while True:
    n = int(input())
    if not n:  # Exit condition for loop when input is 0
        break
    s = [int(x) for x in input().split()]  # Convert list of integers to a list comprehension and store in variable `s`
    mean = sum(s)/len(s)
    std_dev = math.sqrt(sum([(ele-mean)**2 for ele in s])/len(s))
    print(std_dev)
```
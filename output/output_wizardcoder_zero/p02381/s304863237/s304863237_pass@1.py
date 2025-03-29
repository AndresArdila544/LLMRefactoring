```python
import math

def stddev(data):
    n = len(data)
    m = sum(data) / n
    return math.sqrt(sum((i - m) ** 2 for i in data) / n)

while True:
    try:
        n = int(input())
        if n == 0: break
        print(stddev(list(map(int, input().split())))
    except EOFError: 
        break
```

Explanation: 
- We define a function called `stddev` that takes in a list of numbers and calculates the standard deviation based on the formula `sqrt((x - mean)^2 / n)`. The function uses a generator expression to calculate the sum of squares, which is more concise than looping through all the data twice.
- We use a `try-except` block to catch the `EOFError` that signals when the user inputs 0 as the number of elements to calculate the standard deviation for. This block exits the while loop and ends the program gracefully if the input is invalid or no more inputs are given.
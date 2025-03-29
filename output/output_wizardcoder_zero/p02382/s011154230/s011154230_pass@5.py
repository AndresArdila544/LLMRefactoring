```python
from math import sqrt

def distance(A_lst, B_lst):
    return [(abs(a - b)) ** p for a, b in zip(A_lst, B_lst)]

print("{:.6f}".format(sqrt(sum(distance(map(int, input().split()))))) # distance of A and B when p=1
print("{:.6f}".format(sqrt(sum([(abs(a - b) ** 2 for a,b in zip(*[iter(map(int, input().split())]*2)])) ** 0.5)) # distance of A and B when p=2
print("{:.6f}".format(max(distance(map(int, input().split()))) # Chebyshev distance of A and B 
```

Explanation: We can use list comprehensions to reduce the amount of code and make the program more concise.
The `distance` function takes in two lists of integers as parameters. It returns a list of squared differences, which is then summed up to get the distance when p=1. When p=2 or 3, we use the formula `(x-y)**p`, where x and y are coordinates in the Cartesian plane, to calculate the distance. The `max` function returns the maximum value from this list of distances, which is the Chebyshev distance of A and B. In the last line, we call the `distance` function twice for each set of input values and print the result rounded to 6 decimal places. We use `input().split()` to split the input values by spaces and convert them to integers using `map(int, ...)`. The asterisk(*) unzips the resulting iterable into two lists, which are then zipped together with the `zip` function and fed as arguments to `distance`.
```python
while True:
    sides = list(map(int, input().split()))
    if not all(sides): #if sides are 0 break loop since they will trigger ValueError in print statement below
        break
    line = '#' * sides[1] + '\n'
    lines = line * sides[0]
    print(lines)
``` 

The code takes input for the number of rows and columns, then prints a pattern with # on top and bottom using the given numbers. This can be simplified using a while loop as shown above without needing to split or map strings. Also, checking if sides are non-zero allows us to break out of the loop when we receive two zeros.

```python
while True:
    try:
        rows, cols = list(map(int, input().split())) #get inputs and convert to ints as tuple
        if not all([rows, cols]: #check for any zero values in the input tuple
            break
        print('#' * cols + '\n' * rows) #prints the pattern with given dimensions
    except ValueError: #if user inputs non-integer values or empty strings break out of loop
        break
```
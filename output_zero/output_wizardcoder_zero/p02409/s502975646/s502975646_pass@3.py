One possible refactoring is to use a list comprehension for building initialization and a nested loop for printing the result. Here's an example:

```python
import sys

rows = 4
columns = 3
height = 10
buildings = [[[0] * height for j in range(columns)] for i in range(rows)]
informations = int(input())
for _ in range(informations):
    x, y, z, value = map(int, input().split())
    buildings[x - 1][y - 1][z - 1] += value

for row in buildings:
    for col in row:
        for floor in col:
            write(str(floor) + ' ')
        print()
    print('#' * (columns * height + columns - 1)
```
This code initializes the `buildings` list with zeros using a nested list comprehension, converts input values to integers and updates the values accordingly. It also prints each floor in the same order as before but with fewer lines of code. Finally, it prints `#` characters for each row to separate them visually.
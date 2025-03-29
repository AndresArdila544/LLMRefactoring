## Solution
```python
from functools import reduce
a = [[[0 for _ in range(10)] for j in range(3)] for i in range(4)] # declare 4-deep array with 3, 10-deep subarrays
for line in map(lambda x: tuple(map(int,x.split())), input().splitlines()):
    a[line[0]-1][line[1]-1][line[2]-1] += line[3] # access inner array by index and add value of 4th column from input line
for i in range(4):
    for j in range(3):
        for k in range(10):
            print(' '+str(a[i][j][k]), end='')
        print()
    if not (i==3): # don't print "####################" on last inner array access
        print('####################')
```
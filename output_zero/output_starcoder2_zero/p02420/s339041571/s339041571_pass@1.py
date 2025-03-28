Example Input:
5
2
3
4
5
10
9
8
7
6
-

Example Output:
cdefg
cbdegh
abcdfg
abdechg
abcdefg

import sys

while True:
    line = input()
    if line=='-':
        break
    for _ in range(int(input())):
        h = int(input())
        line = line[h:] + line[:h]
    print(line)
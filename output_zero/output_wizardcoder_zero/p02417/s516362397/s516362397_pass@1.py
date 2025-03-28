```python
import fileinput as fi

for line in fi.input():
    T = [0] * 26 # initialize the list with all zeroes
    for c in map(ord, line): # iterate over the line and convert to ASCII codes
        if 'A' <= chr(c) <= 'Z': 
            T[c-ord('A')] += 1
        elif 'a' <= chr(c) <= 'z':
            T[c-ord('a')] += 1
for i in range(26): # iterate over the list and print each character and its count
    print(chr(i+ord('a')), T[i]) 
```
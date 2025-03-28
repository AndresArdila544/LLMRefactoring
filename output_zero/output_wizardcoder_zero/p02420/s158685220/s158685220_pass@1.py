```python
import sys

letters = ''
m = 0
h = 0
for line in sys.stdin:
    if not letters and line == '-': break
    if not m: 
        letters = line.strip('\n')
    elif h == -1 or h == 0: 
        m = int(line)
    else: 
        h = int(line)
        if m > 1: 
            letters = letters[h:] + letters[:h]
            m -= 1
        print(letters) 
        p = 0
```
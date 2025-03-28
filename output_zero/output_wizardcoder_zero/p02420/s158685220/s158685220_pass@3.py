```python
import sys
letters = ""
for line in sys.stdin:
    if not letters and line == '-': break
    elif not letters:
        letters = line.strip('\n')
    elif m := int(line):
        h = int(input())
        letters = letters[h:] + letters[:h]
        if m > 1:
            m -= 1
        else:
            print(letters)
            letters = ""
```
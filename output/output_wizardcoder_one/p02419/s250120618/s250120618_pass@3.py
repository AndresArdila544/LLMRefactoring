```python
import math

raw_input = input()
texts = []
while raw_input != 'END_OF_TEXT':
    texts.append(raw_input)
    raw_input = input()
word = input().lower()
match_count = sum(1 for line in texts if word in line.split())
print(match_count)
```
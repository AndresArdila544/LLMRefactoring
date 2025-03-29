```python
import sys
table = "abcdefghijklmnopqrstuvwxyz"
sentence = input().lower()
for char in table:
    print(f"{char}: {sentence.count(char)}")
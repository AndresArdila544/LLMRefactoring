```python
import sys

d = {chr(i): 0 for i in range(97,123)} #create a dictionary with all letters as keys and initial value of 0
lines = [line.lower() for line in sys.stdin] #read lines and convert to lowercase
for char in ''.join(lines): #iterate through all characters in concatenated lines string
    if ord('a') <= ord(char) <= ord('z'): #check if character is a letter (97-1223)
        d[char] += 1 #increment count for that letter in dictionary
for key, value in sorted(d.items()): #iterate through sorted items of dictionary and print key:value pairs
    print(f'{key} : {value}')
```
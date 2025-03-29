```python
import sys

# Create an empty dictionary with keys for all lowercase letters of the alphabet and initialize their values to zero.
letters = {chr(i): 0 for i in range(97, 123)} 

for line in sys.stdin: # Iterate through each line of input (stdin is a file-like object that represents standard input) and convert all characters to lowercase.
    line = line.lower()
    for char in line:
        if ord(char) >= 97 and ord(char) <= 123: # If the character is a lowercase letter, increment its count in the dictionary.
            letters[char] += 1
for k, v in letters.items(): # Iterate through the items of the dictionary and print each key-value pair with f-strings for formatting.
    print(f'{k} : {v}')
```
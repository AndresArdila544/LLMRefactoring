```python
alphabet = 'abcdefghijklmnopqrstuvwxyz'
letter_counts = {letter: 0 for letter in alphabet}

for char in sys.stdin.read().lower():
    if char in letter_counts:
        letter_counts[char] += 1

for key, value in letter_counts.items():
    print(f'{key}: {value}')
```
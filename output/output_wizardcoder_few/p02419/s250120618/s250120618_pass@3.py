```python
texts = []
while True:
    raw_input = input().lower()
    if raw_input == 'end_of_text':
        break
    texts.append(raw_input)
match_count = sum(1 for line in texts for w in line.split() if w == word)
print(match_count)
```
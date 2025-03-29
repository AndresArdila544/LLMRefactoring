```python
if __name__ == '__main__':
    word = input().lower()
    texts = []
    while True:
        raw_input = input()
        if raw_input == 'END_OF_TEXT':
            break
        texts.append(raw_input)
    match_count = sum([1 for line in texts if word in line.lower()])
    print(match_count)
```
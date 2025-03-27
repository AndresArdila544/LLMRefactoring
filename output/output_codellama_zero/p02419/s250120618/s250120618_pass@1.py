Here is a refactored version of the original Python program:
```
if __name__ == '__main__':
    word = input().lower()
    texts = []
    while True:
        raw_input = input()
        if raw_input == 'END_OF_TEXT':
            break
        texts.append(raw_input.lower())
    
    match_count = 0
    for line in texts:
        match_count += line.count(word)

    print(match_count)
```
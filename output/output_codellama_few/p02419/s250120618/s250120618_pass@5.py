Here is the refactored version of the code:

if __name__ == '__main__':
    word = input().lower()
    texts = []
    while True:
        raw_input = input()
        if raw_input == 'END_OF_TEXT':
            break
        texts.append(raw_input.lower())
    match_count = sum([w.lower() == word for line in texts for w in line.split(' ')])
    print(match_count)
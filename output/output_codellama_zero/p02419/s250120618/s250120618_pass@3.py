if __name__ == '__main__':
    word = input().lower()
    texts = []
    while True:
        raw_input = input().lower()
        if raw_input == 'END_OF_TEXT':
            break
        texts.append(raw_input)

    match_count = sum(w == word for line in texts for w in line.split(' '))
    print(match_count)
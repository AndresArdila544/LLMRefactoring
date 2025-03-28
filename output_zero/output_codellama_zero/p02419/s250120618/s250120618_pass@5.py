if __name__ == '__main__':
    word = input()
    match_count = sum(line.lower().count(word) for line in iter(input, 'END_OF_TEXT'))
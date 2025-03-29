Here's a more concise and readable version of the program:

if __name__ == '__main__':
    word = input().lower()
    texts = []
    for raw_input in iter(lambda: input(), 'END_OF_TEXT'):
        texts.append(raw_input.lower())
    
    match_count = sum(w == word for line in texts for w in line.split(' ') )
    print(match_count)
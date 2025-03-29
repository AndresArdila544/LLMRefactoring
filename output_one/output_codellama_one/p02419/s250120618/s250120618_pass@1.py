def main():
    word = input().lower()
    texts = []
    while True:
        raw_input = input()
        if raw_input == 'END_OF_TEXT':
            break
        texts.append(raw_input.lower())
    
    match_count = 0
    for line in texts:
        match_count += len(re.findall(r'\b' + word + r'\b', line))
    
    print(match_count)

if __name__ == "__main__": main()
import sys

if __name__ == "__main__":
    texts = []
    word = input().lower()
    while True:
        raw_input = input()
        if raw_input == "END_OF_TEXT":
            break
        texts.append(raw_input.lower())
    match_count = 0
    for line in texts:
        for w in line.split(" "):
            if w == word:
                match_count += 1
    print(match_count)
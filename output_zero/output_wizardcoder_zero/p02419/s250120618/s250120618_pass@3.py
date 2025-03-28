refactored_code = """
def count_matches(word):
    texts = []
    
    while True:
        raw_input = input()
        if raw_input == 'END_OF_TEXT':
            break
        else:
            texts.append(raw_input)
            
    match_count = 0
    for line in texts:
        for w in line.split(' '):
            if word.lower() == w.lower():
                match_count += 1
                
    print(match_count)
"""

word = input("Enter the target word to search for: ")
count_matches(word)
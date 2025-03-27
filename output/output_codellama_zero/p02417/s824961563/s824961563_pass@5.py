def get_character_counts(input_string):
    lowercase_string = input_string.lower()
    character_counts = {}
    for char in lowercase_string:
        if char not in character_counts:
            character_counts[char] = 0
        character_counts[char] += 1
    return character_counts

print(get_character_counts("Hello World"))
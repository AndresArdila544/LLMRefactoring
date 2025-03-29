string = input()
for char in string:
    if char.isupper():
        print(char.lower(), end="")
    elif char.islower():
        print(char.upper(), end="")
    else:
        print(char, end="")
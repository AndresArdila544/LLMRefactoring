sentence = input().lower()
for i in sentence:
    if i.isupper():
        print(i.lower(), end="")
    else:
        print(i.upper(), end="")
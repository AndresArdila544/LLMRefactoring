sentence = input().upper()
print("".join([char.lower() if char.isupper() else char.upper() for char in sentence])
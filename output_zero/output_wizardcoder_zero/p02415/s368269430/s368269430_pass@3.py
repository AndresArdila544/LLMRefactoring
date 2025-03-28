sentence = input().lower()
print("".join([char.upper() if char.islower() else char.lower() for char in sentence])
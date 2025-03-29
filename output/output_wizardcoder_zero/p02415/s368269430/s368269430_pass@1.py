sentence = input().upper()
print(''.join([c if c.islower() else c for c in sentence])
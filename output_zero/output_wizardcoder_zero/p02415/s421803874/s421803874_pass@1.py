x = input().lower()
print(''.join(c if c.isalpha() else c for c in x)
# Refactoring the original program
def to_lowercase(string):
    return ''.join([chr(ord(c) if 'a'<=c<='z' else (ord(c)&0xDF) for c in string])
print(to_lowercase(input()))
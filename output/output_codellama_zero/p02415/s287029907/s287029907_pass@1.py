import string
def toggle_case(s):
    return ''.join([string.capwords(c) for c in s])
print(toggle_case(input()))
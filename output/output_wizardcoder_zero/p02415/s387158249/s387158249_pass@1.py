def to_uppercase(s1):
    return ''.join([chr(ord(c) + (-73 if ord('a') <= ord(c) <= ord('z') else 39) for c in s1])
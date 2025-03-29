def swap_case(s):
    return ''.join([char.lower() if char.isupper() else char.upper() for char in s])
print(swap_case(input()))
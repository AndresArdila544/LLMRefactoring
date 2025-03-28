def swap_case(x):
    ans = ''.join([char.lower() if char.isupper() else char.upper() for char in x])
    return ans
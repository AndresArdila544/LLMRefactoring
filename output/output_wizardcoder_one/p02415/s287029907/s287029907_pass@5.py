def convert_case(char):
    if 'a' <= char <= 'z':
        return chr(ord(char) ^ 0x20)
    elif 'A' <= char <= 'Z':
        return chr(ord(char) | 0x20)
    else:
        return char

input_str = input()
for c in input_str:
    print(convert_case(c), end='')
print()
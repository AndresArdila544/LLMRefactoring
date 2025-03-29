def convert_case(c):
    if 'a'<=c<='z':
        return chr(ord(c)^0x20)
    elif 'A'<=c<='Z':
        return chr(ord(c)|0x20)
    else:
        return c
def main():
    string = input()
    for char in string:
        print(convert_case(char), end='')
    print()

main()
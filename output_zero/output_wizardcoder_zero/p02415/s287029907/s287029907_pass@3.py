```python
def convert_case(char):
    if 'a'<=char<='z':
        return chr(ord(char)^0x20)
    elif 'A'<=char<='Z':
        return chr(ord(char)|0x20)
    else:
        return char

for char in input():
    print(convert_case(char), end='')
```
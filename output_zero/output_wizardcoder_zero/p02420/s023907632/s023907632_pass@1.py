```python
while True:
    string = input()
    if string[0] == '-':
        break
    else:
        shuffle_count = int(input())
        for i in range(shuffle_count):
            shuffle_num = int(input())
            c = string.pop(0)
            string += c
        print("".join(string))
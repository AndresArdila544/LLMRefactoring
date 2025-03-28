while True:
    string = input()
    if string[0] == '-':
        break
    shuffle_count = int(input())
    for _ in range(shuffle_count):
        shuffle_num = int(input())
        c = string.pop(0)
        string += c
    print(string)
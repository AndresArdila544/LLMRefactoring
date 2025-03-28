While True:
    string = input()
    if string[0] == '-':
        break
    shuffle_count = int(input())
    for i in range(shuffle_count):
        shuffle_num = int(input())
        string = string.pop(0) + string + string.pop(0)
    print(string)
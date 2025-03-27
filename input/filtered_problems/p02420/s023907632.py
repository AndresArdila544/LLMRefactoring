while True:
    string = [x for x in input()]
    if string[0] == '-':
        break
    else:
        shuffle_count = int(input())
        for i in range(shuffle_count):
            shuffle_num = int(input())
            for j in range(shuffle_num):
                c = string.pop(0)
                string.append(c)
        print("".join(string))


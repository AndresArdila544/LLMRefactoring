while True:
    string = list(input())
    if not string[0]:
        break
    else:
        shuffle_count = int(input())
        for _ in range(shuffle_count):
            shuffle_num = int(input())
            string.insert(len(string) - 1, string[0])
            del string[0]
print("".join(string))
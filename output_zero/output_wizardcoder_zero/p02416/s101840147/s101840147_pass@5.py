input_str = ""
while input_str != '0':
    input_str = input()
    print(sum(map(int, input_str)) if input_str else 0)